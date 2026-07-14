# -*- coding: utf-8 -*-
"""Module contains reporting server wit use API to write results in PSW database"""
import enum
import logging
import os

from http import HTTPStatus
import requests

import enna.core.config
import enna.core.deployment.dependency_manager
import enna.core.helper
import enna.core.exceptions
import enna.core.interfaces.server
import enna.core.logger
import enna.core.reporting.exceptions
import enna.core.reporting.helper
import enna.core.reporting.interface
import enna.core.time
import enna.custom_types


MODULE_LOGGER = logging.getLogger(__name__)
MODULE_CONFIG = enna.core.config.get(enna.core.reporting.interface.__name__)
INSTANCE_CONFIG = enna.core.config.get_instance_config(enna.core.reporting.interface.__name__)


# pylint: disable=inconsistent-quotes
NEEDED_REPORT_FIELDS: list[str] = ['general_meta_data', 'market', 'hardware_version', 'software_version', 'department',
								   'projects', 'tester_name', 'environment', 'environment_identifier',
								   'device_under_test', 'order', 'cluster', 'vehicle_project', 'valuation', 'history',
								   'messages', 'method', 'reference', 'bug_ticket']


class Valuation(enum.Enum):
	"""Enumeration for test valuation"""
	TA_ERROR = "error"
	SYSTEM_ERROR = "failed"
	WARNING = "skipped"
	PASS = "passed"
	INFO = "not_testable"


