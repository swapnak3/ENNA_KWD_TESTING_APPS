# -*- coding: utf-8 -*-
"""Created on 23.11.2023.

@project: enna_kwd_testing.
@author: S6FXUOM, Nikolaus Maier.

Contains stimulations for KWD-TA in context of android_hmi sds settings functions.
"""

import logging

import enna.core.component_system.decorators
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import navigation as navigation_contexts

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper

from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetZoomMode(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set zoom mode in navigation."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self._parameter_keys = ["mode"]
		self.__navigation__set_zoom_level__xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="navigation")

	def _action(self) -> bool:
		"""Execute action.

		Set zoom mode to specific value.

		1. Use go to screen to open 'navigation main menu'
		2. Check zoom mode
		3. Set zoom mode as defined in instance attribute "MODE: MANUAL or AUTO" key "mode".

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		str_xpath__zoom_mode_manual = self.__navigation__set_zoom_level__xpaths.get_xpath("main", "zoom_mode_manual")
		str_xpath__zoom_mode_auto = self.__navigation__set_zoom_level__xpaths.get_xpath("main", "zoom_mode_automatic")
		zoom_mode_new = self.values["mode"]

		if not wrapper_android_hmi.go_to_screen(navigation_contexts.MAIN, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'Navigation App -> MAIN. Something went wrong while navigating to screen.")
			return False

		if "AUTO" in str(zoom_mode_new):
			if wrapper_android_hmi.wait_for_layout_element(str_xpath__zoom_mode_auto, self.__android_hmi, max_time=2):
				MODULE_LOGGER.info(f" Zoom mode already correct = {zoom_mode_new} .")
				return True
			if wrapper_android_hmi.wait_for_layout_element(str_xpath__zoom_mode_manual, self.__android_hmi, max_time=2):
				if not wrapper_android_hmi.wait_and_click(str_xpath__zoom_mode_manual, self.__android_hmi, self._reporting, "Could not click zoom mode button."):
					MODULE_LOGGER.info("Zoom mode was changed.")
				MODULE_LOGGER.info(f" Zoom mode already correct = {zoom_mode_new} .")
				return True
		elif "MANUAL" in str(zoom_mode_new):
			if wrapper_android_hmi.wait_for_layout_element(str_xpath__zoom_mode_manual, self.__android_hmi, max_time=2):
				MODULE_LOGGER.info(f" Zoom mode already correct = {zoom_mode_new} .")
				return True
			if wrapper_android_hmi.wait_and_click(str_xpath__zoom_mode_manual, self.__android_hmi, self._reporting, "Could not click zoom mode button."):
				if wrapper_android_hmi.wait_for_layout_element(str_xpath__zoom_mode_auto, self.__android_hmi, max_time=2):
					MODULE_LOGGER.info(f" Zoom mode already correct = {zoom_mode_new} .")
					return True
		MODULE_LOGGER.info(f" Zoom mode was set to {zoom_mode_new} .")
		return False
