# -*- coding: utf-8 -*-
"""Created on 01.03.2022.

@project: enna_tc_connect_apps_hcp3.
@author: DYX34ZN: Jakob Kein.

Wrapper for some basic functionalities including the corresponding exception handling with default error messages for logging and reporting.
"""
import base64
import logging
import lxml.etree

import enna.core.exceptions
import enna.core.helper
import enna.core.reporting.interface
import enna.core.time

import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.data_interfaces.android_hmi.helper
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.exceptions
import enna_st12.utilities.menu_navigation.interface

import enna_hcp_configuration.common.base
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.decorators.logging import logdecorator
from enna_kwd_testing.utilities.helper import android_hmi_helper

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=protected-access, too-many-positional-arguments
@logdecorator(MODULE_LOGGER)
def wait_for_layout_element(xpath: str, android: enna_st12.data_interfaces.android_hmi.interface.Interface,
							additional_message="", max_time: float = 10) -> bool:
	"""Wrap the functionality to wait for an layout event and the corresponding exception handling.

	:param xpath: string for xpath
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param str additional_message: string for the error message
	:param float max_time: Max time to wait
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"Waiting for xpath: {xpath}")
	try:
		android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath), max_time=max_time)
	except enna.core.exceptions.TimeoutException:
		err_msg = f"The xpath {xpath} did not appear. " + additional_message
		MODULE_LOGGER.error(err_msg)
		# helper.save_screenshot_of_failure(android, path=str(__get_class_from_frame(inspect.stack()[2][0])), name=enna.core.exceptions.TimeoutException.__name__)
		return False
	return True


# pylint: disable=protected-access
@logdecorator(MODULE_LOGGER)
def wait_for_element_invisible(xpath: str, android: enna_st12.data_interfaces.android_hmi.interface.Interface,
							   additional_message="", max_time: float = 10) -> bool:
	"""Wrap the functionality to wait until an element is invisible and the corresponding exception handling.

	:param xpath: string for xpath
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param str additional_message: string for the error message
	:param float max_time: Max time to wait
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"Waiting for xpath to disappear: {xpath}")
	try:
		android.wait_for_element_invisible(xpath, max_time=max_time)
	except enna.core.exceptions.TimeoutException:
		err_msg = f"The xpath {xpath} did not disappear. " + additional_message
		MODULE_LOGGER.error(err_msg)
		# helper.save_screenshot_of_failure(android, path=str(__get_class_from_frame(inspect.stack()[2][0])), name=enna.core.exceptions.TimeoutException.__name__)
		return False
	return True


# pylint: disable=protected-access
@logdecorator(MODULE_LOGGER)
def wait_for_screen_id(screen: str | list, android: enna_st12.data_interfaces.android_hmi.interface.Interface,
					   additional_message="", max_time: float = 10) -> bool:
	"""Wrap the functionality to wait for a layout event and the corresponding exception handling.

	:param screen: Screen id or list of screen ids to wait for.
	:type: str | list
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param str additional_message: string for the error message
	:param float max_time: Max time to wait
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"Waiting for screen id: {screen}")
	try:
		if isinstance(screen, list):
			android.screen_id.wait_for_value(condition=lambda screen_id: screen_id.value in screen, max_time=max_time)
			return True
		if android.screen_id.wait_for_value(condition=lambda screen_id: screen_id.value == screen, max_time=max_time):
			return True
		MODULE_LOGGER.error(f"The given screen: {screen} has the wrong format to be compared to the current screen_id.")
		return False
	except enna.core.exceptions.TimeoutException:
		err_msg = f"The screen '{screen}' did not appear. " + additional_message
		MODULE_LOGGER.error(err_msg)
		# helper.save_screenshot_of_failure(android, path=str(__get_class_from_frame(inspect.stack()[2][0])), name=enna.core.exceptions.TimeoutException.__name__)
		return False


@logdecorator(MODULE_LOGGER)
def wait_for_screen_id_disappear(screen: str, android: enna_st12.data_interfaces.android_hmi.interface.Interface,
								 additional_message="", max_time: float = 10) -> bool:
	"""Wrap the functionality to wait for screen id to disappear and the corresponding exception handling.

	:param str screen: Screen id to wait for.
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param str additional_message: string for the error message
	:param float max_time: Max time to wait
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"Waiting for screen id: {screen}")
	try:
		android.screen_id.wait_for_value(condition=lambda screen_id: screen_id.value != screen, max_time=max_time)
		return True
	except enna.core.exceptions.TimeoutException:
		err_msg = f"The screen '{screen}' did not disappear. " + additional_message
		MODULE_LOGGER.error(err_msg)
		# helper.save_screenshot_of_failure(android, path=str(__get_class_from_frame(inspect.stack()[2][0])), name=enna.core.exceptions.TimeoutException.__name__)
		return False


