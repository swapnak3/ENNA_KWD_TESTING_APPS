# -*- coding: utf-8 -*-
"""Module contains stimulation to control Test Portal."""
import enna.core.reporting.interface
import enna.core.component_system.decorators

import enna_kwd_testing.utilities.test_portal.interface
import enna_kwd_testing.utilities.test_portal.exceptions
import enna_kwd_testing.stimulations.base.keyword_stim_baseclass


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.test_portal")
class SwitchTestPortalMock(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Activation/De-Activation Mock in Test Portal fur current vehicle. """

	def __init__(self, reporting: enna.core.reporting.interface.Interface, test_portal: enna_kwd_testing.utilities.test_portal.interface.Interface) -> None:
		"""Constructor of stimulation for switch a mock on Test Portal.

		:param reporting: Instance of reporting interface.
		:param test_portal: Instance of control a vehicle on Test Portal
		"""
		super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.3")
		self._portal = test_portal
		self.allowed_parameter_keys = ["MOCK", "STATE"]

	def _action(self) -> bool:
		"""Execute Action.
		Switch state of specified mock from vehicle on Test Portal.

		:return: True if success, else False
		"""
		try:
			mock_name = self.values["MOCK"]
			state = self.values["STATE"]
		except KeyError as error:
			self._reporting.add_report_message_ta_error(f"Missing parameter for this stimulation! {error}")
			return False

		try:
			self._portal.switch_activation_of_mock(name=mock_name, state=state)
		except enna_kwd_testing.utilities.test_portal.exceptions.PortalBaseException as error:
			self._reporting.add_report_message_ta_error(f"Error by switch mock '{mock_name}' to state {state}! Error: {error}")
			return False
		self._reporting.add_report_message_pass(f"Mock '{mock_name}' is switch to {state}.")
		return True
