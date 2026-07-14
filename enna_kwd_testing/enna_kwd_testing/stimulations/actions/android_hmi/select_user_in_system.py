# -*- coding: utf-8 -*-
"""Created on 29.02.2024.

@project: enna_kwd_testing.
@author: WZ40Y0R: Simon Schmidt.

Contains stimulations for keyword driven testing in context of android_hmi check colour of warning lamps functions.
"""

import logging

import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.data_interfaces.adb.interface
import enna.data_interfaces.rsi.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.instance_names

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.rsi", instance_name=enna_st12.instance_names.Rsi.MAIN_UNIT)
class SelectUserInSystem(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to select user via HMI."""

	def __init__(self, adb, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, rsi: enna.data_interfaces.rsi.interface.Interface):
		"""Initialize stimulation.

		:param rsi: Instance of rsi interface
		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self._users = []
		self.__rsi = rsi
		self.__adb = adb
		self._reporting = reporting
		self.__android_hmi = android_hmi
		self.__xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="launcher")
		self.allowed_parameter_keys = ["USER"]

	def _action(self) -> bool:
		"""Select user via HMI.

		:return: True if successful, False otherwise
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		name = ""
		self._users = self.__rsi.get("usermanagement.users")
		for i in self._users:
			if i.get("role") == self.values["USER"] and i.get("name") != "#defaultUser":
				name = i.get("name")

		if name == "":
			self._reporting.add_report_message_system_error(f"No user found with role: {self.values['USER']}")
			return False

		checked_user = self.__adb.execute_shell_command("pm list users")

		for j in checked_user.split("\n\t"):
			if name in j and "running" in j:
				return True

		user_button = self.__xpaths.get_xpath("general", "user_button")
		change_button = self.__xpaths.get_xpath("change_user", "change_button")
		select_user_button = f"//*[contains(@text, '{name}')]"

		wrapper_android_hmi.wait_and_click(user_button, self.__android_hmi, self._reporting)
		wrapper_android_hmi.wait_and_click(select_user_button, self.__android_hmi, self._reporting)
		wrapper_android_hmi.wait_and_click(change_button, self.__android_hmi, self._reporting)

		MODULE_LOGGER.info(f"User {self.values['USER']} is selected'")

		return True