# pylint: disable=protected-access
@logdecorator(MODULE_LOGGER)
def compare_screen_id(screen: enna_hcp_configuration.common.base.Element,
					  android: enna_st12.data_interfaces.android_hmi.interface.Interface) -> bool:
	"""Wrap the functionality to wait for an layout event and the corresponding exception handling.

	:param enna_hcp_configuration.common.base.Element screen: Screen id to wait for.
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"Compare screen id '{screen}' to displayed screen id '{android.screen_id}'")
	return android.screen_id.value == screen


@logdecorator(MODULE_LOGGER)
def get_elements_from_layout(xpath, android: enna_st12.data_interfaces.android_hmi.interface.Interface):
	"""Get all matching elements from the layout by given xpath.

	:param str xpath: xpath of the element
	:param enna_st12.data_interfaces.android_hmi.interface.Interface android: android instance
	:return: element
	:rtype: lxml.etree.Element
	"""
	MODULE_LOGGER.info(f"Waiting for xpath: {xpath}")
	try:
		android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath), max_time=15)
	except enna.core.exceptions.TimeoutException:
		MODULE_LOGGER.info(f"The xpath {xpath} did not appear. ")
		# enna_st12.data_interfaces.android_hmi.helper.save_ui_layout(android.layout, android.take_screenshot(), name=str(__get_class_from_frame(inspect.stack()[2][0])))
		return False
	try:
		elements = android.layout.value.xpath(xpath)
	except lxml.etree.XPathError:
		MODULE_LOGGER.info("Element not in the layout.")
		# enna_st12.data_interfaces.android_hmi.helper.save_ui_layout(android.layout, android.take_screenshot(), name=str(__get_class_from_frame(inspect.stack()[2][0])))
		return False
	if not isinstance(elements, list):
		return [elements]
	return elements


@logdecorator(MODULE_LOGGER)
def get_element_by_xpath(xpath: str, android: enna_st12.data_interfaces.android_hmi.interface.Interface, reporting,
						 additional_message=""):
	"""Wrap the functionality to get an element by its xpath and the corresponding exception handling with logging.

	:param xpath: string for xpath
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param enna.core.reporting.interface.Interface reporting: reporting instance
	:param str additional_message: string for the error message
	:return: None if an exception occurred. xml layout, otherwise.
	:rtype: xml element
	"""
	MODULE_LOGGER.info(f"Getting xpath: {xpath}")
	try:
		android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath), max_time=10)
		element: lxml.etree._Element = enna_st12.data_interfaces.android_hmi.helper._get_element_by_xpath(
			android.layout.value, xpath)
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
		err_msg = f"The xpath {xpath} is not present. " + additional_message
	except enna.core.exceptions.TimeoutException:
		err_msg = f"The xpath {xpath} did not appear in the given time. " + additional_message
	else:
		MODULE_LOGGER.info("Recieved xpath.")
		return element
	# -------------------------- This part is executed if any exception from above occurs -------------------------- #
	reporting.add_report_message_ta_error(err_msg)
	# helper.save_screenshot_of_failure(android, path=str(__get_class_from_frame(inspect.stack()[2][0])), name="Exception")
	return None


@logdecorator(MODULE_LOGGER)
def wait_and_click(xpath_element, android: enna_st12.data_interfaces.android_hmi.interface.Interface, reporting,
				   additional_message="", max_time: float = 15) -> bool:
	"""Functionality to wait for an layout element and click on it with the corresponding exception handling.

	:param str xpath_element: string for the destination xpath element
	:param str additional_message: optional additional message for appending to the default error message
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param enna.core.reporting.interface.Interface reporting: reporting instance
	:param float max_time: Maximum time to wait for element to click
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"Waiting for {xpath_element}")
	# -------------------------- Little delay, to avoid clicking on an element from previous layout -------------------------- #
	enna.core.time.sleep(.5)
	try:
		android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath_element), max_time=max_time)
		MODULE_LOGGER.info(f"Waiting done. Now clicking on {xpath_element}")
		android.click_element(xpath_element)
	except enna.core.exceptions.TimeoutException:
		error_message = f"Timeout occured while waiting for {xpath_element}" + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
		error_message = "Element is not enabled. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
		error_message = "Element is not present in the layout. " + additional_message
	else:
		return True
	# -------------------------- This part is executed if any exception from above occurs -------------------------- #
	reporting.add_report_message_ta_error(error_message)
	# helper.save_screenshot_of_failure(android, path=str(__get_class_from_frame(inspect.stack()[2][0])), name="Exception")
	return False


