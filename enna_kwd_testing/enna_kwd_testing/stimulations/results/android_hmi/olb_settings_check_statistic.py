# -*- coding: utf-8 -*-
"""Created on 06.03.2024.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Teubner Claus.

Contains stimulations for keyword driven testing in context of android_hmi aem functions.
"""

import logging

import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import olb

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.speller
import enna_kwd_testing.utilities.xpath_collection.helper

from enna_kwd_testing.utilities.helper import android_hmi_helper, wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=too-many-branches

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckStatisticsInOlb(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check statistics variant in olb.app under statistic_settings."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self._reporting = reporting
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self._screen_id = ""
		self._xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="olb")
		self.allowed_parameter_keys = ["STATISTIC"]
		self.allowed_parameter_values = ["Current year", "Comparison to the same period...", "Comparison to the entire previous year"]
		self.olb_button_xpath_values = ["current_year_button", "comparison_same_period_button", "comparison_entire_previous_year_button"]

	def _action(self) -> bool:
		"""Execute action.

		check statistics variant in olb.app under statistic_settings.

		1. Navigate to 'olb.SETTINGS' screen
		2. Check value Button is selected (STATISTIC: ["Current year", "Comparison to the same period...", "Comparison to the entire previous year"])

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""

		self._screen_id = android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)
		str__statistic_value = "Comparison to the same period..."
		try:
			str__statistic_value = self.values["STATISTIC"]
			str__check_statistic_button_xpath = ""
			if str__statistic_value in self.allowed_parameter_values:
				for i, j in enumerate(self.allowed_parameter_values):
					if str__statistic_value == j:
						str__check_statistic_button_xpath = self._xpaths.get_xpath("settings", self.olb_button_xpath_values[i])
				if str__check_statistic_button_xpath == "":
					MODULE_LOGGER.error(f"Wrong STATISTIC: '{str__statistic_value}', should be one of 'STATISTIC': '{self.allowed_parameter_values[0]}', '{self.allowed_parameter_values[1]}', '{self.allowed_parameter_values[2]}'.")
					return False
		except KeyError as exception:
			MODULE_LOGGER.error(f"{exception}: Wrong STATISTIC: '{str__statistic_value}', should be one of 'STATISTIC': '{self.allowed_parameter_values[0]}', '{self.allowed_parameter_values[1]}', '{self.allowed_parameter_values[2]}'.")
			return False

		if not wrapper_android_hmi.go_to_screen(destination=olb.SETTINGS, reporting=self._reporting, menu_navigation=self.__menu_navigation, retries=5):
			self._reporting.add_report_message_ta_error("Could not go to screen: 'core_services.HOME. Something went wrong while navigating to screen.")
			return False

		error_message = f"Could not found button '{str__statistic_value}'. Xpath '{str__check_statistic_button_xpath}' not found. An error occurred."
		if not wrapper_android_hmi.wait_for_layout_element(xpath=f"{str__check_statistic_button_xpath}", android=self.__android_hmi, additional_message="", max_time=15):
			self._reporting.add_report_message_system_error(error_message)
			return True

		error_message = f"Found button '{str__statistic_value}'. Xpath '{str__check_statistic_button_xpath}' found, but it is noch selected. An error occurred."
		if not wrapper_android_hmi.wait_for_layout_element(xpath=f"{str__check_statistic_button_xpath}[@checked='true']", android=self.__android_hmi, additional_message="", max_time=15):
			self._reporting.add_report_message_system_error(error_message)
			return False

		MODULE_LOGGER.info(f"The button '{str__statistic_value}' is selected.")

		return True
