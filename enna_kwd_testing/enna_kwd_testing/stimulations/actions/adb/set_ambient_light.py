# -*- coding: utf-8 -*-
"""Created on 02.02.2024.

@project: enna_kwd_testing.
@author: SPLATZP: PASCAL PLATZER.

Contains stimulations for keyword driven testing in context of adb ambient light.
"""
import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.package_loader.interface
from enna_kwd_testing.utilities.helper.adb import set_ambient_color

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class SetAmbientlightInSystem(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to set ambient light via adb."""

	def __init__(self, reporting, adb: enna.data_interfaces.adb.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.__adb = adb
		self._colors = {"gray": 0, "orange": 1, "red": 2, "pink": 3, "blue": 4, "green": 5}

	def _action(self) -> bool:
		"""Execute action.

		Set ambient light in system via adb.

		:return: True if successful, False if exception occurs
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		try:
			str_color_name = self.values.get("COLOUR", "")
			int_color_id = self._colors[str_color_name]
		except KeyError as exception:
			self._reporting.add_report_message_ta_error(f"Color not found in Available colors: {exception}")
			return False

		set_ambient_color(self.__adb, int_color_id)

		MODULE_LOGGER.info(f"The ambient light color is set to color index {self.values['COLOUR']}")

		return True
