# -*- coding: utf-8 -*-
"""Created on 21.05.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.

Contains KWD-Keyword 'CLICK_ON_ELEMENT_ON_PHONE'
Contains KWD-Keyword 'SET_TOGGLE_BUTTON_STATE_ON_PHONE'
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
class ClickOnElementOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to click element on phone."""

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

		1. Check if element is visible
		2. Click element

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		xpath_collection = MyAudiXpathLoader(self.__phone.get_package_name_long())

		screen_name = self.values["SCREEN_NAME"].lower()
		element = self.values["XPATH_NAME"].lower()
		try:
			element_xpath = xpath_collection.get_xpath(screen_name, element)
		except KeyError:
			self._reporting.add_report_message_ta_error(f"Click not possible / Xpath for element '{element}' on screen '{screen_name}' not found")
			return False

		try:
			self.__phone.click_element(element_xpath)
			self._reporting.add_report_message_pass(f"Click Element with xpath '{element_xpath}' was successful")
			return True
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			self._reporting.add_report_message_ta_error(f"Click not possible / Element with xpath '{element_xpath}' not found on screen")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
			self._reporting.add_report_message_ta_error(f"Click not possible / Element with xpath '{element_xpath}' is not enabled")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class SetToggleButtonStateOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set the state of a toggle button"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["SCREEN_NAME", "XPATH_NAME", "STATE"]

	def _action(self) -> bool:
		"""Execute action.

		1. Check if element is visible
		2. Set state of toggle button

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		xpath_collection = MyAudiXpathLoader(self.__phone.get_package_name_long())

		screen_name = self.values["SCREEN_NAME"].lower()
		element = self.values["XPATH_NAME"].lower()
		try:
			element_xpath = xpath_collection.get_xpath(screen_name, element)
		except KeyError:
			self._reporting.add_report_message_ta_error(f"Set Toggle Button State not possible / Xpath for element '{element}' on screen '{screen_name}' not found")
			return False

		state = self.values["STATE"].lower() == 'true'

		try:
			self.__phone.set_toggle_button_state(element_xpath, state)
			self._reporting.add_report_message_pass(f"Set Toggle Button State of Element with xpath '{element_xpath}' was successful")
			return True
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			self._reporting.add_report_message_ta_error(f"Set Toggle Button State not possible / Element with xpath '{element_xpath}' not found on screen")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
			self._reporting.add_report_message_ta_error(f"Set Toggle Button State not possible / Element with xpath '{element_xpath}' is not enabled")
			return False
