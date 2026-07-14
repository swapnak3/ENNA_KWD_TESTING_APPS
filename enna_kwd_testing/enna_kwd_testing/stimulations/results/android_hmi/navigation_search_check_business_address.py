# -*- coding: utf-8 -*-
"""Created on 15.12.2023.

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
import enna_kwd_testing.utilities.speller
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.speller")
class CheckBusinessAddress(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check business address in navi.app.
	parameter ADDRESS: str -> default business address 'Carl-Benz-Ring, Mittlere Heide, Gaimersheim'
	"""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface, speller):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		:param enna_kwd_testing.utilities.speller.interface.Interface speller: speller interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self._reporting = reporting
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self._speller = speller
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["ADDRESS"]
		self.default_business_address = "Rathausplatz 2, Ingolstadt"

	def _action(self) -> bool:
		"""Execute action.

		check business address in navi.app.

		1. Navigate to 'navi -> search -> Heimatadresse' screen
		2. Read home address and compare to ADDRESS:"STRING" or default 'Carl-Benz-Ring 7, Mittlere Heide, Gaimersheim'

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		# pylint: disable = too-many-branches
		enna_kwd_testing.utilities.helper.android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)

		if self.allowed_parameter_keys[0] in self.values:
			if self.values[self.allowed_parameter_keys[0]] == "":
				str_business_address = self.default_business_address
			else:
				str_business_address = self.values[self.allowed_parameter_keys[0]]
		else:
			MODULE_LOGGER.error(f"Wrong parameter: '{self.values}', should be something like this -> \n'{self.allowed_parameter_keys[0]}': '{self.default_business_address}'")
			return False

		if not wrapper_android_hmi.go_to_screen(navigation_contexts.SEARCH, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'NAVI.APP -> SEARCH. Something went wrong while navigating to screen.")
			return False
		if not wrapper_android_hmi.wait_for_screen_id(navigation_contexts.SEARCH, android=self.__android_hmi, additional_message="wait for screen", max_time=30):
			return False

		str_search_business_item_assigned = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="searchListBusinessItemAssigned")
		str_search_business_item_not_assigned = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="searchListBusinessItemNotAssigned")
		str_search_business_second_line = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="searchBusinessAddressSecondRow")
		str_search_business_second_line_not = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="searchBusinessAddressSecondRowNot")

		if wrapper_android_hmi.element_exists(str_search_business_item_assigned, android=self.__android_hmi, additional_message="str_search_business_item_assigned", max_time=5):
			str_business_address_second_line = wrapper_android_hmi.get_element_by_xpath(str_search_business_second_line, self.__android_hmi, self._reporting, additional_message="get business address second line")
			if str_business_address in str_business_address_second_line:
				MODULE_LOGGER.info(f"business address: '{str_business_address}' is in: '{str_business_address_second_line}'.")
			else:
				MODULE_LOGGER.error(f"business address: '{str_business_address}' is not in: '{str_business_address_second_line}'.")
				return False
		elif wrapper_android_hmi.element_exists(str_search_business_item_not_assigned, android=self.__android_hmi, additional_message="str_search_business_item_assigned", max_time=5):
			str_business_address_second_line_not = wrapper_android_hmi.get_element_by_xpath(str_search_business_second_line_not, self.__android_hmi, self._reporting, additional_message="get business address second line")
			MODULE_LOGGER.info(f"business address: '{str_business_address}' is not in: '{str_business_address_second_line_not}'.")
			MODULE_LOGGER.error("business address is not set, please set business address before.")
			return False

		return True
