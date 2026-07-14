# -*- coding: utf-8 -*-
"""Created on 04.08.2023.

@project: enna_kwd_testing.
@author: SPLATZP: PASCAL PLATZER.

Contains stimulations for keyword driven testing in context of adb navigation.
"""
import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.package_loader.interface
from enna_kwd_testing.utilities.helper.adb import allow_to_set_position_in_navigation, set_position_in_navigation, set_development_settings

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class SetPositionCcp(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to set position in navigation."""

	def __init__(self, reporting, adb: enna.data_interfaces.adb.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.__adb = adb

	def _action(self) -> bool:
		"""Execute action.

		Set position in navigation.

		:return: True if successful, False if exception occurs
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		try:
			float__latitude = float(self.values["COORDINATES"][0])
			float__longitude = float(self.values["COORDINATES"][1])
			set_development_settings(self.__adb)
			allow_to_set_position_in_navigation(self.__adb)
			set_position_in_navigation(self.__adb, float__latitude, float__longitude)
		except KeyError as exception:
			self._reporting.add_report_message_ta_error(f"An error occurred: {exception}")
			return False

		MODULE_LOGGER.info(f"The CCP is set to {self.values['COORDINATES']}")

		return True
