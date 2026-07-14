# -*- coding: utf-8 -*-
"""Module contains stimulation for touching and checking methods of settings app."""
import enum
import logging
import time

import enna.core.config
import enna.core.exceptions
import enna.core.component_system.decorators
import enna.core.reporting.interface

import enna_st12.instance_names
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.data_interfaces.android_hmi.helper
import enna_st12.utilities.menu_navigation.interface

import enna_hcp_configuration.android.contexts.settings
import enna_hcp_configuration.android.contexts.car
import enna_hcp_configuration.android.xpaths.settings
import enna_hcp_configuration.android.xpaths.car
import enna_hcp_configuration.android.xpaths.permissioncontroller

import enna_kwd_testing.utilities.xpath_collection.helper
import enna_kwd_testing.utilities.xpath_collection.exceptions
import enna_kwd_testing.stimulations.apps._internal
import enna_kwd_testing.stimulations.base.keyword_stim_baseclass


MODULE_LOGGER = logging.getLogger(__name__)


class SupportedLanguages(enum.StrEnum):
	"""Constants of supported languages."""
	# pylint: disable=invalid-name
	bs_BA = "Bosanski (Bosna i Hercegovina)"
	hr_HR = "Hrvatski (Hrvatska)"
	cs_CZ = "Čeština (Česko)"
	da_DK = "Dansk (Danmark)"
	nl_NL = "Nederlands (Nederland)"
	en_GB = "English (United Kingdom)"
	fi_FI = "Suomi (Suomi)"
	fr_FR = "Français (France)"
	de_DE = "Deutsch (Deutschland)"
	el_GR = "Ελληνικά (Ελλάδα)"
	hu_HU = "Magyar (Magyarország)"
	it_IT = "Italiano (Italia)"
	no_NO = "Norsk (Norge)"
	pl_PL = "Polski (Polska)"
	pt_PT = "Português (Portugal)"
	ro_RO = "Română (România)"
	ru_RU = "Русский (Россия)"
	sr_RS = "Srpski (latinica, Srbija)"
	sk_SK = "Slovenčina (Slovensko)"
	sl_SI = "Slovenščina (Slovenija)"
	es_ES = "Español (España)"
	sv_SE = "Svenska (Sverige)"
	tr_TR = "Türkçe (Türkiye)"
	uk_UA = "Українська (Україна)"


# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetGeneralLocationInSystemSettings(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation using location data in system."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.settings.SYSTEM_LOCATION
		self._list_container = enna_hcp_configuration.android.xpaths.settings.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.settings.SYSTEM_LOCATION_USE_SWITCH


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class HideSystemApps(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation hide system apps."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.settings.APPS_APP_INFO_VIEWALL
		self._list_container = enna_hcp_configuration.android.xpaths.settings.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.settings.APPS_HIDE_SYSTEM_APPS


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetAutomaticSystemTime(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation usage automatic system time."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.car.SETTINGS_SYSTEM_DATE_AND_TIME
		self._list_container = enna_hcp_configuration.android.xpaths.car.MAIN_LIST
		self._button = enna_hcp_configuration.android.xpaths.car.SWITCH_SET_AUTOMATIC


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetAutomaticTimeZone(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation usage automatic time zone detection."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.car.SETTINGS_SYSTEM_DATE_AND_TIME
		self._list_container = enna_hcp_configuration.android.xpaths.car.MAIN_LIST
		self._button = enna_hcp_configuration.android.xpaths.car.SWITCH_SET_AUTOMATIC_TIME_ZONE


# pylint: disable=too-many-try-statements, too-many-instance-attributes
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetSystemAppPermission(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Class containing functionality to set system app permission in settings."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Initialize stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param  menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, menu_navigation=menu_navigation, android_hmi=android_hmi)
		self.allowed_parameter_keys = ["APP_NAME", "PERMISSION", "STATE"]

		# Aktuell reicht es aus die System-Apps ausgeblendet zu lassen. Sollten später System-Apps eingepflegt werden, muss der Screen wieder angepasst werden
		self._context_all_apps = enna_hcp_configuration.android.contexts.settings.APPS_APP_INFO

		self._xpath_handler = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="settings")
		self._permissions_list = {'CARINFO': enna_hcp_configuration.android.xpaths.permissioncontroller.PERMISSION_ADDITIONAL.get(),
		                          'CONTACTS': enna_hcp_configuration.android.xpaths.permissioncontroller.PERMISSION_CONTACTS.get(),
		                          'FILES_MEDIA': enna_hcp_configuration.android.xpaths.permissioncontroller.PERMISSION_FILES_MEDIA.get(),
		                          'LOCATION': enna_hcp_configuration.android.xpaths.permissioncontroller.PERMISSION_LOCATION.get(),
		                          'MICROPHONE': enna_hcp_configuration.android.xpaths.permissioncontroller.PERMISSION_MICROPHONE.get(),
		                          'NOTIFICATIONS': enna_hcp_configuration.android.xpaths.permissioncontroller.PERMISSION_NOTIFICATIONS.get(),
		                          'PHONE': enna_hcp_configuration.android.xpaths.permissioncontroller.PERMISSION_PHONE.get(),
		                          'POSITION': enna_hcp_configuration.android.xpaths.permissioncontroller.PERMISSION_LOCATION.get()
		                          }
		self._permission_states = {'ALLOW': enna_hcp_configuration.android.xpaths.permissioncontroller.PERMISSION_ALLOW.get(),
		                           'USAGE': enna_hcp_configuration.android.xpaths.permissioncontroller.PERMISSION_USAGE.get(),
		                           'DENY': enna_hcp_configuration.android.xpaths.permissioncontroller.PERMISSION_DENY.get()
		                           }
		self._apps = {
			"AEM": enna_hcp_configuration.android.xpaths.settings.AEM.get(),
			"ANDROID_AUTO": enna_hcp_configuration.android.xpaths.settings.ANDROID_AUTO.get(),
			"APPLE_CARPLAY": enna_hcp_configuration.android.xpaths.settings.APPLE_CARPLAY.get(),
			"ATX": enna_hcp_configuration.android.xpaths.settings.ATX.get(),
			"AUDI_ASSISTANT": enna_hcp_configuration.android.xpaths.settings.ANDROID_AUTO.get(),
			"CAR": enna_hcp_configuration.android.xpaths.settings.CAR.get(),
			"EXPERIENCES": enna_hcp_configuration.android.xpaths.settings.EXPERIENCES.get(),
			"NAVIGATION": enna_hcp_configuration.android.xpaths.settings.NAVIGATION.get(),
			"THEMES": enna_hcp_configuration.android.xpaths.settings.THEMES.get()
		}
		self._xpath_list_container = None
		self._xpath_app = None
		self._xpath_permission = None
		self._xpath_status = None
		self._xpath_open_permission_menu = None
		self._xpath_permission_additional_car = None
		self._xpath_dialog_accept_button = enna_hcp_configuration.android.xpaths.permissioncontroller.DIALOG_DENY_PERMISSION_ACCEPT_BUTTON.get()
		self._xpath_back_button = enna_hcp_configuration.android.xpaths.permissioncontroller.PERMISSION_BACK_BUTTON.get()

	def _precondition(self) -> bool:
		"""Read all parameters and navigate to settings menu of view all apps.

		:return: True if success, else False
		"""
		try:
			self._xpath_list_container = enna_hcp_configuration.android.xpaths.settings.MAIN_LIST.get()
			self._xpath_app = self._apps[self.values.get("APP_NAME", "unknown").upper()]
			self._xpath_open_permission_menu = enna_hcp_configuration.android.xpaths.settings.PERMISSIONS.get()
			self._xpath_permission = self._permissions_list[self.values.get("PERMISSION", "unknown").upper()]
			self._xpath_status = self._permission_states[self.values.get("STATE", "unknown").upper()]
			self._xpath_permission_additional_car = enna_hcp_configuration.android.xpaths.permissioncontroller.PERMISSION_CARINFO.get()
		except KeyError as error:
			self._reporting.add_report_message_ta_error(f"Missing valid parameter! {error}")
			return False
		# add go_to_screen, because settings.ALL_APPS fails on CLU46 sometimes from settings APPS_...
		self._go_to_screen(enna_hcp_configuration.android.contexts.settings.MAIN)
		return self._go_to_screen(self._context_all_apps)

	def _action(self) -> bool:
		"""Select an app and set a permission to expected status.

		:return: True if success, else False
		"""
		if not self._open_permission_menu():
			return False
		if not self._set_permission():
			return False
		self._reporting.add_report_message_pass(f"Set  permission for {self.values.get("PERMISSION", "")} to {self.values.get("STATE", "")} in app {self.values.get("APP_NAME", "")}")
		return True

	def _open_permission_menu(self, delay: float = 0.7) -> bool:
		"""Open menu to set permission.

		:param delay: delay between steps on click actins
		:return: True if success, else False
		"""
		try:
			# select app in settings app list
			self._android_hmi.wait_for_element_visible(xpath=self._xpath_list_container, max_time=10.0)
			self._android_hmi.click_element_in_list(xpath=self._xpath_app, list_container_xpath=self._xpath_list_container)
			time.sleep(delay)
			# open permissions list for app
			self._android_hmi.wait_for_element_visible(xpath=self._xpath_list_container, max_time=10.0)
			self._android_hmi.click_element_in_list(xpath=self._xpath_open_permission_menu, list_container_xpath=self._xpath_list_container)
			time.sleep(delay)
			# select a permission
			self._android_hmi.wait_for_element_visible(xpath=self._xpath_list_container, max_time=10.0)
			self._android_hmi.click_element_in_list(xpath=self._xpath_permission, list_container_xpath=self._xpath_list_container)
			time.sleep(delay)
			# handling of additional permissions
			if self.values.get("PERMISSION", "").upper() == "CARINFO":
				self._android_hmi.wait_for_element_visible(xpath=self._xpath_permission_additional_car, max_time=10.0)
				self._android_hmi.click_element(xpath=self._xpath_permission_additional_car)
				time.sleep(delay)
		except (enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException, enna.core.exceptions.TimeoutException) as error:
			self._reporting.add_report_message_ta_error(f"Could not open settings menu of permission for {self.values.get("PERMISSION", "")} to {self.values.get("STATE", "")} in app {self.values.get("APP_NAME", "")}! Error: {error}")
			return False
		return True

	def _set_permission(self, delay: float = 0.7) -> bool:
		"""Set permission.

		:param delay: delay between steps on click actins
		:return: True if success, else False
		"""
		try:
			self._android_hmi.wait_for_element_visible(xpath=self._xpath_status, max_time=10.0)
			self._android_hmi.click_element(xpath=self._xpath_status)
			time.sleep(delay)
			# Popup handling
			try:
				self._android_hmi.wait_for_element_visible(self._xpath_dialog_accept_button, max_time=3.0)
				self._android_hmi.click_element(self._xpath_dialog_accept_button)
				time.sleep(delay)
			except enna.core.exceptions.TimeoutException:
				MODULE_LOGGER.debug("No Popup must consent.")
		except (enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException, enna.core.exceptions.TimeoutException) as error:
			self._reporting.add_report_message_system_error(f"Could not set permission for {self.values.get("PERMISSION", "")} to {self.values.get("STATE", "")} in app {self.values.get("APP_NAME", "")}! Error: {error}")
			return False
		return True

	def _postcondition(self) -> bool:
		"""Check setting permission to excepted value.

		:return: True if success, else False
		"""
		try:
			self._android_hmi.wait_for_element_visible(xpath=self._xpath_status, max_time=5.0)
			radio_button = f"{self._xpath_status}/../../..//*[@resource-id='com.android.permissioncontroller:id/radio_button']"
			if not enna_st12.data_interfaces.android_hmi.helper.get_radio_button_state(layout=self._android_hmi.layout.value, xpath=radio_button):
				self._reporting.add_report_message_system_error(f"State of permission for {self.values.get("PERMISSION", "")} to {self.values.get("STATE", "")} in app {self.values.get("APP_NAME", "")} is wrong")
				return False
		except (enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException, enna.core.exceptions.TimeoutException) as error:
			self._reporting.add_report_message_system_error(f"Could not check permission for {self.values.get("PERMISSION", "")} to {self.values.get("STATE", "")} in app {self.values.get("APP_NAME", "")}! Error: {error}")
			return False
		self._reporting.add_report_message_pass(f"State of permission for {self.values.get("PERMISSION", "")} to {self.values.get("STATE", "")} in app {self.values.get("APP_NAME", "")} is checked")
		# close screen to be faster
		try:
			self._android_hmi.wait_for_element_visible(self._xpath_back_button, max_time=5.0)
			self._android_hmi.click_element(self._xpath_back_button)
			try:
				self._android_hmi.wait_for_element_visible(self._xpath_back_button, max_time=5.0)
				self._android_hmi.click_element(self._xpath_back_button)
			except enna.core.exceptions.TimeoutException:
				MODULE_LOGGER.info("Screen could not be closed.")
		except enna.core.exceptions.TimeoutException:
			MODULE_LOGGER.info("Screen could not be closed.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckSystemAppPermission(SetSystemAppPermission):
	"""Stimulation for checking permission of app."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Initialize stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param  menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)

	def _action(self) -> bool:
		"""Select an app permission menu.

		:return: True if success, else False
		"""
		return self._open_permission_menu()


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckSystemLanguage(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Check current system language is equal the expected value."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface) -> None:
		"""Instanced Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation.__init__(self, reporting=reporting, based_on_kwd_spec_version="1.0.4")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=self._reporting, android_hmi=android_hmi,menu_navigation=menu_navigation)
		self._expected_language_code: str = enna.core.config.INFOTAINMENT_SYSTEM.system_language.value
		self._expected_language: str = "unknown"
		self._current_language: str = ""
		self.allowed_parameter_keys.append("LANG")

	def _precondition(self) -> bool:
		"""Navigate to settings language and input menu.

		:return: True if success, else False
		"""
		self._expected_language_code = self.values.get("LANG", enna.core.config.INFOTAINMENT_SYSTEM.system_language.value)
		return self._go_to_screen(destination=enna_hcp_configuration.android.contexts.settings.SYSTEM_LANGUAGESINPUT_INPUT)

	def _action(self) -> bool:
		"""Check Language equal excepted.

		:return: True if success, else False
		"""
		try:
			self._android_hmi.screen_id.wait_for_value(enna_hcp_configuration.android.contexts.settings.SYSTEM_LANGUAGESINPUT_INPUT.name, max_time=3.0)
			self._android_hmi.wait_for_element_visible(xpath=enna_hcp_configuration.android.xpaths.settings.LIST_ITEM_SUMMARY_LANGUAGE.get(), max_time=3.0)
			self._current_language = self._android_hmi.layout.value.xpath(enna_hcp_configuration.android.xpaths.settings.LIST_ITEM_SUMMARY_LANGUAGE.get())[0].attrib["text"]
			self._expected_language = getattr(SupportedLanguages, self._expected_language_code)
			if self._current_language != self._expected_language:
				self._reporting.add_report_message_info(f"Expected Language '{self._expected_language}' not equal current language '{self._current_language}'!")
				return False
		except (AttributeError, enna.core.exceptions.TimeoutException, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as error:
			self._reporting.add_report_message_ta_error(f"Could not check language! {error}")
			return False
		self._reporting.add_report_message_pass(f"Current language is equal expected language. System Language = '{self._current_language}'")
		return True



@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetSystemLanguage(CheckSystemLanguage):
	"""Set system language is equal the expected value."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface) -> None:
		"""Instanced Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)

	def _action(self) -> bool:
		"""Set current system language to expected value.

		:return: True if success, else False
		"""

		if super()._action():
			self._reporting.add_report_message_pass("System Language already is expected.")
			return True
		try:
			if not self._go_to_screen(destination=enna_hcp_configuration.android.contexts.settings.SYSTEM_LANGUAGESINPUT_LANGUAGES):
				return False
			self._android_hmi.wait_for_element_visible(xpath=enna_hcp_configuration.android.xpaths.settings.LIST_CONTAINER.get(), max_time=5.0)
			self._android_hmi.click_element_in_list(xpath=f"//*[contains(@text, '{self._expected_language}')]", list_container_xpath=enna_hcp_configuration.android.xpaths.settings.LIST_CONTAINER.get())
			self._android_hmi.screen_id.wait_for_value(enna_hcp_configuration.android.contexts.settings.SYSTEM_LANGUAGESINPUT_INPUT.name, max_time=10.0)
		except (enna.core.exceptions.TimeoutException, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as error:
			self._reporting.add_report_message_ta_error(f"Could not set to language '{self._expected_language}'! {error}")
			return False
		return super()._action()
