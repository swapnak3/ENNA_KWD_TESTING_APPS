# -*- coding: utf-8 -*-
"""Created on 22.11.2023.

@project: enna_kwd_testing.
@author: SPLATZP: Platzer Pascal.

Contains stimulations for keyword driven testing in context of android_hmi navigation functions.
"""

import logging

import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import navigation

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.helper.android_hmi_helper
import enna_kwd_testing.utilities.speller
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetColourOfMap(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set color of map."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self._reporting = reporting
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self._xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="navigation")
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Execute action.

		route guidance in navi.app.

		1. Navigate to 'navi.settings' screen
		2. Scroll to 'map_colors' in list on screen
		3. Set map_colors.

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""

		try:
			str__map_color = f"settingMapColors{self.values['COLOUR']}"
		except KeyError as exception:
			MODULE_LOGGER.error(f"Value {exception} not found")
			return False

		if not wrapper_android_hmi.go_to_screen(navigation.SETTINGS, self._reporting, self.__menu_navigation):
			self._reporting.add_report_message_ta_error("Could not go to screen: 'NAVI.APP -> SEARCH. Something went wrong while navigating to screen.")
			return False

		str__navi_settings_list_xpath = self._xpaths.get_xpath("settings", "main_list")
		str__navi_settings_map_color_xpath = self._xpaths.get_xpath("settings", str__map_color)

		if not wrapper_android_hmi.wait_and_scroll_in_list(str__navi_settings_map_color_xpath, str__navi_settings_list_xpath, self.__android_hmi):
			self._reporting.add_report_message_ta_error(f"Could not scroll to element: {str__navi_settings_map_color_xpath} in list {str__navi_settings_list_xpath}.")
			return False

		if not wrapper_android_hmi.wait_and_click(str__navi_settings_map_color_xpath, self.__android_hmi, self._reporting):
			self._reporting.add_report_message_ta_error(f"Could not click element: {str__navi_settings_map_color_xpath}.")
			return False

		str__navi_settings_map_color_checked_xpath = f"{str__navi_settings_map_color_xpath}[@checked='true']"

		if not wrapper_android_hmi.wait_for_layout_element(str__navi_settings_map_color_checked_xpath, self.__android_hmi):
			self._reporting.add_report_message_info(f"Map color is not set to {self.values['COLOUR']}")
			return False

		MODULE_LOGGER.info(f"The map color is set to '{self.values['COLOUR']}' ")

		return True
