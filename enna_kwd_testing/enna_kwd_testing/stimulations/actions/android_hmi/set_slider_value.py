# -*- coding: utf-8 -*-
"""Created on 21.09.2023.

@project: enna_kwd_testing.
@author: SPLATZP: Platzer Pascal.

Contains stimulations for keyword driven testing in context of android_hmi slider value.
"""
import logging

import enna.core.component_system.decorators
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.instance_names

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper.android_hmi_helper import get_app_and_screen_name_from_screen

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=consider-ternary-expression
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetSliderValue(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set slider percentage."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__android_hmi = android_hmi

	def _action(self) -> bool:
		"""Execute action.

		Set Slider percentage.

		1. Set slider percentage

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""

		str__orientation = self.values.get("ORIENTATION", "Horizontal")
		xpath_name = self.values["XPATH_NAME"]
		float__slider_percentage = float(self.values["VALUE"])

		str__app_name, str__screen_name = get_app_and_screen_name_from_screen(self._reporting, self.__android_hmi)
		xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app=str__app_name)
		str__slider_xpath = xpaths.get_xpath(str__screen_name, xpath_name)

		if str__orientation == "Vertical":
			orientation = enna_st12.data_interfaces.android_hmi.Orientation.Vertical
		else:
			orientation = enna_st12.data_interfaces.android_hmi.Orientation.Horizontal

		try:
			self.__android_hmi.set_slider_value(str__slider_xpath, float__slider_percentage, orientation)
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException as exception:
			self._reporting.add_report_message_pass(f"Slider Value error: {exception}")
			return False

		self._reporting.add_report_message_pass(f"Slider Value is set to {float__slider_percentage}")

		return True
