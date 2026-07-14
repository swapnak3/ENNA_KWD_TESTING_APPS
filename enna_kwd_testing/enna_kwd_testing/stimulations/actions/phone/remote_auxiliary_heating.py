# -*- coding: utf-8 -*-
"""Created on 26.06.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.

Contains KWD-Keyword 'RAH_PRE_ACTIVATE_HEATING'
Contains KWD-Keyword 'RAH_PRE_DEACTIVATE_HEATING'
Contains KWD-Keyword 'RAH_PRE_ACTIVATE_TIMER'
Contains KWD-Keyword 'RAH_ACTION_ACTIVATE_HEATING'
Contains KWD-Keyword 'RAH_ACTION_DEACTIVATE_HEATING'
Contains KWD-Keyword 'RAH_ACTION_DEACTIVATE_TIMER'
Contains KWD-Keyword 'RAH_ACTION_ACTIVATE_TIMER'
Contains KWD-Keyword 'RAH_PRE_DEACTIVATE_ALL_TIMERS'
Contains KWD-Keyword 'RAH_PRE_SET_ERROR'
Contains KWD-Keyword 'RAH_ACTION_ACTIVATE_HEATING'
Contains KWD-Keyword 'RAH_ACTION_DEACTIVATE_HEATING'
Contains KWD-Keyword 'RAH_ACTION_ACTIVATE_TIMER'
Contains KWD-Keyword 'RAH_ACTION_DEACTIVATE_TIMER'
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
class PreconditionActivateHeating(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to activate the remote auxiliary heating as precondition"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["DURATION", "TIME_REMAINING"]

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Activate Remote Auxiliary Heating

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			duration = self.values["DURATION"]
			time_remaining = self.values["TIME_REMAINING"]

			vehicle.rah_quickstart_service.status.set_state_on(duration, time_remaining)

			self._reporting.add_report_message_pass(f"Activate Remote Auxiliary Heating (Precondition) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Activate Remote Auxiliary Heating (Precondition) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class PreconditionDeactivateHeating(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to deactivate the remote auxiliary heating as precondition"""

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
		2. Deactivate Remote Auxiliary Heating

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			vehicle.rah_quickstart_service.status.set_state_off()

			self._reporting.add_report_message_pass(f"Deactivate Remote Auxiliary Heating (Precondition) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Activate Remote Auxiliary Heating (Precondition) failed with reason: {exc}")
			return False


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

			vehicle.rah_timer_service.status.set_timer_on(timer_id, date_time)

			self._reporting.add_report_message_pass(f"Activate Remote Auxiliary Heating Timer with ID {timer_id} (Precondition) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Activate Remote Auxiliary Heating Timer with ID {timer_id} (Precondition) failed with reason: {exc}")
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

			vehicle.rah_timer_service.status.set_all_timer_off()

			self._reporting.add_report_message_pass(f"Deactivate Remote Auxiliary Heating Timers (Precondition) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Deactivate Remote Auxiliary Heating Timers (Precondition) failed failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class PreconditionSetError(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set the RAH into error state as Precondition"""

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
		2. Deactivate all Timers

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			error = self.values["ERROR"].upper()

			vehicle.rah_quickstart_service.status.set_state_error(error)

			self._reporting.add_report_message_pass(f"Set Status of Remote Auxiliary Heating to Error (Precondition) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Set Status of Remote Auxiliary Heating to Error (Precondition) failed with reason: {exc}")
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

			vehicle.rah_timer_service.jobs.response_to_job_timer_off(timer_id)

			self._reporting.add_report_message_pass(f"Deactivate Remote Auxiliary Heating Timer with ID {timer_id} (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Deactivate Remote Auxiliary Heating Timer with ID {timer_id} (Action) failed with reason: {exc}")
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

			vehicle.rah_timer_service.jobs.response_to_job_timer_on(timer_id, date_time)

			self._reporting.add_report_message_pass(f"Activate Remote Auxiliary Heating Timer with ID {timer_id} (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Activate Remote Auxiliary Heating Timer with ID {timer_id} (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ActionActivateHeating(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to activate the remote auxiliary heating as action"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["DURATION", "TIME_REMAINING"]

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Activate Remote Auxiliary Heating

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			duration = self.values["DURATION"]
			time_remaining = self.values["TIME_REMAINING"]

			vehicle.rah_quickstart_service.jobs.response_to_job_heating_on(duration, time_remaining)

			self._reporting.add_report_message_pass(f"Activate Remote Auxiliary Heating (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Activate Remote Auxiliary Heating (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ActionDeactivateHeating(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to deactivate the remote auxiliary heating as action"""

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
		2. Deactivate Remote Auxiliary Heating

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			vehicle.rah_quickstart_service.jobs.response_to_job_heating_off()

			self._reporting.add_report_message_pass(f"Deactivate Remote Auxiliary Heating (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Deactivate Remote Auxiliary Heating (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ActionHeatingRespondWithError(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to respond with an error while activating/deactivating remote auxiliary heating as action"""

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

			vehicle.rah_quickstart_service.jobs.response_to_job_with_error(error)

			self._reporting.add_report_message_pass(f"Respond to Remote Auxiliary Heating Job (Action) with error successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Respond to Remote Auxiliary Heating Job (Action) with error failed with reason: {exc}")
			return False
