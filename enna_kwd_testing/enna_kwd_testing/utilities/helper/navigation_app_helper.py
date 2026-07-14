# -*- coding: utf-8 -*-
"""Created on 24.11.2023.

@project: enna_tc_connect_apps_hcp3.
@author: S6FXUOM: Nikolaus Maier.

Navigation basic functionalities including the corresponding exception handling with default error messages for logging and reporting.
"""
import logging

import enna.core.exceptions
import enna.core.reporting.interface
import enna.core.time
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.data_interfaces.android_hmi.helper
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.exceptions
import enna_st12.utilities.menu_navigation.interface

from enna_kwd_testing.utilities.decorators.logging import logdecorator
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=protected-access, too-many-positional-arguments
@logdecorator(MODULE_LOGGER)
def swipe_coordinates(android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, cd_x1, cd_y1, cd_x2, cd_y2, reporting: enna.core.reporting.interface.Interface) -> bool:
	"""Function to swipe from x1,y1 coordinates to x2,y2 coordinates in mmi.

	:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: android_hmi instance
	:param enna.core.reporting.interface.Interface reporting: reporting instance
	:param cd_x1: x1
	:type cd_x1: int
	:param cd_y1: y1
	:type cd_y1: int
	:param cd_x2: x2
	:type cd_x2: int
	:param cd_y2: y2
	:type cd_y2: int
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info("swipe coordinates")
	try:
		android_hmi.swipe_coordinates(cd_x1, cd_y1, cd_x2, cd_y2, swipe_time=.7)
	except (enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException, AttributeError):
		err_msg = "Error while swipping in screen."
		reporting.add_report_message_ta_error(err_msg)
		return False
	return True


@logdecorator(MODULE_LOGGER)
def zoom_in_one_step(xpath_element, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface,
					 reporting) -> bool:
	"""Zoom in with one step.

	:param str xpath_element: string for the destination xpath element
	:param enna_st12.data_interfaces.android_hmi android_hmi: android instance
	:param enna.core.reporting.interface.Interface reporting: reporting instance
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	if not wrapper_android_hmi.wait_and_click(xpath_element, android_hmi, reporting, "Could not click zoom in button"):
		MODULE_LOGGER.info("Zoom was not possible to click zoom button")
		return False
	MODULE_LOGGER.info("Zoom in one step.")
	return True


@logdecorator(MODULE_LOGGER)
def zoom_out_one_step(xpath_element, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, reporting) -> bool:
	"""Zoom out with one step.

	:param str xpath_element: string for the destination xpath element
	:param enna_st12.data_interfaces.android_hmi android_hmi: android instance
	:param enna.core.reporting.interface.Interface reporting: reporting instance
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	if not wrapper_android_hmi.wait_and_click(xpath_element, android_hmi, reporting, "Could not click zoom in button"):
		MODULE_LOGGER.info("Zoom was not possible to click zoom button")
		return False
	MODULE_LOGGER.info("Zoom out one step.")
	return True
