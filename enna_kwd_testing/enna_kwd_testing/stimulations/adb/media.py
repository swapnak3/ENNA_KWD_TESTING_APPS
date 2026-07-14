# -*- coding: utf-8 -*-
"""Module contains functions for usage of current media source."""

import logging

import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.data_interfaces.adb.interface
import enna.data_interfaces.adb.exceptions

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class TriggerMediaFunction(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Stimulation to trigger a function of current media source.

	Possible functions: PLAY, PAUSE, SKIP_FORWARD, SKIP_BACKWARD
	Trigger function via input a key event
	"""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface) -> None:
		"""Constructor of Stimulation.

		:param reporting: instance of reporting interface
		:param adb: instance of interface to Android Debug Bridge
		"""
		super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.4")
		self._adb = adb
		self.allowed_parameter_keys = ["STATE", "SOURCE"]

		self.__key_events_to_functions = {
			"SKIP_FORWARD": "input keyevent 87",
			"SKIP_BACKWARD": "input keyevent 88",
			"PLAY": "input keyevent 126",
			"PAUSE": "input keyevent 127"
		}

	def _action(self) -> bool:
		"""Send key event to trigger media function.

		:return: True if success, else false
		"""
		function = self.values.get("STATE", "Not set").upper()

		try:
			self._adb.execute_shell_command(command=self.__key_events_to_functions[function], timeout=5.0)
		except KeyError:
			self._reporting.add_report_message_ta_error(f"Function '{function}' is not supported! Available functions are {self.__key_events_to_functions.keys()}")
			return False
		except enna.data_interfaces.adb.exceptions.ADBException as error:
			self._reporting.add_report_message_system_error(f"Key event to trigger function '{function}' could not send! {error}")
			return False
		self._reporting.add_report_message_pass(f"Sent key event for function '{function}'.")
		return True
