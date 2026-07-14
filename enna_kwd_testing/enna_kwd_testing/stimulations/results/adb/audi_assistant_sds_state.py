# -*- coding: utf-8 -*-
"""Created on 15.11.2023.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Claus Teubner.

Contains stimulations for keyword driven testing in context of adb shell functions.
"""

import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class CheckAssistantState(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check the SDS status to 'listening', 'speaking', 'idle' from adb shell logcat and returns True|False"""

	def __init__(self, reporting, adb: enna.data_interfaces.adb.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.__adb = adb
		self._reporting = reporting
		self.allowed_parameter_keys = ["state"]

	def _action(self) -> bool:
		"""Execute action.

		Get the SDS status from adb shell logcat: 'listening', 'speaking', 'idle'.

		:return:  True if check on State: 'listening'||'speaking'||'idle'  is successful, False if not, or if an enna.data_interfaces.exceptions.ADBException occurs.
		:rtype: bool
		"""
		str_expected_sds_state = str(self.values["STATE"])
		str_possible_sds_states = ["LISTENING", "SPEAKING", "IDLE"]
		if str_expected_sds_state not in str_possible_sds_states:
			MODULE_LOGGER.error(f"Wrong parameter for STATE:'{str_expected_sds_state}', should be one of '{str_possible_sds_states}'")
			return False

		MODULE_LOGGER.info(f"Checking sds status: {str_expected_sds_state}, via adb shell logcat")

		try:
			i = 0
			i_max = 10
			str_checked_sds_state = ""
			while str_checked_sds_state not in ("IDLE", "LISTENING", "SPEAKING"):
				str_checked_sds_state = self.__adb.execute_shell_command("logcat -t 20000 --regex='\\[GDA\\]#onAssistantStateChanged: state=' | tail -1")
				if i > i_max or "Idle" in str_checked_sds_state:
					str_checked_sds_state = "IDLE"
				elif "UserActive" in str_checked_sds_state:
					str_checked_sds_state = "LISTENING"
				elif "SystemActive" in str_checked_sds_state:
					str_checked_sds_state = "SPEAKING"
				else:
					MODULE_LOGGER.info("while status is empty, waiting some seconds for any status, after waitiing sds state is 'Idle'.")
				i += 1

			if str_expected_sds_state == str_checked_sds_state:
				MODULE_LOGGER.info(f"the expected sds status: {str_expected_sds_state} is the sds state: {str_checked_sds_state}")
			else:
				MODULE_LOGGER.info(f"the expected sds status: {str_expected_sds_state} is not the sds state: {str_checked_sds_state}")
				return False
			return True

		except enna.data_interfaces.adb.exceptions.ADBException as exception:
			MODULE_LOGGER.error("An error occurred at executing the adb shell command to check the sds state:")
			MODULE_LOGGER.error(exception)
		return False
