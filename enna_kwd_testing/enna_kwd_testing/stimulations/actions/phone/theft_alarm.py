# -*- coding: utf-8 -*-
"""Created on 01.08.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.

Contains KWD-Keyword 'DWA_TRIGGER_ALARM'
"""
import datetime
import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
from enna_kwd_testing.utilities.phone import interface
from enna_kwd_testing.utilities.phone.myaudi import runtime_storage

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class TriggerAlarm(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to trigger a theft alarm"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["ALARM_TYPE"]

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Check if Alarm-Type is valid
		3. Trigger alarm

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			alarm_type = self.values["ALARM_TYPE"].upper()

			vehicle.dwa_service.jobs.trigger_alarm(alarm_type)

			self._reporting.add_report_message_pass(f"Trigger Theft-Alarm successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Trigger Theft-Alarm failed with reason: {exc}")
			return False