@logdecorator(MODULE_LOGGER)
def wait_and_double_click(xpath_element, android: enna_st12.data_interfaces.android_hmi.interface.Interface, reporting,
						  additional_message="", max_time: float = 15) -> bool:
	"""Functionality to wait for an layout element and double click on it with the corresponding exception handling.

	:param str xpath_element: string for the destination xpath element
	:param str additional_message: optional additional message for appending to the default error message
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param enna.core.reporting.interface.Interface reporting: reporting instance
	:param float max_time: Maximum time to wait for element to click
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"Waiting for {xpath_element}")
	# -------------------------- Little delay, to avoid clicking on an element from previous layout -------------------------- #
	enna.core.time.sleep(.5)
	try:
		android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath_element), max_time=max_time)
		MODULE_LOGGER.info(f"Waiting done. Now clicking on {xpath_element}")
		android.double_click_element(xpath_element)
	except enna.core.exceptions.TimeoutException:
		error_message = f"Timeout occured while waiting for {xpath_element}" + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
		error_message = "Element is not enabled. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
		error_message = "Element is not present in the layout. " + additional_message
	else:
		return True
	# -------------------------- This part is executed if any exception from above occurs -------------------------- #
	reporting.add_report_message_ta_error(error_message)
	# helper.save_screenshot_of_failure(android, path=str(__get_class_from_frame(inspect.stack()[2][0])), name="Exception")
	return False


@logdecorator(MODULE_LOGGER)
def wait_and_long_click(xpath_element, android: enna_st12.data_interfaces.android_hmi.interface.Interface, reporting,
						additional_message="", max_time: float = 15) -> bool:
	"""Functionality to wait for an layout element and long click on it with the corresponding exception handling.

	:param str xpath_element: string for the destination xpath element
	:param str additional_message: optional additional message for appending to the default error message
	:param float max_time: Max time to wait for element to long click
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param enna.core.reporting.interface.Interface reporting: reporting instance
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"Waiting for {xpath_element}")
	# -------------------------- Little delay, to avoid clicking on an element from previous layout -------------------------- #
	enna.core.time.sleep(.5)
	try:
		android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath_element), max_time=max_time)
		MODULE_LOGGER.info(f"Waiting done. Now long clicking on {xpath_element}")
		android.long_click_element(xpath_element)
	except enna.core.exceptions.TimeoutException:
		error_message = f"Timeout occured while waiting for {xpath_element}" + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
		error_message = "Element is not enabled. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
		error_message = "Element is not present in the layout. " + additional_message
	else:
		return True
	# -------------------------- This part is executed if any exception from above occurs -------------------------- #
	reporting.add_report_message_ta_error(error_message)
	# helper.save_screenshot_of_failure(android, path=str(__get_class_from_frame(inspect.stack()[2][0])), name="Exception")
	return False


