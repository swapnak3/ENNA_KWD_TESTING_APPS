# -*- coding: utf-8 -*-
"""Created on 27.05.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.

Contains KWD-Keyword 'CHECK_IMAGE_IS_VISIBLE_ON_ELEMENT_ON_PHONE'
Contains KWD-Keyword 'CHECK_IMAGE_IS_VISIBLE_ON_SCREEN_ON_PHONE'
"""

import logging
from pathlib import Path

import enna.core.component_system.decorators
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.exceptions

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.phone.exceptions
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.definitions import RESOURCES_PATH
from enna_kwd_testing.utilities.phone import interface
from enna_kwd_testing.utilities.phone.myaudi.frontend.myaudi_xpath_collection import MyAudiXpathLoader

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ImageIsVisibleOnElementOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class contains functionality to check if an image is visible on an element"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["SCREEN_NAME", "XPATH_NAME", "IMAGE_TEMPLATE"]

	def _action(self) -> bool:
		"""Execute action.

		1. Check if image is visible on element

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		xpath_collection = MyAudiXpathLoader(self.__phone.get_package_name_long())

		screen_name = self.values["SCREEN_NAME"].lower()
		element = self.values["XPATH_NAME"].lower()
		try:
			element_xpath = xpath_collection.get_xpath(screen_name, element)
		except KeyError:
			self._reporting.add_report_message_ta_error(f"Image-Template Check not possible / Xpath for element '{element}' on screen '{screen_name}' not found")
			return False

		template_image_path = RESOURCES_PATH / "template_data/" / self.values["IMAGE_TEMPLATE"].lower()

		try:
			visible = self.__phone.image_is_visible_on_element(element_xpath, template_image_path)

			if visible:
				self._reporting.add_report_message_pass(f"Image-Template was found on Element with xpath '{element_xpath}'")
				return True
			else:
				self._reporting.add_report_message_ta_error(f"Image-Template was not found on Element with xpath '{element_xpath}'")
				return False
		except enna_kwd_testing.utilities.phone.exceptions.FileNotFoundException as exc:
			self._reporting.add_report_message_ta_error(f"{exc}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			self._reporting.add_report_message_ta_error(f"Image-Template Check not possible / Element with xpath '{element_xpath}' not found on screen")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ImageIsVisibleOnScreenOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class contains functionality to check if an image is visible on a screen"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["IMAGE_TEMPLATE"]

	def _action(self) -> bool:
		"""Execute action.

		1. Check if image is visible on screen

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""

		template_image_path = RESOURCES_PATH / "template_data/" / self.values["IMAGE_TEMPLATE"].lower()

		try:
			visible = self.__phone.image_is_visible_on_screen(template_image_path)

			if visible:
				self._reporting.add_report_message_pass(f"Image-Template was found on screen")
				return True
			else:
				self._reporting.add_report_message_ta_error(f"Image-Template was not found on screen")
				return False
		except enna_kwd_testing.utilities.phone.exceptions.FileNotFoundException as exc:
			self._reporting.add_report_message_ta_error(f"{exc}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			self._reporting.add_report_message_ta_error(f"Image-Template Check not possible")
			return False
