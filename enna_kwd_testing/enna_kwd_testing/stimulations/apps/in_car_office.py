# -*- coding: utf-8 -*-
"""Created on 18.11.2024.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Teubner Claus.

Contains stimulations for keyword driven testing in context of ICO (in car office).
"""
import pathlib
import logging
import time
import cv2


import selenium.webdriver
import selenium.webdriver.edge.service
import selenium.common.exceptions
import selenium.webdriver.edge.options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import enna.core.exceptions
import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.data_interfaces.adb.interface

import enna_st12.data_interfaces.android_hmi.helper
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.utilities.menu_navigation.interface
import enna_st12.utilities.menu_navigation.exceptions

from enna_hcp_configuration.android.contexts import in_car_office
import enna_hcp_configuration.android.xpaths.in_car_office

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
import enna_kwd_testing.stimulations.apps._internal
from enna_kwd_testing.utilities.helper import wrapper_android_hmi


MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckIcoSettingsEmailAccount(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check email account in ico settings."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__android_hmi = android_hmi
		self._reporting = reporting
		self.__menu_navigation = menu_navigation
		self.__xpathhandler = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ['ACCOUNT']
		self.allowed_parameter_values = ['gmail', 'microsoft']
		self._dict_accounts = {'gmail': 'gmail', 'microsoft': 'outlook'}

	def _action(self) -> bool:
		"""Execute action.

		Check if element contains value.

		1. Navigate to screen: ico - settings - edit account - check mail address (in_car_office.settings_edit_account)
		2. Check email address contains given value.

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		enna_kwd_testing.utilities.helper.android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)

		str_account = str(self.values.get('ACCOUNT', "Gmail")).lower()
		if str_account in self.allowed_parameter_values:
			self._reporting.add_report_message_info(f"Parameter for ACCOUNT: '{str_account}'")
		else:
			self._reporting.add_report_message_ta_error(f"Wrong parameter for ACCOUNT: '{str_account}', should be a valid email address containing, eg: {self.allowed_parameter_values}.")
			return False
		str_account = self._dict_accounts[str_account]

		if not wrapper_android_hmi.go_to_screen(in_car_office.SETTINGS_EDIT_ACCOUNT, self._reporting, self.__menu_navigation):
			self._reporting.add_report_message_ta_error("Could not go to screen: 'ICO -> SETTINGS_EDIT_ACCOUNT. Something went wrong while navigating to screen.")
			return False

		str_emailaddress_xpath = self.__xpathhandler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="emailaddress_secondline")
		str_emailaddress_text = self.__android_hmi.layout.value.xpath(str_emailaddress_xpath)[1].attrib["text"]

		if str_account not in str_emailaddress_text:
			error_message = f"Expected email Account '{str_account}' was not found in '{str_emailaddress_text}'."
			self._reporting.add_report_message_ta_error(error_message)
			return False

		self._reporting.add_report_message_info(f"The expected email account '{str_account}' was found in email address '{str_emailaddress_text}'.")
		return True


# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class LinkingOnEmailAccount(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Adding a link to an existing e-mail account on the In-Car-Office app."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Constructor of stimulation.
		
		:param reporting: instance of reporting handler
		:param android_hmi: instance of android hmi control interface
		:param menu_navigation: instance of interface of menu navigation
		"""
		super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.4")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, menu_navigation=menu_navigation, android_hmi=android_hmi)
		self.allowed_parameter_keys = ["EMAIL", "PASSWORD"]

	def _action(self) -> bool:
		"""Linking an e-Mail account

		Go to menu of linking an e-mail account.

		:return: True if success, else false.
		"""
		try:
			self._menu_navigation.go_to_screen(destination=in_car_office.EMAIL_OVERVIEW,max_retries=2)
			self._reporting.add_report_message_pass("Mail account already linked to In-Car-Office.")
			return True
		except enna_st12.utilities.menu_navigation.exceptions.MenuNavigationException:
			MODULE_LOGGER.debug("No Account Linked!")

		if not self._go_to_screen(destination=in_car_office.LINKING_TO_EMAIL_ACOUNT):
			return False
		url = self._reading_qr_code()
		if url is None:
			return False
		print(url)
		if not self._link_account_via_website(url=url):
			return False

		self._reporting.add_report_message_pass("In-Car-Office is linked to an exist E-mail Account!")
		return True

	def _reading_qr_code(self) -> str | None:
		"""Reading qr code.

		:return: url was reading from qr code
		"""
		url = None
		try:
			# pylint: disable=unused-variable
			position = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(layout=self._android_hmi.layout.value, xpath=enna_hcp_configuration.android.xpaths.in_car_office.QR_CODE.get())
			qr_region = [position["x"], position["y"], position["x"] + position["width"], position["y"] + position["height"]]
			qr_code = self._android_hmi.take_screenshot().get_roi(qr_region)
			detector = cv2.QRCodeDetector()
			url, area, _ = detector.detectAndDecode(qr_code.as_ndarray)
		except (cv2.error, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as error:
			self._reporting.add_report_message_system_error(f"Could not reading QR code from MMI! {error}")
		return url

	def _link_account_via_website(self, url: str) -> bool:
		"""Try linking mail account via Website.
		Attention: Only support google or microsoft addresses. Other mail providers is not support yet.

		:param url: url to link e-mail account
		:return: True if success, else false.
		"""
		# pylint: disable=too-many-locals
		result = True

		mail_address: str = self.values.get("EMAIL", "hmi.testing.in.car.office.psw@gmail.com")
		password: str = self.values.get("PASSWORD", "hmi-0815-InCarOffice!")

		delay = 3.0
		short_delay = 0.3
		def _input_text(input_field: WebElement, text: str) -> None:
			"""Input text in input field.
			Simulate manual text input.

			:param input_field: Web-Element for input field
			:param text: text to enter
			"""
			for character in text:
				time.sleep(short_delay)
				input_field.send_keys(character)

		# pylint: disable=consider-ternary-expression
		if "@outlook.de" in mail_address:
			button_account_type = "//*[@id='microsoft']"
		else:
			button_account_type = "//*[@id='google']"

		input_field_email = "//*[@type='email']"
		input_field_password = "//*[@type='password']"
		button_forward = "//*[text()='Weiter']"
		select_all = "//*[text()='Alle auswählen']"
		success_linking = "//*[contains(text(), 'Konto verbunden')]"


		options = selenium.webdriver.edge.options.Options()
		options.add_argument('--disable-blink-features=AutomationControlled')

		service = selenium.webdriver.edge.service.Service(str(pathlib.Path(__file__).parent.joinpath("bin/msedgedriver.exe")))
		web_driver = selenium.webdriver.Edge(service=service, options=options)
		# pylint: disable=too-many-try-statements
		try:
			web_driver.get(url=url)
			time.sleep(delay)
			# select account type
			element = web_driver.find_element(By.XPATH, button_account_type)
			element.click()
			time.sleep(delay)
			# enter mail address and continue
			element = web_driver.find_element(By.XPATH,input_field_email)
			_input_text(element, mail_address) # element.send_keys(mail_address)
			element = web_driver.find_element(By.XPATH, button_forward)
			time.sleep(2 * short_delay)
			element.click()
			time.sleep(delay)
			# enter password and continue
			element = web_driver.find_element(By.XPATH, input_field_password)
			_input_text(element, password) # element.send_keys(password)
			time.sleep(2*short_delay)
			element = web_driver.find_element(By.XPATH, button_forward)
			element.click()
			for i in range(10):
				time.sleep(delay)
				try:
					try:
						element = web_driver.find_element(By.XPATH, select_all)
						element.click()
						time.sleep(delay)
					except selenium.common.exceptions.WebDriverException:
						pass
					element = web_driver.find_element(By.XPATH, button_forward)
					element.click()
				except  selenium.common.exceptions.WebDriverException:
					MODULE_LOGGER.info(f"No more Continue Button in Web Content. Before click {i} times.")
					break
			time.sleep(delay)
			element = web_driver.find_element(By.XPATH, success_linking)

		except selenium.common.exceptions.WebDriverException as error:
			self._reporting.add_report_message_ta_error(f"Could not linking account of '{mail_address}' on MMI!")
			MODULE_LOGGER.error(f"{error}")
			result = False

		web_driver.quit()
		return result

	def _postcondition(self) -> bool:
		"""Check E-Mail overview menu is showing.

		:return: True if success, else false.
		"""
		try:
			self._android_hmi.screen_id.wait_for_value(in_car_office.EMAIL_OVERVIEW.name, max_time=120.0)
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error("Account data would not loaded!")
			return False
		self._reporting.add_report_message_pass("Account data are visible.")
		return True
