# -*- coding: utf-8 -*-
"""Created on 07.05.2024.
@project: enna_kwd_testing.
@author: SPLATZP: PASCAL PLATZER.
Contains stimulations for keyword driven testing in context of adb shell.
"""
import logging
from pathlib import Path

import enna.core.component_system.decorators
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.json_loader.interface
from enna_kwd_testing.definitions import RESOURCES_PATH

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class InstallApkInSystem(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to send ADB Shell commands."""

	def __init__(self, reporting, adb: enna.data_interfaces.adb.interface.Interface):
		"""Initialize stimulation.
		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__adb = adb
		self._path_apk_names = Path(f"{RESOURCES_PATH}/apk_data/apk_data.json")
		self._path_apk = f"{str(RESOURCES_PATH).replace('\\', '/')}/apk_data/apks"
		self.__apk_loader = enna_kwd_testing.utilities.json_loader.interface.JsonLoader(self._path_apk_names)

	def _action(self) -> bool:
		"""Execute action.
		Send ADB Shell command to install a apk
		:return: True if successful, False it exception occurs
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		str__apk_name = self.values.get("APP_NAME", False)
		str__apk_package = self.values.get("APP_PACKAGE", False)

		str_apk = self.__apk_loader.get_value(str__apk_name) if str__apk_name else str__apk_package

		apk = rf"{self._path_apk}/{str_apk}"
		try:
			adb_command = f" install {apk}"
			adb_out = self.__adb.execute_adb_command(adb_command)
			if "Success" not in adb_out:
				self._reporting.add_report_message_system_error(f"Install {str_apk} failed: {adb_out}")
				return False
			self._reporting.add_report_message_pass(f"Successfully install '{str_apk}'")
			return True
		except enna.data_interfaces.adb.exceptions.ADBException as exception:
			self._reporting.add_report_message_system_error(f"An error occurred: {exception}")
			return False
