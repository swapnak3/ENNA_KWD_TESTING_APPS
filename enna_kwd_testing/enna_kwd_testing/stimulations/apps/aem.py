# -*- coding: utf-8 -*-
"""Created on 24.01.2024.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Teubner Claus.

Contains stimulation for keyword driven testing in context of android_hmi aem functions.
"""

import logging
import os

import enna.core.component_system.decorators
import enna.core.config
import enna.core.exceptions
import enna.core.reporting.interface
import enna.data_interfaces.adb.interface

import enna_st12.instance_names
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import assistant, settings

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.stimulations.apps._internal
import enna_kwd_testing.utilities.xpath_collection.helper
import enna_kwd_testing.utilities.xpath_collection.exceptions


MODULE_LOGGER = logging.getLogger(__name__)
VIN_CONFIG = enna.core.config.get("enna.core.vin.common")

# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetAemGdaDeveloperSettingsOnlineVin(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Class containing functionality to set vin in aem - GDA Developer Settings - Online and Connectivity."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Initialize stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=self._reporting, menu_navigation=menu_navigation, android_hmi=android_hmi)
		self._xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="aem_gda")
		self.allowed_parameter_keys = []
		self._keyboard_xpath = "//*[@resource-id='com.audi.automotive.input:id/keyboardViewEx']"


	def _action(self) -> bool:
		"""Execute action.

		set VIN in aem_gda.online_and_connectivity.

		1. Navigate to 'aem_gda.ONLINE_AND_CONNECTIVITY' screen
		2. Enter VIN from config enna.core.vin.common with edit text

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		test_cube_name = os.environ.get("TestCubeName", "unknown")
		vin: str | None = VIN_CONFIG.get(test_cube_name, None)

		if vin is None:
			self._reporting.add_report_message_ta_error(f"Not found a VIN for TestCubeName: '{test_cube_name}'! Please Check TestCubeName in Config.")
			return False
		# pylint: disable=too-many-try-statements
		try:
			if not self._go_to_screen(destination=assistant.AEM_GDA_ONLINE_AND_CONNECTIVITY):
				return False
			online_and_connectivity_list_xpath = self._xpaths.get_xpath("online_and_connectivity", "recyclerviewlist")
			vin_edit_xpath: str = self._xpaths.get_xpath("online_and_connectivity", "vin_edit")
			vin_input_xpath: str = self._xpaths.get_xpath("online_and_connectivity", "vin_edit_input_field")
			vin_save_xpath: str = self._xpaths.get_xpath("online_and_connectivity", "vin_save")
			self._android_hmi.wait_for_element_visible(xpath=online_and_connectivity_list_xpath, max_time=3.0)
			self._android_hmi.click_element_in_list(list_container_xpath=online_and_connectivity_list_xpath, xpath=vin_edit_xpath)
			self._android_hmi.wait_for_element_visible(xpath=vin_input_xpath, max_time=3.0) # open keyboard
			self._android_hmi.click_element(xpath=vin_input_xpath)
			self._android_hmi.wait_for_element_visible(xpath=self._keyboard_xpath, max_time=3.0)
			self._android_hmi.enter_text(text=vin, clear=True) # enter text if keyboard is open
			self._android_hmi.click_element(xpath=vin_save_xpath)
			if not self._go_to_screen(destination=settings.APPS_APP_INFO_VIEWALL_AUDI_ASSISTANT):
				return False
			self._xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="settings")
			force_stop_xpath: str = self._xpaths.get_xpath("APP_INFO_VIEWALL_AUDI_ASSISTANT", "FORCE_STOP")
			ok_button: str = self._xpaths.get_xpath("APP_INFO_VIEWALL_AUDI_ASSISTANT", "BUTTON_OK")
			self._android_hmi.wait_for_element_visible(xpath=force_stop_xpath, max_time=3.0)
			self._android_hmi.click_element(xpath=force_stop_xpath)
			self._android_hmi.wait_for_element_visible(xpath=ok_button, max_time=3.0)
			self._android_hmi.click_element(xpath=ok_button)
		except enna_kwd_testing.utilities.xpath_collection.exceptions.ElementNotFound as error:
			self._reporting.add_report_message_ta_error(f"Xpath not found in config! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException:
			self._reporting.add_report_message_ta_error("No Android device connected!")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException as error:
			self._reporting.add_report_message_ta_error(f"Invalid argument to Android HMI! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException as error:
			self._reporting.add_report_message_system_error(f"UI-Element not found! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException as error:
			self._reporting.add_report_message_system_error(f"Element is not clickable! {error}")
			return False
		except enna.core.exceptions.TimeoutException as error:
			self._reporting.add_report_message_system_error(f"Timeout by search element in screen! {error}")
			return False
		self._reporting.add_report_message_pass(f"VIN '{vin}' is set in GDA Developer Settings.")
		return True
