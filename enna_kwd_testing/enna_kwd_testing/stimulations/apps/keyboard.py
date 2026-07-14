# -*- coding: utf-8 -*-
"""Module contains stimulation for enter text."""

import logging
import time

import enna.core.config
import enna.core.exceptions
import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.instance_names

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.text_tool.helper

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class EnterText(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to enter text."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, ):
		"""Initialize stimulation.

		:param reporting: Instance of reporting interface
		:param adb: Instance of interface to Android Debug Bridge
		:param android_hmi: Instance of interface to ui-automator
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.4")
		self._adb = adb
		self._android_hmi = android_hmi

		self.allowed_parameter_keys = ["TEXT", "KEYBOARD_CLOSE", "LANG"]
		MODULE_LOGGER.debug(f"Allowed Parameter Keys: '{self.allowed_parameter_keys}'.")

		self._keyboard_xpath: str = "//*[@resource-id='com.audi.automotive.input:id/keyboardViewEx']"
		self._input_field: str = "//*[@class='android.widget.EditText']"
		self._keyboard_close: bool = True

	def _action(self) -> bool:
		"""Enter text in input field

		:return: True if success, else False
		"""
		self._keyboard_close = self.values.get("KEYBOARD_CLOSE", True)
		language = self.values.get("LANG", enna.core.config.INFOTAINMENT_SYSTEM.system_language.value)
		try:
			text: str = enna_kwd_testing.utilities.text_tool.helper.get_text_from_configuration(text_id=self.values["TEXT"], language=language)
		except KeyError as exception:
			self._reporting.add_report_message_ta_error(f"Missing parameter Text! {exception}")
			return False

		try:
			self._android_hmi.wait_for_element_visible(xpath=self._input_field, max_time=3.0)
			self._android_hmi.click_element(xpath=self._input_field)  # click in input-field to open Audi Keyboard
			try:
				self._android_hmi.wait_for_element_visible(xpath=self._keyboard_xpath, max_time=3.0)
			except enna.core.exceptions.TimeoutException:
				self._adb.execute_shell_command('ime disable com.github.uiautomator/.FastInputIME')
				self._android_hmi.wait_for_element_visible(xpath=self._keyboard_xpath, max_time=3.0)
			self._android_hmi.enter_text(text=text, clear=True)  # enter text if keyboard is open
		except (enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException, enna.core.exceptions.TimeoutException) as error:
			self._reporting.add_report_message_ta_error(f"Could not enter Text! {error}")
			return False
		MODULE_LOGGER.debug(f"The Text '{text}' is enter in the input field.")
		return True

	def _postcondition(self) -> bool:
		"""Close Keyboard after enter text. That execution is optional.

		:return: True if success, else False
		"""
		if self._keyboard_close:
			try:
				# self._adb.execute_shell_command("am force-stop com.audi.automotive.input", timeout=5.0)
				self._adb.execute_shell_command("ime reset")
				time.sleep(0.5)
				self._android_hmi.wait_for_element_invisible(xpath=self._keyboard_xpath, max_time=2.0)
			except (enna.core.exceptions.TimeoutException, enna.data_interfaces.adb.exceptions.ADBException, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as error:
				msg = f"Error by closing Keyboard! {error}"
				self._reporting.add_report_message_ta_error(msg)
				return False
		return True
