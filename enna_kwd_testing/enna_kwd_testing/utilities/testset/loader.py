# -*- coding: utf-8 -*-
"""Created on 20.10.2023.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.


"""

import json
import logging
import os
from pathlib import Path
import enna_kwd_testing.definitions


MODULE_LOGGER = logging.getLogger(__name__)


def load_testset_from_files(testset_folder: Path | str, testset_file: bool = False, testset_file_name: str = "testset.json") -> list[dict]:
	"""Load a specific testset from a connected drive or folder from file.

	If a testset_file in testset_folder is specified and flag testset_file is True, only the testcases specified in the file are loaded.
	Otherwise, all testcases in the given testset_folder are loaded

	(If available) testset_file format:

	[testid_1, testid_2, testid_3]

	:param testset_folder: folder where load testset file from.
	:type testset_folder: pathlib.Path | str
	:param testset_file: flag to indicate if a testset file is available in testset_folder to load testcases from
	:type testset_file: bool
	:param testset_file_name: name of testset file to load
	:type testset_file_name: str
	:return: List of dictionaries which contain testcase data
	:rtype: list[dict]
	"""
	testcase_list = []
	if testset_file:
		testset_file = Path(testset_folder) / testset_file_name

		with testset_file.open(mode="r", encoding="utf-8") as testset:
			test_set_list = json.load(testset)

		for testcase_id in test_set_list:
			testcase_file = Path(testset_folder) / f"{testcase_id}.json"
			with testcase_file.open(mode="r", encoding="utf-8") as testcase:
				testcase_data = json.load(testcase)
			testcase_list.append(testcase_data)

	else:
		MODULE_LOGGER.info("Found testcase files")
		for testcase_file in os.listdir(testset_folder):
			MODULE_LOGGER.info(testcase_file)
			if testcase_file == "metadata.json":
				testcase_file = Path(testset_folder) / testcase_file
				with testcase_file.open(mode="r", encoding="utf-8") as meta_data:
					enna_kwd_testing.definitions.META_DATA = json.load(meta_data)
				continue
			if not testcase_file.endswith(".json"):
				continue
			testcase_file = Path(testset_folder) / testcase_file
			with testcase_file.open(mode="r", encoding="utf-8") as testcase:
				testcase_data = json.load(testcase)
			testcase_list.append(testcase_data)

	return testcase_list
