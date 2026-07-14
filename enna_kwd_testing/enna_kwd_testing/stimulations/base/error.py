"""Module contains stimulation to execute if a error in test specification."""
import enna.core.component_system.decorators

import enna_kwd_testing.stimulations.base.exceptions
import enna_kwd_testing.stimulations.base.keyword_stim_baseclass


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class NoStimulation(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to raise a exception for No Stimulation assigned."""

	def __init__(self, reporting) -> None:
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")

	def _action(self) -> bool:
		"""Raise exception.

		:raise enna_kwd_testing.stimulations.base.exceptions.NoStimulation: if no stimulation assigned to keyword
		"""
		msg = "No Stimulation assigned to keyword!"
		self._reporting.add_report_message_ta_error(msg)
		raise enna_kwd_testing.stimulations.base.exceptions.NoStimulation(msg)
