# -*- coding: utf-8 -*-
"""Module contains a helper which write reprot file to PSW database."""
import datetime
import logging
import pathlib
import json
import lxml.etree

from psw_tmdb_connector.items.testresult import TestResult
from psw_tmdb_connector.items.testrun import TestRun
from psw_tmdb_connector.connector.factory import DatabaseConnectorFactory
from psw_tmdb_connector.items.enums import TestresultState, TestautomationState

import enna.core.config

MODULE_LOGGER = logging.getLogger(__name__)


def __result_converter(result: str) -> str:
	"""Convert result from report to TMDB conform result.
	By an unknown result will return result state error.

	:param str result: result from report
	:return: result value for TMDB
	:rtype: str
	"""
	possible_results = {
		"Failed": TestresultState.FAILED.value,
		"Skipped": TestresultState.SKIPPED.value,
		"Passed": TestresultState.PASSED.value,
		"Inconclusive": TestresultState.ERROR.value
	}
	return possible_results.get(result, TestresultState.ERROR.value)


def __check_report_path(path: pathlib.Path) -> pathlib.Path:
	"""Check report path is valid.

	:param pathlib.Path path: path toreport
	:return: path to report
	:rtype: pathlib.Path
	:raises OSError: if path to report not exist
	"""
	if not path.exists():
		msg = f"Path is not exist! Path \"{path}\" could not found in file system."
		MODULE_LOGGER.exception(msg)
		raise OSError(msg)
	return path


def __read_messages(test_case: lxml.etree.Element) -> str:
	"""Read messages and det a summary of Error messages.

	:param lxml.etree.Element test_case: test case element
	:return: summary of errors
	:rtype
	"""
	summary = ""
	try:
		summary = test_case.xpath(".//message")[0].text.split("\n")[0].split("|", 2)[-1]
		print(summary)
	except IndexError:
		MODULE_LOGGER.debug(f"Test Case {test_case.attrib["id"]} has no messages.")
	return summary


def __read_report_file(path_to_report: pathlib.Path) -> list[TestResult, ]:
	"""Reading report file. Read the nunit report file was generated with ENNA-Reporting.

	:param str path_to_report: path to folder from nunit report file
	:return: list of test results
	:rtype:   list[TestResult, ]
	:raises FileNotFoundError: if not found unique report in path
	"""
	list_of_test_results = []
	folder = __check_report_path(path_to_report)

	reports = sorted(folder.glob("*_nunit.xml"))
	if len(reports) != 1:
		msg = f"Report File could not found in {folder}! Search result: {reports}."
		MODULE_LOGGER.exception(msg)
		raise FileNotFoundError(msg)

	report = lxml.etree.fromstring(bytes(reports[0].open().read(), encoding="utf-8"))
	for test_case in report.xpath("//test-case"):
		MODULE_LOGGER.debug(f"Test Case: {test_case.attrib["id"]} result is {test_case.attrib["result"]}")
		list_of_test_results.append(TestResult(
			testcase_id=test_case.attrib["id"],
			ergebnis=__result_converter(test_case.attrib["result"]),
			testdatum=datetime.datetime.now(),
			kommentar=__read_messages(test_case),
			testautomation=TestautomationState.AUTOMATED.value,
			language=enna.core.config.INFOTAINMENT_SYSTEM.system_language.value
		))
	return list_of_test_results


def __read_report_meta_data(path_to_report: pathlib.Path) -> TestRun:
	"""Read report Meta Data from file.

	:param pathlib.Path path_to_report: path to report
	:return: test run data
	:rtype: TestRun
	:raises FileNotFoundError: if not found unique report in path
	"""
	path = __check_report_path(path_to_report)
	file = path.joinpath("report_meta_data.json")
	if not file.exists():
		msg = f"Report Meta Data File could not found! Search {file}."
		MODULE_LOGGER.exception(msg)
		raise FileNotFoundError(msg)
	data = json.loads(file.open().read())
	return TestRun(
		tester=data.get("environment_identifier", "Automation"),
		sw=data.get("software_version", "unknown"),
		hw=data.get("hardware_version", "unknown"),
		testlocation=data.get("environment", ""),
		project=data.get("department", "unknown"),
		vehicle=data.get("vehicle","unknown"),
		train=data.get("cluster", "unknown"),
		testauftrag=data.get("order", "unknown"),
		mainunit="",
		testlocation_id=data.get("environment", ""),
		additional_information=data.get("additional_information", "")
		)


def __write_test_results_to_database(results: list[TestResult,], run: TestRun, login: tuple[str, str, str, str]) -> None:
	"""Write results of report in TMDB database.

	:param results: list of results from report
	:param run: Test Run Data
	:param login: tuple with host_user,host_password,db_user,db_password
	"""
	connector = DatabaseConnectorFactory(connector_type="PSW_TMDB_CONNECTOR_PROD_FROM_PSW_NETWORK", credentials=(login[0], login[1]), login=(login[2], login[3])).get_connector_instance()
	connector.write_item_list_testresult(results, run)


def writing_report_after_run(login: tuple) -> None:
	"""Writing results after execute test run.

	:param tuple login: tuple with host_user,host_password,db_user,db_password
	:raises ValueError: if an unknown value in test run data
	"""
	root_path = pathlib.Path(enna.core.config.MAIN_CONFIG.root_log_dir)
	report_path = root_path
	last_time = 0.0
	for folder in root_path.iterdir():
		if folder.stat().st_mtime > last_time:
			last_time = folder.stat().st_mtime
			report_path = folder

	report_path = report_path.joinpath("report")

	report_results = __read_report_file(report_path)
	report_meta_data = __read_report_meta_data(report_path)
	# check test run data
	for key in report_meta_data.return_dict():
		if str(report_meta_data.return_dict()[key]).upper() == "UNKNOWN":
			msg = f"Not valid value in {key}! Interrupting write results in database."
			MODULE_LOGGER.exception(msg)
			raise ValueError(msg)

	__write_test_results_to_database(report_results, report_meta_data, login)


def copy_html_report_to_path(save_path: pathlib.Path) -> None:
	"""Copy HTML-Report to a save path.

	:param pathlib.Path save_path: path to saving HTML-Report
	"""
	root_path = pathlib.Path(enna.core.config.MAIN_CONFIG.root_log_dir)
	report_path = root_path

	if not report_path.exists():
		MODULE_LOGGER.error(f"Path to report not found! Path='{report_path}'")
	last_time = 0.0
	for folder in root_path.iterdir():
		if folder.stat().st_mtime > last_time:
			last_time = folder.stat().st_mtime
			report_path = folder

	report_path = report_path.joinpath("report")
	reports = sorted(report_path.glob("*.html"))
	if len(reports) != 1:
		msg = f"HTML Report could not found in {report_path}! Search result: {reports}."
		MODULE_LOGGER.error(msg)
		return

	try:
		save_path.mkdir(parents=True, exist_ok=True)
	except OSError:
		MODULE_LOGGER.error(f"Save Path '{save_path}' could not created!")
		return

	save_path.joinpath(f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_HTML_Reporting_Results.html").write_text(reports[0].read_text(encoding="utf-8", errors='ignore'), encoding="utf-8", errors='ignore')
	return
