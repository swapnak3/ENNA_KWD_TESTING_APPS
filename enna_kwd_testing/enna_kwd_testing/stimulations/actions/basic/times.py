# -*- coding: utf-8 -*-
"""Created on 07.08.2023.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
"""
import logging

import enna.core.component_system.decorators
import enna.core.time

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class WaitTimeInMs(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to wait a specific time in milliseconds."""

	def __init__(self, reporting):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.allowed_parameter_keys = ["time"]

	def _action(self) -> bool:
		"""Execute action.

		Wait the given time in milliseconds.

		:return: True when finished
		:rtype: bool
		"""
		int_values_in_ms = int(self.values["time"])
		enna.core.time.sleep(int_values_in_ms / 1000)
		return True
