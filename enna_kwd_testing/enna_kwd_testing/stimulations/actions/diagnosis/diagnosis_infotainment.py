# -*- coding: utf-8 -*-
"""Created on 13.03.2024.

@project: enna_kwd_testing.
@author: GLM0UBU: Bjoern Koenig.

Contains stimulations for keyword driven testing in context of diagnosis infotainment system.
"""
import enum
import logging

import enna.core.component_system.decorators
import enna.utilities.diagnosis.helper
import enna.utilities.diagnosis.interface
import enna.utilities.diagnosis.exceptions

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass


MODULE_LOGGER = logging.getLogger(__name__)


class Nodes(enum.Enum):
	"""Diagnosis addresses for infotainment system."""
	INFOTAINMENT_SYSTEM = 0x5F
	NATIVE_PARTITION = 0x8125
	ANDROID_PARTITION = 0x8153


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.utilities.diagnosis")
class WriteAdaption(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Writing Adaption on a node."""

	def __init__(self, reporting, diagnosis: enna.utilities.diagnosis.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna.utilities.diagnosis.interface.Interface diagnosis: Instance of diagnosis interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.__diagnosis = diagnosis
		self.allowed_parameter_keys = ["node", "channel", "param_name", "param_value"]

	def _action(self) -> bool:
		"""Writing Adaption on ECU. For writing use ODIS.

		:return: State of stimulation. If Stimulation success get true, else false.
		:rtype: bool
		"""

		try:
			node = int(self.values["node"], 16)
			channel = self.values["channel"]
			adaption_values = {self.values["param_name"]: self.values["param_value"]}
		except KeyError as error:
			msg = f"Missing Parameter! {error}"
			MODULE_LOGGER.exception(msg)
			self._reporting.add_report_message_ta_error(msg)
			return False

		try:
			current_adaption = enna.utilities.diagnosis.helper.read_adaptation(self.__diagnosis, ecu=node, channel=channel)
			MODULE_LOGGER.debug(str(current_adaption.to_dict()))

			enna.utilities.diagnosis.helper.write_adaptation(self.__diagnosis, ecu=node, channel=channel, values=adaption_values)

		except enna.utilities.diagnosis.exceptions.DiagnosisException:
			msg = f"Error by writing Adaption {channel}.{adaption_values} on {node}"
			MODULE_LOGGER.exception(msg)
			self._reporting.add_report_message_system_error()
			return False

		self._reporting.add_report_message_pass(f"Writing adaption success. Set to {channel}.{adaption_values} on {node}.")
		return True
