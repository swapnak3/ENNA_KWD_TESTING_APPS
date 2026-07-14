# -*- coding: utf-8 -*-
"""The interface from which each proxy and server in this package derive."""

import abc
from pathlib import Path

import enna.core.component_system.decorators
import enna.core.image_processing.image
import enna.core.interfaces.component


# pylint: disable=too-many-public-methods


@enna.core.component_system.decorators.GenerateProxy()
class Interface(enna.core.interfaces.component.Component):
	"""Abstract phone interface."""

	def __init__(self) -> None:
		"""Android server interface initialize."""
		self._connected = enna.core.interfaces.Data(False)

	@abc.abstractmethod
	def get_package_name_short(self):
		"""Get Short Package Name of controlled App"""

	@abc.abstractmethod
	def get_package_name_long(self):
		"""Get Long Package Name of controlled App"""

	@abc.abstractmethod
	def get_app_version(self):
		"""Get App-Version of controlled App"""

	@abc.abstractmethod
	def get_device(self):
		"""Get the device which is related to the phone"""

	@abc.abstractmethod
	def connect(self) -> None:
		"""Connect to a phone.

		:raises enna_kwd_testing.utilities.phone.NoDeviceConnectedException: if the connection attempt fails
		"""

	@abc.abstractmethod
	def disconnect(self) -> None:
		"""Disconnect from phone."""

	@abc.abstractmethod
	def finalize(self) -> None:
		"""Finalize connection to Phone."""

	@property
	def connected(self) -> enna.core.interfaces.Data[bool]:
		"""Get uiautomator connection state to phone.

		:return: True if automation connected, False otherwise
		"""
		return self._connected

	@abc.abstractmethod
	def take_screenshot(self, save_path: Path = None) -> enna.core.image_processing.image.Image:
		"""Take a screenshot from connected phone.

		:param Path save_path: Optional Path for saving the screenshot
		:return: a screenshot as an ENNA image
		:raises enna_kwd_testing.utilities.phone.exceptions.PhoneInterfaceException: if failed to save screenshot from passenger display
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def take_screenshot_of_element(self, xpath: str, save_path: Path = None) -> enna.core.image_processing.image.Image:
		"""Take a screenshot of an element.

		:param str xpath: XPATH to the element, which should be screenshotted
		:param Path save_path: Optional Path for saving the screenshot
		:return: a screenshot as an ENNA image
		:raises enna_kwd_testing.utilities.phone.exceptions.PhoneInterfaceException: if failed to save screenshot from passenger display
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def get_active_package_name(self) -> str:
		"""Get the package name of the currently running foreground application.

		:return: the name of the current foreground application
		:raises enna_kwd_testing.utilities.phone.exceptions.PhoneInterfaceException: if getting active app failed
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def start_app_by_package_name(self, package_name: str) -> bool:
		"""Start an App by its name

		:param str package_name: package which should be started
		:return: True if app was started. False, otherwise.
		:rtype: bool
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def stop_app_by_package_name(self, package_name: str, clear_cache: bool = False):
		"""Stop an App by its name

		:param str package_name: package which should be stopped
		:param bool clear_cache: Should cache be cleared?
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def put_app_in_background(self):
		"""Put App in Background / Goto Home Screen

		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def open_recent_apps(self):
		"""Open recently opened Apps

		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def click_back_button(self):
		"""Click Back-Button of Android-OS

		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def click_element(self, xpath: str) -> None:
		"""Click on an element as defined by an XPath expression.

		:param str xpath: xpath of the element to click
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException: if the element is not enabled
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def get_element_text(self, xpath: str) -> str:
		"""Get text of an element.

		:param str xpath: Element where Text should be read
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def set_element_text(self, xpath: str, text: str, clear: bool = True) -> None:
		"""Send text to an element.

		:param str xpath: Element where Text should be set
		:param str text: text that is sent to the text box
		:param bool clear: If True, clear input field before entering text
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def set_toggle_button_state(self, xpath: str, button_state: bool) -> None:
		"""Set the state of a toggle button as a boolean value.

		:param str xpath: xpath of the toggle button to interact with
		:param bool button_state: new state to set
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def scroll_list_to_top(self, list_container_xpath: str) -> None:
		"""Scroll to the top of a list container.

		If the container is not scrollable, this method will do nothing.

		:param str list_container_xpath: xpath expression for the list container
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException: if the expression cannot be translated
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def scroll_list_to_bottom(self, list_container_xpath: str) -> None:
		"""Scroll to the end of a list container.

		If the container is not scrollable, this method will do nothing.

		:param str list_container_xpath: xpath expression for the list container
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException: if the expression cannot be translated
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def scroll_to_element_in_list(self, list_container_xpath: str, target_xpath: str) -> None:
		"""Scroll to an element within a scrollable container.

		If the container is not scrollable, this method will do nothing.

		:param str list_container_xpath: XPath expression for the list container
		:param str target_xpath: XPath expression for the target element within the list
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException: if the expression cannot be translated
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def click_element_in_list(self, list_container_xpath: str, target_xpath: str) -> None:
		"""Click on an element within a list.

		This method will scroll the target element into view before clicking on it.

		:param str list_container_xpath: XPath expression for the list container
		:param str target_xpath: XPath expression for the target element within the list
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException: if the expression cannot be translated
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def select_screen(self, deep_link_url: str):
		"""Select screen by given deeplink (intent uri).

		:param deep_link_url: deeplink for specific screen.
		"""

	@abc.abstractmethod
	def image_is_visible_on_element(self, xpath: str, template_image_path: str) -> bool:
		"""Check if a template image is visible on a specific element on the screen

		:param str xpath: XPATH to the element, which should be screenshotted
		:param str template_image_path: Path to the image template which should be searched
		:raises enna_kwd_testing.utilities.phone.exceptions.PhoneInterfaceException: if failed to save screenshot from passenger display
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		:return: True if template matches. False, otherwise.
		:rtype: bool
		"""

	@abc.abstractmethod
	def image_is_visible_on_screen(self, template_image_path: str) -> bool:
		"""Check if a template image is visible on the screen

		:param str template_image_path: Path to the image template which should be searched
		:raises enna_kwd_testing.utilities.phone.exceptions.PhoneInterfaceException: if failed to save screenshot from passenger display
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		:return: True if template matches. False, otherwise.
		:rtype: bool
		"""

	@abc.abstractmethod
	def element_is_visible(self, xpath: str) -> bool:
		"""Check if element is visible on screen

		:param str xpath: xpath of the element to wait for
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def element_is_enabled(self, xpath: str) -> bool:
		"""Check if element is enabled on screen

		:param str xpath: xpath of the element to wait for
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises
		"""

	@abc.abstractmethod
	def element_is_selected(self, xpath: str) -> bool:
		"""Check if element is selected on screen

		:param str xpath: xpath of the element to wait for
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises
		"""

	@abc.abstractmethod
	def element_is_checked(self, xpath: str) -> bool:
		"""Check if element is checked on screen

		:param str xpath: xpath of the element to wait for
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises
		"""

	@abc.abstractmethod
	def scroll_horizontal_right(self, list_container_xpath: str):
		"""Scroll horizontally to the right side

		:param str list_container_xpath: xpath expression for the list container
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException: if the expression cannot be translated
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""

	@abc.abstractmethod
	def scroll_horizontal_left(self, list_container_xpath: str):
		"""Scroll horizontally to the left side

		:param str list_container_xpath: xpath expression for the list container
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException: if the expression cannot be translated
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