@logdecorator(MODULE_LOGGER)
def wait_and_long_click_variable_duration(xpath_element,
										  android: enna_st12.data_interfaces.android_hmi.interface.Interface, reporting,
										  additional_message="", duration=0.5, max_time: float = 15) -> bool:
	"""Functionality to wait for a layout element and long click on it's center coordinates with specific duration with the corresponding exception handling.

	:param str xpath_element: string for the destination xpath element
	:param str additional_message: optional additional message for appending to the default error message
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param enna.core.reporting.interface.Interface reporting: reporting instance
	:param float duration: Duration to perform long click.
	:param float max_time: Max. amount of time to wait for element to perform long click on
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"Waiting for {xpath_element}")
	# -------------------------- Little delay, to avoid clicking on an element from previous layout -------------------------- #
	enna.core.time.sleep(.5)
	try:
		android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath_element), max_time=max_time)
		MODULE_LOGGER.info(f"Waiting done. Now long clicking on {xpath_element}")
		elem_bounds = android_hmi_helper.get_bounds_of_element(reporting, android, xpath_element)
		x_value = int(int(elem_bounds["x1"]) + (int(elem_bounds["x2"]) - int(elem_bounds["x1"])) / 2)
		y_value = int(int(elem_bounds["y1"]) + (int(elem_bounds["y2"]) - int(elem_bounds["y1"])) / 2)
		android.long_click_coordinates(x_value, y_value, duration)
	except enna.core.exceptions.TimeoutException:
		error_message = f"Timeout occured while waiting for {xpath_element}" + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
		error_message = "Element is not enabled. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
		error_message = "Element is not present in the layout. " + additional_message
	else:
		return True
	# -------------------------- This part is executed if any exception from above occurs -------------------------- #
	reporting.add_report_message_ta_error(error_message)
	# helper.save_screenshot_of_failure(android, path=str(__get_class_from_frame(inspect.stack()[2][0])), name="Exception")
	return False


@logdecorator(MODULE_LOGGER)
def click_coordinates(x_coordinate, y_coordinate, android: enna_st12.data_interfaces.android_hmi.interface.Interface,
					  reporting, additional_msg="") -> bool:
	"""Functionality to click on specific coordinates with the corresponding exception handling.

	:param x_coordinate: Value of x coordinate
	:type x_coordinate: int, str
	:param y_coordinate: Value of y coordinate.
	:type y_coordinate: int, str
	:param enna_st12.data_interfaces.android_hmi android: android instance.
	:param enna.core.reporting.interface.Interface reporting: reporting instance.
	:param str additional_msg: Additional message to report.
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"Selecting coordinates:{x_coordinate}, {y_coordinate}")
	# -------------------------- Little delay, to avoid clicking on an element from previous layout -------------------------- #
	enna.core.time.sleep(.5)
	try:
		android.click_coordinates(int(x_coordinate), int(y_coordinate))
	except enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException:
		error_message = f"An invalid argument was given to click coordinates method - Argument: {x_coordinate}, {y_coordinate}"
	else:
		return True
	# -------------------------- This part is executed if any exception from above occurs -------------------------- #
	reporting.add_report_message_ta_error(error_message)
	reporting.add_report_message_ta_error(additional_msg)
	# helper.save_screenshot_of_failure(android, path=str(__get_class_from_frame(inspect.stack()[2][0])), name="Exception")
	return False


