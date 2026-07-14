# -*- coding: utf-8 -*-
"""Created on 02.08.2023.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
"""
import datetime
import logging
import pathlib

import enna.core.config
import jinja2

from enna_kwd_testing import ROOT_PATH
from enna_kwd_testing.utilities.stimulation_factory_generator import dependency_finder

INSTANCE_CONFIG = enna.core.config.get(__name__)

DEPENDENCY_FACTORY_CONFIG = INSTANCE_CONFIG["dependency_factory"]
TESTCASE_FACTORY_CONFIG = INSTANCE_CONFIG["testcase_factory"]


MODULE_LOGGER = logging.getLogger(__name__)


class TestSpecificationException(Exception):
	"""Class raised when a test specification is faulty."""


def generate(
		source_data: list[dict],
		output_path: pathlib.Path = ROOT_PATH / DEPENDENCY_FACTORY_CONFIG["dependency_factory_output_path"],
		template_path: pathlib.Path = ROOT_PATH / DEPENDENCY_FACTORY_CONFIG["dependency_factory_template_path"]
) -> str:
	"""Dynamically generate a dependency factory from type enna.core.testing.interface.StimulationFactory in a new file which is decorated with RequireStimulation decorators for the given testset.

	This is necessary to correctly use the enna component system and enable a testset dynamic component initialization
	The dependency factory is of following format:

	@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
	<ALL_DEPENDENCY_DECORATORS>
	class DependencyFactory(Factory):

		def __init__(self, reporting, *args, **kwargs):
			super().__init__(reporting, *args, **kwargs)  # TODO

	:param pathlib.Path source_data: Source data to extract testcase data from
	:param pathlib.Path output_path: Path to save the generated factory file to.
	:param pathlib.Path template_path: Path to jinja template to generate DependencyFactory from.
	:return: Full qualified path to dependency factory class from sources root
	:rtype: str
	:raises TestSpecificationException: If any automation is missing in test specification

	Test sequence input scheme:

	[
		{
			"testcase_id": "<ID>",
			"level": "<TESTLEVEL>",
			"component": "<COMPONENT>",
			"testcase_name": "<TESTCASE_NAME>",
			"testcase_description": "<TESTCASE_DESCRIPTION>",
			"precondition": [
				{
					"step": 1,
					"name": "TEST1",
					"relation": "==",
					"automation": "kdt.keywords_as_stimulations.functions.test.AdbTest",
					"values": {
						"state": 1
					}
				}
			]
		"action": [
			{
				"step": 1,
				"name": "ACTION1",
				"relation": "==",
				"automation": "kdt.keywords_as_stimulations.functions.actions.AndroidHmiTest",
				"values": {
					"text": "Hey Audi"
				}
			}
		]
		"expected_result": [
			{
				"step": 1,
				"name": "EXPECTED_RESULT1",
				"relation": "==",
				"automation": "kdt.keywords_as_stimulations.functions.expected_results.RsiTest",
				"values": {
					"state": "listening"
				}
			},
		]
		"postcondition": [],
		"state": "<TEST_SPECIFICATION_REVIEW_STATE>",
		"author": "<AUTHOR_NAME>",
		"comment": "-",
		"created": "<TEST_SPECIFICATION_CREATED_TIMESTAMP>",
		"last_updated": "<TEST_SPECIFICATION_LAST_UPDATED_TIMESTAMP>",
		"archive_state": <ARCHIVE_STATE>,
		"created_by": "<CREATOR_NAME>",
		"updated_by": "<UPDATER_NAME>"
		}
	]
	"""
	MODULE_LOGGER.debug(f"Count of testcases from folder: {len(source_data)}")
	template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path.parent), keep_trailing_newline=True)
	template = template_env.get_template(template_path.name)

	keywords = dependency_finder.find_keywords_from_testset(source_data)
	dependency_decorators = []
	automations = []
	for keyword in keywords:
		if keyword["automation"] in {"None", None, "", "n.a.", "n.A.", "N.A."}:
			MODULE_LOGGER.error(f"The automation for keyword {keyword} is not available.")
			continue
			# raise TestSpecificationException("The test specification is not correct. The automation for keyword {keyword} is not available.")

		dependency_decorators.append(f"@enna.core.component_system.decorators.RequireStimulation(\"{keyword['automation']}\", arg_name=\"{keyword['automation']}\")")
		automations.append(keyword["automation"])

	dependency_decorators = list(set(dependency_decorators))
	automations = list(set(automations))
	dependency_decorators.sort()

	generated = template.render(
		dependency_decorators=dependency_decorators,
		dependency_amount=len(dependency_decorators),
		current_date=datetime.datetime.now(),
		automations=automations,
		dependency_factory_name=DEPENDENCY_FACTORY_CONFIG["dependency_factory_class_name"],
		testcase_factory_module=TESTCASE_FACTORY_CONFIG["testcase_factory_full_qualified_module_name"],
		testcase_factory_class_name=TESTCASE_FACTORY_CONFIG["testcase_factory_class_name"]
	)
	output_path.write_text(generated, encoding="utf-8")

	full_qualified_output_path = output_path.relative_to(ROOT_PATH).as_posix().replace("/", ".").removesuffix(".py")
	full_qualified_output_class_name = f"{str(full_qualified_output_path)}.{DEPENDENCY_FACTORY_CONFIG['dependency_factory_class_name']}"
	return full_qualified_output_class_name


if __name__ == "__main__":
	# SOURCE_FILE = ROOT_PATH / "enna_kwd_testing/campaigns/json_input/dummy_testsequence.json"
	# TEMPLATE_FILE = ROOT_PATH / "enna_kwd_testing/utilities/stimulation_factory_generator/templates/template.jinja"
	# DEPENDENCY_FACTORY_PATH = ROOT_PATH / "enna_kwd_testing/factories/generated_dependency_factory.py"

	# generate(SOURCE_FILE, DEPENDENCY_FACTORY_PATH, TEMPLATE_FILE)
	pass
