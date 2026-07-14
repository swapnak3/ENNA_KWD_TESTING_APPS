# -*- coding: utf-8 -*-
"""Module contains stimulation for touching and checking methods of phone app."""
import logging
import time

import enna.core.exceptions
import enna.core.component_system.decorators
import enna.core.reporting.interface

import enna_st12.instance_names
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface

import enna_hcp_configuration.android.contexts.phone
import enna_hcp_configuration.android.xpaths.phone

import enna_kwd_testing.utilities.xpath_collection.helper
import enna_kwd_testing.utilities.xpath_collection.exceptions
import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.stimulations.apps._internal


MODULE_LOGGER = logging.getLogger(__name__)



# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetBluetoothState(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation bluetooth of MMI."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.phone.BLUETOOTH_SETTINGS
		self._button = enna_hcp_configuration.android.xpaths.phone.BLUETOOTH_SWITCH_BUTTON


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetSystemWifiState(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation wireless LAN of MMI."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.phone.WIFI_SETTINGS
		self._list_container = enna_hcp_configuration.android.xpaths.phone.MAIN_LIST
		self._button = enna_hcp_configuration.android.xpaths.phone.WIFI_SWITCH_BUTTON


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class DeleteAllBluetoothDevices(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Base class to set switch button"""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, menu_navigation=menu_navigation, android_hmi=android_hmi)
		self._context_device_manager = enna_hcp_configuration.android.contexts.phone.DEVICE_MANAGER
		self._max_count_of_devices = 11


	def _precondition(self) -> bool:
		"""Go to menu of device manager.

		:return: True if success, else False
		"""
		return self._go_to_screen(destination=self._context_device_manager)

	def _action(self) -> bool:
		"""Delete all known devices.

		:return: True if success, else False
		"""
		try:
			app, screen = self._context_device_manager.name.split(".")
			xpath_handler = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app=app)
			settings_button = xpath_handler.get_xpath(screen=screen, element="device_settings_button")
			no_devices = xpath_handler.get_xpath(screen=screen, element="no_device_connected")
			device_options_list = xpath_handler.get_xpath(screen="device_manager_device_options", element="scroll_container")
			delete_button = xpath_handler.get_xpath(screen="device_manager_device_options", element="delete_button")
			close_button = xpath_handler.get_xpath(screen="device_manager_device_options", element="close_button")
		except (enna_kwd_testing.utilities.xpath_collection.exceptions.ElementNotFound, ValueError) as error:
			self._reporting.add_report_message_ta_error(f"Missing necessary xpath in collection! Error: {error}")
			return False


		while len(self._android_hmi.layout.value.xpath(no_devices)) <= 0:
			try:
				self._android_hmi.click_element(xpath=settings_button)
				self._android_hmi.wait_for_element_visible(xpath=device_options_list, max_time=3.0)

				self._android_hmi.click_element_in_list(xpath=delete_button, list_container_xpath=device_options_list)

				try:
					self._android_hmi.wait_for_element_visible(xpath=no_devices, max_time=3.0)
					break
				except enna.core.exceptions.TimeoutException:
					if self._max_count_of_devices <= 0:
						self._reporting.add_report_message_system_error("Could not delete all devices! Please check all devices are deletable.")
						return False
					MODULE_LOGGER.debug("Delete next device")
					self._max_count_of_devices -= 1
					if len(self._android_hmi.layout.value.xpath(close_button)) > 0:
						self._android_hmi.click_element(close_button)
						time.sleep(5.0) # delay toast disappear
					continue

			except (enna.core.exceptions.TimeoutException, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as error:
				self._reporting.add_report_message_ta_error(f"Could not delete bluetooth devices! Error: {error}")
				return False

		self._reporting.add_report_message_pass("All bluetooth devices are deleted.")
		return True
