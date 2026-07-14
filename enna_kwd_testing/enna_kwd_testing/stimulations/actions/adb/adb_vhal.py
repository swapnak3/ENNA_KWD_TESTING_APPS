# -*- coding: utf-8 -*-
"""Created on 04.08.2023.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.

Contains stimulations for keyword driven testing in context of adb vhal functions.
"""
import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class SetTurnSignalState(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set the turn signal state for the target."""

	def __init__(self, reporting, adb: enna.data_interfaces.adb.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__adb = adb
		self.allowed_parameter_keys = ["state"]

	def _action(self) -> bool:
		"""Execute action.

		Set turn signal state for target to the state defined in instance attribute "values" under key "state".

		:return: True if successful, False if an enna.data_interfaces.exceptions.ADBException or a KeyError occurs.
		:rtype: bool
		"""
		turn_signal_state = self.values["state"]
		MODULE_LOGGER.info(f"Setting turn signal state for target to: {turn_signal_state} via adb shell")

		signals = {
			"LEFT": "1",
			"RIGHT": "2",
			"OFF": "0"
		}

		try:
			cmd_state = signals[turn_signal_state]
			self.__adb.execute_shell_command(f"dumpsys activity service com.android.car inject-vhal-event 0x11400408 {cmd_state}")
			return True
		except KeyError:
			MODULE_LOGGER.error(f"The given parameter for the turn signal: '{turn_signal_state}' is not valid. Valid turn signals are: {signals.keys()}")
		except enna.data_interfaces.adb.exceptions.ADBException as exception:
			MODULE_LOGGER.error("An error occurred at executing the adb shell command to set the turn signal state:")
			MODULE_LOGGER.error(exception)
		return False
