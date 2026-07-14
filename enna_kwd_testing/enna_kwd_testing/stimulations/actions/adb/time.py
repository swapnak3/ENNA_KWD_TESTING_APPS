# -*- coding: utf-8 -*-
"""Created on 19.10.2023.

@project: enna_kwd_testing.
@author: SPLATZP: PASCAL PLATZER.

Contains stimulations for keyword driven testing in context of adb time values.
"""
import logging
from datetime import datetime, timedelta

import enna.core.component_system.decorators
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
from enna_kwd_testing.utilities.helper.adb import get_time

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class CheckTimeInSystem(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to check time."""

	def __init__(self, reporting, adb: enna.data_interfaces.adb.interface.Interface):
		"""Initialize stimulation.

		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__adb = adb

	def _action(self) -> bool:
		"""Execute action.

		Check Time for target to value defined in instance attribute "values" under key "TIME".

		:return: True if successful, False it susan exception occurs
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		try:
			try:
				default_time = self.values["TIME"]
			except KeyError as exception:
				default_time = ""
				MODULE_LOGGER.error(f"An error occurred: No '{exception}' set")

			tolerance_time = timedelta(hours=2)
			car_time = get_time(self.__adb)

			default_time = datetime.now().time() if len(default_time) == 0 else datetime.strptime(default_time, "%H:%M").time()
			time_difference = abs(datetime.combine(datetime.min, default_time) - datetime.combine(datetime.min, car_time))

			if time_difference > tolerance_time:
				MODULE_LOGGER.error(f"An error occurred: The time difference = '{time_difference}' is outside the tolerance from +/- 2 hours")
				return False

			MODULE_LOGGER.info("Successfully the Time is correct")
			return True
		except (enna.data_interfaces.adb.exceptions.ADBException, KeyError) as exception:
			MODULE_LOGGER.error(f"An error occurred: {exception}")
			return False
