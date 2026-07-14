# -*- coding: utf-8 -*-
"""Created on 26.06.2024.
   refactor on 14.05.2024.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Claus Teubner.

Contains stimulations for keyword driven testing in context of android_hmi sds settings functions.
"""

import logging
from pathlib import Path

import enna.core.component_system.decorators
import enna.core.config
import enna.core.exceptions
import enna.core.image_processing.helper
import enna.core.time
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.data_interfaces.android_hmi.helper
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.instance_names

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.text_tool.helper
import enna_kwd_testing.utilities.xpath_collection.exceptions
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.definitions import RESOURCES_PATH

MODULE_LOGGER = logging.getLogger(__name__)
MODULE_CONFIG = enna.core.config.get(__name__)

# pylint: disable=too-many-branches

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class ClickOnImage(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Stimulation to recognize position of a picture in keyboard and click on it."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self._android_hmi = android_hmi
		self.allowed_parameter_keys = ["KEY", "MIN_MATCH", "ROI", "ROI_XPATH"]
		self._path_to_img_source = Path(f"{RESOURCES_PATH}\\keyboard")
		self._allowed_parameter_values = ["a", "b", "Keyboard_down", "Lupe", "OK"]
		self._templates: Path = Path(__file__).parent.joinpath("templates")

	def _action(self) -> bool:
		"""Execute action.

		recognize image 'Lupe.png' on screen, press on coordinates from picture position.

		:return: True if successful, False if exception occurs
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		template_name = self.values.get("KEY", "Lupe")
		min_match = self.values.get("MIN_MATCH", 0.95)
		# roi = self.values.get("ROI", [435, 440, 1790, 816]) if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43 else self.values.get("ROI", [435, 430, 2190, 790])
		if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43:
			roi = self.values.get("ROI", [435, 440, 1790, 816])
		elif enna.core.config.INFOTAINMENT_SYSTEM.cluster in {46,48}:
			roi = self.values.get("ROI", [435, 430, 2190, 790])
		elif enna.core.config.INFOTAINMENT_SYSTEM.cluster in {53,55}:
			roi = self.values.get("ROI", [120, 427, 1900, 795])
		else:
			roi = self.values.get("ROI", [0, 0, 2190, 795])

		if template_name in self._allowed_parameter_values:
			template_path = self._templates.joinpath(f"CLU{enna.core.config.INFOTAINMENT_SYSTEM.cluster}/obb_keyboard/{template_name}.png")
			if not template_path.exists():
				self._reporting.add_report_message_ta_error(f"Template '{template_name}' not found! in Path: '{template_path}'!")
				return False
			template = enna.core.image_processing.helper.load_image_from_file(template_path)
		else:
			MODULE_LOGGER.error(msg=f"Value '{template_name}' not defined.\nOnly this values for 'KEY' are allowed: '{self._allowed_parameter_values}")
			return False

		if "ROI" in self.values:
			roi = self.values["ROI"]
			if len(roi) != 4:
				self._reporting.add_report_message_ta_error(f"Region of interest need 4 integers! roi = {roi}")
				return False
		elif "ROI_XPATH" in self.values:
			try:
				xpath = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self._android_hmi, element=self.values["ROI_XPATH"])
				coordinates_size = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(layout=self._android_hmi.layout.value, xpath=xpath)
				roi = [coordinates_size["x"], coordinates_size["y"], coordinates_size["x"] + coordinates_size["width"], coordinates_size["y"] + coordinates_size["height"]]
			except (enna_kwd_testing.utilities.xpath_collection.exceptions.ElementNotFound, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as error:
				self._reporting.add_report_message_ta_error(f"Region of interest could not be set by xpath! {error}")
				return False
		self._reporting.add_report_message_info(f"Search KEY '{template_name}' in ROI '{roi}' from '{template_path}'.")

		enna.core.time.sleep(1)
		try:
			img_screencapture = self._android_hmi.take_screenshot().get_roi(mask=roi) if isinstance(roi, list) else self._android_hmi.take_screenshot()
			matches = enna.core.image_processing.helper.match_template(image=img_screencapture, template=template, min_match=min_match)
		except enna.core.exceptions.ImageProcessingException as error:
			self._reporting.add_report_message_ta_error(f"Error by template matching! {error}")
			return False
		if len(matches) == 1:
			self._reporting.add_report_message_pass(f"Click on coordinate: '{str(int(matches[0][0]) + roi[0])}', '{str(int(matches[0][1]) + roi[1])}'.")
			self._android_hmi.click_coordinates(x_coord=int(matches[0][0]) + roi[0], y_coord=int(matches[0][1]) + roi[1])
			self._reporting.add_report_message_pass(f"Template '{template_name}' found in image on position x={int(matches[0][0]) + roi[0]}, y={int(matches[0][1]) + roi[1]}.")
			return True
		if len(matches) > 1:
			self._reporting.add_report_message_system_error(f"Template '{template_name}' found in image on some positions {matches} plus offset {roi[0]}, {roi[1]}!")
			return False
		self._reporting.add_report_message_system_error(f"Template '{template_name}' not found in image!")
		return False
