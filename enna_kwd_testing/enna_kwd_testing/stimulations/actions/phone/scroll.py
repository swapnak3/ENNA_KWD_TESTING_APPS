# -*- coding: utf-8 -*-
"""Created on 27.05.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.

Contains KWD-Keyword 'SCROLL_TO_ELEMENT_IN_LIST_ON_PHONE'
"""

import logging
from pathlib import Path

import enna.core.component_system.decorators
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.exceptions

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.phone import interface
from enna_kwd_testing.utilities.phone.myaudi.frontend.myaudi_xpath_collection import MyAudiXpathLoader

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ScrollToElementInListOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class contains functionality to scroll to an element inside a list"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["SCREEN_NAME", "XPATH_NAME"]

	def _action(self) -> bool:
		"""Execute action.

		1. Try to scroll to element in list

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		xpath_collection = MyAudiXpathLoader(self.__phone.get_package_name_long())

		screen_name = self.values["SCREEN_NAME"].lower()
		element = self.values["XPATH_NAME"].lower()
		try:
			element_xpath = xpath_collection.get_xpath(screen_name, element)
		except KeyError:
			self._reporting.add_report_message_ta_error(f"Scroll to element not possible / Xpath for element '{element}' on screen '{screen_name}' not found")
			return False

		try:
			list_element_xpath = xpath_collection.get_xpath(screen_name, "main_list")
		except KeyError:
			self._reporting.add_report_message_ta_error(f"Scroll to element not possible / Xpath 'main_list' on screen '{screen_name}' not found")
			return False

		try:
			self.__phone.scroll_to_element_in_list(list_element_xpath, element_xpath)
			self._reporting.add_report_message_pass(f"Scroll to Element with xpath '{element_xpath}' in list with xpath '{list_element_xpath}' was successfully executed")
			return True
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			self._reporting.add_report_message_ta_error(f"Element with xpath '{element_xpath}' not found in list with xpath '{list_element_xpath}'")
			return False
