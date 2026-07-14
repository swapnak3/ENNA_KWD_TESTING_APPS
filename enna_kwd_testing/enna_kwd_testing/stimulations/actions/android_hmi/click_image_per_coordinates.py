# -*- coding: utf-8 -*-
"""Created on 26.06.2024.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Claus Teubner.

Contains stimulations for keyword driven testing in context of android_hmi sds settings functions.
"""

import logging
from pathlib import Path

import enna.core.component_system.decorators
import enna.core.image_processing.helper
import enna.core.time
import enna_st12.data_interfaces.android_hmi.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
from enna_kwd_testing.definitions import RESOURCES_PATH

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class ClickImagePerCoordinates(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to recognize position of a picture and click on it."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__android_hmi = android_hmi
		self.allowed_parameter_keys = ["KEY"]
		self._mask = (435, 440, 1790, 816)
		self._path_to_img_source = Path(f"{RESOURCES_PATH}\\keyboard")
		self._allowed_parameter_values = ["a", "b", "Keyboard_down", "Lupe", "OK"]
	def _action(self) -> bool:
		"""Execute action.

		recognize image 'Lupe.png' on screen, press on coordinates from picture position.

		:return: True if successful, False if exception occurs
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		str_filename = self.values.get("KEY", "Lupe")
		if str_filename in self._allowed_parameter_values:
			key_image = enna.core.image_processing.helper.load_image_from_file(Path(f"{self._path_to_img_source}\\{str_filename}.png"))
		else:
			MODULE_LOGGER.error(msg=f"Value '{str_filename}' not defined.\nOnly this values for 'KEY' are allowed: '{self._allowed_parameter_values}")
			return False

		enna.core.time.sleep(1)
		img_screencapture = self.__android_hmi.take_screenshot()
		pos_found = enna.core.image_processing.helper.match_template(image=img_screencapture, template=key_image, min_match=0.90)
		if len(pos_found) >= 1:
			self.__android_hmi.click_coordinates(x_coord=int(pos_found[0][0]), y_coord=int(pos_found[0][1]))
		else:
			MODULE_LOGGER.error(msg=f"Value '{str_filename}' not found.")
			return False

		return True
