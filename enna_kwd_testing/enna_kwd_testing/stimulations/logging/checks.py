# -*- coding: utf-8 -*-
"""Module contains checks from HCP3 Log."""
import logging

import enna.core.component_system.decorators
import enna.core.config
import enna.core.exceptions
import enna.core.reporting.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.service_list_states.interface

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=too-many-locals, too-many-branches, disable=protected-access

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.service_list_states")
class CheckApn1(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check apn1 state."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, service_list_states: enna_kwd_testing.utilities.service_list_states.interface.Interface) -> None:
		"""Initialize stimulation.

		:param reporting: Instance of reporting interface
		:param service_list_states: utility to check service list
		"""
		super().__init__(reporting=reporting)
		self._service_list = service_list_states
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Check state of APN1.

		:return: True if success, else false
		"""
		expected_state = self.values.get("STATE", False)
		if expected_state == self._service_list.apn1.value:
			self._reporting.add_report_message_pass("CheckApn1 return True")
			return True
		self._reporting.add_report_message_pass("CheckApn1 return False")
		return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.service_list_states")
class CheckApn2(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check apn2 state."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface,
				 service_list_states: enna_kwd_testing.utilities.service_list_states.interface.Interface) -> None:
		"""Initialize stimulation.

		:param reporting: Instance of reporting interface
		:param service_list_states: utility to check service list
		"""
		super().__init__(reporting=reporting)
		self._service_list = service_list_states
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Check state of APN2.

		:return: True if success, else false
		"""
		expected_state = self.values.get("STATE", False)
		if expected_state == self._service_list.apn2.value:
			self._reporting.add_report_message_pass("CheckApn2 return True")
			return True
		self._reporting.add_report_message_pass("CheckApn2 return False")
		return False

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.service_list_states")
class CheckLicenseInServiceList(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check given service state"""

	def __init__(self, reporting: enna.core.reporting.interface.Interface,
			service_list_states: enna_kwd_testing.utilities.service_list_states.interface.Interface) -> None:
		"""Initialize stimulation.

		:param reporting: Instance of reporting interface
		:param service_list_states: utility to check service list
		"""
		super().__init__(reporting=reporting)
		self._service_list = service_list_states
		self.allowed_parameter_keys = ["SERVICE_ID", "STATE"]

	def _action(self) -> bool:
		"""Check state of given service

		:return: True if success, else False
		"""
		expected_state = self.values.get("STATE", False)
		current_service = self.values.get("SERVICE_ID", "NOT SET")
		try:
			service = getattr(self._service_list, current_service)

			if expected_state == service.value:
				self._reporting.add_report_message_pass(f"{current_service} returned True")
				return True
		except AttributeError as error:
			self._reporting.add_report_message_ta_error(f"Missing service '{current_service}' in utility! {error}")
			return False
		self._reporting.add_report_message_pass(f"{current_service} return False")
		return False
