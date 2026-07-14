# -*- coding: utf-8 -*-
"""Contains stimulation for keyword driven testing in context of sds speech input functions."""
import logging

import enna.core.component_system.decorators
import enna.core.exceptions

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.data_logcat.interface
import enna_kwd_testing.utilities.speech.interface

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.speech")
class SpeechInputDriver(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to input a speech input via text to speech for the target."""

	def __init__(self, reporting, speech: enna_kwd_testing.utilities.speech.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: instance of reporting interface.
		:param enna_kwd_testing.utilities.speech.interface.Interface speech: instance of speech interface
		"""
		super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.3")
		self.__speech = speech
		self.allowed_parameter_keys = ["TEXT"]

	def _action(self) -> bool:
		"""Execute action.

		Input natural speech text to target which is defined under key in instance attribute "values" under key "state".

		:return: True if successful, False if any exception occurs on execution
		"""
		try:
			speech_input = self.values["TEXT"]
		except KeyError:
			self._reporting.add_report_message_ta_error("Missing text for speech input!")
			return False

		try:
			# self.__speech.driver_speak(text=speech_input)
			self.__speech.speak(text=speech_input) # workaround mono input
		except Exception as error:  # pylint: disable = broad-exception-caught
			self._reporting.add_report_message_system_error(f"Could not say '{speech_input}' on Audio Device! {error}")
			return False
		self._reporting.add_report_message_pass(f"Input text: '{speech_input}' as speech input to target.")
		return True
