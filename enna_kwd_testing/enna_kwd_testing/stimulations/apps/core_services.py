# -*- coding: utf-8 -*-
"""Created on 22.03.2024.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Teubner Claus.

Contains stimulations for keyword driven testing in context of android_hmi aem functions.
"""
import logging
import os

import enna.core.component_system.decorators
import enna.core.config
import enna.core.exceptions
import enna.core.reporting.interface
import enna.core.time
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import core_services

import enna_kwd_testing.stimulations.apps._internal
import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.exceptions
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import android_hmi_helper, wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)
VIN_CONFIG = enna.core.config.get("enna.core.vin.common")

# pylint: disable=too-many-locals, too-many-branches, disable=protected-access

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckApn1(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Class containing functionality to check apn1 state."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self.__android_hmi = android_hmi
		self.__xpath_handler = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["STATE"]

	def _precondition(self) -> bool:
		"""Navigate to CoreServices Home Menu.

		:return: true if success, else false
		"""
		# in clu46 (23.10.2025) CoreServices.app shows after restart the last screen-menue, but HOME ist selected.
		self._go_to_screen(destination=core_services.HEALTH_CHECK if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43 else core_services.HEALTH_CHECK)
		return self._go_to_screen(destination=core_services.HEALTH_CHECK if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43 else core_services.HOME)

	def _action(self) -> bool:
		"""Check APN 1 state

		:return: True if successful, False if an error occurs in any step.
		"""
		expected_state = self.values.get("STATE", None)

		apn1_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.APN1_TEXT")
		apn1_text = self.__android_hmi.layout.value.xpath(apn1_xpath)[0].attrib["text"] if len(self.__android_hmi.layout.value.xpath(apn1_xpath)) != 0 else "UNKNOWN"


		apn1_check_text_connected = "CONNECTED" if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43 else "APN1 CONNECTED"
		apn1_check_text_blocked = "BLOCKED" if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43 else "APN1 BLOCKED"
		if apn1_text == apn1_check_text_connected:
			apn1_text = "CONNECTED"
		elif apn1_text == apn1_check_text_blocked:
			apn1_text = "DISCONNECTED"
		else:
			self._reporting.add_report_message_system_error(f"The APN 1 state is '{apn1_text}' and not {apn1_check_text_connected} or {apn1_check_text_blocked}.")
			return False

		if expected_state != apn1_text:
			self._reporting.add_report_message_system_error(f"The APN 1 state is '{apn1_text}' and not '{expected_state}'.")
			return False

		self._reporting.add_report_message_pass(f"The APN 1 state is '{apn1_text}' ")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckApn2(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Class containing functionality to check apn2 state."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self.__android_hmi = android_hmi
		self.__xpath_handler = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["STATE"]

	def _precondition(self) -> bool:
		"""Navigate to CoreServices Home Menu.

		:return: true if success, else false
		"""
		# in clu46 (23.10.2025) CoreServices.app shows after restart the last screen-menue, but HOME ist selected.
		self._go_to_screen(destination=core_services.HEALTH_CHECK if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43 else core_services.HEALTH_CHECK)
		return self._go_to_screen(destination=core_services.HEALTH_CHECK if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43 else core_services.HOME)

	def _action(self) -> bool:
		"""Check APN 2 state

		:return: True if successful, False if an error occurs in any step.
		"""
		expected_state = self.values.get("STATE", None)

		apn2_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.APN2_TEXT")
		apn2_text = self.__android_hmi.layout.value.xpath(apn2_xpath)[0].attrib["text"] if len(self.__android_hmi.layout.value.xpath(apn2_xpath)) != 0 else "UNKNOWN"

		apn2_check_text_connected = "CONNECTED" if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43 else "APN2 CONNECTED"
		apn2_check_text_blocked = "BLOCKED" if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43 else "APN2 BLOCKED"
		if apn2_text == apn2_check_text_connected:
			apn2_text = "CONNECTED"
		elif apn2_text == apn2_check_text_blocked:
			apn2_text = "DISCONNECTED"
		else:
			self._reporting.add_report_message_system_error(f"The APN 2 state is '{apn2_text}' and not {apn2_check_text_connected} or {apn2_check_text_blocked}.")
			return False

		if expected_state != apn2_text:
			self._reporting.add_report_message_system_error(f"The APN 2 state is '{apn2_text}' and not '{expected_state}'.")
			return False

		self._reporting.add_report_message_pass(f"The APN 2 state is '{apn2_text}' ")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetCoreServicesSave(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Class containing functionality to set apn1 in core-services.app in home menu."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self.__android_hmi = android_hmi
		self._screen_id = ""
		self.__xpath_handler = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["STATE"]

	def _precondition(self) -> bool:
		"""Navigate to CoreServices Home Menu.

		:return: true if success, else false
		"""
		return self._go_to_screen(destination=core_services.HOME if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43 else core_services.CONFIGURATION)

	def _action(self) -> bool:
		"""Press 'SAVE CAR SETTINGS' and wait until 'Count of ServiceList Entries' counts up over 20

		:return: True if successful, False if an error occurs in any step.
		"""
		try:
			save_car_settings_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.CHANGECARSETTINGS")
			popup_confirm_button = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.POPUP_CONFIRM_BUTTON")
			count_of_sle_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.SLENTRIES")
		except enna_kwd_testing.utilities.xpath_collection.exceptions.ElementNotFound as error:
			self._reporting.add_report_message_ta_error(f"Could not found button! Error: {error}.")
			return False
		# click save configuration button
		try:
			self.__android_hmi.wait_for_element_visible(xpath=save_car_settings_xpath, max_time=2.0)
			self.__android_hmi.click_element(xpath=save_car_settings_xpath)
			if enna.core.config.INFOTAINMENT_SYSTEM.cluster > 43:
				self.__android_hmi.wait_for_element_visible(xpath=popup_confirm_button, max_time=2.0)
				self.__android_hmi.click_element(xpath=popup_confirm_button)
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error("Could not found configuration button!")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException:
			self._reporting.add_report_message_system_error("CloUld not click configuration button!")
			return False
		separator: str = " " if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43 else "SL entries: "
		# wait service list is not available (detect refresh of service list was done)
		try:
			self.__android_hmi.wait_for_event("layout", condition=lambda msg: int(self.__android_hmi.layout.value.xpath(count_of_sle_xpath)[0].attrib["text"].split(separator)[1]) < 20, max_time=5.0)
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error("Refresh Service List would not triggered!")
			return False
		except (IndexError, ValueError, TypeError) as error:
			self._reporting.add_report_message_ta_error(f"Error by reading service List entries! {error}")
		# detect service list is reloaded
		try:
			self.__android_hmi.wait_for_event("layout", condition=lambda msg: int(self.__android_hmi.layout.value.xpath(count_of_sle_xpath)[0].attrib["text"].split(separator)[1]) > 20,  max_time=10.0)
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error("Refresh Service List would not success!")
			return False
		except (IndexError, ValueError, TypeError) as error:
			self._reporting.add_report_message_ta_error(f"Error by reading service List entries! {error}")

		self._reporting.add_report_message_pass("Successful refreshing Service List.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckServiceIdStateDisableReasons(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Class containing functionality to check license in service list ."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self.__android_hmi = android_hmi
		self.__xpath_handler = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["SERVICE_ID", "REASON_CONNECTIVITY", "REASON_BACKEND", "REASON_LICENSE", "REASON_CONFIG"]

	def _precondition(self) -> bool:
		"""Navigate to CoreServices Home Menu.

		:return: true if success, else false
		"""
		return self._go_to_screen(destination=core_services.SERVICE_LIST_DISABLE_REASONS)

	def _action(self) -> bool:
		"""Execute action.

		Check if element visible.

		1. Navigate to screen core services service list
		2. Check License in service list

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		try:
			str__service_id = self.values["SERVICE_ID"]
			str__reason_connectivity = self.values.get("REASON REASON_CONNECTIVITY", "ignorieren")
			str__reason_backend = self.values.get("REASON_BACKEND", "ignorieren")
			str__reason_license = self.values.get("REASON_LICENSE", "ignorieren")
			str__reason_config = self.values.get("REASON_CONFIG", "ignorieren")
		except KeyError as exc:
			self._reporting.add_report_message_ta_error(f"The key '{exc}' is not found")
			return False

		if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43:
			str__dismiss_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.DISMISS")
			if wrapper_android_hmi.wait_and_click(str__dismiss_xpath, self.__android_hmi, self._reporting, max_time=1.0):
				info_message = f"I have to press the '{str__dismiss_xpath}' button for enable scrolling."
				self._reporting.add_report_message_info(info_message)

		bool_return = True

		str_service_id_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.SERVICE_ID")
		str_service_id_xpath = f"{str_service_id_xpath}[contains(@text, '{str__service_id}')]"
		if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43:
			str_disable_reasons_recyclerview_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core.services.DISABLE_REASONS_RECYCLERVIEW")
			if not wrapper_android_hmi.wait_and_scroll_in_list(str_service_id_xpath, str_disable_reasons_recyclerview_xpath, self.__android_hmi, max_time=15):
				self._reporting.add_report_message_ta_error(f"The service with ID {str__service_id} not found in list.")
				bool_return = False
		else:
			service_list_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.SERVICE_LIST")
			if not wrapper_android_hmi.wait_and_click_in_list(xpath_element=str_service_id_xpath, xpath_container=service_list_xpath, android=self.__android_hmi, reporting=self._reporting):
				self._reporting.add_report_message_ta_error(f"The service with ID {str__service_id} not found in list.")
				return False

		str_reason_connectivity_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.REASON_CONNECTIVITY")
		if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43:
			str_reason_connectivity_xpath = f"{str_service_id_xpath}/following-sibling::*{str(str_reason_connectivity_xpath).replace('//*', '')}"
		str_reason_connectivity_text = self.__android_hmi.layout.value.xpath(str_reason_connectivity_xpath)[0].attrib["text"]
		if str__reason_connectivity not in("ignorieren", str_reason_connectivity_text):
			self._reporting.add_report_message_ta_error(f"The Reason Connectivity is not '{str__reason_connectivity}'. The Reason Connectivity is '{str_reason_connectivity_text}'.")
			bool_return = False

		str_reason_backend_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.REASON_BACKEND")
		if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43:
			str_reason_backend_xpath = f"{str_service_id_xpath}/following-sibling::*{str(str_reason_backend_xpath).replace('//*', '')}"
		str_reason_backend_text = self.__android_hmi.layout.value.xpath(str_reason_backend_xpath)[0].attrib["text"]
		if str__reason_backend not in("ignorieren", str_reason_backend_text):
			self._reporting.add_report_message_ta_error(f"The Reason Backend is not '{str__reason_backend}'. The Reason Backend is '{str_reason_backend_text}'.")
			bool_return = False

		str_reason_license_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.REASON_LICENSE")
		if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43:
			str_reason_license_xpath = f"{str_service_id_xpath}/following-sibling::*{str(str_reason_license_xpath).replace('//*', '')}"
		str_reason_license_text = self.__android_hmi.layout.value.xpath(str_reason_license_xpath)[0].attrib["text"]
		if str__reason_license not in("ignorieren", str_reason_license_text):
			self._reporting.add_report_message_ta_error(f"The Reason License is not '{str__reason_license}'. The Reason License is '{str_reason_license_text}'.")
			bool_return = False

		str_reason_config_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.REASON_CONFIG")
		if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43:
			str_reason_config_xpath = f"{str_service_id_xpath}/following-sibling::*{str(str_reason_config_xpath).replace('//*', '')}"
		str_reason_config_text = self.__android_hmi.layout.value.xpath(str_reason_config_xpath)[0].attrib["text"]
		if str__reason_config not in("ignorieren", str_reason_config_text):
			self._reporting.add_report_message_ta_error(f"The Reason Config is not '{str__reason_config}'. The Reason Config is '{str_reason_config_text}'.")
			bool_return = False

		if not bool_return:
			return False

		MODULE_LOGGER.info(f"\nThe 'REASON CONNECTIVITY' is '{str_reason_connectivity_text}'."
						   f"\nThe 'REASON BACKEND' is '{str_reason_backend_text}'."
		                   f"\nThe 'REASON LICENSE' is '{str_reason_license_text}'."
						   f"\nThe 'REASON CONFIG' is '{str_reason_config_text}'.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetVinInCoreServices(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Class containing functionality to set vin in core-services.app in home menu."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self.__android_hmi = android_hmi
		self._screen_id = ""
		self.__xpath_handler = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.__xpath_handler_unknown = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="core_services")
		self.allowed_parameter_keys = ["VIN"]

	def _precondition(self) -> bool:
		"""Navigate to CoreServices Home Menu.

		:return: true if success, else false
		"""
		return self._go_to_screen(destination=core_services.HOME if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43 else core_services.CONFIGURATION)

	def _action(self) -> bool:
		"""Execute action.

		set VIN in core_services.app in home menu.

		1. Navigate to 'core_services.HOME' screen
		2. Enter VIN in 'VIN:' with Edit

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""

		self._screen_id = android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)

		test_cube_name = os.environ.get("TestCubeName", "unknown")
		vin: str | None = VIN_CONFIG.get(test_cube_name, None)

		if vin is None:
			self._reporting.add_report_message_ta_error(f"Not found a VIN for TestCubeName: '{test_cube_name}'! Please Check TestCubeName in Config.")
			return False

		str__vin_value = self.values.get("VIN", vin)
		if  vin == str__vin_value:
			self._reporting.add_report_message_info(f"No special VIN for TestCubeName given, use default VIN: '{vin}' for {test_cube_name}!")

		str__vin_edit_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.VIN_EDIT")
		if not wrapper_android_hmi.wait_and_click(str__vin_edit_xpath, self.__android_hmi, self._reporting):
			self._reporting.add_report_message_system_error(f"Could not edit '{str__vin_edit_xpath}'. An error occurred.")
			return False

		self.__android_hmi.enter_text(text=str__vin_value, clear=True)  # enter text if keyboard is open

		str__vin_ok_button = self.__xpath_handler_unknown.get_xpath(screen="unknown", element="core_services.OK")
		str__vin_save_button = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.CHANGECARSETTINGS")

		if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43: # first ok button, then save button
			if not wrapper_android_hmi.wait_and_click(str__vin_ok_button, self.__android_hmi, self._reporting):
				self._reporting.add_report_message_ta_error(f"Could not click on ok button: {str__vin_ok_button}.")
				return False

			if not wrapper_android_hmi.wait_and_click(str__vin_save_button, self.__android_hmi, self._reporting):
				self._reporting.add_report_message_ta_error(f"Could not click on save button: {str__vin_save_button}.")
				return False
		else: # cl46 - first save button, then confirm button
			if not wrapper_android_hmi.wait_and_click(str__vin_save_button, self.__android_hmi, self._reporting):
				self._reporting.add_report_message_ta_error(f"Could not click on save button: {str__vin_save_button}.")
				return False

			if not wrapper_android_hmi.wait_and_click(str__vin_ok_button, self.__android_hmi, self._reporting):
				self._reporting.add_report_message_ta_error(f"Could not click on ok button: {str__vin_ok_button}.")
				return False

		MODULE_LOGGER.info(f"The VIN: is set to '{str__vin_value}' ")

		return True

	def _postcondition(self):
		"""Execute generic postcondition for keyword driven stimulation.

			:return: True if successful, False otherwise
			:rtype: bool
		"""
		# self._speller.activate_keyboard()
		# self.__android_hmi._InputMethodMixIn.set_fastinput_ime(enable=False)

		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckVinInCoreServices(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Class containing functionality to set vin in core-services.app in home menu."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self.__android_hmi = android_hmi
		self._screen_id = ""
		self.__xpath_handler = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["VIN"]

	def _precondition(self) -> bool:
		"""Navigate to CoreServices Home Menu.

		:return: true if success, else false
		"""
		return self._go_to_screen(destination=core_services.HOME if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43 else core_services.CONFIGURATION)

	def _action(self) -> bool:
		"""Execute action.

		check VIN in core_services.app in home menu.

		1. Navigate to 'core_services.HOME' screen
		2. Read VIN in 'VIN:' and compare it with parameter VIN

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""

		self._screen_id = android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)

		test_cube_name = os.environ.get("TestCubeName", "unknown")
		vin: str | None = VIN_CONFIG.get(test_cube_name, None)

		if vin is None:
			self._reporting.add_report_message_ta_error(f"Not found a VIN for TestCubeName: '{test_cube_name}'! Please Check TestCubeName in Config.")
			return False

		str__vin_value = self.values.get("VIN", vin)
		if vin == str__vin_value:
			self._reporting.add_report_message_info(f"No special VIN for TestCubeName given, use default VIN: '{vin}' for {test_cube_name}!")

		str__vin_edit_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.VIN_EDIT")
		str__vin_core_services = wrapper_android_hmi.get_element_by_xpath(str__vin_edit_xpath, self.__android_hmi, self._reporting)
		if str__vin_value != str__vin_core_services.get('text'):
			self._reporting.add_report_message_system_error(f"Search VIN: '{str__vin_value}' is not the same VIN: '{str__vin_core_services.get('text')}' on CoreServices. An error occurred.")
			return False

		self._reporting.add_report_message_info(f"The searched VIN: '{str__vin_value}' is set in CoreServices.")
		MODULE_LOGGER.info(f"The searched VIN: '{str__vin_value}' is set in CoreServices.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckServiceIdLicenseState(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Class containing functionality to check license in service list ."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self.__android_hmi = android_hmi
		self.__xpath_handler = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["SERVICE_ID", "STATE"]

	def _precondition(self) -> bool:
		"""Navigate to CoreServices Home Menu.

		:return: true if success, else false
		"""
		return self._go_to_screen(destination=core_services.SERVICE_LIST_DISABLE_REASONS)

	def _action(self) -> bool:
		"""Execute action.

		Check if element visible.

		1. Navigate to screen core services service list
		2. Check License in service list

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		try:
			str_service_id = self.values["SERVICE_ID"]
			str_license_state = self.values["STATE"]
		except KeyError as exc:
			self._reporting.add_report_message_ta_error(f"The key '{exc}' is not found")
			return False

		if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43:
			str__dismiss_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.DISMISS")
			if wrapper_android_hmi.wait_and_click(str__dismiss_xpath, self.__android_hmi, self._reporting, max_time=1.0):
				info_message = f"I have to press the '{str__dismiss_xpath}' button for enable scrolling."
				self._reporting.add_report_message_info(info_message)

		service_list_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.SERVICE_LIST")
		service_id_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.SERVICE_ID")
		license_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.LICENSE")
		service_id_xpath = f"{service_id_xpath}[contains(@text, '{str_service_id}')]"

		if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43:
			if not wrapper_android_hmi.wait_and_scroll_in_list(service_id_xpath, service_list_xpath, self.__android_hmi, max_time=7):
				self._reporting.add_report_message_ta_error("The service list is not found.")
				return False

			license_state_xpath = f"{service_id_xpath}/following-sibling::*{str(license_xpath).replace('//*', '')}"
		else:
			if not wrapper_android_hmi.wait_and_click_in_list(xpath_element=service_id_xpath, xpath_container=service_list_xpath, android=self.__android_hmi, reporting=self._reporting):
				self._reporting.add_report_message_ta_error(f"The service with ID {str_service_id} not found in list.")
				return False

			license_state_xpath = license_xpath

		if not wrapper_android_hmi.wait_for_layout_element(license_state_xpath, self.__android_hmi, max_time=7):
			self._reporting.add_report_message_ta_error(f"The service with ID {str_service_id} not found in list.")
			return False

		str_license_text = self.__android_hmi.layout.value.xpath(license_state_xpath)[0].attrib["text"]

		if str_license_text != str_license_state:
			self._reporting.add_report_message_info(f"The license is not '{str_license_state}'. The license is '{str_license_text}'.")
			return False

		MODULE_LOGGER.info(f"The license for '{str_service_id}' is '{str_license_text}'.")

		return True
