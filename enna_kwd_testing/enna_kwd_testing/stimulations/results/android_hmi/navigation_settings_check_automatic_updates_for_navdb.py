# -*- coding: utf-8 -*-
"""Created on 17.01.2024.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Claus Teubner.

Contains stimulations for keyword driven testing in context of android_hmi navigation functions.
"""

import logging

import enna.core.component_system.decorators
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import navigation as navigation_contexts

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckAutomaticUpdatesNavdb(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to activate/deactivate the switch for automatic updates from navdb in navigation settings.

		parameter STATE: ACTIVATED -> check state of activate automatic updates is activated, DEACTIVATED -> check state of deactivate automatic updates is deactivated '"""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Execute action.

		Check state for automatic updates option is ACTIVATED/DEACTIVATED

		1. Navigate to 'navigation ->  navigation.settings_naviinfo' screen
		2. Check button state to given state defined in instance attribute "values" under key "state".

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		enna_kwd_testing.utilities.helper.android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)

		str_toggle_button_state = str(self.values["STATE"])
		if str_toggle_button_state == "ACTIVATED":
			bool_toggle_button_state = True
		elif str_toggle_button_state == "DEACTIVATED":
			bool_toggle_button_state = False
		else:
			MODULE_LOGGER.error(f"Wrong parameter for STATE:'{str_toggle_button_state}', should be 'ACTIVATED' or 'DEACTIVATED")
			return False

		if not wrapper_android_hmi.go_to_screen(navigation_contexts.SETTINGS_NAVIINFORMATION, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'NAVIGATION -> SETTINGS_NAVIINFORMATION. Something went wrong while navigating to screen.")
			return False

		if not wrapper_android_hmi.wait_for_screen_id(navigation_contexts.SETTINGS_NAVIINFORMATION, android=self.__android_hmi, additional_message="wait for screen", max_time=30):
			return False

		str_xpath__automatic_database_update_switch = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="AutomaticDatabaseUpdate-switch")

		if (state := wrapper_android_hmi.wait_and_get_toggle_button_state(str_xpath__automatic_database_update_switch, self.__android_hmi, self._reporting,
		                                                                  f"Could not get toggle button '{bool_toggle_button_state}' for '{str_xpath__automatic_database_update_switch}'.\n"
		                                                                  f"An error occurred.\n"
		                                                                  f"Perhaps, there is no switch for 'Automatische Updates'.\n"
		                                                                  f"Check, if the system has online connection.")
		) is None:
			return False
		return state == bool_toggle_button_state
