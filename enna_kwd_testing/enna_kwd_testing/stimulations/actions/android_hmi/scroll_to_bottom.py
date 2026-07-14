# -*- coding: utf-8 -*-
"""Created on 29.04.2024.

@project: enna_kwd_testing.
@author: SPLATZP: Platzer Pascal.

Contains stimulations for keyword driven testing in context of android_hmi scroll to element.
"""

import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi
from enna_kwd_testing.utilities.helper.android_hmi_helper import get_app_and_screen_name_from_screen

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=consider-ternary-expression

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class ScrollToBottom(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality scroll to bottom list."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.__android_hmi = android_hmi

	def _action(self) -> bool:
		"""Execute action.

		Scroll to bottom.

		1. Scroll to bottom

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		str__app_name, str__screen_name = get_app_and_screen_name_from_screen(self._reporting, self.__android_hmi)
		xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app=str__app_name)
		list_element = xpaths.get_xpath(str__screen_name, "main_list")

		if not wrapper_android_hmi.wait_and_scroll_list_to_bottom(list_element, self.__android_hmi):
			self._reporting.add_report_message_system_error("Could not scroll to bottom.")
			return False

		self._reporting.add_report_message_pass("The List is scrolled to the bottom")

		return True
