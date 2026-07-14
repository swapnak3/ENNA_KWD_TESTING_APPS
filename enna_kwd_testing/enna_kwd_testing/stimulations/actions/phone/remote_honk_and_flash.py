# -*- coding: utf-8 -*-
"""Created on 12.09.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.

Contains KWD-Keyword 'RHF_START_HONK_AND_FLASH'
Contains KWD-Keyword 'RHF_START_HONK_AND_FLASH_RESPOND_WITH_ERROR'
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
class ActionHonkAndFlash(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to start honk and flash as action"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["FLASH_STATE", "HONK_STATE"]

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Start honk and flash

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			flash_state = self.values["FLASH_STATE"].upper()
			honk_state = self.values["HONK_STATE"].upper()

			vehicle.rhf_service.jobs.response_to_job_start_honk_and_flash(flash_state, honk_state)

			self._reporting.add_report_message_pass(f"Start honk and flash (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Start honk and flash (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ActionHonkAndFlashRespondWithError(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to respond with an error while starting honk and flash as action"""

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

			vehicle.rhf_service.jobs.response_to_job_with_error(error)

			self._reporting.add_report_message_pass(f"Respond to start honk and flash (Action) with an error successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Respond to start honk and flash (Action) with an error failed with reason: {exc}")
			return False