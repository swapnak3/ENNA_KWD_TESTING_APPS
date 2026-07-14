# -*- coding: utf-8 -*-
"""Created on 05.12.2023.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Claus Teubner.

Contains stimulations for keyword driven testing in context of android_hmi navigation functions.
"""

import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import navigation as navigation_contexts

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.helper.android_hmi_helper
import enna_kwd_testing.utilities.speller
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)

# pylint: disable=too-many-positional-arguments
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.speller")
class SetMapModeCompassButton(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set mode of compass on map in navi.app.
	parameter VALUE: 2D_NORTHWARD | 2D_HEADING_UP | 3D -> default VALUE: '3D'
	"""

	def __init__(self, reporting, adb: enna.data_interfaces.adb.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface, speller):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		:param enna_kwd_testing.utilities.speller.interface.Interface speller: speller interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self._reporting = reporting
		self.__adb = adb
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self._speller = speller
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["VALUE"]
		self.allowed_parameter_values = ["2D_NORTHWARD", "2D_HEADING_UP", "3D"]
		self.logcat_parameter_values_dict = {"2D_NORTHWARD": "viewMode=NORTH_2D", "2D_HEADING_UP": "viewMode=DRIVE_2D", "3D": "viewMode=DRIVE_3D"}
		self.default_parameter_value = "3D"

	def _action(self) -> bool:
		"""Execute action.

		set mode of compass button on map in navi.app.

		1. check for correct parameter value.
		2. Navigate to 'navigation.main' screen.
		3. if no status of viewMode in logcat, press compass icon so often, till KEY-VALUE is identical with mapMode to set.

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		# pylint: disable = too-many-branches
		enna_kwd_testing.utilities.helper.android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)

		# 1. check for correct parameter value.
		if self.values["VALUE"] in self.allowed_parameter_values:
			tocheck_value_str = self.values["VALUE"]
		elif not self.values["VALUE"]:
			tocheck_value_str = self.default_parameter_value
		else:
			MODULE_LOGGER.error(f"Wrong parameter: '{self.values}', should be one of -> \nVALUE: '{self.allowed_parameter_values}'")
			return False

		# 2. Navigate to 'navigation.main' screen.
		if not wrapper_android_hmi.go_to_screen(navigation_contexts.MAIN, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'NAVI.APP -> MAIN. Something went wrong while navigating to screen.")
			return False
		if not wrapper_android_hmi.wait_for_screen_id(navigation_contexts.MAIN, android=self.__android_hmi, additional_message="wait for screen", max_time=30):
			MODULE_LOGGER.error("Wait for screen-id: 'navigation.MAIN. Something went wrong while waiting for screen-id.")
			return False

		# 3. if no status of viewMode in logcat, press compass icon so often, till KEY-VALUE is identical with mapMode to set.
		i = 0
		i_max = 15
		checked_state_str = ""
		try:
			button_compass_button_str = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="compass")
			while checked_state_str not in self.allowed_parameter_values or i < i_max:
				checked_state_str = self.__adb.execute_shell_command("sleep 1;logcat -d --regex='src - current    =ReconfigurationRequest=' | tail -1")
				if "mapMode=MapMode(" in checked_state_str:
					checked_state_str = checked_state_str.split("mapMode=MapMode(")[1].split(",")[0]
				if self.logcat_parameter_values_dict[tocheck_value_str] == checked_state_str:
					MODULE_LOGGER.info(f"Map mode is {tocheck_value_str} ({checked_state_str}), finished.")
					return True
				MODULE_LOGGER.info(f"Map mode is {checked_state_str}, click compass to change to {tocheck_value_str} - {self.logcat_parameter_values_dict[tocheck_value_str]}.")
				i += 1
				if not wrapper_android_hmi.wait_and_click(button_compass_button_str, self.__android_hmi, "Pressing 'compass button', failed."):
					return False
		except enna.data_interfaces.adb.exceptions.ADBException as exception:
			MODULE_LOGGER.error("An error occurred at executing the adb shell command to check the 'map mode' state:")
			MODULE_LOGGER.error(exception)
			return False
		return True
