# -*- coding: utf-8 -*-
"""Created on 17.08.2023.

@project: enna_kwd_testing
@author: DYX34ZN: Jakob Kein

Contains stimulations for keyword driven testing in context of sds speech recognition functions.
"""
import logging
import re

import enna.core.component_system.decorators
import enna.core.exceptions

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.data_logcat.interface
import enna_kwd_testing.utilities.speech.interface
import enna_kwd_testing.utilities.text_comparison.helper
from enna_kwd_testing.utilities.text_tool.get_text import get_text_from_texttool_sds_csv

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.speech")
class CheckSpeechOutput(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to input a speech input via text to speech for the target."""

	def __init__(self, reporting, speech: enna_kwd_testing.utilities.speech.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: instance of reporting interface.
		:param enna_kwd_testing.utilities.speech.interface.Interface speech: instance of speech interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")

		self.__speech = speech
		self.allowed_parameter_keys = ["text", "object_id", "variant_id"]

	def _precondition(self) -> bool:
		"""Execute precondition for keyword stimulation.

		Start listening for speech input by speech utility.

		:return: True if successful, False if any exception occurs on execution
		:rtype: bool
		"""
		try:
			self.__speech.start_listening()
		except Exception as exception:  # pylint: disable = broad-exception-caught
			MODULE_LOGGER.error("An error occurred at starting to listen for speech inputs on stimulation executing system.")
			MODULE_LOGGER.error(exception)
			return False
		return True

	def _action(self) -> bool:
		"""Execute action for keyword stimulation.

		Recognize microphone input (from keyword stimulation executing system) and check if the input is equal to the expected text which is defined
		under key "expected" in the instance attribute "values"

		:return: True if successful, False if any exception occurs on execution
		:rtype: bool
		"""
		try:
			str__text_id = self.values["PROPERTY_NAME"]
			str__default_text = get_text_from_texttool_sds_csv(str__text_id)
		except KeyError:
			str__default_text_with_language_id = self.values["TEXT"]
			str__default_text = re.search(r".*text:(?P<text>.*)}", str__default_text_with_language_id).group("text").strip().strip(".").lower().replace(",", "")

		MODULE_LOGGER.info(f"Check if expected text '{str__default_text}' appears as sound input on microphone.")
		try:
			self.__speech.wait_for_event("current_phrase", max_time=30, use_cache=False)
		except Exception as exception:  # pylint: disable = broad-exception-caught
			MODULE_LOGGER.error("An error occurred at proceeding speech recognition.")
			MODULE_LOGGER.error(exception)
			return False
		str__recognized_text = "".join(ch for ch in self.__speech.current_phrase.value if ch.isalnum() or ch.isspace()).lower().strip()
		threshold = 0.65
		match = enna_kwd_testing.utilities.text_comparison.helper.match_text(str__default_text, str__recognized_text)
		self._reporting.add_report_message_info(f"Text match between expected and actual speech response: {match}")
		self._reporting.add_report_message_info(f"[SDS] Expected answer: '{str__default_text}'")
		self._reporting.add_report_message_info(f"[SDS] Current answer: '{str__recognized_text}'")
		if match >= threshold:
			self._reporting.add_report_message_info("The recognized text from speech recognition is equal to the expected text.")
			MODULE_LOGGER.error(f"Expected text is: {str__default_text}")
			MODULE_LOGGER.error(f"Recognized text is: {str__recognized_text}")
			return True
		self._reporting.add_report_message_system_error("The recognized text from speech recognition is not equal to the expected text.")
		MODULE_LOGGER.error(f"Expected text is: {str__default_text}")
		MODULE_LOGGER.error(f"Recognized text is: {str__recognized_text}")
		return False

	def _postcondition(self) -> bool:
		"""Stop listening

		:return: True if successful, else False
		"""
		self.__speech.stop_listening()
		return True
