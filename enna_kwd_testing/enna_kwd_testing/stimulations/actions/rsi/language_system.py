# -*- coding: utf-8 -*-
"""Created on 25.09.2023.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
"""
import logging
import time

import enna.core.config
import enna.core.event_helper
import enna.core.component_system.decorators
import enna.core.exceptions
import enna.core.interfaces
import enna.data_interfaces.rsi.exceptions
import enna.data_interfaces.rsi.interface

import enna_hcp_configuration.android.analyzer
import enna_hcp_configuration.android.graph

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.rsi")
class SetCurrentSystemLanguage(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to set the current system language via rsi data interface."""

	def __init__(self, reporting, rsi: enna.data_interfaces.rsi.interface.Interface):
		"""Initialize keyword stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.rsi.interface.Interface rsi: Instance of rsi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__rsi = rsi
		self.allowed_parameter_keys = ["lang"]

	def _action(self) -> bool:
		"""Execute action.

		Set the system language via rsi data interface.
		If the system language is already equal to the desired value then do nothing.
		If the system language must be set, then set it by creating the rsi element and for verification implicitly wait a maximum amount of 10 seconds for the changes to be done in the system.

		:return: True if language was set correctly, False otherwise
		:rtype: bool
		"""
		str__rsi_service__current_system_language = "language/system/LANGUAGE_SYSTEM/currentSystemLanguage"
		str_language_to_set = self.values["lang"]

		str_current_system_language = self.__rsi.get(str__rsi_service__current_system_language)
		if str_current_system_language == str_language_to_set:
			MODULE_LOGGER.info(f"The system language is already equal to: {str_language_to_set}. Nothing to do here.")
			return True

		MODULE_LOGGER.debug(f"Set system language from currently: '{str_current_system_language}' to '{str_language_to_set}'.")
		try:
			self.__rsi.create_element("language/changeRequests", {"componentType": "graphicalUserInterface", "newLanguage": str_language_to_set})
		except (enna.core.exceptions.EventNotFoundException, enna.data_interfaces.rsi.exceptions.RSIException) as exception:
			MODULE_LOGGER.debug(f"Error by writing system language to {str_language_to_set}! Unexpected response from post request.")
			MODULE_LOGGER.exception(exception)

		timeout = time.time() + 10.0
		while self.__rsi.get(str__rsi_service__current_system_language) != str_language_to_set:
			time.sleep(0.1)
			if time.time() > timeout:
				actual_language = self.__rsi.get(str__rsi_service__current_system_language)
				MODULE_LOGGER.debug(f"Could not set system language to: {str_language_to_set}")
				MODULE_LOGGER.debug(f"Current system language is: {actual_language}")
				# set current language in config and screen analyzer
				language_config = {"system_language": actual_language}
				# enna.core.config.INFOTAINMENT_SYSTEM["system_language"] = str(actual_language)
				enna_hcp_configuration.android.analyzer.initialize(language_config)
				enna_hcp_configuration.android.graph.initialize(language_config)
				self._reporting.add_report_message_system_error(f"Could not set system language to: {str_language_to_set}! Current system language is: {actual_language}.")
				return False

		# set new language in config and screen analyzer
		language_config = {"system_language": str_language_to_set}
		# enna.core.config.INFOTAINMENT_SYSTEM["system_language"] = str_language_to_set
		enna_hcp_configuration.android.analyzer.initialize(language_config)
		enna_hcp_configuration.android.graph.initialize(language_config)
		MODULE_LOGGER.debug(f"System language was successfully set from '{str_current_system_language}' to '{str_language_to_set}'.")
		self._reporting.add_report_message_pass(f"System language was successfully set from '{str_current_system_language}' to '{str_language_to_set}'.")
		return True
