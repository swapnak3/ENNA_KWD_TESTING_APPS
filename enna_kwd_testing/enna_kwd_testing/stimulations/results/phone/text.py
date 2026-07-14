# -*- coding: utf-8 -*-
"""Created on 27.05.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.

Contains KWD-Keyword 'CHECK_ELEMENT_TEXT_ON_PHONE'
"""

import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.exceptions

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.phone.interface import Interface
from enna_kwd_testing.utilities.phone.myaudi.frontend.myaudi_xpath_collection import MyAudiXpathLoader
from enna_kwd_testing.utilities.phone.myaudi.resources.localized_texts import LocalizedTexts

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class CheckTextOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check the text of an element on the phone."""

	def __init__(self, reporting, phone: Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["SCREEN_NAME", "XPATH_NAME", "CMS_TEXT_ID"]

	def _action(self) -> bool:
		"""Execute action.

		1. Check if element is visible
		2. Get Text of element
		3. Get Text from CMS-Data
		4. Compare the element Text and the Text from the CMS-Data

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		xpath_collection = MyAudiXpathLoader(self.__phone.get_package_name_long())

		screen_name = self.values["SCREEN_NAME"].lower()
		element = self.values["XPATH_NAME"].lower()
		try:
			element_xpath = xpath_collection.get_xpath(screen_name, element)
		except KeyError:
			self._reporting.add_report_message_ta_error(f"Comparing Text with CMS not possible / Xpath for element '{element}' on screen '{screen_name}' not found")
			return False

		is_visible = self.__phone.element_is_visible(element_xpath)

		if is_visible:
			try:
				element_text = self.__phone.get_element_text(element_xpath)

				cms_text_id = self.values["CMS_TEXT_ID"].lower()
				cms_data = LocalizedTexts(self.__phone.get_app_version())
				try:
					cms_data_text = cms_data.get_text(cms_text_id)
				except KeyError:
					self._reporting.add_report_message_ta_error(f"Comparing Text with CMS not possible / CMS-Text-ID '{cms_text_id}' not found in Resource-File")
					return False

				if element_text == cms_data_text:
					self._reporting.add_report_message_pass(f"Text from Element with xpath '{element_xpath}' matches Text from CMS-Data")
					return True

				self._reporting.add_report_message_ta_error(f"Text from Element with xpath '{element_xpath}' not matches Text from CMS-Data")
				return False

			except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
				self._reporting.add_report_message_ta_error(f"Comparing Text not possible / Element with xpath '{element_xpath}' not found on screen")
				return False

		self._reporting.add_report_message_ta_error(f"Comparing Text not possible / Element with xpath '{element_xpath}' is not visible")
		return False
