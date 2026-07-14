# -*- coding: utf-8 -*-
"""Created on 29.11.2023.

@project: enna_kwd_testing.
@author: S6FXUOM, Nikolaus Maier.

Contains stimulations for KWD-TA in context of android_hmi sds settings functions.
"""

import logging

import enna.core.component_system.decorators
import enna.core.time
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import phone

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper

from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetSystemBluetoothState(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set system bluetooth state in settings."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self._parameter_keys = ["STATE"]
		self.__bluetooth__setsystembluetoothstate__xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="settings_connection_bluetooth")

	def _action(self) -> bool:
		"""Execute action.

		Set bluetooth state to specific state .

		1. Use go to screen to open 'Settings -> Connection -> Bluetooth'
		2. Set system bluetooth state in settings


		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		str_switch_control_button = self.__bluetooth__setsystembluetoothstate__xpaths.get_xpath("bluetooth_main", "switch_control_button")

		bt_state_new = str(self.values["STATE"])
		if bt_state_new == "ACTIVATED":
			bool_toggle_button_state = True
		elif bt_state_new == "DEACTIVATED":
			bool_toggle_button_state = False
		else:
			MODULE_LOGGER.error(f"Wrong parameter for STATE:'{bt_state_new}', should be 'ACTIVATED' or 'DEACTIVATED")
			return False

		if not wrapper_android_hmi.go_to_screen(phone.BLUETOOTH_SETTINGS, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'Bluetooth settings. Something went wrong while navigating to screen.")
			return False

		if not wrapper_android_hmi.wait_for_layout_element(str_switch_control_button, self.__android_hmi, msg := "Switch button not present on layout"):
			MODULE_LOGGER.error(msg)
			return False

		if not wrapper_android_hmi.wait_and_set_toggle_button_state(str_switch_control_button, bool_toggle_button_state, self.__android_hmi, self._reporting,
																	f"Could not get toggle button state for '{str_switch_control_button}' button. An error occurred."):
			return False

		return True
