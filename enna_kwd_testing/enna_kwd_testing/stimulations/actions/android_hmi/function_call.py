# -*- coding: utf-8 -*-
"""Created on 09.11.2023.

@project: enna_kwd_testing.
@author: S6FXUOM, Nikolaus Maier.

Contains stimulations for KWD-TA in context of android_hmi sds settings functions.
"""

import logging

import enna.core.component_system.decorators

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class FunctionCall(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to return given string, this function is only relevent for car testing."""

	def __init__(self, reporting):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")

	def _action(self) -> bool:
		"""Execute action.

		Return given string, without action.

		1. Return string

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		self._reporting.add_report_message_info(f"Function Call was executed:'{self.values}'")

		return True
