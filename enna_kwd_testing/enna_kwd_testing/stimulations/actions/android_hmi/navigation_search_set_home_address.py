# -*- coding: utf-8 -*-
"""Created on 14.12.2023.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Claus Teubner.

Contains stimulations for keyword driven testing in context of android_hmi navigation functions.
"""

import logging

import enna.core.component_system.decorators
import enna.core.time
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import navigation as navigation_contexts

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.helper.android_hmi_helper
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetHomeAddress(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set home address in navi.app.
	parameter ADDRESS: str -> default home address 'Rathausplatz 2, 85049 Ingolstadt'
	"""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self._reporting = reporting
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["ADDRESS"]
		self.default_home_address = "Rathausplatz 2, 85049 Ingolstadt"

	def _action(self) -> bool:
		"""Execute action.

		set home address in navi.app.

		1. Navigate to 'navi -> search -> Heimatadresse' screen
		2. Enter home address 'Rathausplatz 2, 85049 Ingolstadt'

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		# pylint: disable = too-many-branches
		enna_kwd_testing.utilities.helper.android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)
		# str_home_address = ""

		if self.allowed_parameter_keys[0] in self.values:
			if self.values[self.allowed_parameter_keys[0]] == "":
				str_home_address = self.default_home_address
			else:
				str_home_address = self.values[self.allowed_parameter_keys[0]]
		else:
			MODULE_LOGGER.error(f"Wrong parameter: '{self.values}', should be something like this -> \n'{self.allowed_parameter_keys[0]}': '{self.default_home_address}'")
			return False

		if not wrapper_android_hmi.go_to_screen(navigation_contexts.SEARCH, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'NAVI.APP -> SEARCH. Something went wrong while navigating to screen.")
			return False
		if not wrapper_android_hmi.wait_for_screen_id(navigation_contexts.SEARCH, android=self.__android_hmi, additional_message="wait for screen", max_time=30):
			return False
		str_recycler_view_list = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="recyclerViewList")
		str_search_list_home_item_details = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="searchListHomeItemDetails")
		str_search_home_address_label = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="searchHomeAddressLabel")
		if wrapper_android_hmi.element_exists(str_search_list_home_item_details, android=self.__android_hmi, additional_message="list_search_list_result_item", max_time=5):
			if not wrapper_android_hmi.wait_and_long_click_variable_duration(str_search_home_address_label, self.__android_hmi, self._reporting, f"Could not find and click '{str_search_home_address_label}' in destination list.", 1.5, 15.0):
				return False
			enna.core.time.sleep(2)
			str_search_linear_layout_image_button_2 = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="searchLinearLayoutImageButton2")
			if not wrapper_android_hmi.wait_and_click(str_search_linear_layout_image_button_2, self.__android_hmi, "Press 'wastebasket' failed."):
				return False

		if not wrapper_android_hmi.wait_and_click_in_list(str_search_home_address_label, str_recycler_view_list, self.__android_hmi, f"Could not find and click '{str_search_home_address_label}' in destination list."):
			return False

		# self._speller.enter_text(str_home_address, True)
		self.__android_hmi.enter_text(text=str_home_address, clear=True)  # enter text if keyboard is open

		if not wrapper_android_hmi.wait_for_screen_id(navigation_contexts.SEARCH_DETAILS, android=self.__android_hmi, additional_message="wait for screen", max_time=30):
			return False
		enna.core.time.sleep(2)
		str_recycler_view_list = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="recyclerViewList")
		str_search_list_result_item = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="searchListResultItem")
		str_search_list_result_item_0 = str_search_list_result_item + "[@index='0']"
		if not wrapper_android_hmi.wait_and_click_in_list(str_search_list_result_item_0, str_recycler_view_list, self.__android_hmi, f"Could not find and click '{str_search_home_address_label}' in destination list."):
			return False
		if not wrapper_android_hmi.wait_for_screen_id(navigation_contexts.SEARCH_DETAILS, android=self.__android_hmi, additional_message="wait for screen", max_time=30):
			return False
		str_button_speichern = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="buttonSpeichern")
		if not wrapper_android_hmi.wait_and_click(str_button_speichern, self.__android_hmi, "Press 'Speichern' failed."):
			return False

		return True

	def _postcondition(self) -> bool:
		"""Execute generic postcondition for keyword driven stimulation.

			:return: True if successful, False otherwise
			:rtype: bool
		"""
		# self._speller.activate_keyboard()
		# self.__android_hmi._InputMethodMixIn.set_fastinput_ime(enable=False)

		return True
