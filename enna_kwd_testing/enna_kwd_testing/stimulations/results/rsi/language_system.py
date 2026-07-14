# -*- coding: utf-8 -*-
"""Created on 25.09.2023.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
"""
import logging

import enna.core.component_system.decorators
import enna.data_interfaces.rsi.exceptions
import enna.data_interfaces.rsi.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.rsi")
class CheckCurrentSystemLanguage(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to check the current system language via rsi data interface."""

	def __init__(self, reporting, rsi: enna.data_interfaces.rsi.interface.Interface):
		"""Initialize keyword stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.rsi.interface.Interface rsi: Instance of rsi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.__rsi = rsi
		self.allowed_parameter_keys = ["lang"]

	def _action(self) -> bool:
		"""Execute action.

		Check the current system language via rsi data interface
		Check if the current system language is equal to the parameter "lang"

		:return: True if language was equal to parameter language, False otherwise
		:rtype: bool
		"""
		str__rsi_service__current_system_language = "language/system/LANGUAGE_SYSTEM/currentSystemLanguage"
		str_language_to_check = self.values["lang"]

		str_current_system_language = self.__rsi.get(str__rsi_service__current_system_language)
		MODULE_LOGGER.debug(f"Current system language is: {str_current_system_language};\tExpected is: {str_language_to_check}")
		return str_current_system_language == str_language_to_check
