# -*- coding: utf-8 -*-
"""Created on 14.05.2024.

@project: enna_kwd_testing.
@author: SPLATZP: Platzer Pascal.

Contains stimulations for keyword driven testing in context of android_hmi home dashboard.
"""

import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import launcher

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi
from enna_kwd_testing.utilities.helper.android_hmi_helper import get_app_and_screen_name_from_screen

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=consider-ternary-expression, disable=too-many-locals, disable=too-many-branches


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation")
class GoToDashboardTile(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality go to dashboard tile."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface

		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation

	def _action(self) -> bool:
		"""Execute action.

		GO to Dashboard Tile.

		1. Navigate to Home
		2. Swipe to Dashboard Tile

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		str__tile_nr = self.values.get("TILE", False)

		if not wrapper_android_hmi.go_to_screen(launcher.HOME, self._reporting, self.__menu_navigation):
			self._reporting.add_report_message_system_error("Could not go to screen: 'launcher.HOME. Something went wrong while navigating to screen.")
			return False

		str__app_name, str__screen_name = get_app_and_screen_name_from_screen(self._reporting, self.__android_hmi)
		xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app=str__app_name)

		str__dashboard_page_1 = xpaths.get_xpath(str__screen_name, "DashboardPage1")
		str__dashboard_page_2 = xpaths.get_xpath(str__screen_name, "DashboardPage2")
		str__xpath_tile = xpaths.get_xpath(str__screen_name, f"Tile{str__tile_nr}")
		str__xpath_tile_0 = xpaths.get_xpath(str__screen_name, "Tile0")
		str__xpath_ai_screen = xpaths.get_xpath(str__screen_name, "AIScreen")

		if self.__android_hmi.layout.value.xpath(str__xpath_ai_screen):
			self.__android_hmi.swipe_element(str__xpath_ai_screen, enna_st12.data_interfaces.android_hmi.Direction.Left)

		if not self.__android_hmi.layout.value.xpath(str__dashboard_page_2) and int(str__tile_nr) > 2:
			self.__android_hmi.swipe_element(str__xpath_tile_0, enna_st12.data_interfaces.android_hmi.Direction.Left)

		if not self.__android_hmi.layout.value.xpath(str__dashboard_page_1) and int(str__tile_nr) < 2:
			self.__android_hmi.swipe_element(str__dashboard_page_2, enna_st12.data_interfaces.android_hmi.Direction.Right)

		if not wrapper_android_hmi.wait_for_layout_element(str__xpath_tile, self.__android_hmi, self._reporting):
			self._reporting.add_report_message_system_error(f"Xpath element Tile '{str__xpath_tile}' is not visible.")
			return False

		self._reporting.add_report_message_pass(f"The Tile {str__tile_nr} is shown.")

		return True
