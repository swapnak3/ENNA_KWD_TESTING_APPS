# -*- coding: utf-8 -*-
"""Created on 24.04.2024.

@project: enna_kwd_testing.
@author: T6B0NVV: TEC: Frank Isselhard.

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
class CheckServiceForTli(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""lass containing functionality to check the traffic light information activity from adb shell logcat and returns True|False"""

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

		Get the traffic light information activity from adb shell.

		:return:  True if the check of services is successful, False if not, or if an enna.data_interfaces.exceptions.ADBException occurs.
		:rtype: bool
		"""
		str_expected_tli_service = str(self.values["SERVICES"])
		str_expected_tli_services = ["intent={cmp=technology.cariad.trafficlightinformation/.TliForegroundService}", "intent={cmp=technology.cariad.trafficlightinformation/.TliService}"]
		if str_expected_tli_service not in str_expected_tli_services:
			MODULE_LOGGER.error(f"Wrong parameter for SERVICES:'{str_expected_tli_service}', should be one of '{str_expected_tli_services}'")
			return False

		MODULE_LOGGER.info(f"Checking traffic lights service: {str_expected_tli_service}, via adb shell dumpsys")

		try:
			str_checked_tli_service = self.__adb.execute_shell_command("dumpsys activity services technology.cariad.trafficlightinformation")
			MODULE_LOGGER.info(str_checked_tli_service)

			# find returns the position of the string if the search string is found and -1 otherwise
			find_index =  str_checked_tli_service.find(str_expected_tli_service)
			if find_index == -1:
				MODULE_LOGGER.info(f"traffic light service: {str_expected_tli_service} is not in the activity services.")
				return False

			MODULE_LOGGER.info(f"traffic light service: {str_expected_tli_service} is the activity services.")
			return True

		except enna.data_interfaces.adb.exceptions.ADBException as exception:
			MODULE_LOGGER.error("An error occurred at executing the adb shell command to check the traffic light service:")
			MODULE_LOGGER.error(exception)
		return False
