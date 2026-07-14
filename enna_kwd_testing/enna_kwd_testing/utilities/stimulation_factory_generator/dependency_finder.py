# -*- coding: utf-8 -*-
"""Created on 02.08.2023.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.

Contains function to find dependencies for given set of stimulations.
"""
import logging

MODULE_LOGGER = logging.getLogger(__name__)


def find_keywords_from_testset(testset: list[dict]) -> list[dict]:
	"""Extract all keywords from the given testset.

	:param dict testset: Testset to extract the keywords to execute from
	:return: List of keywords which shall be executed in the given testset
	:rtype: list[dict]
	"""
	keywords = []

	for testcase in testset:
		try:
			preconditions_from_testcase = [precondition for precondition in testcase["precondition"] if precondition["name"] not in {"", None}]
			MODULE_LOGGER.debug(preconditions_from_testcase)
		except KeyError:
			MODULE_LOGGER.debug("No preconditions specified.")
			preconditions_from_testcase = []

		actions_from_testcase = [action for action in testcase["action"] if action["name"] not in {"", None}]
		expected_results_from_testcase = [expected_result for expected_result in testcase["expectedresult"] if expected_result["name"] not in {"", None}]

		try:
			postconditions_from_testcase = [postcondition for postcondition in testcase["postcondition"] if postcondition["name"] not in {"", None}]
			MODULE_LOGGER.debug(postconditions_from_testcase)
		except KeyError:
			MODULE_LOGGER.debug("No postconditions specified.")
			postconditions_from_testcase = []

		keywords += preconditions_from_testcase + actions_from_testcase + expected_results_from_testcase + postconditions_from_testcase
	return keywords
