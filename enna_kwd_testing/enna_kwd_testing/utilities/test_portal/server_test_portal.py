# -*- coding: utf-8 -*-
"""Module contains server for control test portal via API."""
import datetime
import logging
import requests

import enna.core.config
import enna.core.interfaces.server
import enna.core.logger
import enna.core.exceptions

import enna_kwd_testing.utilities.test_portal.exceptions
import enna_kwd_testing.utilities.test_portal.interface


INSTANCE_CONFIG = enna.core.config.get_instance_config(__name__)
MODULE_LOGGER = logging.getLogger(__name__)


class Mock:
	"""Class for available mock."""

	def __init__(self, name: str, activation_state: bool, link: str) -> None:
		"""Constructor for Mock.

		:param name: name of mock (could read in Test Portal e.g. https://tprt.moria.app.apl.eu.dp.odp.cloud.vwgroup.com/tprt/start#!/mocks/BAUNEEGFZ21050455)
		:param activation_state: current activation state
		:param link: link to could chacnge mock content via PATCH request
		"""
		self._name = name
		self._activation_state = activation_state
		self._link = link

	@property
	def name(self) -> str:
		"""Return name of mock.

		:return: name
		"""
		return self._name

	@property
	def link(self) -> str:
		"""Return link for controlling mock. With link could mock activate/deactivate via PATCH request

		:return: link
		"""
		return self._link

	@property
	def activation_state(self) -> bool:
		"""Return current activation state of mock. True is activated. False is deactivated.

		:return: activation state
		"""
		return self._activation_state

	@activation_state.setter
	def activation_state(self, value: bool) -> None:
		"""Change activation state of mock.

		:param value: new activation state
		"""
		self._activation_state = bool(value)


