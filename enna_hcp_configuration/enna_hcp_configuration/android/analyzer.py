# -*- coding: utf-8 -*-
"""The main analyzer which references all others."""
import logging
import pathlib
import importlib

import enna_hcp_configuration.android.contexts
import enna_hcp_configuration.android.xpaths
import enna_hcp_configuration.android.base


MODULE_LOGGER = logging.getLogger(__name__)


class MainAnalyzer:
	"""Container for the main HMI analyzer.

	All other analyzers are registered here.
	"""

	def __init__(self):
		"""Initialize the analyzer."""
		self.__contexts = []

	def clear_contexts(self):
		"""Clear the context container."""
		self.__contexts = []

	def add_context(self, context):
		"""Add context to the MainAnalyzer object.

		:param enna_hcp_configuration.android.base.ContextAnalyzer context: context to add
		"""
		self.__contexts.append(context)

	def detect(self, layout):
		"""Detect screens and popups for the given layout.

		:param lxml.etree.Element layout: the HMI layout to analyze
		:return: screen ID and popup IDs as a tuple
		:rtype: (str, list[str])
		"""
		screen_id = enna_hcp_configuration.android.base.UNKNOWN_SCREEN_ID
		for context in self.__contexts:
			if (detected_screen := context.detect_screen(layout)) is not None:
				screen_id = detected_screen
				break
		popup_ids = []
		for context in self.__contexts:
			popup_ids.extend(context.detect_popups(layout))
		return screen_id, popup_ids


# pylint:disable=unused-argument
def initialize(enna_main_config):
	"""Initialize the android based screen detection.

	This will unregister and re-register all extensions according to the main ENNA config.

	:param dict enna_main_config: the enna main config
	"""
	enna_hcp_configuration.android.xpaths.LANG = enna_main_config.get("system_language", "unknown")
	enna_hcp_configuration.android.xpaths.CLUSTER = f"clu{enna_main_config.get("cluster", "unknown")}"

	ANALYZER.clear_contexts()
	for context in pathlib.Path(__file__).parent.joinpath("contexts").iterdir():
		context = context.name.replace(".py", "")
		if not context.startswith("_") and context != "WAIT_SCREENS":
			ANALYZER.add_context(importlib.import_module(f"enna_hcp_configuration.android.contexts.{context}").CONTEXT)
			MODULE_LOGGER.info(f"Add contexts for '{context}'.")

	MODULE_LOGGER.info(f"Initialization PSW contexts of MMI is success. Cluster = {enna_hcp_configuration.android.xpaths.CLUSTER} and System Language = {enna_hcp_configuration.android.xpaths.LANG}")


ANALYZER = MainAnalyzer()
