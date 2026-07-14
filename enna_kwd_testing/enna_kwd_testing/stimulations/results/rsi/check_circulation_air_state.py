# -*- coding: utf-8 -*-
"""Created on 24.01.2024.

@project: enna_kwd_testing.
@author: SPLATZP: Platzer Pascal.

Contains stimulations for keyword driven testing in context of rsi circulation air state functions.
"""
import logging

import enna.core.component_system.decorators
import enna.core.exceptions
import enna.core.interfaces
import enna.data_interfaces.rsi.exceptions
import enna.data_interfaces.rsi.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.rsi")
class CheckCirculationAirState(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to check circulation air state via rsi data interface."""

	def __init__(self, reporting, rsi: enna.data_interfaces.rsi.interface.Interface):
		"""Initialize keyword stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.rsi.interface.Interface rsi: Instance of rsi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.__rsi = rsi
		self.__str_value = "hvac/switchControls/airCirculationManual/switchValue"

	def _action(self) -> bool:
		"""Execute action.

		Check circulation air state via rsi data interface.

		:return: True if value was set correctly, False otherwise
		:rtype: bool
		"""

		try:
			str_value_to_compare = self.values["STATE"]
		except ValueError as exc:
			self._reporting.add_report_message_ta_error(f"Value Error: {exc}.")

		try:
			str_current_value = self.__rsi.get(self.__str_value)
		except (enna.core.exceptions.EventNotFoundException, enna.data_interfaces.rsi.exceptions.RSIException) as exception:
			self._reporting.add_report_message_ta_error(f"The RSI Server did not react, value can not read with Service {self.__str_value}.")
			MODULE_LOGGER.exception(exception)
			return False

		if not str_current_value == str_value_to_compare:
			self._reporting.add_report_message_system_error(f"The circulation air state is not {str_value_to_compare}.")
			return False

		MODULE_LOGGER.info(f"The circulation air state is {str_value_to_compare}.")
		return True
