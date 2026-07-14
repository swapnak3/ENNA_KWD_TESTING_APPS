# -*- coding: utf-8 -*-
"""Created on 14.02.2024.

@project: enna_kwd_testing.
@author: S6FXUOM, Nikolaus Maier.

Contains stimulations for KWD-TA in context of android_hmi functions.
"""

import logging

import enna.core.component_system.decorators

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class NoInteraction(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to do nothing."""

	def __init__(self, reporting):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")

	def _action(self) -> bool:
		"""Execute action.

		Return given string, without action.

		1. This function is a placeholder to keep the correct structur in CB.

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		self._reporting.add_report_message_info("No Interaction function was executed: Waiting for evaluation in expected result.")

		return True
