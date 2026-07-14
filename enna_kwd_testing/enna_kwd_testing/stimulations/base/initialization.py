# -*- coding: utf-8 -*-
"""Module contains testcases to initialization test bench."""

import abc
import datetime
import logging
import time
import requests

import enna.core.config
import enna.core.component_system.decorators
import enna.core.interfaces.testing
import enna.data_interfaces.adb.exceptions
import enna.utilities.diagnosis.helper

import enna_hcp_configuration.android.analyzer

import enna_kwd_testing.stimulations.base.exceptions


MODULE_LOGGER = logging.getLogger(__name__)


class _SetSystemLanguage(enna.core.interfaces.testing.Stimulation, metaclass=abc.ABCMeta):
	"""Base clas for set the System Language"""

	def __init__(self, reporting, rsi) -> None:
		"""Constructor to set language via rsi.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna.data_interfaces.rsi.interface.Interface rsi: Instance of rsi
		"""

		super().__init__(reporting)
		self._rsi = rsi
		self._target_language = None

	def _action(self) -> bool:
		"""Execute set language. Language will change via RSI.

		:raise enna_kwd_testing.stimulations.base.exceptions.AttributeNotDefined: if attribute of target language not defined
		:return: True if language was set correctly, False otherwise
		:rtype: bool
		"""
		uri_language_update = "language/changeRequests"
		uri_read_current_language = "language/system/LANGUAGE_SYSTEM/currentSystemLanguage"

		if not isinstance(self._target_language, str):
			msg = "You do not define attribute for target Language!"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.stimulations.base.exceptions.AttributeNotDefined(msg)

		current_language = self._rsi.get(uri_read_current_language)
		if self._target_language == current_language:
			MODULE_LOGGER.info("Current Language is equal witch target language!")
		else:
			try:
				payload = {"componentType": "graphicalUserInterface", "newLanguage": self._target_language}
				self._rsi.create_element(uri_language_update, payload)
			except (enna.core.exceptions.EventNotFoundException, enna.data_interfaces.rsi.exceptions.RSIException):
				MODULE_LOGGER.error(f"No positive response if send language update to language {self._target_language}!")
		time.sleep(5.0)
		new_language = self._rsi.get(uri_read_current_language)
		language_config = {"system_language": new_language}
		enna_hcp_configuration.android.analyzer.initialize(language_config)
		if self._target_language == new_language:
			MODULE_LOGGER.info(f"Language change from '{current_language}' to '{new_language}' is successfully.")
			return True
		MODULE_LOGGER.error(f"Language change from '{new_language}' to '{self._target_language}' is not successfully.")
		return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.rsi")
class SetSystemLanguageToEnglish(_SetSystemLanguage):
	"""Stimulation set System Language to english (United Kingdom)."""

	def __init__(self, reporting, rsi) -> None:
		"""""Constructor to set language to english.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna.data_interfaces.rsi.interface.Interface rsi: Instance of rsi
		"""
		super().__init__(reporting, rsi)
		self._target_language = "en_GB"


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.rsi")
class SetSystemLanguageToGerman(_SetSystemLanguage):
	"""Stimulation set System Language to german."""

	def __init__(self, reporting, rsi) -> None:
		"""""Constructor to set language to german.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna.data_interfaces.rsi.interface.Interface rsi: Instance of rsi
		"""
		super().__init__(reporting, rsi)
		self._target_language = "de_DE"


