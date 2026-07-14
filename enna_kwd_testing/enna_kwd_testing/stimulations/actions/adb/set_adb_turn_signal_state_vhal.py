# -*- coding: utf-8 -*-
"""Created on 22.03.2024.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Teubner Claus.

Contains stimulations for keyword driven testing in context of adb turn signal state.
"""
import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class SetAdbTurnSignalStateVhal(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set the turn signal state for the target."""

	def __init__(self, reporting, adb: enna.data_interfaces.adb.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__adb = adb
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Execute action.

		Set turn signal state for target to the state defined in instance attribute "OFF, LEFT, RIGHT" under key "STATE".

		:return: True if successful, False if an enna.data_interfaces.exceptions.ADBException or a KeyError occurs.
		:rtype: bool
		"""
		self.allowed_parameter_keys = ["STATE"]

		turn_signal_state = self.values[self.allowed_parameter_keys[0]]
		MODULE_LOGGER.info(f"Setting turn signal state for target to: {turn_signal_state} via adb shell")
		signals = {
			"LEFT": "1",
			"RIGHT": "2",
			"OFF": "0"
		}
		if turn_signal_state in signals:
			cmd_state = signals[turn_signal_state]
			try:
				self.__adb.execute_shell_command(f"dumpsys activity service com.android.car inject-vhal-event 0x11400408 {cmd_state}")
			except KeyError:
				MODULE_LOGGER.error(f"The given parameter for the turn signal: '{turn_signal_state}' is not valid. Valid turn signals are: {signals.keys()}")
			except enna.data_interfaces.adb.exceptions.ADBException as exception:
				MODULE_LOGGER.error("An error occurred at executing the adb shell command to set the turn signal state:")
				MODULE_LOGGER.error(exception)
				return False
		else:
			MODULE_LOGGER.error(f"The given parameter for the turn signal: '{turn_signal_state}' is not valid. Valid turn signals are: {signals.keys()}")
			return False

		try:
			check_state = self.__adb.execute_shell_command("dumpsys car_service | grep -i event | grep -i Property:0x11400408").split(", ")[6].replace("int32Values: ", "")[1]
			if check_state == cmd_state:
				MODULE_LOGGER.info(f"Setting turn signal state for target to: {turn_signal_state} via adb shell was i.O.")
			else:
				MODULE_LOGGER.error("An error occurred at executing the adb shell command to check the turn signal state:")
				return False
		except enna.data_interfaces.adb.exceptions.ADBException as exception:
			MODULE_LOGGER.error("An error occurred at executing the adb shell command to check the turn signal state:")
			MODULE_LOGGER.error(exception)
			return False
		return True
