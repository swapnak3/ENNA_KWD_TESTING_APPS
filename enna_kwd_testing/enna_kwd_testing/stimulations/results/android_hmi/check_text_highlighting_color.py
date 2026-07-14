# -*- coding: utf-8 -*-
"""Created on 26.04.2024

@project: enna_kwd_testing.
@author: SPLATZP: Platzer Pascal.

Contains stimulations for keyword driven testing in context of text highlighting.
"""

import logging
from pathlib import Path

import enna.core.component_system.decorators
import enna.core.image_processing.helper
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from PIL import Image

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.definitions import RESOURCES_PATH
from enna_kwd_testing.utilities.image_helper.helper import replace_rgb_colors_from_image
from enna_kwd_testing.utilities.text_comparison.helper import get_text

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=too-many-locals, too-many-branches

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckTextHighLightingColor(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to Verifies the highlighting of Text."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__android_hmi = android_hmi
		self._path_to_img_source = Path(f"{RESOURCES_PATH}\\text_highlighting\\highlighting.png")

	def _action(self) -> bool:
		"""Execute action.

		Check the highlighting of Text.

		1. Check the text is highlighted

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		str__language = self.values.get("LANG", "de_DE")
		str__texttool_source = self.values.get("LABEL_SOURCE", "Panorama")

		try:
			list__rgb_color = self.values["LABEL_COLOR"]
		except KeyError as exception:
			self._reporting.add_report_message_system_error(f"Value {exception} not found")
			return False

		try:
			str__label = self.values["LABEL"]
			str__label = get_text(text_id=str__label, language=str__language, texttool_source=str__texttool_source)
			if not str__label:
				str__label = self.values["LABEL"]
		except KeyError as exception:
			str__label = ""
			self._reporting.add_report_message_info(f"Value {exception} not found")

		self.__android_hmi.connect()

		frame = self.__android_hmi.take_screenshot()
		enna.core.image_processing.helper.save_image(frame, path=self._path_to_img_source, file_extension=".png")
		image_data = Image.open(rf"{self._path_to_img_source}")
		replace_rgb_colors_from_image(input_image=image_data, file_path=self._path_to_img_source, rgb_reference=list__rgb_color)
		image_new_check = enna.core.image_processing.helper.load_image_from_file(Path(f"{self._path_to_img_source}"))

		image_text_list_psm_single_block = enna.core.image_processing.helper.get_text(image=image_new_check)
		image_text_list_psm_auto = enna.core.image_processing.helper.get_text(image=image_new_check)
		if str__label in image_text_list_psm_single_block[0] or str__label in image_text_list_psm_auto[0]:
			self._reporting.add_report_message_pass(f"Text {str__label} is highlighted")
			return True

		self._reporting.add_report_message_system_error(f"Text {str__label} is not highlighted")
		return False
