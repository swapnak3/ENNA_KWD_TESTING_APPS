# -*- coding: utf-8 -*-
"""Created on 01.08.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.

Contains KWD-Keyword 'RPC_ACTION_DEACTIVATE_CLIMATISATION'
Contains KWD-Keyword 'RPC_ACTION_ACTIVATE_CLIMATISATION'
Contains KWD-Keyword 'RPC_ACTION_CLIMATE_RESPOND_WITH_ERROR'
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
class ActionActivateClimatisation(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to activate the remote profile climatisation as action"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["DURATION", "TIME_REMAINING", "HEATER_SOURCE", "CLIMATISATION_STATE"]

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Activate Remote Profile Climatisation

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			duration = self.values["DURATION"]
			time_remaining = self.values["TIME_REMAINING"]
			heater_source = self.values["HEATER_SOURCE"].upper()
			climatisation_state = self.values["CLIMATISATION_STATE"].upper()

			vehicle.rpc_service.jobs.response_to_job_climatisation_on(duration, time_remaining, heater_source, climatisation_state)

			self._reporting.add_report_message_pass(f"Activate Remote Profile Climatisation (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Activate Remote Profile Climatisation (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ActionDeactivateClimatisation(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to deactivate the remote profile climatisation as action"""

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
		2. Activate Remote Profile Climatisation

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			vehicle.rpc_service.jobs.response_to_job_climatisation_off()

			self._reporting.add_report_message_pass(f"Deactivate Remote Profile Climatisation (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Deactivate Remote Profile Climatisation (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ActionClimatisationRespondWithError(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to respond with an error while activating/deactivating remote profile climatisation as action"""

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

			vehicle.rpc_service.jobs.response_to_job_with_error(error)

			self._reporting.add_report_message_pass(f"Respond to Remote Profile Climatisation Job (Action) with error successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Respond to Remote Profile Climatisation Job (Action) with error failed with reason: {exc}")
			return False
