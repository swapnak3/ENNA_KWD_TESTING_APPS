# -*- coding: utf-8 -*-
"""Module contains base stimulation for touching and checking methods on android hmi system."""
import enum
import logging
import importlib

import enna.core.config
import enna.core.exceptions
import enna.core.reporting.interface

import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.data_interfaces.android_hmi.helper
import enna_st12.utilities.menu_navigation.exceptions
import enna_st12.utilities.menu_navigation.interface

import enna_hcp_configuration.common.base
import enna_hcp_configuration.android.contexts
import enna_hcp_configuration.android.xpaths
import enna_hcp_configuration.android.contexts.launcher

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
import enna_kwd_testing.utilities.xpath_collection.exceptions
from enna_kwd_testing.utilities.text_tool.helper import get_text_from_configuration, AvailableSources


MODULE_LOGGER = logging.getLogger(__name__)

class ElementTypes(enum.StrEnum):
	"""Constants of element types"""
	BUTTON = "BUTTON"
	ICON = "ICON"
	TEXT = "TEXT"
	NOT_SET = "not set"


class BaseMenuNavigation:
	"""Base class of menu navigation. Contains methods for get destination context and go to screen"""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of base class for menu navigation.

		:param reporting: instance of report handler
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		:param android_hmi: instance of android hmi control interface
		"""
		self._reporting = reporting
		self._menu_navigation = menu_navigation
		self._android_hmi = android_hmi


	def _get_destination_context(self, screen_name: str) -> enna_hcp_configuration.common.base.Element:
		"""Get context of destination by screen name.

		:param screen_name: screen name of destination e.g. 'settings.main'
		:return: context of destination
		:raise enna_st12.utilities.menu_navigation.exceptions.MenuNavigationException: if screen name not found in enna_hcp_configuration
		"""
		try:
			app, screen  =screen_name.split(".")
			destination = getattr(getattr(enna_hcp_configuration.android.contexts, app.lower()), screen.upper())
		except (AttributeError, ValueError) as error:
			msg = f"Screen '{screen_name}' not exist in ENNA_HCP_CONFIGURATION! Error: {error}"
			MODULE_LOGGER.exception(msg)
			self._reporting.add_report_message_ta_error(msg)
			raise enna_st12.utilities.menu_navigation.exceptions.MenuNavigationException(msg)
		return destination

	def _go_to_screen(self, destination: enna_hcp_configuration.common.base.Element) -> bool:
		"""	Navigate to destination.

		:param destination: destination menu
		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			self._android_hmi.wait_for_event("layout", condition=lambda msg: self._android_hmi.layout.value.xpath(enna_hcp_configuration.android.xpaths.APP_LIST_BUTTON.get()), max_time=30.0)
			self._menu_navigation.go_to_screen(destination, max_retries=5)
		except (enna_st12.utilities.menu_navigation.exceptions.MenuNavigationException, enna.core.exceptions.TimeoutException) as error:
			err_msg = f"Error while navigating to the screen: {destination.name}. Error: {error}"
			self._reporting.add_report_message_ta_error(err_msg)
			return False
		self._reporting.add_report_message_pass(f"Successfully navigate to screen {destination}")
		return True