@logdecorator(MODULE_LOGGER)
def wait_and_click_in_list(xpath_element, xpath_container,
						   android: enna_st12.data_interfaces.android_hmi.interface.Interface, reporting,
						   additional_message="", max_time: float = 15) -> bool:
	"""Wrap the functionality to wait for an container, look for and click on a element in that container.

	:param str xpath_element: string for the destination xpath element
	:param str xpath_container: scrolling happens in this container
	:param str additional_message: optional additional message for appending to the default error message
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param enna.core.reporting.interface.Interface reporting: reporting instance
	:param float max_time: Max. amount of time to wait for list container
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	try:
		android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath_container),
							   max_time=max_time)
		android.click_element_in_list(xpath_element, xpath_container)
	except enna.core.exceptions.TimeoutException:
		error_message = f"Timeout occured while waiting for {xpath_container}. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
		error_message = "Element is not enabled. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
		error_message = "Element is not present in the layout. " + additional_message
	else:
		return True
	# -------------------------- This part is executed if any exception from above occurs -------------------------- #
	reporting.add_report_message_ta_error(error_message)
	# helper.save_screenshot_of_failure(android, path=str(__get_class_from_frame(inspect.stack()[2][0])), name="Exception")
	return False


@logdecorator(MODULE_LOGGER)
def wait_and_scroll_in_list(xpath_element, xpath_container,
							android: enna_st12.data_interfaces.android_hmi.interface.Interface, additional_message="",
							max_time: float = 10) -> bool:
	"""Wrap the functionality to wait for an container, look for an element in that container.

	:param str xpath_element: string for the destination xpath element
	:param str xpath_container: scrolling happens in this container
	:param str additional_message: optional additional message for appending to the default error message
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param float max_time: Maximum time in seconds to wait for proposals to appear.
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	try:
		android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath_container),
							   max_time=max_time)
		android.scroll_to_element_in_list(xpath_container, xpath_element)
	except enna.core.exceptions.TimeoutException:
		error_message = f"Timeout occured while waiting for {xpath_container}. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
		error_message = "Element is not enabled. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
		error_message = "Element is not present in the layout. " + additional_message
	else:
		return True
	# -------------------------- This part is executed if any exception from above occurs -------------------------- #
	MODULE_LOGGER.info(error_message)
	# helper.save_screenshot_of_failure(android, path=str(__get_class_from_frame(inspect.stack()[2][0])), name="Exception")
	return False


@logdecorator(MODULE_LOGGER)
def wait_and_scroll_list_to_bottom(xpath_container, android: enna_st12.data_interfaces.android_hmi.interface.Interface,
								   additional_message="", xpath_for_blacklist=None, max_time: float = 10) -> bool:
	"""Wrap the functionality to scroll a list container to bottom.

	:param str xpath_container: scrolling happens in this container
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param xpath_for_blacklist: optional xpath expressions that are not considered in the detection for reaching the end of a list to scroll
	:type xpath_for_blacklist: str or list
	:param str additional_message: optional additional message for appending to the default error message
	:param float max_time: Max. time in to wait for list container
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	try:
		android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath_container),
							   max_time=max_time)
		android.scroll_list_to_bottom(xpath_container, xpath_for_blacklist)
	except enna.core.exceptions.TimeoutException:
		error_message = f"Timeout occured while waiting for {xpath_container}. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
		error_message = "Element is not enabled. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
		error_message = "Element is not present in the layout. " + additional_message
	else:
		return True
	# -------------------------- This part is executed if any exception from above occurs -------------------------- #
	MODULE_LOGGER.info(error_message)
	# helper.save_screenshot_of_failure(android, path=str(__get_class_from_frame(inspect.stack()[2][0])), name="Exception")
	return False


@logdecorator(MODULE_LOGGER)
def wait_and_scroll_list_to_top(xpath_container, android: enna_st12.data_interfaces.android_hmi.interface.Interface,
								additional_message="", xpath_for_blacklist=None, max_time: float = 10) -> bool:
	"""Wrap the functionality to scroll a list container to top.

	:param str xpath_container: scrolling happens in this container
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param xpath_for_blacklist: optional xpath expressions that are not considered in the detection for reaching the end of a list to scroll
	:type xpath_for_blacklist: str or list
	:param str additional_message: optional additional message for appending to the default error message
	:param float max_time: Max. time to wait for list container.
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	try:
		android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath_container),
							   max_time=max_time)
		android.scroll_list_to_top(xpath_container, xpath_for_blacklist)
	except enna.core.exceptions.TimeoutException:
		error_message = f"Timeout occured while waiting for {xpath_container}. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
		error_message = "Element is not enabled. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
		error_message = "Element is not present in the layout. " + additional_message
	else:
		return True
	# -------------------------- This part is executed if any exception from above occurs -------------------------- #
	MODULE_LOGGER.info(error_message)
	# helper.save_screenshot_of_failure(android, path=str(__get_class_from_frame(inspect.stack()[2][0])), name="Exception")
	return False


