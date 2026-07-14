# -*- coding: utf-8 -*-
"""Created on 13.06.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.

Contains KWD-Keyword 'PRE_SET_VIN'
"""
import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
from enna_kwd_testing.utilities.phone import interface
from enna_kwd_testing.utilities.phone.myaudi import runtime_storage
from enna_kwd_testing.utilities.phone.myaudi.backend import vehicle_factory

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class SetVIN(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to save VIN globally for a full testcase"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["VIN"]

	def _action(self) -> bool:
		"""Execute action.

		1. Save VIN

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		runtime_storage.USED_VIN = self.values["VIN"].upper()

		runtime_storage.USED_VEHICLE = vehicle_factory.vehicle(runtime_storage.USED_VIN)

		return True
