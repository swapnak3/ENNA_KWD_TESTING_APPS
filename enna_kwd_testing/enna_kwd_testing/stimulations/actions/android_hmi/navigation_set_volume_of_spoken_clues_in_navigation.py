# -*- coding: utf-8 -*-
"""Created on 06.12.2023.

@project: enna_kwd_testing.
@author: SPLATZP: Platzer Pascal.

Contains stimulations for keyword driven testing in context of android_hmi navigation functions.
"""

import logging

import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import navigation

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.helper.android_hmi_helper
import enna_kwd_testing.utilities.speller
import enna_kwd_testing.utilities.xpath_collection.helper

from enna_kwd_testing.utilities.helper import wrapper_android_hmi
from enna_kwd_testing.utilities.helper.adb import get_volume

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=too-many-branches

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class SetVolumeOfSpokenCluesInNavigation(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set volume of spoken clues in navigation."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface,
				 menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.__adb = adb
		self._reporting = reporting
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self._xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="navigation")
		self.allowed_parameter_keys = ["VALUE"]

	def _action(self) -> bool:
		"""Execute action.

		route guidance in navi.app.

		1. Navigate to 'navigation.settings' screen
		2. Scroll to 'volume of spoken clues' in list on screen
		3. Set volume of spoken clues.

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""

		try:
			int__value_to_set = int(self.values["VALUE"])
		except KeyError as exception:
			self._reporting.add_report_message_ta_error(f"Value {exception} not found")
			return False

		if int__value_to_set > 34 or int__value_to_set < 0:
			self._reporting.add_report_message_ta_error(f"Wrong value '{int__value_to_set}' please use a value between 0 and 34.")
			return False

		str__navi_settings_list_xpath = self._xpaths.get_xpath("settings", "main_list")
		str__navi_settings_volume_seek_bar_xpath = self._xpaths.get_xpath("settings", "settingAnnouncementVolume-seekBar")
		str__navi_settings_volume_minus_button_xpath = self._xpaths.get_xpath("settings", "settingAnnouncementVolume-minusButton")
		str__navi_settings_volume_plus_button_xpath = self._xpaths.get_xpath("settings", "settingAnnouncementVolume-plusButton")

		if not wrapper_android_hmi.go_to_screen(navigation.SETTINGS, self._reporting, self.__menu_navigation):
			self._reporting.add_report_message_ta_error("Could not go to screen: 'NAVI.APP -> SETTING. Something went wrong while navigating to screen.")
			return False

		if not wrapper_android_hmi.wait_and_scroll_in_list(str__navi_settings_volume_seek_bar_xpath, str__navi_settings_list_xpath, self.__android_hmi):
			self._reporting.add_report_message_ta_error(f"Could not scroll to element: {str__navi_settings_volume_seek_bar_xpath} in list {str__navi_settings_list_xpath}.")
			return False

		try:
			if get_volume(self.__adb, "android.car.VOLUME_GROUP/0/1") > int__value_to_set:
				str__volume_differance = get_volume(self.__adb, "android.car.VOLUME_GROUP/0/1") - int__value_to_set
				for _ in range(int(str__volume_differance)):
					if not wrapper_android_hmi.wait_and_click(str__navi_settings_volume_minus_button_xpath, self.__android_hmi, self._reporting):
						self._reporting.add_report_message_ta_error(f"Could not click element: {str__navi_settings_volume_minus_button_xpath}.")
						return False
		except (enna.data_interfaces.adb.exceptions.ADBException, KeyError) as exception:
			self._reporting.add_report_message_ta_error(f"An error occurred: {exception}")
			return False

		try:
			if get_volume(self.__adb, "android.car.VOLUME_GROUP/0/1") < int__value_to_set:
				str__volume_differance = int__value_to_set - get_volume(self.__adb, "android.car.VOLUME_GROUP/0/1")
				for _ in range(int(str__volume_differance)):
					if not wrapper_android_hmi.wait_and_click(str__navi_settings_volume_plus_button_xpath, self.__android_hmi, self._reporting):
						self._reporting.add_report_message_ta_error(f"Could not click element: {str__navi_settings_volume_plus_button_xpath}.")
						return False
			volume = get_volume(self.__adb, "android.car.VOLUME_GROUP/0/1")
			if volume != int__value_to_set:
				self._reporting.add_report_message_system_error("An error occurred: The Volume is not correctly set")
				return False
		except (enna.data_interfaces.adb.exceptions.ADBException, KeyError) as exception:
			self._reporting.add_report_message_ta_error(f"An error occurred: {exception}")
			return False

		MODULE_LOGGER.info(f"The volume of spoken clues is set to '{self.values['VALUE']}' ")

		return True
