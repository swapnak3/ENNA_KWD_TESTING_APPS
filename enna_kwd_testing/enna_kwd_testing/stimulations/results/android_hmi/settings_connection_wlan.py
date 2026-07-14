"""Created on 18.12.2023.

@project: enna_kwd_testing.
@author: T6B0NVV: Frank Isselhard.

Contains stimulations for keyword driven testing in context of android_hmi settings functions.
"""

import logging

import enna.core.component_system.decorators
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
class CheckSystemWlanState(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check the wlan option in connection settings.

		parameter STATE: TRUE -> wlan is on, FALSE -> wlan is off '"""

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
		self._parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Execute action.

		Check the state of the wlan option

		1. Navigate to 'settings ->  connections' screen
		2. Click on the WLAN section of the connection settings
		2. Scroll to 'wlan' button on screen
		3. Get button state to check the state defined in instance attribute "values" under key "state".

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		enna_kwd_testing.utilities.helper.android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)

		str_toggle_button_state = str(self.values["STATE"])
		if str_toggle_button_state == "TRUE":
			bool_toggle_button_state = True
		elif str_toggle_button_state == "FALSE":
			bool_toggle_button_state = False
		else:
			MODULE_LOGGER.error(f"Wrong parameter for STATE:'{str_toggle_button_state}', should be 'TRUE' or 'FALSE")
			return False

		if not wrapper_android_hmi.go_to_screen(phone.CONNECTIONS, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'SETTINGS -> CONNECTIONS. Something went wrong while navigating to screen.")
			return False

		str_xpath_wlan_settings = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="wlan_title")
		if wrapper_android_hmi.element_exists(str_xpath_wlan_settings, self.__android_hmi):
			wrapper_android_hmi.wait_and_click(str_xpath_wlan_settings,  self.__android_hmi,  self._reporting)
		else:
			return False

		str_xpath__list_container = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="main_list")
		str_xpath__short_prompt_switch = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="wlan_switch_btn")
		if not wrapper_android_hmi.wait_and_scroll_in_list(str_xpath__short_prompt_switch, str_xpath__list_container, self.__android_hmi,
														   f"Could not find '{str_xpath__short_prompt_switch}' in settings -> connections."):
			return False

		state = wrapper_android_hmi.wait_and_get_toggle_button_state(str_xpath__short_prompt_switch, self.__android_hmi, self._reporting,
																	f"Could not get toggle button state for '{str_xpath__short_prompt_switch}' button. An error occurred.")
		if not state == bool_toggle_button_state:
			return False
		return True