# pylint: disable=too-many-public-methods,too-many-instance-attributes, too-many-positional-arguments
class Server(enna.core.reporting.interface.Interface, enna.core.interfaces.server.Server):
	"""Sever implementation a reporting interface to psw test results in database."""

	def __init__(self, instance_name: str) -> None:
		"""Constructor of reporting interface to save results in PSW database.

		:param str instance_name: name of instance which it will create
		:raises enna.core.exceptions.ConfigurationException, if missing
		:raises enna.core.exceptions.ConfigurationException, if missing a necessary keyword in instance config
		"""
		enna.core.reporting.interface.Interface.__init__(self)
		enna.core.interfaces.server.Server.__init__(self, instance_name)
		self.__read_configuration(instance_name=instance_name)
		self.__current_valuation = Valuation.INFO
		self.__current_test = None
		self.__parent_test = []
		self.__report_started = False
		self._set_online()
		self._report_path = enna.core.interfaces.Data("online")
		self._signal_property("report_path", self.report_path)

	def __read_configuration(self, instance_name: str) -> None:
		"""Read instance configuration for reporting interface.

		:param str instance_name: name of server instance
		:raises enna.core.exceptions.ConfigurationException: if missing a necessary keyword in instance config
		"""
		try:
			instance_config = INSTANCE_CONFIG[instance_name]
			# workaround for overhand login data of REST api.
			if "tmdb_user" in os.environ:
				instance_config["user"] = os.environ["tmdb_user"]
			if "tmdb_password" in os.environ:
				instance_config["password"] = os.environ["tmdb_password"]
		except KeyError:
			message = f"Missing instance name '{instance_name}' in instance configuration! Please check file 'config/enna/core/reporting/{MODULE_CONFIG.get('instance_config', '')}'"
			MODULE_LOGGER.exception(message)
			raise enna.core.exceptions.ConfigurationException(message)
		try:
			self.__authentication = (instance_config['user'], instance_config['password'])
			self.__url = instance_config['url']
			self.__reporting_fields = instance_config['Fields']
			for field in NEEDED_REPORT_FIELDS:
				if field in self.__reporting_fields:
					message = f"Value for field '{field}' must be a dict['name': str, 'value': any]"
					try:
						if 'name' not in self.__reporting_fields[field] or 'value' not in self.__reporting_fields[
							field]:
							MODULE_LOGGER.exception(message)
							raise enna.core.exceptions.ConfigurationException(message)
					except (TypeError, ValueError, KeyError):
						MODULE_LOGGER.exception(message)
						raise enna.core.exceptions.ConfigurationException(message)
				else:
					message = f"Missing field '{field}' in configuration Fields! Please check your instance config."
					MODULE_LOGGER.exception(message)
					raise enna.core.exceptions.ConfigurationException(message)
		except KeyError as e:
			message = f"Missing Keyword in instance configuration: {e}. Please check file 'config/enna/core/reporting/{MODULE_CONFIG.get('instance_config', '')}'"
			MODULE_LOGGER.exception(message)
			raise enna.core.exceptions.ConfigurationException(message)

	def start_report(self, report_name: str, path: list[str], campaign_name: str = "") -> None:
		"""Start the report. Only one report can be started at the same time.

		:param report_name: Name of the report
		:param path: Structure of where report should be located. I.E.: ['0001_Test', 'Testing']
		:param campaign_name: Optional clean campaign name which is executed to create report, if it differs from report name
		:raises enna.core.reporting.exceptions.AlreadyStartedException: If a report is already started
		"""
		self.__reporting_fields['tester_name']['value'] = os.getlogin()
		self.__reporting_fields['environment_identifier']['value'] = os.environ.get('TestCubeName', 'UNKNOWN')

		self.__report_started = True

	def end_report(self) -> None:
		"""End the report and closes any open test groups and test cases.

		:raises enna.core.reporting.exceptions.NotStartedException: If no report was previously started
		"""
		if not self.__report_started:
			raise enna.core.reporting.exceptions.NotStartedException("Reporting must be started before ending!")
		MODULE_LOGGER.info("Reporting ended.")

	def start_testgroup(self, name: str) -> None:
		"""Start a new test group in the active report or test group.

		:param name: Name of the test group
		"""
		MODULE_LOGGER.debug("In that report is this not supported.")

	def end_testgroup(self) -> None:
		"""Close active test group."""
		MODULE_LOGGER.debug("In that report is this not supported.")

	def start_testcase(self, name: str) -> None:
		"""Start a new test case in the active test group.

		:param name: Name of the test case
		"""
		if len(self.__parent_test) == 0:
			self.__current_valuation = Valuation.INFO
			self.__reporting_fields['messages']['value'] = ""
			self.__reporting_fields['reference']['value'] = None
		self.__parent_test.append(self.__current_test)
		self.__current_test = name
		MODULE_LOGGER.info(f"Start reporting for testcase '{name}'")

	def end_testcase(self, result: bool) -> None:
		"""End active test.

		:param result: Test case result
		"""
		if self.__current_test is None:
			MODULE_LOGGER.error("Test case must be started before ending!")
			return
		self.__reporting_fields['valuation']['value'] = self.__current_valuation.value
		MODULE_LOGGER.info(f"Start reporting for testcase '{self.__current_test}'")
		self.__current_test = self.__parent_test.pop(-1)

		if len(self.__parent_test) == 0:
			self.__send_to_database()

	def add_report_message_info(self, message: str) -> None:
		"""Add a new report message as info to the active test case.

		Info messages are for information that simplifies analysis.

		:param message: report message
		"""
		self.__add_report_message(message, Valuation.INFO)

	def add_report_message_pass(self, message: str) -> None:
		"""Add a new report message as pass to the active test case.

		Pass messages are for signaling that a stimulation ran successfully.

		:param message: report message
		"""
		self.__add_report_message(message, Valuation.PASS)

	def add_report_message_warning(self, message: str) -> None:
		"""Add a new report message as warning to the active test case.

		Warning messages report that the system did not fully perform as expected and therefore manual investigation is needed.

		:param message: report message
		"""
		self.__add_report_message(message, Valuation.WARNING)

	def add_report_message_system_error(self, message: str) -> None:
		"""Add a new report message as system error to the active test case.

		System error messages report unexpected behavior in the system under test.

		:param message: report message
		"""
		self.__add_report_message(message, Valuation.SYSTEM_ERROR)

	def add_report_message_ta_error(self, message: str) -> None:
		"""Add a new report message as test automation error to the active test case.

		Test automation error messages report errors in the test automation that need to be checked by an automation developer.

		:param message: report message
		"""
		self.__add_report_message(message, Valuation.TA_ERROR)

	def add_test_result_pass(self, name: str, message: str, meta_data: enna.core.reporting.MetaData | None = None,
							 id_reference: str = "",
							 reporting_platform: enna.custom_types.ReportingPlatform = enna.custom_types.ReportingPlatform.UNKNOWN) -> None:
		"""Add a new test result as pass to the active test case.

		The valuation of a test result is PASS if the system performs as expected.

		:param name: Name which will identify the test result. Typically a descriptive name of the related test.
		:param message: Message that will be appended to the test result
		:param meta_data: Optional dict with meta data (see :py:class:`enna.core.reporting.interface.Interface` for dict format)
		:param id_reference: Optional test id reference if one exists
		:param reporting_platform: Optional reporting platform
		"""
		self.__add_test_result(name, message, Valuation.PASS, id_reference)

	def add_test_result_system_error(self, name: str, message: str,
									 meta_data: enna.core.reporting.MetaData | None = None, id_reference: str = "",
									 reporting_platform: enna.custom_types.ReportingPlatform = enna.custom_types.ReportingPlatform.UNKNOWN) -> None:
		"""Add a new test result as system_error to the active test case.

		The valuation of a test result is system error, i.e. FAIL, if the system didn't perform as expected.

		:param name: Name which will identify the test result. Typically a descriptive name of the related test.
		:param message: Message that will be appended to the test result
		:param meta_data: Optional dict with meta data (see :py:class:`enna.core.reporting.interface.Interface` for dict format)
		:param id_reference: Optional test id reference if one exists
		:param reporting_platform: Optional reporting platform
		"""
		self.__add_test_result(name, message, Valuation.SYSTEM_ERROR, id_reference)

	def add_test_result_ta_error(self, name: str, message: str, meta_data: enna.core.reporting.MetaData | None = None,
								 id_reference: str = "",
								 reporting_platform: enna.custom_types.ReportingPlatform = enna.custom_types.ReportingPlatform.UNKNOWN) -> None:
		"""Add a new test result as ta_error to the active test case.

		The valuation of a test result is TA error, i.e. ERROR, if the test did not execute as expected.

		:param name: Name which will identify the test result. Typically a descriptive name of the related test.
		:param message: Message that will be appended to the test result
		:param meta_data: Optional dict with meta data (see :py:class:`enna.core.reporting.interface.Interface` for dict format)
		:param id_reference: Optional test id reference if one exists
		:param reporting_platform: Optional reporting platform
		"""
		self.__add_test_result(name, message, Valuation.TA_ERROR, id_reference)

	def add_test_result_not_tested(self, name: str, message: str, meta_data: enna.core.reporting.MetaData | None = None,
								   id_reference: str = "",
								   reporting_platform: enna.custom_types.ReportingPlatform = enna.custom_types.ReportingPlatform.UNKNOWN) -> None:
		"""Add a new test result as not testable to the active test case.

		Test case with result not testable. In general, this function is used if a pre-conditions fails or a passive model didn't append its test cases.

		:param name: Name which will identify the test result. Typically a descriptive name of the related test.
		:param message: Message that will be appended to the test result
		:param meta_data: Optional dict with meta data (see :py:class:`enna.core.reporting.interface.Interface` for dict format)
		:param id_reference: Optional test id reference if one exists
		:param reporting_platform: Optional reporting platform
		"""
		self.__add_test_result(name, message, Valuation.WARNING, id_reference)

	def attach_meta_data_to_test_case(self, meta_data: enna.core.reporting.MetaData) -> None:
		"""Attach meta data to the active test case.

		:param meta_data: Dict with meta data (see :py:class:`enna.core.reporting.interface.Interface` for dict format)
		"""
		MODULE_LOGGER.debug("Not supported for that report!")

	def attach_meta_data_to_report(self, meta_data: enna.core.reporting.MetaData) -> None:
		"""Attach meta data to the active report.

		:param meta_data: Dict with meta data (see :py:class:`enna.core.reporting.interface.Interface` for dict format)
		"""
		forbidden_fields = ['valuation', 'reference', 'general_meta_data', 'history', 'bug_ticket']
		for keyword in meta_data:
			if keyword in forbidden_fields:
				MODULE_LOGGER.error(f"Keyword '{keyword}' is not allowed to write in report meta data.")
				continue
			if keyword in self.__reporting_fields:
				self.__reporting_fields[keyword]['value'] = meta_data[keyword]
				MODULE_LOGGER.info(f"Update report field '{keyword}' with value '{meta_data[keyword]}'")
			else:
				self.__reporting_fields['general_meta_data']['value'] += f"{keyword}: {meta_data[keyword]}\n"
				MODULE_LOGGER.info(f"Add to general report meta data: '{keyword}: {meta_data[keyword]}'")

	def attach_file_to_test_case(self, content: bytearray, file_name: str) -> None:
		"""Attach something to the active test case.

		:param content: Content to be attached
		:param file_name: Name the content as displayed as in the report. It is no literal file but rather a named entry in the database.
		"""
		MODULE_LOGGER.error("Not yet implemented!")

	def attach_file_to_test_case_from_file(self, file_name: str, file_path: str) -> None:
		"""Attach a file to the active test case.

		:param file_name: Name of the file that is displayed in report
		:param file_path: Path to the file containing full path and file name
		"""
		MODULE_LOGGER.error("Not yet implemented!")

	def attach_file_to_report(self, content: bytearray, file_name: str) -> None:
		"""Attach something to the active report.

		:param content: Content to be attached
		:param file_name: Name the content as displayed as in the report. It is no literal file but rather a named entry in the database.
		"""
		MODULE_LOGGER.error("Not yet implemented!")

	def attach_file_to_report_from_file(self, file_name: str, file_path: str) -> None:
		"""Attach a file to the report.

		:param file_name: Name of the file that is displayed in report
		:param file_path: Path to the file containing full path and file name
		"""
		MODULE_LOGGER.error("Not yet implemented!")

	def set_reporting_level(self, reporting_level: enna.core.reporting.Valuation) -> None:
		"""Set logging level of reporting.

		:param reporting_level: New logging level for reporting.
		"""
		MODULE_LOGGER.debug("Not aupported for that report!")

	def __update_valuation(self, new_valuation: Valuation) -> None:
		"""Update current test valuation.
		Valuation will change if priority of new valuation higher like current valuation.

		:param Valuation new_valuation: new valuation for test
		"""
		priority = [Valuation.TA_ERROR, Valuation.SYSTEM_ERROR, Valuation.WARNING, Valuation.PASS, Valuation.INFO]

		if priority.index(new_valuation) < priority.index(self.__current_valuation):
			self.__current_valuation = new_valuation
			MODULE_LOGGER.debug(f"Test valuation is updated to {self.__current_valuation.name}.")
		else:
			MODULE_LOGGER.debug(
				f"No update of current test valuation. Current valuation is {self.__current_valuation.name}")

	def __send_to_database(self) -> None:
		"""Send a request to database.

		:raises ReportingConnectionError: if requests method raise an exception.
		"""
		if self.__reporting_fields['reference']['value'] is None:
			MODULE_LOGGER.error("Test result could not save missing reference to testcase.")
			return
		if self.__reporting_fields['software_version']['value'] is None or self.__reporting_fields['hardware_version'][
			'value'] is None:
			MODULE_LOGGER.error("Test result could not save missing version of softwars or hardware.")
			return

		data = {}
		for key in self.__reporting_fields:
			data[self.__reporting_fields[key]['name']] = self.__reporting_fields[key]['value']
		try:
			response = requests.post(url=self.__url, auth=self.__authentication, verify=False, json=data, timeout=30.0)

			if response.status_code == HTTPStatus.CREATED:
				MODULE_LOGGER.debug("Data save success in database.")
			elif response.status_code == HTTPStatus.UNAUTHORIZED:
				MODULE_LOGGER.error(
					f"You have not rights to write on '{self.__url}'! Error: {response.status_code}, Message: {response.reason}")
			else:
				MODULE_LOGGER.error(
					f"Unknown error while writing to '{self.__url}'! Error: {response.status_code}, Message: {response.reason}")

		except (requests.ConnectionError, requests.HTTPError) as e:
			message = f"No connection to '{self.__url}'! Error: {e}"
			MODULE_LOGGER.exception(message)
			raise ReportingConnectionError(message)

	def __add_message(self, message: str, valuation: Valuation = Valuation.INFO) -> None:
		"""Add message to testcase result.
		Format for added Message is "<YYYY-mm-dd | HH:MM:SS> <Valuation>: <message>"

		:param str message: message
		:param Valuation valuation: valuation of message, default is INFO
		"""
		if valuation in (Valuation.TA_ERROR, Valuation.SYSTEM_ERROR, Valuation.WARNING):
			self.__reporting_fields['messages']['value'] += f"{enna.core.time.now_as_string()} {valuation.name}: {message}\n"
			self.__reporting_fields['messages']['value'] = self.__reporting_fields['messages']['value'][:4096]
			MODULE_LOGGER.debug(f"Added message to result: {enna.core.time.now_as_string()} {valuation.name}: {message}")

	def __add_report_message(self, message: str, valuation: Valuation) -> None:
		"""Add report message to testcase result and update current valuation of testcase result

		:param str message: message
		:param Valuation valuation: valuation of report message, default is INFO
		"""
		# self.__update_valuation(valuation)
		self.__add_message(message, valuation)

	def __add_test_result(self, name: str, message: str, valuation: Valuation, id_reference: str = "") -> None:
		"""Add a new test result as to test case and update valuation of test case.

		:param name: Name which will identify the test result. Typically a descriptive name of the related test.
		:param message: Message that will be appended to the test result
		:param Valuation valuation: valuation of test result
		:param id_reference: Optional test id reference if one exists
		"""
		if id_reference != "":
			self.__reporting_fields['reference']['value'] = id_reference
		self.__update_valuation(valuation)
		MODULE_LOGGER.debug(f"{name}\n{message}")
		# self.__add_message(f"{name}:: {message}", valuation)


# Extension for reporting exceptions
class ReportingConnectionError(enna.core.reporting.exceptions.ReportingException):
	"""Exception raise if a connection to is not possible"""
