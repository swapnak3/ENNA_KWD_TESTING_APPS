# -*- coding: utf-8 -*-
"""Created on 11.04.2024.

@project: enna_kwd_testing.
@author: WZ40Y0R: Simon Schmidt.

Contains stimulations for keyword driven testing in context of android_hmi set user mode in ico.
"""

import logging

import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.data_interfaces.rsi.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.instance_names

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetUserModeInICO(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to select user mode in ico."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self._reporting = reporting
		self.__android_hmi = android_hmi
		self.__xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="in_car_office")
		self.allowed_parameter_keys = ["MODE"]

	def _action(self) -> bool:
		"""Select user mode in ico.

		1. Check if welcome screen is shown
		2. If first screen(Welcome screen) is shown -> select user mode
		3. If second screen is shown -> go to settings
		4. Check which mode is selected
		5. Select user mode

		:return: True if successful, False otherwise
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		welcome_message_text = self.__xpaths.get_xpath("ico_welcome_screen", "welcome_message_text")
		smartphone_btn = self.__xpaths.get_xpath("ico_welcome_screen", "connect_smaprtphone_btn")
		account_btn = self.__xpaths.get_xpath("ico_welcome_screen", "connect_account_btn")

		wrapper_android_hmi.wait_for_layout_element(welcome_message_text, self.__android_hmi)
		if wrapper_android_hmi.element_exists(welcome_message_text, self.__android_hmi):
			if self.values["MODE"] == "SMARTPHONE":
				self.__android_hmi.click_element(smartphone_btn)
				return True
			if self.values["MODE"] == "CLOUD_MODE" or self.values["MODE"] == "MICROSOFT":
				self.__android_hmi.click_element(account_btn)
				return True

		settings_btn = self.__xpaths.get_xpath("email_overview", "settings_button")
		change_mode_text = self.__xpaths.get_xpath("ico_general_settings", "change_mode_text")
		change_mode_btn = self.__xpaths.get_xpath("ico_general_settings", "change_mode")

		self.__android_hmi.click_element(settings_btn)

		mode_text = wrapper_android_hmi.get_element_by_xpath(change_mode_text, self.__android_hmi, self._reporting).attrib["text"]

		if self.values["MODE"] == "SMARTPHONE":
			if "Smartphone-Anwendung" in mode_text or "smartphone use" in mode_text:
				self.__android_hmi.click_element(change_mode_btn)
		elif self.values["MODE"] == "CLOUD_MODE" or self.values["MODE"] == "MICROSOFT":
			if "Account-Anwendung" in mode_text or "account use" in mode_text:
				self.__android_hmi.click_element(change_mode_btn)

		MODULE_LOGGER.info(f"User mode: {self.values['MODE']} is selected'")

		return True
