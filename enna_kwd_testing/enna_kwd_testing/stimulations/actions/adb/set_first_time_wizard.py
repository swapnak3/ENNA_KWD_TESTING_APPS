# -*- coding: utf-8 -*-
"""Created on 15.05.2024.

@project: enna_kwd_testing.
@author: SPLATZP: PASCAL PLATZER.

Contains stimulations for keyword driven testing in context of adb shell FTW.
"""
import logging
from pathlib import Path

import enna.core.component_system.decorators
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.json_loader.interface
from enna_kwd_testing.definitions import RESOURCES_PATH

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class SetFirstTimeWizard(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to send ADB Shell command to open the first time wizard."""

	def __init__(self, reporting, adb: enna.data_interfaces.adb.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.__adb = adb
		self._path_commands = Path(f"{RESOURCES_PATH}/adb_commands/adb_shell_commands_collection.json")
		self.__adb_commands = enna_kwd_testing.utilities.json_loader.interface.JsonLoader(self._path_commands)

	def _action(self) -> bool:
		"""Execute action.

		Send ADB Shell command to start the first time wizard

		:return: True if successful, False it exception occurs
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		str_adb_shell_command = self.__adb_commands.get_value("start_first_time_wizard")

		try:
			self.__adb.execute_adb_command("root")
			self.__adb.execute_shell_command(str_adb_shell_command)
			self._reporting.add_report_message_pass(f"Successfully send '{str_adb_shell_command}' command")
			return True

		except enna.data_interfaces.adb.exceptions.ADBException as exception:
			MODULE_LOGGER.error(f"An error occurred: {exception}")
			return False
