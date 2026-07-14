# -*- coding: utf-8 -*-
"""Created on 14.12.2023.

@project: enna_kwd_testing.
@author: SPLATZP: Platzer Pascal.

Contains stimulations for keyword driven testing in context of android_hmi navigation functions.
"""

import logging

import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper.adb import get_volume

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class CheckVolumeOfSpokenCluesInNavigation(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check the volume of spoken clues in navigation."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface):
		"""Initialize stimulation.

		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.__adb = adb
		self._reporting = reporting
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Execute action.

		route guidance in navi.app.

		1. Check volume of spoken clues.

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""

		try:
			int__value_to_check = int(self.values["VALUE"])
		except KeyError as exception:
			self._reporting.add_report_message_ta_error(f"Value {exception} not found")
			return False

		if int__value_to_check > 34 or int__value_to_check < 0:
			self._reporting.add_report_message_ta_error(f"Wrong value '{int__value_to_check}' please use a value between 0 and 34.")
			return False

		str__volume_in_car = get_volume(self.__adb, "android.car.VOLUME_GROUP/0/1")

		if str__volume_in_car != int__value_to_check:
			self._reporting.add_report_message_system_error(f"The Volume is not '{int__value_to_check}'. The Volume is '{str__volume_in_car}'")
			return False

		MODULE_LOGGER.info(f"The volume of spoken clues is '{self.values['VALUE']}' ")

		return True
