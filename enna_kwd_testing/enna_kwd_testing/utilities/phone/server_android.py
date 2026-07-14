# -*- coding: utf-8 -*-
"""Module contains server for control a android phone."""
import logging
import os.path
import re
import typing
from datetime import datetime
from pathlib import Path

import enna.core.config
import enna.core.exceptions
import enna.core.image_processing.helper
import enna.core.image_processing.image
import enna.core.interfaces.server
import enna.core.logger
import enna_st12.data_interfaces.android_hmi
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.data_interfaces.android_hmi.helper
import numpy
import uiautomator2
import uiautomator2.exceptions
from enna.core import helper

import enna_kwd_testing.utilities.phone.exceptions
import enna_kwd_testing.utilities.phone.interface
from enna_kwd_testing.definitions import TEMP_PATH
from enna_kwd_testing.utilities.image_helper.helper import template_matching_opencv

INSTANCE_CONFIG = enna.core.config.get_instance_config(__name__)
MODULE_LOGGER = logging.getLogger(__name__)

# pylint: disable=too-many-public-methods,too-many-branches


class Server(enna_kwd_testing.utilities.phone.interface.Interface, enna.core.interfaces.server.Server):
	"""Provide access for controlling an android device."""

	def __init__(self, instance_name) -> None:
		"""Constructor for interface to an android device.

		:param str instance_name: mame of implementation instance
		"""
		self._instance_name = instance_name
		enna_kwd_testing.utilities.phone.interface.Interface.__init__(self)
		enna.core.interfaces.server.Server.__init__(self, instance_name=self._instance_name)
		self.__instance_logger = enna.core.logger.InstanceLogger(MODULE_LOGGER, self._instance_name)
		self.__read_instance_configuration()
		self.__device: uiautomator2.Device | None = None
		self.__display_id: int = 0

		self.connect()
		self._set_online()

	_xpath_to_selector_regex_main = re.compile(r"(?P<classname>//[.a-zA-Z*0-9]+)(?P<equals>(\[@.*?=.*?])*(\)\[(?P<instance>\d+)])*)")
	_xpath_to_selector_regex_with_contains = re.compile(r"contains+.@(.*?),\s*(['\"].*?['\"])")
	_xpath_to_selector_regex_attributes = re.compile(r"\[@(.*?)=(.*?)]")
	_xpath_to_selector_key_replacer = {
		"text": "text",
		"class": "className",
		"content-desc": "description",
		"checkable": "checkable",
		"checked": "checked",
		"clickable": "clickable",
		"long-clickable": "longClickable",
		"scrollable": "scrollable",
		"enabled": "enabled",
		"focusable": "focusable",
		"focused": "focused",
		"selected": "selected",
		"package": "packageName",
		"resource-id": "resourceId",
		"index": "index",
		"display-id": "displayId"
	}

	def __safely_save_ui_dump_and_raise_exc(self, exc: type, error_message: str, tag: str) -> typing.NoReturn:
		"""Save the UI layout, while making sure it doesn't crash if adb connection is lost, and raise the given exception type with the error message.

		:param exc: Exception type
		:param error_message: Error message for logging and exception raising
		:param tag: Info tag that is added to the file name
		"""
		try:
			xml = self.__device.dump_hierarchy()

			path = enna.core.logger.LOG_PATH.parent.joinpath("ui_layout")
			if not path.exists():
				path.mkdir(parents=True)

			# Use .uix and .png file extensions instead of .xml and .jpg, as the uiautomator viewer file selection widgets forces these extensions.
			# To save disk space, the jpg encoding is used instead of png.
			# Despite the file selection widget limitation, the uiautomator viewer can cope with other image formats such as jpg and is able to open them in spite of the .png file extension.
			layout_file_name = path.joinpath(f"{datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")}{f"_{tag}" if tag else ""}.uix")
			screenshot_file_name = layout_file_name.with_suffix(".png")
			try:
				with open(layout_file_name, "w", encoding="utf-8") as layout_file:
					layout_file.write(xml)
			except Exception:  # pylint: disable = broad-exception-caught
				error_message += f"Could not save UI layout {layout_file_name}"

			try:
				with open(screenshot_file_name, "wb") as screenshot_file:
					screenshot_file.write(self.take_screenshot().get_bytearray(ext=".jpg"))
			except Exception:  # pylint: disable = broad-exception-caught
				error_message += f"Could not save UI screenshot {screenshot_file_name}"
		except Exception as ex:  # pylint: disable = broad-exception-caught
			error_message += f"Failed to save UI dump due to error: {ex}"

		raise exc(error_message)

	def _translate_xpath_to_kwargs(self, xpath: str) -> dict[str, str]:
		"""Translate an XPath expression into the Android selector expression equivalent.

		:param str xpath: the xpath to translate
		:return: the corresponding Android selector expression as a dict
		:raises enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException: if the expression cannot be translated
		"""
		result = {}

		if regex_main_result := self._xpath_to_selector_regex_main.search(xpath):
			if (class_available := regex_main_result.group("classname")) and class_available != "//*":
				result["className"] = regex_main_result.group("classname").replace(r"/", "")

			if regex_main_result.group("equals"):
				matched_attributes = self._xpath_to_selector_regex_attributes.findall(str(regex_main_result.group("equals")))
				for attribute in matched_attributes:
					if (matched_attribute := self._xpath_to_selector_key_replacer.get(attribute[0])) is None:
						raise enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException(f"Invalid attribute '{attribute[0]}' for this function. Valid XPath attributes are {list(self._xpath_to_selector_key_replacer)}")
					result[matched_attribute] = attribute[1].replace(r'"', "").replace(r"'", "")

			if regex_main_result.group("instance"):
				result["instance"] = int(regex_main_result.group("instance").replace(r'"', "").replace(r"'", ""))

		if regex_contains_result := self._xpath_to_selector_regex_with_contains.findall(xpath):
			for contains_xpath in regex_contains_result:
				if contains_xpath[0] == "content-desc":
					result["descriptionContains"] = contains_xpath[1].replace(r'"', "").replace(r"'", "")
				elif contains_xpath[0] == "text":
					result["textContains"] = contains_xpath[1].replace(r'"', "").replace(r"'", "")
				elif contains_xpath[0] == "resource-id":
					result["resourceIdContains"] = contains_xpath[1].replace(r'"', "").replace(r"'", "")
				else:
					raise enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException(
						f"Invalid XPath {xpath} for this function. XPaths that includes 'contains' are only supported for 'content-desc', 'text' or 'resource-id' XPaths.")

		if matched_attributes := self._xpath_to_selector_regex_attributes.findall(xpath):
			for attribute in matched_attributes:
				if (matched_attribute := self._xpath_to_selector_key_replacer.get(attribute[0])) is None:
					raise enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException(f"Invalid attribute '{attribute[0]}' for this function. Valid XPath attributes are {list(self._xpath_to_selector_key_replacer)}")
				result[matched_attribute] = attribute[1].replace(r'"', "").replace(r"'", "")

		if not result:
			raise enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException(f"Can't parse {xpath}, must be a [contains(@key, 'value')] (only for key == 'content-desc' or 'text') or a [@key=value] XPath.")

		return result

	def __read_instance_configuration(self):
		"""Reading instance config for phone.

		:raises enna.core.exceptions.ConfigurationException:
		"""
		try:
			self.__serial_number = INSTANCE_CONFIG[self._instance_name]["serial"]
		except KeyError:
			msg = f"No found serial number for this phone '{self._instance_name}'! Pleas check your instance configuration file."
			self.__instance_logger.exception(msg)
			raise enna.core.exceptions.ConfigurationException(msg)

	def __get_element_by_xpath(self, xpath: str, caller_name: str) -> uiautomator2.xpath.XPathSelector:
		"""Query uiautomator2 to find an element using uiautomator2.xpath.XPathSelector.

		:param str xpath: xpath which describes the element
		:param caller_name: name of caller function for naming UI dump files
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if element is not found
		:return: the element
		"""
		element = self.__device.xpath(xpath, self.__display_id)
		if element.exists:
			return element

		self.__safely_save_ui_dump_and_raise_exc(enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException, f"The element with XPath {xpath} does not exist in the UI layout!", caller_name)

	def __check_element_enabled(self, elem: uiautomator2.xpath.XPathSelector, xpath: str, caller_name: str) -> None:
		"""Provide a helper which raises if an element cannot be interacted with based on the current UI layout. Currently, it must be enabled.

		:param elem: the element to check
		:param str xpath: xpath for logging purposes
		:param str caller_name: name of caller function for naming UI dump files
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException: if element is not enabled
		"""
		if not enna.core.helper.strtobool(elem.attrib["enabled"]):
			self.__safely_save_ui_dump_and_raise_exc(enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException, f"The element with XPath {xpath} is not enabled!", caller_name)

	def get_package_name_short(self):
		"""Get Short Package Name of controlled App

		:return: Short Package name
		:rtype: str
		"""
		return INSTANCE_CONFIG[self._instance_name]["package_name_short"]

	def get_package_name_long(self):
		"""Get Long Package Name of controlled App

		:return: Long Package name
		:rtype: str
		"""
		return INSTANCE_CONFIG[self._instance_name]["package_name_long"]

	def get_app_version(self):
		"""Get App-Version of controlled App

		:return: App-Version
		:rtype: str
		"""
		return INSTANCE_CONFIG[self._instance_name]["app_version"]

	def get_device(self):
		"""Get the device which is related to the phone

		:return: Phone device
		:rtype: uiautomator2.Device
		"""
		return self.__device

	def connect(self) -> None:
		"""Connect to a phone.

		:raises enna_kwd_testing.utilities.phone.NoDeviceConnectedException: if the connection attempt fails
		"""
		if self.connected.value:
			self.__instance_logger.debug(f"Device '{self.__serial_number}' is already connected.")
			return
		try:
			self.__device = uiautomator2.connect_usb(serial=self.__serial_number)
		except uiautomator2.ConnectError as err:
			msg = f"Connection to device '{self.__serial_number}' is failed!"
			self.__instance_logger.exception(msg)
			self.__instance_logger.exception(err)
			raise enna_kwd_testing.utilities.phone.exceptions.NoDeviceConnectedException(msg)
		self._connected = enna.core.interfaces.Data(True)
		self._signal_property("connected", self.connected)
		self.__instance_logger.info(f"Device '{self.__serial_number}' is connect.")

	def disconnect(self) -> None:
		"""Disconnect from phone."""
		if self.connected.value:
			self._connected = enna.core.interfaces.Data(False)
			self._signal_property("connected", self.connected)
			self.__instance_logger.info(f"Disconnecting device '{self.__serial_number}'.")

	def finalize(self) -> None:
		"""Finalize connection to Phone."""
		self.disconnect()
		enna.core.interfaces.server.Server.finalize(self)

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def take_screenshot(self, save_path: Path = None) -> enna.core.image_processing.image.Image:
		"""Take a screenshot from connected phone.

		:param Path save_path: Optional Path for saving the screenshot
		:return: a screenshot as an ENNA image
		:raises enna_kwd_testing.utilities.phone.exceptions.PhoneInterfaceException: if failed to save screenshot from passenger display
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		try:
			screenshot = enna.core.image_processing.image.Image(self.__device.screenshot(format="opencv"))

			image_save_path = save_path if save_path is not None else TEMP_PATH / "temp_image_take_screenshot"
			enna.core.image_processing.helper.save_image(screenshot, path=image_save_path, file_extension=".png")
		except (enna.core.exceptions.ImageProcessingException, IOError, SyntaxError, ValueError) as exc:
			MODULE_LOGGER.error(msg := f"{exc}: Taking screenshot of device failed")
			raise enna_kwd_testing.utilities.phone.exceptions.PhoneInterfaceException(msg)
		return screenshot

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def take_screenshot_of_element(self, xpath: str, save_path: Path = None) -> enna.core.image_processing.image.Image:
		"""Take a screenshot of an element.

		:param str xpath: XPATH to the element, which should be screenshotted
		:param Path save_path: Optional Path for saving the screenshot
		:return: a screenshot as an ENNA image
		:raises enna_kwd_testing.utilities.phone.exceptions.PhoneInterfaceException: if failed to save screenshot from passenger display
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		element = self.__get_element_by_xpath(xpath, self.take_screenshot_of_element.__name__)
		screenshot = enna.core.image_processing.image.Image(numpy.array(element.screenshot()))

		image_save_path = save_path if save_path is not None else TEMP_PATH / "temp_image_take_screenshot_of_element"
		enna.core.image_processing.helper.save_image(screenshot, path=image_save_path, file_extension=".png")
		return screenshot

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def get_active_package_name(self) -> str:
		"""Get the package name of the currently running foreground application.

		:return: the name of the current foreground application
		:raises enna_kwd_testing.utilities.phone.exceptions.PhoneInterfaceException: if getting active app failed
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		try:
			app_info = self.__device.app_current()
			return app_info['package']
		except OSError as exc:
			MODULE_LOGGER.error(msg := f"{exc}: Getting focused app failed")
			raise enna_kwd_testing.utilities.phone.exceptions.PhoneInterfaceException(msg)

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def start_app_by_package_name(self, package_name: str) -> bool:
		"""Start an App by its package name

		:param str package_name: package which should be started
		:return: True if app was started. False, otherwise.
		:rtype: bool
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		self.__device.app_start(package_name)
		return self.__device.app_wait(package_name, front=True) > 0

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def stop_app_by_package_name(self, package_name: str, clear_cache: bool = False):
		"""Stop an App by its package name

		:param str package_name: package which should be stopped
		:param bool clear_cache: Should cache be cleared?
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		self.__device.app_stop(package_name)
		if clear_cache:
			self.__device.app_clear(package_name)

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def put_app_in_background(self):
		"""Put App in Background / Goto Home Screen

		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		self.__device.press(key="home")

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def open_recent_apps(self):
		"""Open recently opened Apps

		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		self.__device.press(key="recent")

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def click_back_button(self):

		"""Click Back-Button of Android-OS
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		self.__device.press(key="back")

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def click_element(self, xpath: str) -> None:
		"""Click on an element as defined by an XPath expression.

		:param str xpath: xpath of the element to click
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException: if the element is not enabled
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		element = self.__get_element_by_xpath(xpath, self.click_element.__name__)
		self.__check_element_enabled(element, xpath, self.click_element.__name__)
		element.click()

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def get_element_text(self, xpath: str) -> str:
		"""Get text of an element.

		:param str xpath: Element where Text should be read
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		:return: Text of the element
		:rtype: str
		"""
		element = self.__get_element_by_xpath(xpath, self.get_element_text.__name__)
		return element.attrib["text"]

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def set_element_text(self, xpath: str, text: str, clear: bool = True) -> None:
		"""Send text to an element.

		:param str xpath: Element where Text should be set
		:param str text: text that is sent to the text box
		:param bool clear: If True, clear input field before entering text
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		element = self.__get_element_by_xpath(xpath, self.set_element_text.__name__)
		if clear:
			element.set_text(text)
		else:
			element.set_text(element.attrib["text"] + text)

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def set_toggle_button_state(self, xpath: str, button_state: bool) -> None:
		"""Set the state of a toggle button (Switch-Button or Checkbox) as a boolean value.

		:param str xpath: xpath of the toggle button to interact with
		:param bool button_state: toggle button state to set
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		element = self.__get_element_by_xpath(xpath, self.click_element.__name__)
		self.__check_element_enabled(element, xpath, self.click_element.__name__)

		checked_state_now = helper.strtobool(element.get().attrib["checked"])
		if checked_state_now and not button_state:  # Checked, but should be unchecked
			element.click()
		elif not checked_state_now and button_state:  # Unchecked, but should be checked
			element.click()

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def scroll_list_to_top(self, list_container_xpath: str) -> None:
		"""Scroll to the top of a list container.

		If the container is not scrollable, this method will do nothing.

		:param str list_container_xpath: xpath expression for the list container
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException: if the expression cannot be translated
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		list_container_element = self.__get_element_by_xpath(list_container_xpath, self.scroll_list_to_top.__name__)
		scrollable_state = enna.core.helper.strtobool(list_container_element.get().attrib["scrollable"])

		if not scrollable_state:
			self.__instance_logger.exception(f"The list container with xpath {list_container_xpath} is not scrollable, not executing a scroll to top")
			return

		list_container_xpath_translated = self._translate_xpath_to_kwargs(list_container_xpath)
		self.__device(**list_container_xpath_translated).fling.toBeginning()
		# self.__device(**list_container_xpath_translated).scroll.toBeginning()

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def scroll_list_to_bottom(self, list_container_xpath: str) -> None:
		"""Scroll to the end of a list container.

		If the container is not scrollable, this method will do nothing.

		:param str list_container_xpath: xpath expression for the list container
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException: if the expression cannot be translated
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		list_container_element = self.__get_element_by_xpath(list_container_xpath, self.scroll_list_to_bottom.__name__)
		scrollable_state = enna.core.helper.strtobool(list_container_element.get().attrib["scrollable"])

		if not scrollable_state:
			self.__instance_logger.exception(f"The list container with xpath {list_container_xpath} is not scrollable, not executing a scroll to top")
			return

		list_container_xpath_translated = self._translate_xpath_to_kwargs(list_container_xpath)
		self.__device(**list_container_xpath_translated).fling.toEnd()
		# self.__device(**list_container_xpath_translated).scroll.toEnd()

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def scroll_to_element_in_list(self, list_container_xpath: str, target_xpath: str) -> None:
		"""Scroll to an element within a scrollable container.

		If the container is not scrollable, this method will do nothing.

		:param str list_container_xpath: XPath expression for the list container
		:param str target_xpath: XPath expression for the target element within the list
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException: if the expression cannot be translated
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		self.scroll_list_to_top(list_container_xpath)

		list_container_xpath_translated = self._translate_xpath_to_kwargs(list_container_xpath)
		list_container_element = self.__device(**list_container_xpath_translated)

		# Scroll to element in List
		target_xpath_translated = self._translate_xpath_to_kwargs(target_xpath)
		list_container_element.scroll_to(**target_xpath_translated)

		# Check if element is visible after scrolling
		if not self.element_is_visible(target_xpath):
			raise enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException(f"Element with xpath {target_xpath} was not found in list with xpath {list_container_xpath}")

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def click_element_in_list(self, list_container_xpath: str, target_xpath: str) -> None:
		"""Click on an element within a list.

		This method will scroll the target element into view before clicking on it.

		:param str list_container_xpath: XPath expression for the list container
		:param str target_xpath: XPath expression for the target element within the list
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException: if the expression cannot be translated
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		self.scroll_to_element_in_list(list_container_xpath, target_xpath)
		self.click_element(target_xpath)

	def select_screen(self, deep_link_url: str):
		"""Select screen by given deeplink (intent uri).

		:param str deep_link_url: deeplink for specific screen.
		"""
		MODULE_LOGGER.info(f"Select screen with following url '{self.get_package_name_short()}://appNavigation{deep_link_url}'")
		# Working example: device.shell(f"adb shell am start -a android.intent.action.VIEW -d \"myaudi-p://appNavigation/loggedIn/vehicleDashboard/BAUPSWF4823041101/remoteAuxiliaryHeating/quickStartOrQuickStop\"")
		response = self.__device.shell(f"am start -a android.intent.action.VIEW -d \"{self.get_package_name_short()}://appNavigation/{deep_link_url}\"")
		MODULE_LOGGER.debug(response)

	def image_is_visible_on_element(self, xpath: str, template_image_path: str) -> bool:
		"""Check if a template image is visible on a specific element on the screen

		:param str xpath: XPATH to the element, which should be screenshotted
		:param str template_image_path: Path to the image template which should be searched
		:raises enna_kwd_testing.utilities.phone.exceptions.PhoneInterfaceException: if failed to save screenshot from passenger display
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		:return: True if template matches. False, otherwise.
		:rtype: bool
		"""
		element_image = self.take_screenshot_of_element(xpath)
		image_save_path = TEMP_PATH / "temp_image_is_visible_on_element"
		enna.core.image_processing.helper.save_image(element_image, path=image_save_path, file_extension=".png")

		template_image = f"{template_image_path}.png"
		if os.path.isfile(template_image):
			return template_matching_opencv(f"{image_save_path}.png", template_image)

		raise enna_kwd_testing.utilities.phone.exceptions.FileNotFoundException(f"Template-Image at path '{template_image}]' does not exists")

	def image_is_visible_on_screen(self, template_image_path: str) -> bool:
		"""Check if a template image is visible on the screen

		:param str template_image_path: Path to the image template which should be searched
		:raises enna_kwd_testing.utilities.phone.exceptions.PhoneInterfaceException: if failed to save screenshot from passenger display
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		:return: True if template matches. False, otherwise.
		:rtype: bool
		"""
		screenshot = self.take_screenshot()
		image_save_path = TEMP_PATH / "temp_image_is_visible_on_screen"
		enna.core.image_processing.helper.save_image(screenshot, path=image_save_path, file_extension=".png")

		template_image = f"{template_image_path}.png"
		if os.path.isfile(template_image):
			return template_matching_opencv(f"{image_save_path}.png", template_image)

		raise enna_kwd_testing.utilities.phone.exceptions.FileNotFoundException(f"Template-Image at path '{template_image}]' was not found")

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def element_is_visible(self, xpath: str) -> bool:
		"""Check if element is visible on screen

		:param str xpath: xpath of the element to wait for
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		:return: True if element is visible. False, otherwise.
		:rtype: bool
		"""
		try:
			self.__get_element_by_xpath(xpath, self.element_is_visible.__name__)
			return True
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			return False

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def element_is_enabled(self, xpath: str) -> bool:
		"""Check if element is enabled on screen

		:param str xpath: xpath of the element to wait for
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:return: True if element is enabled. False, otherwise.
		:rtype: bool
		"""
		element = self.__get_element_by_xpath(xpath, self.element_is_enabled.__name__)
		return enna.core.helper.strtobool(element.attrib["enabled"])

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def element_is_selected(self, xpath: str) -> bool:
		"""Check if element is selected on screen

		:param str xpath: xpath of the element to wait for
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:return: True if element is selected. False, otherwise.
		:rtype: bool
		"""
		element = self.__get_element_by_xpath(xpath, self.element_is_selected.__name__)
		return enna.core.helper.strtobool(element.attrib["selected"])

	@enna.core.helper.call_if_connected(exc=enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException)
	def element_is_checked(self, xpath: str) -> bool:
		"""Check if element is checked on screen

		:param str xpath: xpath of the element to wait for
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:return: True if element is checked. False, otherwise.
		:rtype: bool
		"""
		element = self.__get_element_by_xpath(xpath, self.element_is_checked.__name__)
		return enna.core.helper.strtobool(element.attrib["checked"])

	def scroll_horizontal_right(self, list_container_xpath: str):
		"""Scroll horizontally to the right side

		:param str list_container_xpath: xpath expression for the list container
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException: if the expression cannot be translated
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		list_swipe_container_xpath_translated = self._translate_xpath_to_kwargs(list_container_xpath)
		self.__device(**list_swipe_container_xpath_translated).scroll.horiz.forward()

	def scroll_horizontal_left(self, list_container_xpath: str):
		"""Scroll horizontally to the left side

		:param str list_container_xpath: xpath expression for the list container
		:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the element was not found in the UI layout
		:raises enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException: if the expression cannot be translated
		:raises enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException: if the android device is not connected, or the connection fails
		"""
		list_swipe_container_xpath_translated = self._translate_xpath_to_kwargs(list_container_xpath)
		self.__device(**list_swipe_container_xpath_translated).scroll.horiz.backward()
