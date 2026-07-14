# -*- coding: utf-8 -*-
"""Module contains all functionality that is needed to have a working RUDI client."""
import base64
import logging

import enna.core.component_system.decorators
import enna.core.exceptions
import enna.core.interfaces.server
import enna.core.time
import enna.data_interfaces.adb.exceptions
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.instance_names

import enna_kwd_testing.utilities.speller.exceptions
import enna_kwd_testing.utilities.speller.interface

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb", instance_name=enna_st12.instance_names.Ecu.HCP3)
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class Server(enna_kwd_testing.utilities.speller.interface.Interface, enna.core.interfaces.server.Server):
	"""Provide functionality of a speller."""

	def __init__(self, adb, android_hmi):
		"""Speller for input box.

		:param enna.data_interfaces.adb.interface.Interface adb: adb interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: android_hmi interface
		:raises enna.core.exceptions.ConfigurationException: if the configuration is incomplete or invalid
		:raises enna_tc_hmi_hcp3.utilities.speller.exceptions.SpellerException: if failed to start FastInputIME
		"""
		enna_kwd_testing.utilities.speller.interface.Interface.__init__(self)
		enna.core.interfaces.server.Server.__init__(self)
		self.__adb = adb
		self.__android = android_hmi
		self._set_online()

	def delete_text(self, key: str = "global_search", item: str ="clearTextButton"):
		"""Delete the text string in the search area.

		:param key: str: key from xpath_collection for screen
		:param item: str: item from xpath_collection for clearTextButton
		:raises enna_tc_hmi_hcp3.utilities.speller.exceptions.SpellerException: if during text input any exception occurs
		"""

		clear_text_button = "//*[@class='android.widget.EditText']"
		# close_detail_overlay_button = get_xpath('detailOverlayContent', 'Close_detailOverlay_Button')

		try:
			self.__android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(clear_text_button), max_time=7)
			self.__android.click_element(clear_text_button)
		# self.__android.wait_for_event('layout', condition=lambda layout: layout.value.xpath(close_detail_overlay_button), max_time=Waittime.mid.value)
		# self.__android.click_element(close_detail_overlay_button)
		except (enna.core.exceptions.TimeoutException, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as ex:
			raise enna_kwd_testing.utilities.speller.exceptions.SpellerException(f"Failed to close search window with Exception '{ex}'.") from ex
		try:
			self.__adb.execute_shell_command(["ime", "disable", "com.github.uiautomator/.FastInputIME"], timeout=60)
		except enna.data_interfaces.adb.exceptions.ADBException as exc:
			raise enna_kwd_testing.utilities.speller.exceptions.SpellerException(f"Failed to disable FastInputIME by ADB with Exception '{exc}'.") from exc

	def enter_text(self, text="text", clear=True):
		"""Input text.

		:param str text: Name of search text
		:param bool clear: If True, clear input field before entering text
		:raises enna_tc_hmi_hcp3.utilities.speller.exceptions.SpellerException: if during text input any exception occurs
		:return: execution time stamp as string, when the text was entered
		:rtype: str
		"""

		editor_text = "//*[@class='android.widget.EditText']"
		# editor_text_input = editor_text + "/@text" + f"='{text}'"

		try:
			self.__adb.execute_shell_command(["ime", "enable", "com.github.uiautomator/.FastInputIME"], timeout=60)
			self.__adb.execute_shell_command(["ime", "set", "com.github.uiautomator/.FastInputIME"], timeout=60)
		except enna.data_interfaces.adb.exceptions.ADBException as exc:
			raise enna_kwd_testing.utilities.speller.exceptions.SpellerException(f"Failed to enable and set FastInputIME by ADB with Exception '{exc}'.") from exc

		try:
			self.__android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(editor_text), max_time=7)
			self.__android.click_element(editor_text)
			btext = text.encode("utf-8")
			base64text = base64.b64encode(btext).decode()
			cmd = "ADB_SET_TEXT" if clear else "ADB_INPUT_TEXT"
			self.__adb.execute_shell_command(["am", "broadcast", "-a", cmd, "--es", "text", base64text], timeout=60)
		except (enna.core.exceptions.TimeoutException, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException, enna.data_interfaces.adb.exceptions.ADBException) as ex:
			raise enna_kwd_testing.utilities.speller.exceptions.SpellerException(f"Failed to put text to search area with Exception '{ex}'.") from ex

		try:
			enna.core.time.sleep(6)
			# self.__android.wait_for_event("layout", condition=lambda layout: layout.value.xpath(editor_text_input), max_time=7)
		except (enna.core.exceptions.TimeoutException, enna.core.exceptions.EventNotFoundException) as ex:
			raise enna_kwd_testing.utilities.speller.exceptions.SpellerException(f"Inputed text not match the text in Search bar with Exception '{ex}'.") from ex

		return enna.core.time.now_as_string()

	def activate_keyboard(self) -> bool:
		"""Deactivate FastInputIME for android.
		Deactivating FastInputIME activates the visible keyboard.
		:return: True if successful
		:rtype: bool
		:raises enna_tc_connect_apps_hcp3.utilities.speller.exceptions.SpellerException: If FastInputIME can´t be disabled.
		"""

		try:
			self.__adb.execute_shell_command(["ime", "disable", "com.github.uiautomator/.FastInputIME"], timeout=60)
			self.__adb.execute_shell_command(["ime", "set", "com.audi.automotive.input/com.nuance.swype.input.IME"], timeout=60)
		except enna.data_interfaces.adb.exceptions.ADBException as exc:
			raise enna_kwd_testing.utilities.speller.exceptions.SpellerException(f"Failed to disable FastInputIME by ADB with Exception '{exc}'.") from exc
		return True
