# -*- coding: utf-8 -*-
"""Created on 21.09.2023.
	Repair on 25.09.2024.

@project: enna_kwd_testing.
@author: SPLATZP: Platzer Pascal.

Contains stimulations for keyword driven testing in context of android_hmi apn state.
"""

import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import core_services

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckApn1(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check apn1 state."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Execute action.

		Check if element visible.

		1. Navigate to screen CoreService
		2. Check APN 1 state

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		try:
			str_apn_state = self.values["STATE"]
		except KeyError as exception:
			self._reporting.add_report_message_ta_error(f"Value {exception} not found")
			return False

		if not wrapper_android_hmi.go_to_screen(core_services.HEALTH_CHECK, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'core_services.HEALTH_CHECK' . Something went wrong while navigating to screen.")
			return False

		apn_xpath = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.APN1_STATE")
		self.__android_hmi.wait_for_element_visible(apn_xpath, max_time=7)
		str_apn_state_car = self.__android_hmi.layout.value.xpath(apn_xpath)[0].attrib["text"]

		if str_apn_state not in str_apn_state_car:
			MODULE_LOGGER.error(f"The APN 1 state is '{str_apn_state_car}' and not '{str_apn_state}'.")
			return False

		MODULE_LOGGER.info(f"The APN 1 state is '{str_apn_state_car}' ")

		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckApn2(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check apn2 state."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Execute action.

		Check APN State.

		1. Navigate to screen CoreService
		2. Check APN 2 state

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		try:
			str_apn_state = self.values["STATE"]
		except KeyError as exception:
			self._reporting.add_report_message_ta_error(f"Value {exception} not found")
			return False

		if not wrapper_android_hmi.go_to_screen(core_services.HEALTH_CHECK, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'core_services.HEALTH_CHECK' . Something went wrong while navigating to screen.")
			return False

		apn_xpath = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="core_services.APN2_STATE")
		self.__android_hmi.wait_for_element_visible(apn_xpath, max_time=7)
		str_apn_state_car = self.__android_hmi.layout.value.xpath(apn_xpath)[0].attrib["text"]

		if str_apn_state not in str_apn_state_car:
			MODULE_LOGGER.error(f"The APN 2 state is '{str_apn_state_car}' and not '{str_apn_state}'.")
			return False

		MODULE_LOGGER.info(f"The APN 2 state is '{str_apn_state_car}' ")

		return True
