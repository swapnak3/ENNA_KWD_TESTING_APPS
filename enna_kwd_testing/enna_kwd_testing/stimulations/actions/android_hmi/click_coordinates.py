# -*- coding: utf-8 -*-
"""Created on 11.07.2024.

@project: enna_kwd_testing.
@author:SPLATZP: Platzer Pascal.

Contains stimulation for keyword driven testing in context of android_hmi click coordinates.
"""

import logging

import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.core.time
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.data_interfaces.android_hmi.helper
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.exceptions
import enna_st12.utilities.menu_navigation.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=too-many-locals, too-many-branches, too-many-statements

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class ClickCoordinates(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to click coordinates."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self._reporting = reporting
		self.__android_hmi = android_hmi

	def _action(self) -> bool:
		"""click coordinates.

		1. click coordinates

		:return: True if successful, False otherwise
		:rtype: bool
		"""

		try:
			str__target_coordinates_x = self.values["X"]
			int__coordinate_x = int(str__target_coordinates_x)
			str__target_coordinates_y = self.values["Y"]
			int__coordinate_y = int(str__target_coordinates_y)
		except KeyError as exception:
			self._reporting.add_report_message_info(f"No {exception} coordinate given")
			return False

		try:
			self.__android_hmi.click_coordinates(int__coordinate_x, int__coordinate_y)
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException:
			self._reporting.add_report_message_system_error("Could not click coordinates")
			return False

		self._reporting.add_report_message_pass("Click Coordinates successfully")

		return True
