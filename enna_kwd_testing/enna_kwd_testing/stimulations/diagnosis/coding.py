# -*- coding: utf-8 -*-
"""Module contains stimulation to coding vehicle via ODB."""
import logging
import time

import enna.core.exceptions
import enna.core.component_system.decorators
import enna.core.reporting.interface

import enna.utilities.diagnosis.interface
import enna.utilities.diagnosis.helper
import enna.utilities.diagnosis.exceptions
import enna.utilities.susan.interface
import enna.utilities.susan.exceptions

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass


MODULE_LOGGER = logging.getLogger(__name__)


def _vehicle_restart(susan: enna.utilities.susan.interface.Interface, reporting: enna.core.reporting.interface.Interface) -> bool:
	"""Trigger a restart from vehicle.

	:param susan: instance of SUSAN-Box interface
	:param reporting: instance of reporting interface
	:return:  True if success, else False
	"""
	try:
		susan.set_terminal_clamp_s(state=False)
		susan.set_terminal_clamp_15(state=False)
		susan.set_terminal_comfort_ready_state(state=False)
	except enna.utilities.susan.exceptions.SUSANException as error:
		reporting.add_report_message_ta_error(f"Could not shutdown vehicle! Error: {error}")
		return False
	time.sleep(300.0) # Time until bus sleep
	try:
		susan.set_terminal_comfort_ready_state(state=True)
		susan.set_terminal_clamp_s(state=True)
		susan.set_terminal_clamp_15(state=True)
	except enna.utilities.susan.exceptions.SUSANException as error:
		reporting.add_report_message_ta_error(f"Could not reboot vehicle! Error: {error}")
		return False
	time.sleep(120.0) # Time to restart complete
	return True

def _write_coding_textual_with_access_check(diagnosis: enna.utilities.diagnosis.interface.Interface, ecu: int, values: dict[str, str]) -> None:
	"""Write coding textual. Before coding check SFD status from ECU.

	:param diagnosis: instance of On-Board-Diagnosis interface
	:param ecu: diagnosis address from ECU
	:param values: values to coding {'ParamName1': 'paramValue1', 'ParamName2': 'paramValue2', ...} e.g. {"Param_SuspeArmSide": "left_hand_drive"}
	:raise enna.utilities.diagnosis.exceptions.DiagnosisException: if security access denied
	"""
	# pylint: disable=protected-access
	enna.utilities.diagnosis.helper._open_connection(diagnosis=diagnosis, ecu=ecu)
	sfd: enna.utilities.diagnosis.DiagnosisSfdResult = diagnosis.get_sfd_status()
	MODULE_LOGGER.debug(f"ECU {hex(ecu)} security access status = {sfd.role}")
	if sfd.role == enna.utilities.diagnosis.SfdRole.NO_UNLOCK:
		raise enna.utilities.diagnosis.exceptions.DiagnosisException(f"ECU {hex(ecu)} is security access denied!")
	diagnosis.write_coding_textual(values, ecu_reset=False)
	enna.utilities.diagnosis.helper._close_connection(diagnosis=diagnosis)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.utilities.diagnosis")
@enna.core.component_system.decorators.RequireComponent("enna.utilities.susan")
class CodingSteeringWheelPositionOnVehicle(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Stimulation to coding steering wheel position on vehicle."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, diagnosis: enna.utilities.diagnosis.interface.Interface, susan: enna.utilities.susan.interface.Interface) -> None:
		"""Constructor coding steering wheel.


		:param reporting: instance of reporting interface
		:param diagnosis: instance of On-Board-Diagnosis interface
		:param susan: instance of SUSAN-Box interface
		"""
		super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.3")
		self._diagnosis = diagnosis
		self._susan = susan
		self.allowed_parameter_keys = ["POSITION"]


	def _action(self) -> bool:
		"""Execute coding steering wheel position.

		:return: True if success, else False
		"""
		expected_position = self.values.get("POSITION", "left_hand_drive")
		try:
			_write_coding_textual_with_access_check(self._diagnosis, 0x8125, {"Param_SuspeArmSide": expected_position})
			_write_coding_textual_with_access_check(self._diagnosis, 0x8153, {"Param_SuspeArmSide": expected_position})
		except enna.utilities.diagnosis.exceptions.DiagnosisException as error:
			self._reporting.add_report_message_ta_error(f"Could not coding steering wheel to {expected_position}! Error: {error}")
			return False
		self._reporting.add_report_message_pass(f"Write coding steering wheel to {expected_position}")
		return _vehicle_restart(susan=self._susan, reporting=self._reporting)
