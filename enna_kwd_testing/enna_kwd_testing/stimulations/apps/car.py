# -*- coding: utf-8 -*-
"""Module contains stimulation for touching and checking methods of car app."""
import logging
import time

import enna.core.exceptions
import enna.core.component_system.decorators
import enna.core.reporting.interface

import enna_st12.instance_names
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
import enna_st12.data_interfaces.android_hmi.helper
import enna_st12.data_interfaces.android_hmi.exceptions

import enna_hcp_configuration.android.contexts.settings
import enna_hcp_configuration.android.contexts.car
import enna_hcp_configuration.android.xpaths.car

import enna_kwd_testing.stimulations.apps._internal
import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.text_tool.helper
import enna_kwd_testing.stimulations.image_processing.general



MODULE_LOGGER = logging.getLogger(__name__)

# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetAssistantTLI(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation/Deactivation traffic light information in drier assistant systems."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.car.DRIVER_ASSISTANCE_EFFICIENCY
		self._button = enna_hcp_configuration.android.xpaths.car.TRAFFIC_LIGHT_SWITCH

# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetAudiDriveSelect(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	""" Change Drive Select Mode """

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param android_hmi: instance of android hmi control interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, menu_navigation=menu_navigation, android_hmi=android_hmi)
		self.allowed_parameter_keys = ["MODE"]
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _precondition(self) -> bool:
		""" got to drive mode selection screen
		:return: True if navigate to screen was successful
		"""
		return self._go_to_screen(self._get_destination_context("settings.car_audi_drive_select"))

	def _action(self) -> bool:
		""" switch to given drive select mode

		:return: True if success, else False
		"""
		xpath_name = self.values.get("mode")
		if xpath_name is None:
			MODULE_LOGGER.error('Missing parameter : MODE')
			return False

		self._screen_name = self._android_hmi.screen_id.value
		self._xpath = self._get_xpath_by_parameters(xpath_name=xpath_name, screen_name=self._screen_name)

		try:
			self._android_hmi.wait_for_element_visible(xpath=self._xpath, max_time=self._timeout)
			self._android_hmi.click_element(self._xpath)
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException:
			self._reporting.add_report_message_ta_error(f"No connection to android device! Click on element '{self.values}' is not possible.")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' not find in current screen!")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' is currently not clickable!")
			return False
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' not found in screen, during TIMEOUT: {self._timeout}!")
			return False
		self._reporting.add_report_message_info(f"Element '{self.values}' is clicked.")

		time.sleep(1)
		self._android_hmi.wait_for_element_visible(xpath=self._xpath,max_time=3)
		element = enna_st12.data_interfaces.android_hmi.helper._get_element_by_xpath(self._android_hmi.layout.value, self._xpath)

		checked = element.attrib["checked"]=='true'
		if not checked:
			self._reporting.add_report_message_system_error(f"Mode '{xpath_name}' is not selected.")
			return False
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckTextResultInCarSearch(enna_kwd_testing.stimulations.image_processing.general._BaseImageProcessing): # pylint: disable=protected-access
	"""Class containing functionality to Verifies the text."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting)
		self._android_hmi = android_hmi

	def _action(self) -> bool:
		"""Check Search result in global search.
		Expand all groups in search result list.
		Check search result is visible in list.

		:return: True if successful, False if an error occurs in any step.
		"""
		xpath_search_result_list = "//*[@resource-id='de.eso.globalsearch:id/recyclerViewList']"
		xpath_more_button = "//*[contains(@content-desc, '###de.eso.globalsearch:string/result_headline_button_text__show_more')]"
		label = self.values.get("LABEL", "Text is undefined in Test Case. ")
		language = self.values.get("LANG", "de_DE")

		expected_result = enna_kwd_testing.utilities.text_tool.helper.get_text_from_configuration(text_id=label, language=language)
		xpath_expected_result = f"//*[contains(@text, '{expected_result}')]"

		max_retries = 5
		try: # pylint: disable=too-many-try-statements
			time.sleep(0.5)
			self._android_hmi.wait_for_element_visible(xpath=xpath_search_result_list, max_time=15.0)
			# expand all groups inner result list
			while max_retries > 0:
				try:
					self._android_hmi.click_element_in_list(xpath=xpath_more_button, list_container_xpath=xpath_search_result_list)
					time.sleep(0.5)
					self._android_hmi.wait_for_element_visible(xpath=xpath_search_result_list, max_time=1.0)
				except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
					MODULE_LOGGER.info("All search results are expanded.")
					break
				max_retries -= 1
			# scroll to result
			try:
				self._android_hmi.wait_for_element_visible(xpath=xpath_search_result_list, max_time=3.0)
				self._android_hmi.scroll_to_element_in_list(list_container_xpath=xpath_search_result_list, target_xpath=xpath_expected_result)
			except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
				self._reporting.add_report_message_system_error(f"Result '{expected_result}' not found in result list!")
				return False
			time.sleep(0.5)
			coordinates_size = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(layout=self._android_hmi.layout.value, xpath=xpath_expected_result)
			roi = [coordinates_size["x"], coordinates_size["y"], coordinates_size["x"] + coordinates_size["width"], coordinates_size["y"] + coordinates_size["height"]]
			text = self._get_text_from_image(self._android_hmi.take_screenshot().get_roi(mask=roi), language=language)
			if text != expected_result:
				self._reporting.add_report_message_system_error(f"Could not recognize text '{expected_result}' in image!")
				return False

		except (enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException, enna.core.exceptions.TimeoutException, enna.core.exceptions.ImageProcessingException) as error:
			self._reporting.add_report_message_ta_error(f"Could not execution finding search result! {error}")
			return False

		self._reporting.add_report_message_pass(f"Result '{expected_result}' is visible in list")
		return True