@logdecorator(MODULE_LOGGER)
def go_to_screen(destination, reporting, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface,
				 retries=5) -> bool:
	"""Wrap the functionality to wait for an layout event and the corresponding exception handling.

	:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: menu navigation interface.
	:param enna.core.reporting.interface.Interface reporting: reporting instance.
	:param enna_hcp_configuration.common.base.Element destination: destination screen.
	:param int retries: Number ob retries for menu navigation.
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"navigating to the screen: {destination}")
	try:
		menu_navigation.go_to_screen(destination, max_retries=retries)
	except (enna_st12.utilities.menu_navigation.exceptions.MenuNavigationException, AttributeError):
		err_msg = f"Error while navigating to the screen: {destination}"
		reporting.add_report_message_ta_error(err_msg)
		return False
	return True


# pylint: disable=protected-access
@logdecorator(MODULE_LOGGER)
def element_exists(xpath: str, android, additional_message="", max_time: float = 1) -> bool:
	"""Wrap the functionality to check if an element exists on the current layout.

	:param xpath: string for xpath
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param str additional_message: string for the error message
	:param float max_time: Max time to wait for element
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"Waiting for xpath: {xpath}")
	try:
		android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath), max_time=max_time)
	except enna.core.exceptions.TimeoutException:
		err_msg = f"The xpath {xpath} did not appear. " + additional_message
		MODULE_LOGGER.info(err_msg)
		return False
	return True


@logdecorator(MODULE_LOGGER)
def wait_and_get_toggle_button_state(xpath_element, android: enna_st12.data_interfaces.android_hmi.interface.Interface,
									 reporting, additional_message="", max_time: float = 15) -> bool | None:
	"""Wrap the functionality to get state of a toggle-button.

	:param str xpath_element: string for the destination xpath element
	:param str additional_message: optional additional message for appending to the default error message
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param enna.core.reporting.interface.Interface reporting: reporting instance
	:param float max_time: Max. amount of time to wait for list container
	:return: False if toggle button state is False. True, otherwise. None if an error occurrs
	:rtype: bool | None
	"""
	try:
		android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath_element), max_time=max_time)
		toggle_button_object = get_element_by_xpath(xpath_element, android, reporting)
		return enna.core.helper.strtobool(toggle_button_object.attrib["checked"])
	except enna.core.exceptions.TimeoutException:
		error_message = f"The xpath {xpath_element} did not appear. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException:
		error_message = "No Android Device connected or connection failed. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException:
		error_message = "One or more arguments have invalid type or value. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
		error_message = "Toggle-Button was not found in GUI. " + additional_message
	reporting.add_report_message_ta_error(error_message)
	return None