MODULE_CONFIG = enna.core.config.get(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class RegistryRSI(enna.core.interfaces.testing.Stimulation, metaclass=abc.ABCMeta):
	"""Register all services from RSI Data Tool to test bench."""

	def __init__(self, reporting) -> None:
		"""Constructor of stimulation of regeistry services.

		 :param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		 """
		super().__init__(reporting)
		self.__read_configuration()
		self.__services = []

	def __read_configuration(self):
		"""Read configuration for test bench."""
		self.__rsi_port = MODULE_CONFIG.get("rsi_port", 14712)
		self.__target = MODULE_CONFIG.get("target", "172.16.250.248")
		self.__host = MODULE_CONFIG.get("host", "172.16.250.250")
		self.__data_tool_port = 3333

	def _precondition(self) -> bool:
		"""Reading services from  RSI-Data-Tool.

		:return: True if RSI-Data-Tool available
		:rtype: bool
		:raises ConnectionError: if not running RSI-Data-Tool found.
		"""
		try:
			response = requests.get(f"http://localhost:{self.__data_tool_port}", timeout=10.0)
			if response.status_code == 200:
				try:
					for service in response.json()["data"]:
						self.__services.append(service["name"])
						MODULE_LOGGER.debug(f"Service {service['name']} run on RSI-Data-Tool.")
				except (KeyError, IndexError):
					MODULE_LOGGER.error("Service could not read name does not exist in schema.")
			else:
				msg = f"Negative response by get request to RSI-Data-Tool. Error-Code: {response.status_code} - {response.reason}"
				MODULE_LOGGER.exception(msg)
				raise ConnectionError(msg)
		except requests.RequestException:
			msg = "Request exception by try connect to RSI-Data-Tool!"
			MODULE_LOGGER.exception(msg)
			raise ConnectionError(msg)
		return True

	def _action(self) -> bool:
		"""Register all services from RSI-Data-Tool on bench.

		:return: Register is finished
		:rtype: bool
		"""
		for service in self.__services:
			body = {"http_uri": f"http://{self.__host}:{self.__data_tool_port}/{service}"}
			try:
				response = requests.put(f"http://{self.__target}:{self.__rsi_port}/{service}", json=body, timeout=10.0)
				time.sleep(0.2)
				if response.status_code == 201:
					self._reporting.add_report_message_pass(f"{service} registry OK.")
				else:
					self._reporting.add_report_message_system_error(f"http://{self.__target}:{self.__rsi_port}/{service} registry Failed! Reason: {response.status_code} - {response.reason}")
			except requests.RequestException:
				self._reporting.add_report_message_system_error(f"Can not connect to service: http://{self.__target}:{self.__rsi_port}/{service}")

		return True


@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class DeactivateFirewall(enna.core.interfaces.testing.Stimulation, metaclass=abc.ABCMeta):
	"""Deactivate Firewall on RSI Gateway"""

	def __init__(self, reporting, adb) -> None:
		"""Constructor of deactivation firewall.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of android debug bridge
		"""
		super().__init__(reporting)
		self.__adb = adb

	def _action(self) -> bool:
		"""deactivate firewall

		:return: True if success, otherwise false
		:rtype: bool
		"""
		try:
			if enna.core.config.INFOTAINMENT_SYSTEM.cluster >= 46:
				self.__adb.execute_shell_command(command="setenforce 0", timeout=10.0)
				self._reporting.add_report_message_info("Set enforce to 0")
			self.__adb.execute_shell_command(command="ip6tables -j ACCEPT -I OUTPUT" , timeout=10.0)
			self.__adb.execute_shell_command(command="ip6tables -j ACCEPT -I INPUT", timeout=10.0)
			self.__adb.execute_shell_command(command="ip6tables -j ACCEPT -I FORWARD", timeout=10.0)
			self.__adb.execute_shell_command(command="sync", timeout=10.0)
		except enna.data_interfaces.adb.exceptions.ADBException:
			self._reporting.add_report_message_system_error("Could not deactivate firewall.")
			return False
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class SetTimeOnRSI(enna.core.interfaces.testing.Stimulation, metaclass=abc.ABCMeta):
	"""Set system time on RSI Tool. For Audi Assistant is necessary to set a UTC Time."""

	def __init__(self, reporting) -> None:
		"""Constructor of stimulation of Time on RSI.

		 :param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		 """
		super().__init__(reporting)
		self.__read_configuration()

	def __read_configuration(self):
		"""Read configuration for test bench."""
		self.__rsi_port = MODULE_CONFIG.get("rsi_port", 14712)
		self.__target = MODULE_CONFIG.get("target", "172.16.250.248")

	def _action(self) -> bool:
		"""Set Current time in RSI service Time.

		:return:
		"""
		url = f"http://{self.__target}:{self.__rsi_port}"
		response = requests.get(f"{url}/Time/times/", timeout=10.0)
		for timer in response.json()["data"]:
			new_time = {
				"date": datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d'),
				"time": datetime.datetime.now(datetime.UTC).strftime('%H:%M:%S.000'),
				"unix": int(time.time())
			}
			response = requests.post(f"{url}{timer['uri']}", json=new_time, timeout=10.0)
			time.sleep(0.2)
			if response.status_code == 200:
				self._reporting.add_report_message_pass(f"Set current time is success for {timer['name']}")
			else:
				self._reporting.add_report_message_system_error(f"Set current time is unsuccessful for {timer['name']}")
				return False
		return True
