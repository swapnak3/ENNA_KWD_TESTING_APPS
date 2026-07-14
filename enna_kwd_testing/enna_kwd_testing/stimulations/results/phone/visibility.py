# -*- coding: utf-8 -*-
"""Created on 27.05.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.

Contains KWD-Keyword 'CHECK_ELEMENT_IS_VISIBLE_ON_PHONE'
Contains KWD-Keyword 'CHECK_ELEMENT_IS_NOT_VISIBLE_ON_PHONE'
Contains KWD-Keyword 'CHECK_ELEMENT_IS_ENABLED_ON_PHONE'
Contains KWD-Keyword 'CHECK_ELEMENT_IS_SELECTED_ON_PHONE'
Contains KWD-Keyword 'CHECK_ELEMENT_IS_CHECKED_ON_PHONE'
"""
import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.interface
import enna_st12
import enna_st12.data_interfaces.android_hmi.exceptions

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.phone.interface import Interface
from enna_kwd_testing.utilities.phone.myaudi.frontend.myaudi_xpath_collection import MyAudiXpathLoader

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class CheckElementIsVisibleOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check if element is visible"""

	def __init__(self, reporting, phone: Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["SCREEN_NAME", "XPATH_NAME"]

	def _action(self) -> bool:
		"""Execute action.

		1. Check if element is visible

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		xpath_collection = MyAudiXpathLoader(self.__phone.get_package_name_long())

		screen_name = self.values["SCREEN_NAME"].lower()
		element = self.values["XPATH_NAME"].lower()
		try:
			element_xpath = xpath_collection.get_xpath(screen_name, element)
		except KeyError:
			self._reporting.add_report_message_ta_error(f"Check if element is visible not possible / Xpath for element '{element}' on screen '{screen_name}' not found")
			return False

		visible = self.__phone.element_is_visible(element_xpath)

		if visible:
			self._reporting.add_report_message_pass(f"Element with xpath '{element_xpath}' is visible on screen")
			return True

		self._reporting.add_report_message_ta_error(f"Element with xpath '{element_xpath}' is not visible on screen")
		return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class CheckElementIsNotVisibleOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check if element is not visible"""

	def __init__(self, reporting, phone: Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["SCREEN_NAME", "XPATH_NAME"]

	def _action(self) -> bool:
		"""Execute action.

		1. Check if element is not visible

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		xpath_collection = MyAudiXpathLoader(self.__phone.get_package_name_long())

		screen_name = self.values["SCREEN_NAME"].lower()
		element = self.values["XPATH_NAME"].lower()
		try:
			element_xpath = xpath_collection.get_xpath(screen_name, element)
		except KeyError:
			self._reporting.add_report_message_ta_error(f"Check if element is not visible not possible / Xpath for element '{element}' on screen '{screen_name}' not found")
			return False

		visible = self.__phone.element_is_visible(element_xpath)

		if not visible:
			self._reporting.add_report_message_pass(f"Element with xpath '{element_xpath}' is not visible on screen")
			return True

		self._reporting.add_report_message_ta_error(f"Element with xpath '{element_xpath}' is visible on screen")
		return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class CheckElementIsEnabledOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check if element is enabled"""

	def __init__(self, reporting, phone: Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["SCREEN_NAME", "XPATH_NAME"]

	def _action(self) -> bool:
		"""Execute action.

		1. Check if element is enabled

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		xpath_collection = MyAudiXpathLoader(self.__phone.get_package_name_long())

		screen_name = self.values["SCREEN_NAME"].lower()
		element = self.values["XPATH_NAME"].lower()
		try:
			element_xpath = xpath_collection.get_xpath(screen_name, element)
		except KeyError:
			self._reporting.add_report_message_ta_error(f"Check if element is enabled not possible / Xpath for element '{element}' on screen '{screen_name}' not found")
			return False

		try:
			enabled = self.__phone.element_is_enabled(element_xpath)

			if enabled:
				self._reporting.add_report_message_pass(f"Element with xpath '{element_xpath}' is enabled")
				return True

			self._reporting.add_report_message_ta_error(f"Element with xpath '{element_xpath}' is not enabled")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			self._reporting.add_report_message_ta_error(f"Check if element is enabled not possible / Element with xpath '{element_xpath}' is not visible on screen")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class CheckElementIsSelectedOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check if element is selected"""

	def __init__(self, reporting, phone: Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["SCREEN_NAME", "XPATH_NAME"]

	def _action(self) -> bool:
		"""Execute action.

		1. Check if element is selected

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		xpath_collection = MyAudiXpathLoader(self.__phone.get_package_name_long())

		screen_name = self.values["SCREEN_NAME"].lower()
		element = self.values["XPATH_NAME"].lower()
		try:
			element_xpath = xpath_collection.get_xpath(screen_name, element)
		except KeyError:
			self._reporting.add_report_message_ta_error(f"Check if element is selected not possible / Xpath for element '{element}' on screen '{screen_name}' not found")
			return False

		try:
			selected = self.__phone.element_is_selected(element_xpath)

			if selected:
				self._reporting.add_report_message_pass(f"Element with xpath '{element_xpath}' is selected")
				return True

			self._reporting.add_report_message_ta_error(f"Element with xpath '{element_xpath}' is not selected")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			self._reporting.add_report_message_ta_error(f"Check if element is selected not possible / Element with xpath '{element_xpath}' is not visible on screen")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class CheckElementIsCheckedOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check if element is checked"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["SCREEN_NAME", "XPATH_NAME"]

	def _action(self) -> bool:
		"""Execute action.

		1. Check if element is checked

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		xpath_collection = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="myaudi")

		screen_name = self.values["SCREEN_NAME"].lower()
		element = self.values["XPATH_NAME"].lower()
		try:
			element_xpath = xpath_collection.get_xpath(screen_name, element)
		except KeyError:
			self._reporting.add_report_message_ta_error(f"Check if element is checked not possible / Xpath for element '{element}' on screen '{screen_name}' not found")
			return False

		try:
			checked = self.__phone.element_is_checked(element_xpath)

			if checked:
				self._reporting.add_report_message_pass(f"Element with xpath '{element_xpath}' is checked")
				return True

			self._reporting.add_report_message_ta_error(f"Element with xpath '{element_xpath}' is not checked")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			self._reporting.add_report_message_ta_error(f"Check if element is checked not possible / Element with xpath '{element_xpath}' is not visible")
			return False
