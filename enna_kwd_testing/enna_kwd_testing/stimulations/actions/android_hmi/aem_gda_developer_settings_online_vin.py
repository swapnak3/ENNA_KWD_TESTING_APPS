# -*- coding: utf-8 -*-
"""Created on 24.01.2024.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Teubner Claus.

Contains stimulations for keyword driven testing in context of android_hmi aem functions.
"""

import logging

import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import assistant

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper

from enna_kwd_testing.utilities.helper import android_hmi_helper, wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=too-many-branches

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetAemGdaDevloperSettingsOnlineAndConnectivityVin(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set vin in aem - GDA Developer Settings - Online and Connectivity."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self._reporting = reporting
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self._screen_id = ""
		self._xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="aem_gda")
		self.allowed_parameter_keys = ["VIN"]

	def _action(self) -> bool:
		"""Execute action.

		set VIN in aem_gda.online_and_connectivity.

		1. Navigate to 'aem_gda.ONLINE_AND_CONNECTIVITY' screen
		2. Enter VIN in 'VIN:' with Edit

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""

		self._screen_id = android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)

		# HMI 53
		str__vin_value = "BAUNEEGFZ21050484"

		try:
			str__vin_value = self.values["VIN"]
		except KeyError as exception:
			MODULE_LOGGER.error(f"{exception}: Wrong parameter for VIN:'{str__vin_value}', should be something like 'VIN: BAUNEEGFZ2105....'.")
			return False

		if not wrapper_android_hmi.go_to_screen(assistant.AEM_GDA_ONLINE_AND_CONNECTIVITY, self._reporting, self.__menu_navigation):
			self._reporting.add_report_message_ta_error("Could not go to screen: 'AEM_GDA.ONLINE_AND_CONNECTIVITY. Something went wrong while navigating to screen.")
			return False

		str__online_and_connectivity_list_xpath = self._xpaths.get_xpath("online_and_connectivity", "recyclerviewlist")
		str__vin_edit_xpath = self._xpaths.get_xpath("online_and_connectivity", "vin_edit")
		str__vin_save_xpath = self._xpaths.get_xpath("online_and_connectivity", "vin_save")

		if not wrapper_android_hmi.wait_and_scroll_in_list(str__vin_edit_xpath, str__online_and_connectivity_list_xpath, self.__android_hmi):
			self._reporting.add_report_message_ta_error(f"Could not scroll to element: {str__vin_edit_xpath} in list {str__online_and_connectivity_list_xpath}.")
			return False

		error_massage = f"Could not edit '{str__vin_edit_xpath}' button. An error occurred."

		if not wrapper_android_hmi.wait_and_click_in_list(str__vin_edit_xpath, str__online_and_connectivity_list_xpath, self.__android_hmi, self._reporting):
			self._reporting.add_report_message_system_error(error_massage)
			return False

		# self._speller.enter_text(text=str__vin_value, clear=True)
		self.__android_hmi.enter_text(text=str__vin_value, clear=True)  # enter text if keyboard is open

		if not wrapper_android_hmi.wait_and_click(str__vin_save_xpath, self.__android_hmi, self._reporting):
			self._reporting.add_report_message_ta_error(f"Could not click to element: {str__vin_save_xpath}.")
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
