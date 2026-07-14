# -*- coding: utf-8 -*-
"""Created on 23.07.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.

Contains KWD-Keyword 'RAH_B9PA_PRE_ACTIVATE_TIMER'
Contains KWD-Keyword 'RAH_B9PA_PRE_DEACTIVATE_ALL_TIMERS'
Contains KWD-Keyword 'RAH_B9PA_ACTION_ACTIVATE_TIMER'
Contains KWD-Keyword 'RAH_B9PA_ACTION_DEACTIVATE_TIMER'
Contains KWD-Keyword 'RAH_B9PA_ACTION_ACTIVATE_TIMER'
Contains KWD-Keyword 'RAH_B9PA_ACTION_DEACTIVATE_TIMER'
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
class PreconditionActivateTimer(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to activate Timer with custom time"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["TIMER_ID", "START_TIME"]

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

			list_date = [int(i) for i in start_time.split(',')]

			date_time = datetime.datetime(year=list_date[0], month=list_date[1], day=list_date[2], hour=list_date[3], minute=list_date[4])

			vehicle.rah_b9pa_timer_service.status.set_state_on(timer_id, date_time)

			self._reporting.add_report_message_pass(f"Activate Remote Auxiliary Heating (B9PA) Timer with ID {timer_id} (Precondition) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Activate Remote Auxiliary Heating (B9PA) Timer with ID {timer_id} (Precondition) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class PreconditionDeactivateAllTimers(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to deactivate all Timers"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Deactivate all Timers

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			vehicle.rah_b9pa_timer_service.status.set_all_timer_off()

			self._reporting.add_report_message_pass(f"Deactivate Remote Auxiliary Heating (B9PA) Timers (Precondition) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Deactivate Remote Auxiliary Heating (B9PA) Timers (Precondition) failed with reason: {exc}")
			return False


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
		self.allowed_parameter_keys = ["TIMER_ID", "START_TIME", "HEATER_MODE", "START_MODE"]

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
			heater_mode = self.values["HEATER_MODE"].upper()
			start_mode = self.values["START_MODE"].upper()

			list_date = [int(i) for i in start_time.split(',')]

			date_time = datetime.datetime(year=list_date[0], month=list_date[1], day=list_date[2], hour=list_date[3], minute=list_date[4])

			vehicle.rah_b9pa_timer_service.jobs.response_to_job_timer_on(timer_id, date_time, heater_mode, start_mode)

			self._reporting.add_report_message_pass(f"Activate Remote Auxiliary Heating (B9PA) Timer with ID {timer_id} (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Activate Remote Auxiliary Heating (B9PA) Timer with ID {timer_id} (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ActionDeactivateTimer(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to deactivate a Timer"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Deactivate the Timer

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			timer_id = self.values["TIMER_ID"]

			vehicle.rah_b9pa_timer_service.jobs.response_to_job_timer_off(timer_id)

			self._reporting.add_report_message_pass(f"Deactivate Remote Auxiliary Heating (B9PA) Timer with ID {timer_id} (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Deactivate Remote Auxiliary Heating (B9PA) Timer with ID {timer_id} (Action) failed with reason: {exc}")
			return False
