# -*- coding: utf-8 -*-
"""Created on 09.10.2023.

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
class CheckZoomLevel(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check zoom level in navigation."""

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

		Check zoom level to specific values (value and unit).

		1. Check zoom values

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		zoom_scale_unit_new = self.values["METRIC"]
		zoom_scale_value_new = self.values["LEVEL"]

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

		zoom_scale_shown = wrapper_android_hmi.get_element_by_xpath(self._xpaths.get_xpath("main", "zoom_scale"), self.__android_hmi, self._reporting)

		if str(zoom_scale_value_new) + zoom_scale_unit_new == zoom_scale_shown.get("text"):
			MODULE_LOGGER.info("Zoom level is correct.")
			return True

		MODULE_LOGGER.error("Zoom level is not correct.")
		return False
