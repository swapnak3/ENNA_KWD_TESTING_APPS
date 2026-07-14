# -*- coding: utf-8 -*-
"""Module contains help function to using xpath collection.

@author: GLM0UBU: Björn König
@author: VDGA3GV: amn: Andreas Ampferl.

"""
import importlib
import logging
import re

import enna.core.config
import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna_st12.data_interfaces.android_hmi.interface

import enna_hcp_configuration.android.xpaths

import enna_kwd_testing.utilities.xpath_collection.exceptions


MODULE_LOGGER = logging.getLogger(__name__)

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class XpathHandler:
	"""Handler for xpath from collection."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, app: str = "launcher") -> None:
		"""Constructor of xpath handler. Loading xpath's which relevant for app.

		:param reporting: instance of reporting interface
		:param app: name of app
		"""
		self._reporting = reporting
		self._app_name = app
		self._default_data: dict = enna.core.config.get_system_specific_mapping(__name__, subfolder_name="data", file_key="default")
		self._data: dict = enna.core.config.get_system_specific_mapping(__name__, subfolder_name="data", file_key=app)

	def get_xpath(self, screen: str, element: str) -> str:
		"""Get xpath of current app with screen name and element name.

		:param screen: name of screen
		:param element: name of element
		:raise enna_kwd_testing.utilities.xpath_collection.exceptions.ElementNotFound: if element not found
		:return: xpath of searched element
		"""
		try:
			if "." in element:
				module = importlib.import_module(f"enna_hcp_configuration.android.xpaths.{element.split(".")[0].lower()}")
				xpath: enna_hcp_configuration.android.xpaths.XpathString = getattr(module, element.split(".")[1].upper())
			else:
				module = importlib.import_module("enna_hcp_configuration.android.xpaths")
				xpath: enna_hcp_configuration.android.xpaths.XpathString = getattr(module, element.upper())
			return xpath.get()

		except (ImportError, AttributeError) as error:
			msg = f"Xpath '{element}' not found in ENNA_HCP_CONFIGURATION! {error}"
			MODULE_LOGGER.warning(msg)
			self._reporting.add_report_message_warning(msg)

		# deprecated implementation
		screen = screen.lower()
		element = element.lower()
		try:
			xpath = self._data[screen][element]
			MODULE_LOGGER.debug(f"Element '{element}' find in app: '{self._app_name}' -> screen: '{screen}'.")
		except KeyError:
			if element in self._default_data:
				xpath = self._default_data[element]
				MODULE_LOGGER.debug(f"Element '{element}' find in 'default'.")
			else:
				try:
					xpath_element = getattr(enna_hcp_configuration.android.xpaths, element.upper())
					xpath = xpath_element.get()
					MODULE_LOGGER.debug(f"Element '{element}' find in 'enna_hcp_configuration.android.xpaths'.")
				except AttributeError:
					msg = f"Element is not found! Search in app: '{self._app_name}' -> screen: '{screen}' -> element: {element}"
					MODULE_LOGGER.error(msg)
					raise enna_kwd_testing.utilities.xpath_collection.exceptions.ElementNotFound(msg)

		find_link = re.match(r'(?P<element>[{{][\w\W]+[}}])*', xpath)
		if find_link.group("element") is not None:
			replace_element = str(find_link.group("element")).replace("{", "").replace("}", "").split("->")
			return xpath.replace(str(find_link.group("element")), self.get_xpath(replace_element[0], replace_element[-1]))
		return xpath

	@classmethod
	def get_xpath_app_screen_id(cls, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, element: str) -> str:
		"""	Extend get_xpath with automated path/file recognition from screen_id

		:param reporting: instance of reporting interface
		:param str android_hmi: interface of ui-automator connection
		:param str element: element to load xpath for from file space
		:return: resolved xpath
		"""
		MODULE_LOGGER.warning("Method 'get_xpath_app_screen_id' is deprecated! Not longer supported!")
		try:
			app_name, screen_name = android_hmi.screen_id.value.split(".")
		except ValueError:
			app_name = "unknown"
			screen_name = "unknown"

		return cls(reporting=reporting, app=app_name).get_xpath(screen=screen_name, element=element)
