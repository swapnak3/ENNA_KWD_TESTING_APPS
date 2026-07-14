# -*- coding: utf-8 -*-
"""Created on 19.04.2022.

@project: enna_tc_connect_apps_hcp3.
@author: DYX34ZN: Jakob Kein.
"""
import logging
from enum import Enum

import enna.core.exceptions

MODULE_LOGGER = logging.getLogger(__name__)


class ToastTexts(Enum):
	"""Possible toast texts to wait for."""

	CAL_SETTINGS_BLOCKING_TOAST = "Eingeschränkte Funktion während der Fahrt."
	CAL_SETTINGS_SOURCE_DESELECTED_TOAST = "Das Gerät wurde deselektiert"
	CAL_SOURCE_SELECTOR_BLOCKING_TOAST = CAL_SETTINGS_BLOCKING_TOAST
	LEGAL_BLOCKING_TOAST = ["Eingeschränkte Funktion während der Fahrt", "Eingeschränkte Funktion während der Fahrt.", "*Eingeschränkte Funktion während der Fahrt."]
	LEGAL_BLOCKING_TOAST_DISCLAIMER = "*Zu Ihrer Sicherheit ist diese Funktion während der Fahrt nicht verfügbar."
	LEGAL_PRIVACY_ACTIVE_POPUP_OK = "OK"


class ServiceListEntry(Enum):
	"""Possible service list entries to wait for."""

	OBB_V1 = "obb_v1"


class OnlineState(Enum):
	"""Possible online states for apn1 and apn2."""

	CONNECTED = "CONNECTED"
	UNKNOWN = "UNKNOWN"
	BLOCKED = "BLOCKED"


def wait_for_specific_toast(data_logcat, toast_text: ToastTexts, max_time=10, cover_dev_text=False):
	"""Wait for a specific toast message by it´s text.

	:param enna_tc_connect_apps_hcp3.utilities.data_logcat.interface.Interface data_logcat: Instance of data_logcat interface.
	:param ToastTexts toast_text: Text of toast message to wait for.
	:param int max_time: Maximum time to wait for toast message.
	:param bool cover_dev_text: Flag to trigger exact match comparison or containing comparison (for dev texts, starting with '*').
	:return: True if message appeared, False otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"Wait for toast message with text: '{toast_text.value}'.")
	try:
		if cover_dev_text:
			MODULE_LOGGER.info(f"Wait for toast message. Cover dev texts is '{str(cover_dev_text)}'. So check for required text with leading '*' too.")
			data_logcat.wait_for_event("toast", condition=lambda x: any(((text == data_logcat.toast) or ("*" + text == data_logcat.toast)) for text in toast_text.value), max_time=max_time)  # pylint: disable=consider-using-in
		else:
			data_logcat.wait_for_event("toast", condition=lambda x: data_logcat.toast in toast_text.value if isinstance(toast_text.value, list) else [toast_text.value], max_time=max_time)
	except enna.core.exceptions.TimeoutException:
		MODULE_LOGGER.info(f"Toast message with text {toast_text.value} did not appear.")
		return False
	finally:
		data_logcat.toast = None
	return True


def wait_for_apn1_online(data_logcat, max_time=15):
	"""Wait if logcat entry for apn1 online appears.

	:param enna_tc_connect_apps_hcp3.utilities.data_logcat.interface.Interface data_logcat: Instance of data_logcat interface.
	:param int max_time: Maximum time to wait for logcat message to appear.
	:return: True if logcat message appeared, False otherwise.
	:rtype: bool
	"""
	try:
		data_logcat.wait_for_event("apn1_connection_state", condition=lambda x: x == OnlineState.CONNECTED.value, max_time=max_time)
	except enna.core.exceptions.TimeoutException:
		return False
	finally:
		data_logcat.toast = None
	return True


def wait_for_event(data_logcat, event: str, condition=None, additional_message="", max_time=10):
	"""Wrap the functionality to wait for an layout event and the corresponding exception handling.

	:param enna_tc_connect_apps_hcp3.utlities.data_logcat.interface.Interface data_logcat: Instance of data_logcat interface
	:param str event: Event name to wait for
	:param callable condition: Condition to match
	:param str additional_message: string for the error message
	:param int max_time: Max time to wait
	:return: False if an exception occurred. True, otherwise.
	:rtype: bool
	"""
	MODULE_LOGGER.info(f"Waiting for event {event}")
	try:
		data_logcat.wait_for_event(event, condition=condition, max_time=max_time)
	except enna.core.exceptions.TimeoutException:
		err_msg = f"The event {event} did not appear. " + additional_message
		MODULE_LOGGER.error(err_msg)
		return False
	return True


def wait_for_c2p_zero_conf_started(data_logcat, max_time=10) -> bool:
	"""Wait until event zero_conf_started appeared and property zero_conf_started is True.

	:param enna_tc_connect_apps_hcp3.utilities.data_logcat.interface.Interface data_logcat: Instance of data_logcat interface
	:param int max_time: Maximum amount of time to wait for zero conf manager starting
	:return: True if zero conf manager started, False otherwise
	:rtype: bool
	"""
	try:
		data_logcat.wait_for_event("zero_conf_started", max_time=max_time)
	except enna.core.exceptions.TimeoutException:
		MODULE_LOGGER.error("Event 'zero_conf_started' to indicate that the car 2 phone ZeroConfManager was started did not appear.")
	return data_logcat.zero_conf_started
