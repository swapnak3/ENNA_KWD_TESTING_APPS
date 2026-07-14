# -*- coding: utf-8 -*-
"""Created on 14.02.2024.

@project: enna_kwd_testing.
@author: SPLATZP: Platzer Pascal.

Contains stimulations for keyword driven testing in context of text.
"""

import logging

import enna.core.component_system.decorators
import enna.core.time
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper

from enna_kwd_testing.utilities.helper.adb import set_keyboard_fast_input, set_keyboard
from enna_kwd_testing.utilities.text_comparison.helper import text_comparison_list

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class CheckTextResultInCarSearch(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to Verifies the text."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__android_hmi = android_hmi
		self.__adb = adb
		self._xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="car")

	def _action(self) -> bool:
		"""Execute action.

		Check Text in car search.

		1. Get values
		2. Set keyboard to fast input
		3. Click show more if the show more button is shown
		4. Verifies the text with textool

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		try:
			str__property_name = self.values["LABEL"]
		except KeyError as exception:
			self._reporting.add_report_message_ta_error(f"KeyError '{exception}'")
			return False

		str__language = self.values.get("LANG", "de_DE")

		# Disable the keyboard
		set_keyboard_fast_input(self.__adb)

		try:
			str_show_more_xpath = self._xpaths.get_xpath("search", "show_more")
			str_close_group_xpath = self._xpaths.get_xpath("search", "button_show_less")
			str__text_result_from_car_xpath = self._xpaths.get_xpath("search", "listItem_textStart")
		except KeyError as exception:
			self._reporting.add_report_message_ta_error(f"Xpath not found with {exception}")
			return False

		# Check if show more button visible
		enna.core.time.sleep(2)
		if self.__android_hmi.layout.value.xpath(str_show_more_xpath):
			self.__android_hmi.click_element(str_show_more_xpath)
			enna.core.time.sleep(1)

			# Here is clicked again, because it can happen that Enna does not pass on the click_element
			if not self.__android_hmi.layout.value.xpath(str_close_group_xpath):
				self.__android_hmi.click_element(str_show_more_xpath)
			self.__android_hmi.wait_for_element_visible(str_close_group_xpath, max_time=7)

		result, incorrect_text, default_text = text_comparison_list(self.__android_hmi, str__text_result_from_car_xpath, text_id=str__property_name, language=str__language)
		if not result:
			self._reporting.add_report_message_system_error(f"The text is wrong: The text is '{incorrect_text}' and not '{default_text}'.")
			return False

		MODULE_LOGGER.info(f"Success: '{default_text}' is shown in result list")
		self._reporting.add_report_message_info(f"Success: '{default_text}' is shown in result list")

		return True

	def _postcondition(self):
		"""Execute generic postcondition for keyword driven stimulation.

			1. activate keyboard

			:return: True if successful, False otherwise
			:rtype: bool
		"""
		set_keyboard(self.__adb)
		return True
