# -*- coding: utf-8 -*-
"""Created on 09.11.2023.

@project: enna_kwd_testing.
@author: S6FXUOM, Nikolaus Maier.

Contains stimulations for KWD-TA in context of android_hmi sds settings functions.
"""

import logging
import re

import enna.core.component_system.decorators
import enna.core.time
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import navigation as navigation_contexts

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import navigation_app_helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)

# pylint: disable=too-many-branches

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetZoomLevel(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set zoom level in navigation."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self._parameter_keys = ["LEVEL", "METRIC"]
		self._xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="navigation")

	def _action(self) -> bool:
		"""Execute action.

		Set zoom level to specific values (value and unit).

		1. Use go to screen to open 'navigation main menu'
		2. Check zoom units and setup the right unit
		3. Set zoom values as defined in instance attribute "Level" & key "level" and attribute "METRIC" key "metric".

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		str_xpath__zoom_out_button = self._xpaths.get_xpath("main", "zoom_out_button")
		str_xpath__zoom_in_button = self._xpaths.get_xpath("main", "zoom_in_button")

		zoom_scale_unit_new = self.values["METRIC"]
		zoom_scale_value_new = self.values["LEVEL"]
		# Valuation created for METER and KILOMETER, engl. has , instead of .

		if zoom_scale_unit_new == "METER":
			zoom_scale_unit_new = "m"
		elif zoom_scale_unit_new == "KILOMETER":
			zoom_scale_unit_new = "km"
		else:
			MODULE_LOGGER.error("Unknown Scale Unit")
			return False

		if not wrapper_android_hmi.go_to_screen(navigation_contexts.MAIN, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'Navigation App -> MAIN. Something went wrong while navigating to screen.")
			return False

		if not navigation_app_helper.swipe_coordinates(self.__android_hmi, 1800, 270, 1600, 400, "Could not swipe coordinates"):
			return False

		zoom_scale_old = wrapper_android_hmi.get_element_by_xpath(self._xpaths.get_xpath("main", "zoom_scale"), self.__android_hmi, self._reporting).get("text")
		zoom_scale_old_save = zoom_scale_old

		# zoom until units are correct

		if zoom_scale_unit_new == "km":
			while re.sub("[0-9]", "", zoom_scale_old) != "km":
				navigation_app_helper.zoom_out_one_step(str_xpath__zoom_out_button, self.__android_hmi, self._reporting)
				enna.core.time.sleep(1)
				zoom_scale_old = wrapper_android_hmi.get_element_by_xpath(self._xpaths.get_xpath("main", "zoom_scale"), self.__android_hmi, self._reporting).get("text")
		elif zoom_scale_unit_new == "m":
			while re.sub("[0-9]", "", zoom_scale_old) != "m":
				navigation_app_helper.zoom_in_one_step(str_xpath__zoom_in_button, self.__android_hmi, self._reporting)
				enna.core.time.sleep(1)
				zoom_scale_old = wrapper_android_hmi.get_element_by_xpath(self._xpaths.get_xpath("main", "zoom_scale"), self.__android_hmi, self._reporting).get("text")

		enna.core.time.sleep(1)

		# Unit are similar km == km, m == m

		if zoom_scale_value_new > float(re.sub("[a-zA-Z]", "", zoom_scale_old)):
			while zoom_scale_value_new > float(re.sub("[a-zA-Z]", "", zoom_scale_old)):
				navigation_app_helper.zoom_out_one_step(str_xpath__zoom_out_button, self.__android_hmi, self._reporting)
				enna.core.time.sleep(1)
				zoom_scale_old = wrapper_android_hmi.get_element_by_xpath(self._xpaths.get_xpath("main", "zoom_scale"), self.__android_hmi, self._reporting).get("text")
		elif zoom_scale_value_new < float(re.sub("[a-zA-Z]", "", zoom_scale_old)):
			while zoom_scale_value_new < float(re.sub("[a-zA-Z]", "", zoom_scale_old)):
				navigation_app_helper.zoom_in_one_step(str_xpath__zoom_in_button, self.__android_hmi, self._reporting)
				enna.core.time.sleep(1)
				zoom_scale_old = wrapper_android_hmi.get_element_by_xpath(self._xpaths.get_xpath("main", "zoom_scale"), self.__android_hmi, self._reporting).get("text")

		MODULE_LOGGER.info(f" Zoom new: {zoom_scale_value_new, zoom_scale_unit_new}, Zoom old: {zoom_scale_old_save}'.")
		return True
