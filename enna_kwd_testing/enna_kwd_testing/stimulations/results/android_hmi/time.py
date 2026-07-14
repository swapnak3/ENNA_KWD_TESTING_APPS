# -*- coding: utf-8 -*-
"""Created on 18.03.2024.

@project: enna_kwd_testing.
@author: WZ40Y0R: Simon Schmidt.

Contains stimulations for keyword driven testing in context of android_hmi time values.
"""

import logging

import enna.core.component_system.decorators
import enna.core.time
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import settings

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckTimeFormatInSystem(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to time in settings -> system -> time."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="settings")

	def _action(self) -> bool:
		"""Execute action.

		1. Navigate to 'settings -> system -> date&time -> 24h-Timeformat'
		2. Check the value-button 12-24h

		:return: True if successful, False it susan exception occurs
		:rtype: bool
		"""

		toggle_button = self.__xpathloader.get_xpath("unknown", "car.TIME_FORMAT")
		time_settings_list = self.__xpathloader.get_xpath("unknown", "car.TIME_CONTAINER")

		if not wrapper_android_hmi.go_to_screen(settings.SYSTEM, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'settings.SYSTEM'. Something went wrong while navigating to screen.")
			return False

		str_xpath__system_list = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="main_list")
		str_xpath_date_time = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="date_time")
		self.__android_hmi.scroll_to_element_in_list(str_xpath__system_list, str_xpath_date_time)
		self.__android_hmi.click_element(str_xpath_date_time)

		enna.core.time.sleep(2)
		self.__android_hmi.scroll_list_to_bottom(time_settings_list)

		toggle_button_state = wrapper_android_hmi.wait_and_get_toggle_button_state(toggle_button, self.__android_hmi, reporting=self._reporting)

		if self.values["FORMAT"] == "12h":
			if not toggle_button_state:
				return True
		elif self.values["FORMAT"] == "24h":
			if toggle_button_state:
				return True
		else:
			return False

		MODULE_LOGGER.info(f"Time format: {self.values['FORMAT']} is set.")

		return True
