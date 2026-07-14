# -*- coding: utf-8 -*-
"""Created on 31.07.2024.

@project: enna_kwd_testing.
@author: WZ40Y0R: Simon Schmidt

Contains KWD-Keyword 'RDT_ACTION_ACTIVATE_TIMER'
Contains KWD-Keyword 'RDT_ACTION_TIMER_RESPOND_WITH_ERROR'
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
class ActionActivateTimer(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to activate Timer with custom time"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["TIMER_ID", "START_TIME", "HEATER_SOURCE"]

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Activate Timer

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			timer_id = self.values["TIMER_ID"]
			start_time = self.values["START_TIME"]
			heater_source = self.values["HEATER_SOURCE"].upper()

			list_date = [int(i) for i in start_time.split(',')]

			date_time = datetime.datetime(year=list_date[0], month=list_date[1], day=list_date[2], hour=list_date[3], minute=list_date[4])

			vehicle.rdt_service.jobs.response_to_job_timer_on(timer_id, date_time, heater_source)

			self._reporting.add_report_message_pass(f"Activate Remote Departure Timer with ID {timer_id} successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Activate Remote Departure Timer with ID {timer_id} failed with reason: {exc}")


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ActionDeactivateTimer(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to deactivate Timer with custom time"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["TIMER_ID"]

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Deactivate Timer

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			timer_id = self.values["TIMER_ID"]

			vehicle.rdt_service.jobs.response_to_job_timer_off(timer_id)

			self._reporting.add_report_message_pass(f"Deactivate Remote Departure Timer with ID {timer_id} successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Deactivate Remote Departure Timer with ID {timer_id} failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ActionTimerRespondWithError(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to respond with an error while activating/deactivating remote departure timer as action"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["ERROR"]

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Respond to job with error

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			error = self.values["ERROR"].upper()

			vehicle.rdt_service.jobs.response_to_job_with_error(error)

			self._reporting.add_report_message_pass(f"Respond to Remote Departure Timer Job (Action) with error successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Respond to Remote Departure Timer Job (Action) with error failed with reason: {exc}")
			return False
