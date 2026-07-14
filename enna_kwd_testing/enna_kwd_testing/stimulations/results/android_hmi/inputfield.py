# -*- coding: utf-8 -*-
"""Created on 26.10.2023.

@project: enna_kwd_testing.
@author: SPLATZP: Platzer Pascal.

Contains stimulations for keyword driven testing in context of speller enter text.
"""

import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.speller")
class CheckEnteredText(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to Verifies the text of an input field."""

	def __init__(self, reporting, speller, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_kwd_testing.utilities.speller.interface.Interface speller: speller interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__android_hmi = android_hmi
		self._speller = speller

	def _action(self) -> bool:
		"""Execute action.

		Enter text in input field.

		1. Verifies the text of an input field

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		try:
			str_text = self.values["TEXT"]
		except KeyError as exception:
			self._reporting.add_report_message_ta_error(f"Value {exception} not found")
			return False

		editor_text = "//*[@class='android.widget.EditText']"
		if not wrapper_android_hmi.element_exists(android=self.__android_hmi, xpath=editor_text, max_time=7):
			MODULE_LOGGER.error(f"The Element {editor_text} is not shown.")
			return False
		str_text_car = self.__android_hmi.layout.value.xpath(editor_text)[0].attrib["text"]

		if str_text_car != str_text:
			MODULE_LOGGER.error(f"The Text {str_text} is not shown in the input field. The shown text is {str_text_car}")
			return False

		MODULE_LOGGER.info(f"The Text {str_text} is shown in the input field ")

		return True
