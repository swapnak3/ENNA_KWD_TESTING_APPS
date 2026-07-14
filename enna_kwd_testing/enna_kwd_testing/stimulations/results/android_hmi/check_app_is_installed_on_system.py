# -*- coding: utf-8 -*-
"""Created on 23.04.2024.

@project: enna_kwd_testing.
@author: SPLATZP: Platzer Pascal.

Contains stimulations for keyword driven testing to check app is installed on system.
"""

import logging
from pathlib import Path

import enna.core.component_system.decorators
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.definitions import RESOURCES_PATH
from enna_kwd_testing.utilities.package_loader.interface import PackageLoader

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckAppIsInstalledOnSystem(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check app is installed on system."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__android_hmi = android_hmi
		self.__package_loader = PackageLoader(Path(f"{RESOURCES_PATH}/packages/package_collection.json"))

	def _action(self) -> bool:
		"""Execute action.

		Check app is installed.

		1. Get values
		2. Check app is installed or not

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		try:
			str__package = self.values["APP_PACKAGE_NAME"]
		except KeyError as exception:
			str__package = self.values["APP_NAME"]
			str__package = self.__package_loader.get_package(str__package)
			self._reporting.add_report_message_info(f"{exception} not assigned Continue with APP_NAME.")

		try:
			str__installed_state = self.values["STATE"]
		except KeyError as exception:
			self._reporting.add_report_message_ta_error(f"Error: No STATE set {exception}.")
			return False

		list__apps_from_system = self.__android_hmi.get_installed_apps()
		if str__package in list__apps_from_system and str__installed_state == "TRUE":
			self._reporting.add_report_message_pass(f"APP '{str__package}' is installed on system.")
			return True
		if str__package not in list__apps_from_system and str__installed_state == "TRUE":
			self._reporting.add_report_message_system_error(f"APP '{str__package}' is not installed on system.")
			return False
		if str__package not in list__apps_from_system and str__installed_state == "FALSE":
			self._reporting.add_report_message_pass(f"APP '{str__package}' is not installed on system.")
			return True
		if str__package in list__apps_from_system and str__installed_state == "FALSE":
			self._reporting.add_report_message_system_error(f"APP '{str__package}' is installed on system.")
			return False

		return True
