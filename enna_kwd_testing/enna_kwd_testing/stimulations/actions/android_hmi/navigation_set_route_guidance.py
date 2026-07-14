# -*- coding: utf-8 -*-
"""Created on 17.11.2023.

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
import enna_kwd_testing.utilities.helper.android_hmi_helper
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetRouteGuidance(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set route guidance in navi.app.
	parameter STATE: True -> default destination 'Muenchen'
	parameter DESTINATION: 'Berlin'
	parameter COORDINATES: '48.7838361, 11.3824322'"""

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
		self.allowed_parameter_keys = ["STATE"]
		MODULE_LOGGER.debug(f"Allowed Parameter Keys: '{self.allowed_parameter_keys}'.")
		self._keyboard_xpath = "//*[@resource-id='com.audi.automotive.input:id/keyboardViewEx']"

	def _action(self) -> bool:
		"""Execute action.

		route guidance in navi.app.

		1. Navigate to 'navi -> search -> general' screen
		2. Scroll to 'Simply start talking' button in list on screen
		3. Set button state of 'Simply start talking', to given state defined in instance attribute "values" under key "state".

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		# pylint: disable = too-many-branches
		navigation_unknown_screen = "navigation.unknown"
		default_search_position = "Muenchen"
		enna_kwd_testing.utilities.helper.android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)
		str_search_position = "Ingolstadt"

		if "STATE" in self.values:
			if self.values["STATE"] == "TRUE":
				str_search_position = default_search_position
		elif "DESTINATION" in self.values:
			str_search_position = str(self.values["DESTINATION"])
		elif "COORDINATES" in self.values:
			# str_search_position = str(self.values["COORDINATES"])
			MODULE_LOGGER.error("COORDINATES still not implemented :-).^\nThis option will come later, perhaps :-)")
			return False
		else:
			MODULE_LOGGER.error(f"Wrong parameter: '{self.values}', should be -> \nSTATE: 'TRUE' or \nDESTINATION: 'City' or \nCOORDINATES: '48.7838361, 11.3824322'")
			return False

		if not wrapper_android_hmi.go_to_screen(navigation_contexts.SEARCH, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'NAVI.APP -> SEARCH. Something went wrong while navigating to screen.")
			return False

		str_edittext_xpath = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="edit_text")
		try:
			self.__android_hmi.wait_for_element_visible(xpath=str_edittext_xpath, max_time=3.0)
			self.__android_hmi.click_element(xpath=str_edittext_xpath)   # click in input-field to open Audi Keyboard
			self.__android_hmi.wait_for_element_visible(xpath=self._keyboard_xpath, max_time=3.0)
			# self._speller.enter_text(text=str_search_position, clear=True)
			self.__android_hmi.enter_text(text=str_search_position, clear=True)  # enter text if keyboard is open
		except RuntimeError as exc:
			MODULE_LOGGER.error(f"Could not enter Text: '{exc}' . Something went wrong while enter text.")
			return False

		if not wrapper_android_hmi.wait_for_screen_id(navigation_contexts.SEARCH_DETAILS.name, android=self.__android_hmi, additional_message="wait for screen", max_time=30):
			return False
		str_recycler_view_list = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="recyclerViewList")
		list_search_list_result_item = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="firstRowFirstText")
		if not wrapper_android_hmi.wait_and_click_in_list(list_search_list_result_item, str_recycler_view_list, self.__android_hmi, f"Could not find and click '{list_search_list_result_item}' in destination list."):
			return False

		if wrapper_android_hmi.wait_for_screen_id(navigation_unknown_screen, android=self.__android_hmi, additional_message="wait for screen", max_time=5):
			str_dialog_title = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="dialog_title_replace_route_or_add_as_stopover")
			str_button_replace_route = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="button_replace_route")
			if wrapper_android_hmi.wait_for_layout_element(str_dialog_title, self.__android_hmi, "PopUp replace route is shown, press replace destination."):
				if not wrapper_android_hmi.wait_and_click(str_button_replace_route, self.__android_hmi, "Pressed 'replace route' failed."):
					return False

		if not wrapper_android_hmi.wait_for_screen_id(navigation_contexts.GUIDANCE.name, android=self.__android_hmi, additional_message="wait for screen", max_time=30):
			return False
		str_destination_flag_icon = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="destinationFlagIcon")
		if not wrapper_android_hmi.wait_for_layout_element(str_destination_flag_icon, self.__android_hmi, f"'{str_destination_flag_icon}' does not appear."):
			MODULE_LOGGER.error("Destination flag icon does not appear.")
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