class BaseOfUsageElement(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Base class for usage an android hmi element."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of base class for usage.

		:param reporting: instance of report handler
		:param android_hmi: instance of android hmi control interface
		"""
		super().__init__(reporting=reporting)
		self._android_hmi = android_hmi
		# ELEMENT PARAMETER is deprecated and will be removed
		self.allowed_parameter_keys = ["ELEMENT", "LABEL", "XPATH_NAME", "XPATH_PARENT", "XPATH_EXTENSION", "LABEL_SOURCE", "LANG", "TIMEOUT", "LIST_CONTAINER", "LABEL_LIST"]
		self._xpath = ""
		self._timeout: float = 1.0
		self._screen_name: str = ""
		self.__list_container: str = ""

	def _precondition(self) -> bool:
		"""Generate xpath by parameter from test specification.

		:return: True if success, else False
		"""
		xpath_name = self.values.get("XPATH_NAME", "")
		label = self.values.get("LABEL", "") # will ignore if 'xpath_name' exist
		label_list = self.values.get("LABEL_LIST", None) # will ignore if 'xpath_name' or 'label' exist

		xpath_parent = self.values.get("XPATH_PARENT", "")
		xpath_extension = self.values.get("XPATH_EXTENSION", "")
		language = self.values.get("LANG", enna.core.config.INFOTAINMENT_SYSTEM.system_language.value)

		self.__list_container = self.values.get("LIST_CONTAINER", "")  # xpath name of list container
		self._timeout = self.values.get("TIMEOUT", self._timeout)

		try:
			self._android_hmi.wait_for_event("screen_id", condition=lambda msg: self._android_hmi.screen_id.value != "", max_time=10.0)
			self._screen_name = self._android_hmi.screen_id.value
			self._xpath = self._get_xpath_by_parameters(label=label, xpath_name=xpath_name, screen_name=self._screen_name, xpath_parent=xpath_parent, xpath_extension=xpath_extension, language=language, label_list=label_list)
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_ta_error(f"Error by instance of android hmi interface! {error}")
			return False
		except enna.core.exceptions.ConfigurationException as error:
			self._reporting.add_report_message_ta_error(f"Error by parameters from specification! {error}")
			return False
		except enna.core.exceptions.TimeoutException as error:
			self._reporting.add_report_message_ta_error(f"Could not reading screen id! {error}")
		return True

	# pylint: disable=line-too-long, too-many-positional-arguments
	def _get_xpath_by_parameters(self, label: str = "", xpath_name: str = "", xpath_parent: str = "", xpath_extension: str = "", screen_name: str = "", display: str = AvailableSources.CENTER,
	                             language: str = enna.core.config.INFOTAINMENT_SYSTEM.system_language.value, label_list: list[str] | None = None) -> str:
		"""Get a xpath by parameters from test specification.

		:param label: label of text
		:param xpath_name: name of a xpath from xpath collections
		:param xpath_parent:
		:param xpath_extension:
		:param screen_name: name of current screen.
		:param display: name of display. Possible 'center' or 'passenger'. Default is center 'display'
		:param language: language code for search texts
		:param label_list: list of labels
		:return: xpath for this parameter
		:raises enna.core.exceptions.ConfigurationException: if error with parameters
		"""
		xpath = "//unknown"
		# returns xpath from xpath collection if a xpath_name set. In this case the element type doesn't care.
		if xpath_name:
			try:
				app, screen = screen_name.split(".")
			except ValueError:
				app = screen = "unknown"
			xpath = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app=app).get_xpath(screen=screen, element=xpath_name)
		# returns a xpath which search a text if element type equal text.
		elif label:
			xpath = f"//*[contains(@text,'{get_text_from_configuration(text_id=label, source=display, language=language)}') or contains(@content-desc,'{label.lower()}')]"
		elif isinstance(label_list,list):
			text_list="".join([get_text_from_configuration(text_id=text, source=display, language=language) for text in label_list])
			xpath = f"//*[contains(@text, '{text_list}')]"

		# add a xpath parent (to delete)
		if xpath_parent:
			MODULE_LOGGER.warning("Parameter \"XPATH_PARENT\" is deprecated! Please don't use it longer.")
			xpath = f"//*[@text='{xpath_parent}' or @content-desc='{xpath_parent}' or @resource-id='{xpath_parent}']/.{xpath}"

		# add a xpath extension (to delete)
		if xpath_extension:
			MODULE_LOGGER.warning("Parameter \"XPATH_EXTENSION\" is deprecated! Please don't use it longer.")
			xpath = f"{xpath}//*[@text='{xpath_extension}' or @content-desc='{xpath_extension}' or @resource-id='{xpath_extension}']"

		return xpath

	def _get_list_container(self) -> str:
		"""Return xpath of list container for current screen.
		Default return xpath '//*[@scrollable="true"]'

		:return: xpath of list container for current screen
		"""
		try:
			# usage own define List containe
			if self.__list_container:
				return enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="mind your business").get_xpath(screen="mind your business", element=self.__list_container)
			# usage List Container from current app
			app_name = self._android_hmi.screen_id.value.split(".")[0]
			module = importlib.import_module(f"enna_hcp_configuration.android.xpaths.{app_name}")
			return getattr(module, "LIST_CONTAINER").get()

		except (ImportError, AttributeError, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException, enna_kwd_testing.utilities.xpath_collection.exceptions.ElementNotFound) as error:
			MODULE_LOGGER.warning(f"No List container fond for app: {error}")
			return '//*[@scrollable="true"]'


class CheckSwitchButtonInScreen(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, BaseMenuNavigation):
	"""Base class to check switch button"""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		BaseMenuNavigation.__init__(self, reporting=reporting, menu_navigation=menu_navigation, android_hmi=android_hmi)
		self._android_hmi = android_hmi
		self._screen: enna_hcp_configuration.common.base.Element = enna_hcp_configuration.android.contexts.launcher.APP_LIST
		self._button: enna_hcp_configuration.android.xpaths.XpathString = enna_hcp_configuration.android.xpaths.UNDEFINED
		self._list_container: enna_hcp_configuration.android.xpaths.XpathString = enna_hcp_configuration.android.xpaths.UNDEFINED
		self._expected_state: bool = True
		self.allowed_parameter_keys = ["STATE"]

	def _precondition(self) -> bool:
		"""Navigate to screen which contains switch button and set switch button to expected state.

		:return: True if successful, False if an error occurs in any step.
		"""
		self._expected_state = self.values.get("STATE", self._expected_state)
		if not self._go_to_screen(self._screen):
			return False
		try:
			if self._list_container!=enna_hcp_configuration.android.xpaths.UNDEFINED:
				self._android_hmi.wait_for_element_visible(self._list_container.get(), max_time=3.0)
				self._android_hmi.scroll_to_element_in_list(list_container_xpath=self._list_container.get(), target_xpath=self._button.get())
		except enna.core.exceptions.TimeoutException as error:
			self._reporting.add_report_message_ta_error(f"List Container '{self._list_container}' did not appear on screen '{self._screen.name}' before timeout! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_ta_error(f"HMI error! {error}")
			return False
		return True

	def _action(self) -> bool:
		""" Relax

		:return: True if successful, False if an error occurs in any step.
		"""
		return True

	def _postcondition(self) -> bool:
		""" Check if current state equals expected state.

		:return: True if successful, False if an error occurs in any step.
		"""
		try:
			self._android_hmi.wait_for_element_visible(f"{self._button.get()}[@checked='{str(self._expected_state).lower()}']", max_time=5.0)
		except enna.core.exceptions.TimeoutException as error:
			self._reporting.add_report_message_system_error(f"State of switch button '{self._button}' is not equal expected State! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_ta_error(f"UI-Automator error! {error}")
			return False
		self._reporting.add_report_message_pass(f"State of switch button '{self._button}' is {self._expected_state}")
		return True

class SetSwitchButtonInScreen(CheckSwitchButtonInScreen):
	"""Base class to set switch button"""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, menu_navigation=menu_navigation, android_hmi=android_hmi)

	def _action(self) -> bool:
		"""Navigate to screen which contains switch button and set switch button to expected state.

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			self._android_hmi.wait_for_element_visible(self._button.get(), max_time=3.0)
			self._android_hmi.set_toggle_button_state(xpath=self._button.get(), button_state=self._expected_state)
		except enna.core.exceptions.TimeoutException as error:
			self._reporting.add_report_message_ta_error(f"Button '{self._button}' did not appear on screen '{self._screen.name}' before timeout! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_ta_error(f"HMI error! {error}")
			return False
		return True