class Server(enna_kwd_testing.utilities.test_portal.interface.Interface, enna.core.interfaces.server.Server):
	"""Provide access for controlling test portal."""

	def __init__(self, instance_name) -> None:
		"""Constructor for interface to controller for test portal.

		:param str instance_name: mame of implementation instance
		"""
		enna_kwd_testing.utilities.test_portal.interface.Interface.__init__(self)
		enna.core.interfaces.server.Server.__init__(self, instance_name=instance_name)
		self.___mocks = []
		self.__instance_logger = enna.core.logger.InstanceLogger(MODULE_LOGGER, instance_name=instance_name)
		self.__read_configuration(instance_name=instance_name)
		self.__base_url = "https://tprt-service.moria.app.apl.eu.dp.odp.cloud.vwgroup.com/tprt-service"
		self.__session = requests.session()
		self.__session.verify = False

		self._set_online()

	def __read_configuration(self, instance_name: str) -> None:
		"""Reading instance configuration.

		:param instance_name: name of instance
		:raise enna.core.exceptions.ConfigurationException: if configuration for instance is wrong or missing
		"""
		try:
			config = INSTANCE_CONFIG[instance_name]
			self.__user = config["user"]
			self.__password = config["password"]
			self.__vin = config["vin"]
			self.__vehicle = config["vehicle"]
		except KeyError as error:
			msg = f"Missing mandatory key in instance configuration! Error: {error}."
			self.__instance_logger.exception(msg)
			raise enna.core.exceptions.ConfigurationException(msg)

	def __login(self) -> None:
		"""Login on Test Portal.

		:raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError: if login failed
		"""
		payload = {"username": self.__user, "password": self.__password}
		headers = {"Accept": "application/json;charset=UTF-8"}
		uri = "/login"
		try:
			response = self.__session.post(f"{self.__base_url}{uri}",json=payload, headers=headers)
			if response.status_code == 200:
				self.__session.headers = {
					"Accept": "application/json, */*",
					"Content-Type": "application/json;charset=utf-8",
					"Authorization": f"{response.headers["Authorization"]}"
				}
				self.__instance_logger.info("Login on Test Portal success.")
			else:
				msg = f"Login on Test Portal is not successful! url= {self.__base_url}{uri} Error: {response.status_code} Reason {response.reason}."
				self.__instance_logger.exception(msg)
				raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError(msg)
		except requests.RequestException as error:
			msg = f"Login on Test Portal is not successful! url= {self.__base_url}{uri} Error: {error}"
			self.__instance_logger.exception(msg)
			raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError(msg)

	def __find_nock(self, name: str) -> Mock:
		"""Find mock in vehicle.

		:param name: name of mock.
		:return: object of vehicle mock
		:raises enna_kwd_testing.utilities.test_portal.exceptions.PortalMockNotFound: if mock not available for vehicle
		"""
		for mock in self.___mocks:
			if mock.name == name:
				return mock
		msg = f"Mock '{name}' is not available for vehicle! Check vehicle mocks for {self.__vin} in Test Portal."
		self.__instance_logger.exception(msg)
		raise enna_kwd_testing.utilities.test_portal.exceptions.PortalMockNotFound(msg)

	def __get_mocks(self):
		"""Get all mocks what are available for this vehicle.

		:raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError: if failed reading mocks
		"""
		uri = f"/v1/mocks?page=0&searchTerm={self.__vin}&size=50&templateFilterMode=nonTemplatesOnly"
		try:
			response = self.__session.get(url=f"{self.__base_url}{uri}")
			if response.status_code < 400:
				for mock in response.json()["_embedded"]["mocks"]:
					self.___mocks.append(Mock(name=mock["name"], activation_state=mock["active"], link=mock["_links"]["self"]["href"]))
					self.__instance_logger.debug(f"Mock: {mock["name"]} \t {mock["active"]} \t {mock["_links"]["self"]["href"]}")
			else:
				msg = f"Could not read Mocks of vehicle {self.__vin}! Error: {response.status_code} Reason {response.reason}."
				self.__instance_logger.exception(msg)
				raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError(msg)
		except requests.RequestException as error:
			msg = f"Could not read Mocks of vehicle {self.__vin}! Error: {error}"
			self.__instance_logger.exception(msg)
			raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError(msg)

	def __connect(self) -> None:
		"""Connecting to Test Portal."""
		self.__login()
		self.__get_mocks()
		self._connected = enna.core.interfaces.Data(True)
		self._signal_property("connected", self.connected)


	def switch_enabling_vehicle_mocking(self, state: bool) -> None:
		"""Enable or disable mocking for this vehicle. Status could you on Test Portal https://tprt.moria.app.apl.eu.dp.odp.cloud.vwgroup.com/tprt

		:param state: True to enable, False to disable
		:raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError: if failed switching vehicle mocking
		"""
		if not self.connected.value:
			self.__connect()

		uri = f"/v1/vehicles/{self.__vehicle}"
		payload = {"mocked": state}
		try:
			response = self.__session.patch(url=f"{self.__base_url}{uri}", json=payload)
			if response.status_code < 400:
				self.__instance_logger.info(f"Status of enabling mocking for vehicle is {state}.")
			else:
				msg = f"Could not read Mocks of vehicle {self.__vin}! url= {self.__base_url}{uri} Error: {response.status_code} Reason {response.reason}."
				self.__instance_logger.exception(msg)
				raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError(msg)
		except requests.RequestException as error:
			msg = f"Could not read Mocks of vehicle {self.__vin}! url= {self.__base_url}{uri} Error: {error}"
			self.__instance_logger.exception(msg)
			raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError(msg)

	def switch_activation_of_mock(self, name: str, state: bool) -> None:
		"""Switch activation of mock to true or false.
		Example: One activate mock. If get the method name of mock e.g. "OCC_MOCK_WITH_WARNINGS_V2" with and state true.
		For deactivate get state false.

		:param name: name of mock
		:param state: ture to activate, false to deactivate
		:raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError: if error activate mock in test portal
		:raise enna_kwd_testing.utilities.test_portal.exceptions.PortalMockNotFound: if mock not available for vehicle
		"""
		self.switch_enabling_vehicle_mocking(state=True)
		mock = self.__find_nock(name=name)
		payload = {"active": state}

		if mock.activation_state == state:
			self.__instance_logger.info(f"State of mock '{name}' need not change. Mock has correct state.")
			return

		try:
			response = self.__session.patch(mock.link, json=payload)
			if response.status_code < 400:
				self.__instance_logger.info(f"Mock '{name}' activation state is {state}.")
				mock.activation_state = state
			else:
				msg = f"Mock {name} could not change state to {state}! url = {mock.link} Error: {response.status_code} Reason {response.reason}."
				self.__instance_logger.exception(msg)
				raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError(msg)

		except requests.RequestException as error:
			msg = f"Could not activate Mock '{name}'! url = {mock.link} Error: {error}"
			self.__instance_logger.exception(msg)
			raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError(msg)

	def deactivation_all_mocks(self):
		"""Deactivate all mocks for this vehicle. And disable mocking for this vehicle"""
		if not self.connected.value:
			self.__connect()
		for mock in self.___mocks:
			if mock.activation_state:
				self.switch_activation_of_mock(name=mock.name, state=False)
		self.switch_enabling_vehicle_mocking(state=False)


	def send_job(self, name: str) -> None:
		"""Send a new job request on vehicle.
		Example: Send job "notifyCustomerDataplanJob_v1_0_1_OK" -> Backend send data plan is available and active on vehicle.

		:param name: name of job
		:raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError: if failed switching vehicle mocking
		"""
		if not self.connected.value:
			self.__connect()
		today = datetime.date.today()
		payload = {
			"vin": self.__vin,
			"jobName": name,
			"deliveryDate": f"{today.year}-{today.month}-{today.day + 1}T00:00:00.000Z",
			"expiryDate": f"{today.year}-{today.month}-{today.day + 2}T00:00:00.000Z"
		}
		uri = "/v1/vehiclejobs/invocation"
		try:
			response = self.__session.post(f"{self.__base_url}{uri}", json=payload)
			if response.status_code < 400:
				self.__instance_logger.info(f"Send job '{name}' on vehicle {self.__vin}.")
			else:
				msg = f"Could not send job '{name}'! url= {self.__base_url}{uri} Error: {response.status_code} Reason {response.reason}."
				self.__instance_logger.exception(msg)
				raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError(msg)

		except requests.RequestException as error:
			msg = f"Could not activate Mock '{name}'! url = {self.__base_url}{uri} Error: {error}"
			self.__instance_logger.exception(msg)
			raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError(msg)



	def read_vehicle_by_vin(self) -> None:
		"""Read vehicle by VIN. So that coould read vehicle number to needed for enabling mocking in console.

		:raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError: if error by reading vehicle in test portal.
		"""
		if not self.connected.value:
			self.__connect()

		uri = f"/v1/vehicles/?vin={self.__vin}"
		# payload = {"vin": self.__vin}
		try:
			response = self.__session.get(f"{self.__base_url}{uri}")
			if response.status_code < 400:
				self.__instance_logger.info(response.json()["_embedded"])
			else:
				msg = f"Could not read vehicle '{self.__vin}'! url= {self.__base_url}{uri} Error: {response.status_code} Reason {response.reason}."
				self.__instance_logger.exception(msg)
				raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError(msg)

		except requests.RequestException as error:
			msg = f"Could not read vehicle '{self.__vin}'! url= {self.__base_url}{uri} Error: {error}"
			self.__instance_logger.exception(msg)
			raise enna_kwd_testing.utilities.test_portal.exceptions.PortalConnectionError(msg)