@logdecorator(MODULE_LOGGER)
def wait_and_set_toggle_button_state(xpath_element, new_state: bool,
									 android: enna_st12.data_interfaces.android_hmi.interface.Interface, reporting,
									 additional_message="", max_time: float = 15) -> bool:
	"""Wrap the functionality to set a new state on a toggle-button.

	:param str xpath_element: string for the destination xpath element
	:param str new_state: new toggle-state - True or False
	:param str additional_message: optional additional message for appending to the default error message
	:param enna_st12.data_interfaces.android_hmi android: android instance
	:param enna.core.reporting.interface.Interface reporting: reporting instance
	:param float max_time: Max. amount of time to wait for list container
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	try:
		android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath_element), max_time=max_time)
		android.set_toggle_button_state(xpath_element, new_state)
	except enna.core.exceptions.TimeoutException:
		error_message = f"The xpath {xpath_element} did not appear. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException:
		error_message = "No Android Device connected or connection failed. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException:
		error_message = "One or more arguments have invalid type or value. " + additional_message
	except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
		error_message = "Toggle-Button was not found in GUI. " + additional_message
	else:
		return True
	# -------------------------- This part is executed if any exception from above occurs -------------------------- #
	reporting.add_report_message_ta_error(error_message)
	return False


@logdecorator(MODULE_LOGGER)
def enter_address(self, address, clear=True):
	"""Input destination.

	:param bool clear: If True, clear input field before entering text
	:param str address: Name of recorder instance
	:raises enna_tc_navigation_hcp3.utilities.speller.exceptions.NavSpellerException: if during address input any exception occurs
	:return: execution time stamp as string, when the address was entered
	:rtype: str
	"""
	editor_text = self.__open_xpath.get_xpath("navigationBar", "textBox")
	editor_text_address = editor_text + "/@text"

	self.__adb.execute_shell_command(["ime", "enable", "com.github.uiautomator/.FastInputIME"], timeout=60)
	self.__adb.execute_shell_command(["ime", "set", "com.github.uiautomator/.FastInputIME"], timeout=60)

	self.__android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(editor_text), max_time=5)
	self.__android.click_element(editor_text)
	btext = address.encode("utf-8")
	base64text = base64.b64encode(btext).decode()
	cmd = "ADB_SET_TEXT" if clear else "ADB_INPUT_TEXT"
	self.__adb.execute_shell_command(["am", "broadcast", "-a", cmd, "--es", "text", base64text], timeout=60)

	self.__android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(editor_text_address), max_time=5)

	return enna.core.time.now_as_string()


@logdecorator(MODULE_LOGGER)
def scroll_to_app_in_app_grid(android_hmi, reporting, appname: str) -> bool:
	"""Scroll to xpath in app grid.

	Will try to scroll list to top before scrolling to xpath.

	:param str appname: xpath to scroll to in list
	:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
	:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface.
	:return: True if successful, False otherwise
	:rtype: bool
	"""
	xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=reporting, app="launcher")
	str_xpath__app_grid__container = xpaths.get_xpath("general", "main_list")
	if not wait_and_double_click(xpaths.get_xpath("general", "app_grid_button"), android_hmi, reporting, msg := "Could not fling list to top. Try going to top by scrolling"):
		reporting.add_report_message_warning(msg)
	if not wait_and_scroll_list_to_top(str_xpath__app_grid__container, android_hmi, "Waiting and trying again."):
		enna.core.time.sleep(3)
		wait_and_scroll_list_to_top(str_xpath__app_grid__container, android_hmi, "Could not scroll calendar event list to top.")
	enna.core.time.sleep(3)
	if not wait_and_scroll_in_list(appname, str_xpath__app_grid__container, android_hmi, msg := "Could not scroll to list element."):
		reporting.add_report_message_warning(msg)
	if not wait_for_layout_element(appname, android_hmi, msg := "Xpath did not appear on screen."):
		reporting.add_report_message_warning(msg)
		return False
	return True
