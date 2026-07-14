# -*- coding: utf-8 -*-
"""Created on 08.02.2024.

@project: enna_kwd_testing.
@author: SPLATZP: PASCAL PLATZER.

Contains stimulations for keyword driven testing in context of adb ambient light.
"""
import logging
from pathlib import Path

import enna.core.component_system.decorators
import enna.core.image_processing.helper
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from PIL import Image

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
from enna_kwd_testing.definitions import RESOURCES_PATH
from enna_kwd_testing.utilities.image_helper.helper import get_most_common_color

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckAmbientlightInSystem(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to check ambient light."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.__android_hmi = android_hmi
		self._mask = (1267, 770, 1367, 800)
		self._path_to_img_source = Path(f"{RESOURCES_PATH}\\ambient_light\\img")

	def _action(self) -> bool:
		"""Execute action.

		Check ambient light in system.

		:return: True if successful, False if exception occurs
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		str_color_name = self.values.get("COLOUR", "")

		self.__android_hmi.connect()
		frame = self.__android_hmi.take_screenshot()
		enna.core.image_processing.helper.save_image(frame, path=self._path_to_img_source, file_extension=".png")
		image = Image.open(f"{self._path_to_img_source}.png")
		str__color_from_device = get_most_common_color(image, self._mask)

		if not str_color_name == str__color_from_device:
			self._reporting.add_report_message_system_error(f"The visible Color is {str__color_from_device} and not {str_color_name}")
			return False

		self._reporting.add_report_message_pass(f"The ambient light color is {str__color_from_device}")

		return True
