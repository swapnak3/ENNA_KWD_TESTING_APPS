# -*- coding: utf-8 -*-
"""Created on 22.03.2024.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Teubner Claus.

Contains stimulations for keyword driven testing in context of android_hmi aem functions.
"""
import logging
import time

import enna.core.config
import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.core.time
import enna.core.exceptions
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.utilities.menu_navigation.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.stimulations.apps._internal
import enna_kwd_testing.utilities.speller
import enna_kwd_testing.utilities.xpath_collection.helper
import enna_kwd_testing.utilities.xpath_collection.exceptions


MODULE_LOGGER = logging.getLogger(__name__)

# pylint: disable=too-many-locals, too-many-branches, disable=protected-access

class _SetCheckMagicServiceConnection(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Class containing functionality to check apn1 state."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, navigate_to_screen:enna_kwd_testing.stimulations.base.keyword_stim_baseclass):
		r"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_kwd_testing.stimulations.base.keyword_stim_baseclass navigate_to_screen: Instance of navigate to screen
		"""
		super().__init__(reporting, android_hmi)
		self._navigate_to_screen = navigate_to_screen
		self._xpath_handler = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["STATE"]
		self.states = {"CONNECTED": "connected", "DISCONNECTED": "disconnected"}
		self.states_reverse = {value: key for key, value in self.states.items()}

	def _precondition(self) -> bool:
		"""Navigate to Magic Service.

		:return: true if success, else false
		"""
		self._navigate_to_screen.values={"SCREEN_NAME": "magic_engineering.magic_service"}
		return self._navigate_to_screen.start()

	def _get_connection_state(self) -> bool:
		"""get the currently set apn state, but we must already be on the correct screen for that

		:return: True if successful, False if an error occurs in any step.
		"""
		connection_state = self._android_hmi.layout.value.xpath(self.connection_status_xpath)[0].attrib["text"] if len(self._android_hmi.layout.value.xpath(self.connection_status_xpath)) != 0 else "UNKNOWN"
		return self.states_reverse.get(connection_state,"UNKNOWN")
	def _action(self) -> bool:
		"""prepare everything to check/set apn state

		:return: True if successful, False if an error occurs in any step.
		"""
		# pylint: disable=attribute-defined-outside-init
		self.expected_state = self.values.get("STATE", None)
		if self.expected_state not in self.states:
			self._reporting.add_report_message_system_error(f"The MAGIC service connection status '{self.expected_state}' is not an allowed value from {list(self.states.keys())}.")
			return False
		self.connection_status_xpath = self._xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self._android_hmi, element="connection_status")
		self.connection_status = self._get_connection_state()

		if self.connection_status is None:
			self._reporting.add_report_message_system_error(f"The MAGIC service connection status is '{self.connection_status}' which is not an allowed value from {list(self.states.keys())}.")
			return False

		return True

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.general.NavigateToScreen", arg_name="navigate_to_screen")
class CheckMagicServiceConnection(_SetCheckMagicServiceConnection):
	"""check connection to magic service"""
	def _action(self) -> bool:
		"""check connection to magic service

		:return: True if successful, False if an error occurs in any step.
		"""
		if not super()._action():
			return False

		if self.expected_state != self.connection_status:
			self._reporting.add_report_message_system_error(f"The MAGIC service connection status is '{self.connection_status}' and not '{self.expected_state}'.")
			return False

		self._reporting.add_report_message_pass(f"The MAGIC service connection status is '{self.connection_status}' ")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.general.NavigateToScreen", arg_name="navigate_to_screen")
class SetUpMagicServiceConnection(_SetCheckMagicServiceConnection):
	"""set up connection to magic service"""

	def _action(self) -> bool:
		"""set up connection to magic service
		
		:return: True if successful, False if an error occurs in any step.
		"""
		# pylint: disable=attribute-defined-outside-init
		if not super()._action():
			return False

		if self.expected_state != self.connection_status:
			self._reporting.add_report_message_info(f"The MAGIC service connection status is '{self.connection_status}' and not '{self.expected_state}'.")
			self._screen_name = self._android_hmi.screen_id.value
			self._xpath = self._get_xpath_by_parameters(xpath_name="button_close_magic_client" if self.connection_status == "CONNECTED" else "button_connect_magic_client", screen_name=self._screen_name)
			self._android_hmi.wait_for_element_visible(xpath=self._xpath, max_time=self._timeout)
			self._android_hmi.click_element(self._xpath)
			time.sleep(2)
			self.connection_status = self._get_connection_state()
			if self.expected_state != self.connection_status:
				self._reporting.add_report_message_system_error(f"The MAGIC service connection status is '{self.connection_status}' and not '{self.expected_state}'.")
				return False

		self._reporting.add_report_message_pass(f"The MAGIC service connection status is '{self.connection_status}' ")
		return True

class _CheckAPNState(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	""" Check State of APN-Connection"""
	def __init__(self, reporting, apn_number:int , android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, navigate_to_screen:enna_kwd_testing.stimulations.base.keyword_stim_baseclass):
		r"""Initialize stimulation.

		:param int apn_number: Number of APN [1,2]
		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_kwd_testing.stimulations.base.keyword_stim_baseclass navigate_to_screen: Instance of navigate to screen
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self._navigate_to_screen = navigate_to_screen
		self._screen_name = "magic_engineering.connectivity"
		self.__android_hmi = android_hmi
		self.__xpath_handler = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.apn_number=apn_number
		apn_ids=["apn1_connected","apn2_connected"]
		self.apn_id=apn_ids[apn_number-1]
		self.allowed_parameter_keys = ["STATE"]
		self.states = {"CONNECTED": True, "DISCONNECTED": False}
		self.states_reverse = {value: key for key, value in self.states.items()}

	def _precondition(self) -> bool:
		"""Navigate to Magic Service.

		:return: true if success, else false
		"""
		self._navigate_to_screen.values={"SCREEN_NAME": self._screen_name}
		return self._navigate_to_screen.start()

	def _action(self) -> bool:
		"""prepare everything to check/set apn state

		:return: True if successful, False if an error occurs in any step.
		"""
		# pylint: disable=attribute-defined-outside-init
		self.expected_state = self.values.get("STATE", None)
		if self.expected_state not in self.states:
			self._reporting.add_report_message_system_error(f"The MAGIC service connection status '{self.expected_state}' is not an allowed value from {list(self.states.keys())}.")
			return False

		self.connection_status_xpath = self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element=self.apn_id)
		try:
			self.__android_hmi.scroll_to_element_in_list(list_container_xpath=self.__xpath_handler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="list_network_state"), target_xpath=self.connection_status_xpath)
			self.__android_hmi.wait_for_element_visible(self.connection_status_xpath,3)
			self.connection_status = True
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException:
			self.connection_status = False

		if self.connection_status != self.states[self.expected_state]:
			self._reporting.add_report_message_system_error(f"The APN {self.apn_number} state is  '{self.states_reverse[self.connection_status]}' and not {self.expected_state}")
			return False
		self._reporting.add_report_message_pass(f"The APN {self.apn_number} state is '{self.states_reverse[self.connection_status]}' ")
		return True

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.general.NavigateToScreen", arg_name="navigate_to_screen")
class CheckApn1(_CheckAPNState):
	"""Check APN1 State"""
	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, navigate_to_screen:enna_kwd_testing.stimulations.base.keyword_stim_baseclass):
		r"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_kwd_testing.stimulations.base.keyword_stim_baseclass navigate_to_screen: Instance of navigate to screen
		"""
		super().__init__(reporting, 1, android_hmi, navigate_to_screen)

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.general.NavigateToScreen", arg_name="navigate_to_screen")
class CheckApn2(_CheckAPNState):
	"""Check APN2 State"""
	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, navigate_to_screen:enna_kwd_testing.stimulations.base.keyword_stim_baseclass):
		r"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_kwd_testing.stimulations.base.keyword_stim_baseclass navigate_to_screen: Instance of navigate to screen
		"""
		super().__init__(reporting, 2, android_hmi, navigate_to_screen)

class _SuccessfulDummy(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""prepared class for equivalent on magic adaptor"""
	def __init__(self, reporting):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")

	def _action(self) -> bool:
		"""dummy action to avoid skipping

		:return: True if successful, False if an error occurs in any step.
		"""
		self._reporting.add_report_message_info("WARNING!!! This is a dummy Stimulation, successful by default to avoid skipping of Testcase run")
		return True



@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class SetCoreServicesSave(_SuccessfulDummy):
	"""Placeholder for future implementation"""

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class CheckServiceIdStateDisableReasons(_SuccessfulDummy):
	"""Placeholder for future implementation"""

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class SetVinInCoreServices(_SuccessfulDummy):
	"""Placeholder for future implementation"""

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class CheckVinInCoreServices(_SuccessfulDummy):
	"""Placeholder for future implementation"""

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class CheckServiceIdLicenseState(_SuccessfulDummy):
	"""Placeholder for future implementation"""
