# -*- coding: utf-8 -*-
"""Created on 27.11.2023.

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
class SetDestinationSearchOption(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set option search."""

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

		set search option.

		1. Navigate to 'navi.Search' screen
		2. Click on 'search option'
		3. Check if search option is set

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""

		try:
			str_search_option_to_set = self.values["OPTION"].lower()
		except KeyError as exception:
			self._reporting.add_report_message_ta_error(f"Key error: {exception} not found in values.")

		str_active_button = "google" if str_search_option_to_set == "intern" else "intern"

		if not wrapper_android_hmi.go_to_screen(navigation.SEARCH, self._reporting, self.__menu_navigation):
			self._reporting.add_report_message_ta_error("Could not go to screen: 'NAVI.APP -> SEARCH. Something went wrong while navigating to screen.")
			return False

		str__search_button_set_to_xpath = self._xpaths.get_xpath("search", f"searchButton_set_{str_search_option_to_set}")
		str__search_button_active_xpath = self._xpaths.get_xpath("search", f"searchButton_set_{str_active_button}")

		if not wrapper_android_hmi.wait_for_layout_element(str__search_button_set_to_xpath, self.__android_hmi):
			if not wrapper_android_hmi.wait_and_click(str__search_button_active_xpath, self.__android_hmi, self._reporting):
				self._reporting.add_report_message_ta_error(f"Could not click element: {str__search_button_active_xpath}.")
				return False

		if not wrapper_android_hmi.wait_for_layout_element(str__search_button_set_to_xpath, self.__android_hmi):
			self._reporting.add_report_message_info(f"Could set search option to: {str_search_option_to_set}.")
			return False

		MODULE_LOGGER.info(f"The search option is set to {str_search_option_to_set}")

		return True
