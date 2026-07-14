# -*- coding: utf-8 -*-
"""The interface from which each proxy and server in this package derive."""

import abc

import enna.core.component_system.decorators
import enna.core.interfaces
import enna.core.interfaces.component


@enna.core.component_system.decorators.GenerateProxy()
class Interface(enna.core.interfaces.component.Component):
	"""Abstract interface for controlling test portal."""

	def __init__(self) -> None:
		"""Constructor of interface."""
		self._connected = enna.core.interfaces.Data(False)

	@abc.abstractmethod
	def switch_enabling_vehicle_mocking(self, state: bool) -> None:
		"""Enable or disable mocking for this vehicle. Status could you on Test Portal https://tprt.moria.app.apl.eu.dp.odp.cloud.vwgroup.com/tprt

		:param state: True to enable, False to disable
		:raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError: if failed switching vehicle mocking
		"""

	@abc.abstractmethod
	def switch_activation_of_mock(self, name: str, state: bool) -> None:
		"""Switch activation of mock to true or false.
		Example: One activate mock. If get the method name of mock e.g. "OCC_MOCK_WITH_WARNINGS_V2" with and state true.
		For deactivate get state false.

		:param name: name of mock
		:param state: ture to activate, false to deactivate
		:raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError if error activate mock in test portal
		:raise: enna_kwd_testing.utilities.test_portal.exceptions.PortalMockNotFound if mock not available for vehicle
		"""

	@abc.abstractmethod
	def deactivation_all_mocks(self):
		"""Deactivate all mocks for this vehicle. And disable mocking for this vehicle"""

	@abc.abstractmethod
	def send_job(self, name: str) -> None:
		"""Send a new job request on vehicle.
		Example: Send job "notifyCustomerDataplanJob_v1_0_1_OK" -> Backend send data plan is available and active on vehicle.

		:param name: name of job
		:raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError: if failed switching vehicle mocking
		"""

	@abc.abstractmethod
	def read_vehicle_by_vin(self) -> None:
		"""Read vehicle by VIN. So that coould read vehicle number to needed for enabling mocking in console."""

	@property
	def connected(self) -> enna.core.interfaces.Data[bool]:
		"""Return state of connection for Test Portal.

		:return: True is connected, False is Disconnected.
		"""
		return self._connected
