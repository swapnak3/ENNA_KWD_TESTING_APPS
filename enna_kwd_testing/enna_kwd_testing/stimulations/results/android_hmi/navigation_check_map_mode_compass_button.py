# -*- coding: utf-8 -*-
"""Created on 13.12.2023.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Claus Teubner.

Contains stimulations for keyword driven testing in context of android_hmi navigation functions.
"""

import logging
import pathlib

import enna.core.component_system.decorators
import enna.core.image_processing.helper
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import launcher as launcher_contexts
from enna_hcp_configuration.android.contexts import navigation as navigation_contexts

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.helper.android_hmi_helper
import enna_kwd_testing.utilities.speller
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.speller")
class CheckMapModeCompassButton(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check map mode in navi.app.
	parameter VALUE: 2D_NORTHWARD | 2D_HEADING_UP | 3D -> default VALUE: '2D_HEADING_UP'
	"""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface, speller):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		:param enna_kwd_testing.utilities.speller.interface.Interface speller: speller interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self._reporting = reporting
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self._speller = speller
		self.allowed_parameter_keys = ["VALUE"]
		self.allowed_parameter_values = ["2D_NORTHWARD", "2D_HEADING_UP", "3D"]
		self.default_parameter_value = "2D_HEADING_UP"
		self.nav_fzg_position_arrow_2d = enna.core.image_processing.helper.load_image_from_file(pathlib.Path(__file__).resolve().parent.parent.parent.parent.joinpath("resources/ref_img", "NaviFzgPositionArrow2D.png"))
		self.nav_fzg_position_arrow_3d = enna.core.image_processing.helper.load_image_from_file(pathlib.Path(__file__).resolve().parent.parent.parent.parent.joinpath("resources/ref_img", "NaviFzgPositionArrow3D.png"))
		self.__list_button_2d = []
		self.__list_button_3d = []

	def _action(self) -> bool:
		"""Execute action.

		check/compare map mode in navi.app.

		1. Navigate to 'navigation.main' screen.
		2. search for car-arrow and position with image processing.

		:return: True, if car-arrow and position compares with Key-VALUE, False if an error occurs in any step.
		:rtype: bool
		"""
		# pylint: disable = too-many-branches
		enna_kwd_testing.utilities.helper.android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)

		if self.values["VALUE"] in self.allowed_parameter_values:
			compass_value_str = self.values["VALUE"]
		elif not self.values["VALUE"]:
			compass_value_str = self.default_parameter_value
		else:
			MODULE_LOGGER.error(f"Wrong parameter: '{self.values}', should be one of -> \nVALUE: '{self.allowed_parameter_values}'")
			return False

		if not wrapper_android_hmi.go_to_screen(navigation_contexts.MAIN, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'NAVI.APP -> MAIN. Something went wrong while navigating to screen.")
			return False
		if not wrapper_android_hmi.wait_for_screen_id(navigation_contexts.MAIN, android=self.__android_hmi, additional_message="wait for screen", max_time=30):
			MODULE_LOGGER.error("Wait for screen-id: 'navigation.MAIN. Something went wrong while waiting for screen-id.")
			return False

		template = self.__android_hmi.take_screenshot()
		self.__list_button_2d = enna.core.image_processing.helper.match_template(image=self.nav_fzg_position_arrow_2d, template=template, min_match=0.60)
		self.__list_button_3d = enna.core.image_processing.helper.match_template(image=self.nav_fzg_position_arrow_3d, template=template, min_match=0.60)

		if len(self.__list_button_2d) == 0 and len(self.__list_button_3d) == 0:
			if not wrapper_android_hmi.go_to_screen(navigation_contexts.MAIN, self._reporting, self.__menu_navigation):
				MODULE_LOGGER.error("Could not go to screen: 'NAVI.APP -> MAIN. Something went wrong while navigating to screen.")
				return False
			if not wrapper_android_hmi.go_to_screen(launcher_contexts.HOME, self._reporting, self.__menu_navigation):
				MODULE_LOGGER.error("Could not go to screen: 'Launcher -> HOME. Something went wrong while navigating to screen.")
				return False
			if not wrapper_android_hmi.wait_for_screen_id(launcher_contexts.HOME, android=self.__android_hmi, additional_message="wait for screen", max_time=30):
				MODULE_LOGGER.error("Wait for screen-id: 'Launcher -> HOME. Something went wrong while waiting for screen-id.")
				return False
			template = self.__android_hmi.take_screenshot()
			self.__list_button_2d = enna.core.image_processing.helper.match_template(image=self.nav_fzg_position_arrow_2d, template=template, min_match=0.80)
			self.__list_button_3d = enna.core.image_processing.helper.match_template(image=self.nav_fzg_position_arrow_3d, template=template, min_match=0.80)
			if len(self.__list_button_2d) == 0 and len(self.__list_button_3d) == 0:
				MODULE_LOGGER.error("No Car-Arrow shown on dashboard map.")
				return False

		compass_map_str = ""
		if len(self.__list_button_3d) > 0 and len(self.__list_button_3d) > len(self.__list_button_2d):
			compass_map_str = "3D"
		elif len(self.__list_button_2d) > 0 and len(self.__list_button_2d) > len(self.__list_button_3d):
			if 530 < self.__list_button_2d[0][1] < 560:
				compass_map_str = "2D_HEADING_UP"
			elif 340 < self.__list_button_2d[0][1] < 360:
				compass_map_str = "2D_NORTHWARD"
		else:
			MODULE_LOGGER.error(f"Error, no Car-Arrow found, but should be {compass_value_str}.")
			return False

		if compass_map_str == compass_value_str:
			MODULE_LOGGER.info(f"Found Car-Arrow: {compass_map_str}, is same with searched {compass_value_str}, success.")
		else:
			MODULE_LOGGER.error(f"Error, found Car-Arrow: {compass_map_str}, but should be {compass_value_str}, it's not the same.")
			return False
		return True
