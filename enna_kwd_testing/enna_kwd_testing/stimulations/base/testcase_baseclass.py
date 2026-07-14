# -*- coding: utf-8 -*-
"""Created on 23.06.2023.

@project: enna_kwd_testing.
@author: DYX34ZN:  Jakob Kein.

Contains the baseclass for a generic testcase for keyword driven testing
"""
import logging
import pathlib

import enna.core.config
import enna.core.interfaces.testing
import enna.core.reporting.interface
import enna.data_interfaces.adb.interface
import enna.data_interfaces.adb.exceptions

import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.data_interfaces.android_hmi.helper


from enna_kwd_testing.utilities.rsi.helper import recreate_buffered_rsi_element


MODULE_LOGGER = logging.getLogger(__name__)
save_path = pathlib.Path(enna.core.config.get(__name__).get("save_path", "ui_layout"))


# pylint: disable=line-too-long, too-many-positional-arguments
class StimulationBase(enna.core.interfaces.testing.Stimulation):
	"""Stimulation frame for stimulation processes in context of keyword driven testing."""

	def __init__(self, test_ids: enna.core.interfaces.testing.TestCaseSpecification | None =None, reporting: enna.core.reporting.interface.Interface | None =None, adb: enna.data_interfaces.adb.interface.Interface | None = None , android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface | None = None, preconditions: list[dict] | None = None, teststeps: list[dict] | None = None, postconditions: list[dict] | None = None, initialized_keyword_objects: dict | None = None) -> None:
		"""Initialize stimulation object.

		:param test_ids: Test specification object for testcase
		:param reporting: Instance of reporting interface
		:param adb: Instance of interface to Android Debug Bridge
		:param android_hmi: Instance of uiautomator
		:param preconditions: Preconditions of testcase as list of tuples (combining function and parameters)
		:param teststeps: teststeps of testcase as a list of dictionaries containing "action" and "results" as keys for one teststep
		:param postconditions: Postconditions of testcase as list of tuples (combining function and parameters)
		:param initialized_keyword_objects: objects for keywords execution
		"""
		super().__init__(reporting)
		self.initialized_keyword_stims = initialized_keyword_objects
		self.precondition_workflow = [] if preconditions is None else preconditions
		self.teststeps = [] if teststeps is None else teststeps
		self.postcondition_workflow = [] if postconditions is None else postconditions
		self.test_ids = test_ids
		self.__android_hmi = android_hmi
		self.__adb = adb

	def _precondition(self) -> bool:
		"""Execute generic precondition for keyword driven stimulation.

		Start the speech listener during preconditions due to timing issues at interface start up.

		:return: True if successful, False otherwise
		:rtype: bool
		"""
		self._reporting.attach_meta_data_to_test_case({"TESTING_LANGUAGE": enna.core.config.INFOTAINMENT_SYSTEM.system_language.value})
		self._reporting.add_report_message_info(f"Testing language is '{enna.core.config.INFOTAINMENT_SYSTEM.system_language.value}'.")
		executed_preconditions = {}
		for precondition in self.precondition_workflow:
			precondition_stim = self.initialized_keyword_stims[precondition["automation"]]
			setattr(precondition_stim, "values", precondition["values"])
			MODULE_LOGGER.info(f"Executing precondition step {precondition['step']} with name: {precondition['name']} mapped to function: {precondition['automation']} with parameters: {precondition['values']}")
			result = precondition_stim.start()
			executed_preconditions.update({precondition["name"]: result})
			if not result:
				self._append_test_ids_not_tested(self.test_ids, "Testcase skipped due to failing precondition")
				self.__make_screen_shot_of_test_case()
				return False
		return True

	def _action(self) -> bool:
		"""Execute generic action for keyword driven stimulation.

		:return: True if successful, False otherwise
		:rtype: bool
		"""
		executed_expected_results = {}
		executed_actions = {}

		for _, teststep in enumerate(self.teststeps, start=1):
			action = teststep["action"]
			action_automation = action["automation"]

			action_stim = self.initialized_keyword_stims[action_automation]
			setattr(action_stim, "values", action["values"])
			MODULE_LOGGER.info(f"Executing action step {action['step']} with name: {action['name']} mapped to function: {action['automation']} with parameters: {action['values']}")
			expected_result = action_stim.start()
			executed_actions.update({action["name"]: expected_result})
			if not executed_actions[action["name"]]:
				self._append_test_ids_ta_error(self.test_ids, f"An error occurred in test case {action['step']} at action: {action['name']}. Stopping testcase.")
				self.__make_screen_shot_of_test_case()
				return False

			for expected_result in teststep["results"]:
				expected_result_automation = expected_result["automation"]
				expected_result_stim = self.initialized_keyword_stims[expected_result_automation]
				setattr(expected_result_stim, "values", expected_result["values"])
				MODULE_LOGGER.info(f"Executing expected_result step {expected_result['step']} with name: {expected_result['name']} mapped to function: {expected_result['automation']} with parameters: {expected_result['values']}")
				result = expected_result_stim.start()
				executed_expected_results.update({expected_result["name"]: result})

		if self.__adb is not None:
			try:
				current_language: str = self.__adb.execute_shell_command(command="getprop persist.sys.locale", timeout=5.0, stream=False)
				if current_language.replace("-", "_") != enna.core.config.INFOTAINMENT_SYSTEM.system_language.value:
					self._reporting.add_report_message_ta_error(self.test_ids, f"Test Case executed with wrong language! Expected language is '{enna.core.config.INFOTAINMENT_SYSTEM.system_language.value}'. Current language is '{current_language}'.")
					executed_expected_results.update({"Checking System Language": False})
			except Exception: # pylint: disable=broad-exception-caught
				self._reporting.add_report_message_warning("Checking system language could not executed!")

		if all(executed_expected_results.values()):
			self._append_test_ids_pass(self.test_ids, "All 'expected results' PASSED -> Testcase passed.")
			return True
		for test, expected_result in executed_expected_results.items():
			if not expected_result:
				self._append_test_ids_system_error(self.test_ids, f"The testcase failed in expected result validation: {test}")

		self.__make_screen_shot_of_test_case()
		return False

	def _postcondition(self) -> bool:
		"""Execute generic postcondition for keyword driven stimulation.

		:return: True if successful, False otherwise
		:rtype: bool
		"""
		result_collector = []
		if self.__android_hmi is not None:
			try:
				self.__android_hmi.connect()
			except Exception as error: # pylint: disable=broad-exception-caught
				MODULE_LOGGER.error(f"Reconnect android hmi is failed! In Test Case {self.test_ids.id}. {error}")
		try:
			recreate_buffered_rsi_element()
		except Exception as error: # pylint: disable=broad-exception-caught
			MODULE_LOGGER.error(f"Not re-create RSI elnments! {error}")

		for postcondition in self.postcondition_workflow:
			postcondition_stim = self.initialized_keyword_stims[postcondition["automation"]]
			setattr(postcondition_stim, "values", postcondition["values"])
			MODULE_LOGGER.info(f"Executing postcondition step {postcondition['step']} with name: {postcondition['name']} mapped to function: {postcondition['automation']} with parameters: {postcondition['values']}")
			if not (result := postcondition_stim.start()):
				self._reporting.add_report_message_warning(f"An error occurred on postcondition - step: {postcondition['step']}: {postcondition['name']}")
			result_collector.append(result)

		if all(result_collector):
			return True
		return False

	def __make_screen_shot_of_test_case(self) -> None:
		"""Take a screenshot and save under path of test case."""
		if self.__android_hmi is not None:
			try:
				enna_st12.data_interfaces.android_hmi.helper.save_ui_layout(self.__android_hmi.layout, self.__android_hmi.take_screenshot(), name="error", path=save_path.joinpath(self.test_ids.id))
			except Exception as error: # pylint: disable=broad-exception-caught
				MODULE_LOGGER.debug(f"Could not take screenshot for Test Case! {error}")
