# -*- coding: utf-8 -*-
"""Created on 07.08.2023.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.

Contains stimulations for keyword driven testing in context of diagnosis conmod interface.
"""
import logging

import enna.core.component_system.decorators
import enna.utilities.diagnosis.exceptions
import enna.utilities.diagnosis.helper as diagnosis_helper
import enna.utilities.diagnosis.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.utilities.diagnosis")
class SetFlightMode(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to set flight mode on conmod with diagnosis address 0x75."""

	def __init__(self, reporting, diagnosis: enna.utilities.diagnosis.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna.utilities.diagnosis.interface.Interface diagnosis: Instance of diagnosis interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__diagnosis = diagnosis
		self.allowed_parameter_keys = ["state"]

	def _action(self) -> bool:
		"""Execute action.

		Set Basic functions connect -> flight mode (channel = Basic_functions_connect -> Param_Flymo) to the given state.

		:return: True if successful, False it susan exception occurs
		:rtype: bool
		"""
		state_to_set = self.values["state"]
		try:
			diagnosis_helper.write_adaptation(self.__diagnosis, 0x75, channel="Basic_functions_connect", values={"Param_Flymo": state_to_set})
			MODULE_LOGGER.info(f"Successfully wrote adaption to conmod (0x75): Basic_functions_connect -> Param_Flymo: {state_to_set} | Flight mode: {state_to_set}")
		except enna.utilities.diagnosis.exceptions.DiagnosisException as exception:
			MODULE_LOGGER.error(f"An error occurred when trying to set the flight mode on conmod (0x75) to {state_to_set} via diagnosis interface:")
			MODULE_LOGGER.error(exception)
			return False
		return True
