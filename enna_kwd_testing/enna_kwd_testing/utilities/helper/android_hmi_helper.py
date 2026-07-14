# -*- coding: utf-8 -*-
"""Created on 31.05.2022.

@project: enna_tc_connect_apps_hcp3.
@author: DYX34ZN: Jakob Kein.

Contains helper functions for android_hmi context.
"""

import inspect
import logging
import re
import time

import enna.core.exceptions
import enna.core.time
import enna_st12.data_interfaces.android_hmi.exceptions
import lxml.etree

MODULE_LOGGER = logging.getLogger(__name__)


def __get_class_from_frame(frame):
	"""Get class from a frame.

	:param frame frame: Frame to get class from.
	:return: class name
	:rtype: str
	"""
	args, _, _, value_dict = inspect.getargvalues(frame)
	if len(args) and args[0] == "self":
		instance = value_dict.get("self", None)
		if instance:
			return str(getattr(instance, "__class__", None)).rsplit(".", maxsplit=1)[-1].replace(">", "").replace("'", "").replace("<", "")
	return None


def get_bounds_of_element(reporting, android_hmi, xpath, timeout=10):
	"""Get bounds of Gui element by it´s xpath selector after waiting specific time for xpath.

	:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
	:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface.
	:param str xpath: Xpath selector for object to get bounds from.
	:param int timeout: Max time to wait for layout element.
	:return: bounds x1, x2, y1, y2 (upper left, under right corners).
	:rtype: dict.
	:raise AttributeError: when bounds could not be accessed or element was not found.
	"""
	MODULE_LOGGER.debug(msg := f"Getting bounds for element: {xpath}")
	reporting.add_report_message_info(msg)
	MODULE_LOGGER.info(f"Waiting for xpath: {xpath}")
	try:
		android_hmi.wait_for_event("layout", condition=lambda layout: layout.value.xpath(xpath), max_time=timeout)
	except enna.core.exceptions.TimeoutException:
		MODULE_LOGGER.error(f"Layout element with xpath: {xpath} did not appear.")
		return False
	try:
		bounds_as_string = android_hmi.layout.value.xpath(xpath)[0].attrib["bounds"]
		bounds_as_list = bounds_as_string.replace("[", "").replace("]", ",").split(",")
		return {"x1": bounds_as_list[0], "x2": bounds_as_list[2], "y1": bounds_as_list[1], "y2": bounds_as_list[3]}
	except (IndexError, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as exc:
		MODULE_LOGGER.error(msg := f"Could not get bounds for element: {xpath}")
		reporting.add_report_message_ta_error(msg)
		raise AttributeError(f"Could not get bounds for element with Exception: {exc}")


def check_timespan_format(timeformat, time_value):
	"""Check time format HH:MM - HH:MM. pm tbd.

	:param str timeformat: time format to check ("24" for -> MM:HH - MM:HH)
	:param str time_value: string with time that should be checked
	:return: True or False
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"Time format check for {time_value} in format {timeformat}.")
	# Check for format <Name of Appointment> > <HH:MM> - <HH:MM>
	try:
		if timeformat == "24":
			time_checked = re.match(r"([01]?[0-9]|2[0-9]):[0-5][0-9] - ([01]?[0-9]|2[0-9]):[0-5][0-9]", time_value)
			if time_checked is None:
				return False
			return True
		return False
	except enna.core.exceptions.TimeoutException:
		MODULE_LOGGER.info("The time format could not be checked.")
		return False


def get_app_name_from_screen(reporting, android_hmi, timeout: int = 15) -> str | bool:
	"""Get the app name from screen id.

	:param timeout: Time to wait for screen id
	:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
	:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface.
	:return: app_name
	:rtype: str
	"""
	try:
		screen = wait_till_screen_id_is_not_empty(reporting, android_hmi, timeout=timeout)
		app_name = str(screen).split(".")
		return app_name[0]
	except (IndexError, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as exc:
		MODULE_LOGGER.error(msg := f"{exc}: Could not get app name from screen id")
		reporting.add_report_message_ta_error(msg)
		return False


def get_screen_name_from_screen(reporting, android_hmi) -> str | bool:
	"""Get the screen name from screen id.

	:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
	:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface.
	:return: screen_name
	:rtype: str
	"""
	try:
		screen = wait_till_screen_id_is_not_empty(reporting, android_hmi)
		screen_name = str(screen).split(".")
		return screen_name[1]
	except (IndexError, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as exc:
		MODULE_LOGGER.error(msg := f"{exc}: Could not get screen name from screen id")
		reporting.add_report_message_ta_error(msg)
		return False


def get_app_and_screen_name_from_screen(reporting, android_hmi) -> tuple[str, str] | bool:
	"""Get the screen and app name from screen id.

	:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
	:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface.
	:return: app_name and screen name
	:rtype: str
	"""
	try:
		screen = wait_till_screen_id_is_not_empty(reporting, android_hmi)
		name = str(screen).split(".")
		return name[0], name[1]
	except (IndexError, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as exc:
		MODULE_LOGGER.error(msg := f"{exc}: Could not get screen and app name from screen id")
		reporting.add_report_message_ta_error(msg)
		return False


def wait_till_screen_id_is_not_empty(reporting, android_hmi, timeout=10) -> str | bool:
	"""Wait till screen id is not empty.

	:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
	:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface.
	:param int timeout: max waiting time
	:return: screen_id
	:rtype: str
	"""

	starttime = time.time()
	enna.core.time.sleep(1)
	while len(str(android_hmi.screen_id)) == 0:
		if (time.time() - starttime) > timeout:
			MODULE_LOGGER.error(msg := f"After {timeout} seconds, screen_id variable is still empty")
			reporting.add_report_message_ta_error(msg)
			return False
	return android_hmi.screen_id


def wait_till_screen_id_is_visible(screen_id, reporting, android_hmi, timeout=10) -> str | bool:
	"""Wait till screen id is the same as given id.

	:param string screen_id: Screen ID that is wanted
	:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
	:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface.
	:param int timeout: max waiting time
	:return: screen_id
	:rtype: str
	"""

	starttime = time.time()
	enna.core.time.sleep(1)

	app, screen = get_app_and_screen_name_from_screen(reporting, android_hmi)
	str_screen_id = f"{app}.{screen}"

	while screen_id != str_screen_id:
		if (time.time() - starttime) > timeout:
			MODULE_LOGGER.error(msg := f"After {timeout} seconds, given screen_id {screen_id} is not the actual screen: {str_screen_id}")
			reporting.add_report_message_ta_error(msg)
			return False
	return android_hmi.screen_id


def get_element_center_coordinates(layout, xpath):
	"""Calculate the center coordinates of an element found by given xpath.

	:param lxml.etree.Element layout: the UI layout to look in
	:param str xpath: xpath of the target element
	:return: tuple with coordinates
	:rtype: tuple
	:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the searched for element does not exist in the UI layout
	"""
	coordinates_size = get_element_coordinates_and_size(layout, xpath)
	x_center = round(coordinates_size["x"] + (coordinates_size["width"] / 2))
	y_center = round(coordinates_size["y"] + (coordinates_size["height"] / 2))
	return x_center, y_center


def get_element_coordinates_and_size(layout, xpath):
	"""Return top left coordinates and size of an element found by given xpath.

	:param lxml.etree.Element layout: the UI layout to look in
	:param str xpath: xpath of the target element
	:return: dict with keys x, y, width and height
	:rtype: dict
	:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the searched for element does not exist in the UI layout
	"""
	element = get_element_by_xpath(layout, xpath)
	bounds = [int(x) for x in re.findall(r"\d+", element.attrib["bounds"])]
	return {"x": bounds[0], "y": bounds[1], "width": bounds[2] - bounds[0], "height": bounds[3] - bounds[1]}


def get_element_by_xpath(layout, xpath):
	"""Evaluate XPath on the layout and return the first element that is found.

	:param lxml.etree.Element layout: the UI layout to look in
	:param str xpath: xpath of the element
	:return: element
	:rtype: lxml.etree.Element
	:raises enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException: if the searched for element does not exist in the UI layout
	"""
	try:
		return layout.xpath(xpath)[0]
	except (IndexError, lxml.etree.XPathError):
		raise enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException(f"UI element not found! Element XPath {xpath}!")
