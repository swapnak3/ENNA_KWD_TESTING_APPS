# -*- coding: utf-8 -*-
"""Created on 19.03.2023.

@project: .
@author: SPLATZP: Pascal Platzer.

Contains helper functions for xpath.
"""
import logging

MODULE_LOGGER = logging.getLogger(__name__)

# pylint: disable=too-many-positional-arguments
def create_xpath(element_type, label="", xpath_name="", xpath_extension="", xpath_collection="", screen_name="") -> bool | str:
	"""Generate XPath based on the element type.

	:param str element_type: The type of element.
	:param str label: The label entry element.
	:param str xpath_name: The xpath_name or description of the element.
	:param str xpath_extension: The name or description of the xpath extension.
	:param str screen_name: The name or description of the screen.
	:param object xpath_collection: Xpath loader object.

	:return: The generated Xpath.
	:rtype: bool | str.
	:raise ValueError: when element was not found in xpath action.
	"""

	xpath_action = {
		"ICON": icon_xpath,
		"TEXT": text_xpath,
		"BUTTON": button_xpath
	}

	try:
		if element_type not in xpath_action:
			MODULE_LOGGER.error(f"Element with xpath: {element_type} did not appear.")
			return False
		return xpath_action[element_type](label=label, xpath_name=xpath_name, xpath_extension=xpath_extension, xpath_collection=xpath_collection, screen_name=screen_name)
	except ValueError as e:
		MODULE_LOGGER.error(f"{e}.")
		return False


def icon_xpath(label="", xpath_name="", xpath_extension="", xpath_collection="", screen_name="") -> bool | str:
	"""Generate XPath based on the element type icon.

		:param str label: The label entry element.
		:param str xpath_name: The name or description of the element.
		:param str xpath_extension: The name or description of the xpath extension.
		:param str screen_name: The name or description of the screen.
		:param object xpath_collection: Xpath loader object.

		:return: The generated Xpath.
		:rtype: bool | str.
	"""

	if xpath_name != "" and label == "" and xpath_extension == "":
		try:
			str__icon_xpath = xpath_collection.get_xpath(screen_name, xpath_name)
			return str__icon_xpath
		except KeyError as exception:
			MODULE_LOGGER.error(f"Xpath Key '{exception}' not found in section {screen_name} of {xpath_collection.get_filepath()}.")
			return False
	if xpath_name != "" and label != "" and xpath_extension != "":
		try:
			str__label = f"//*[contains(@text, '{label}')]"
			str__icon_xpath = xpath_collection.get_xpath(screen_name, xpath_name)
			str__xpath_extension = xpath_collection.get_xpath(screen_name, xpath_extension)
			str__icon_xpath_to_click = f"{str__label}/ancestor::*{str__xpath_extension}[1]{str__icon_xpath}"
			return str__icon_xpath_to_click
		except KeyError as exception:
			MODULE_LOGGER.error(f"Xpath Key '{exception}' not found in section {screen_name} of {xpath_collection.get_filepath()}.")
			return False
	if xpath_name != "" and label == "" and xpath_extension != "":
		try:
			str__xpath_extension = xpath_collection.get_xpath(screen_name, xpath_name)
			str__icon_xpath = xpath_collection.get_xpath(screen_name, xpath_extension)
			str__icon_xpath_to_click = f"{str__xpath_extension}{str__icon_xpath.replace('//*', '')}"
			return str__icon_xpath_to_click
		except KeyError as exception:
			MODULE_LOGGER.error(f"Xpath Key '{exception}' not found in section {screen_name} of {xpath_collection.get_filepath()}.")
			return False

	return False


def text_xpath(xpath_name="", xpath_extension="", label="", xpath_collection="", screen_name="") -> bool | str:
	"""Generate XPath based on the element type text.

		:param str xpath_name: The name or description of the element.
		:param str xpath_extension: The name or description of the xpath extension.
		:param str label: The label entry element.
		:param str screen_name: The name or description of the screen.
		:param dobject xpath_collection: Xpath loader object.
		:returns: The generated Xpath.
		:rtype:  bool | str
	"""
	try:
		if label == "" and xpath_name != "":
			str__text_xpath = xpath_collection.get_xpath(screen_name, xpath_name)
			return str__text_xpath
	except KeyError as exception:
		MODULE_LOGGER.error(f"Xpath Key '{exception}' not found in section {screen_name} of {xpath_collection.get_filepath()}.")
		return False

	try:
		if label != "" and xpath_name == "":
			str__label = f"//*[contains(@text, '{label}')]"
			str__text_xpath = f"{str__label}"
			return str__text_xpath
	except KeyError as exception:
		MODULE_LOGGER.error(f"Xpath Key '{exception}' not found in section {screen_name} of {xpath_collection.get_filepath()}.")
		return False

	try:
		if label != "" and xpath_name != "":
			str__text_xpath = xpath_collection.get_xpath(screen_name, xpath_name)
			str__label_xpath = f"{str__text_xpath}[contains(@text, '{label}')]"
			str__text_xpath = f"{str__label_xpath}"
			return str__text_xpath
	except KeyError as exception:
		MODULE_LOGGER.error(f"Xpath Key '{exception}' not found in section {screen_name} of {xpath_collection.get_filepath()}.")
		return False

	try:
		if label != "" and xpath_name != "" and xpath_extension != "":
			str__label_xpath = f"[contains(@text, '{label}')]"
			str__xpath_name = xpath_collection.get_xpath(screen_name, xpath_name)
			str__xpath_extension = xpath_collection.get_xpath(screen_name, xpath_extension)
			str__text_xpath = f"{str__xpath_name}/ancestor::*{str__xpath_extension}[1]{str__label_xpath}"
			return str__text_xpath
	except KeyError as exception:
		MODULE_LOGGER.error(f"Xpath Key '{exception}' not found in section {screen_name} of {xpath_collection.get_filepath()}.")
		return False

	return False


def button_xpath(xpath_name="", xpath_extension="", label="", xpath_collection="", screen_name="") -> bool | str:
	"""Generate XPath based on the element type button.

		:param str xpath_name: The name or description of the element.
		:param str xpath_extension: The name or description of the xpath extension.
		:param str label: The label or text entry element.
		:param str screen_name: The name or description of the screen.
		:param dobject xpath_collection: Xpath loader object.

		:return: The generated Xpath.
		:rtype: bool | str.
		"""
	if xpath_name != "" and label == "":
		try:
			str__button_xpath = xpath_collection.get_xpath(screen_name, xpath_name)
			return str__button_xpath
		except KeyError as exception:
			MODULE_LOGGER.error(f"Xpath Key '{exception}' not found in section {screen_name} of {xpath_collection.get_filepath()}.")
			return False

	if xpath_name != "" and label != "" and xpath_extension != "":
		try:
			str__label = f"//*[contains(@text, '{label}')]"
			str__xpath_button = xpath_collection.get_xpath(screen_name, xpath_name)
			str__xpath_extension = xpath_collection.get_xpath(screen_name, xpath_extension)
			str__button_xpath_to_click = f"{str__label}/ancestor::*{str__xpath_extension.replace('//*', '')}[1]{str__xpath_button}"
			return str__button_xpath_to_click
		except KeyError as exception:
			MODULE_LOGGER.error(f"Xpath Key '{exception}' not found in section {screen_name} of {xpath_collection.get_filepath()}.")
			return False
	if xpath_name != "" and label == "" and xpath_extension != "":
		try:
			str__xpath_extension = xpath_collection.get_xpath(screen_name, xpath_name)
			str__xpath_button = xpath_collection.get_xpath(screen_name, xpath_extension)
			str__button_xpath_to_click = f"{str__xpath_extension}{str__xpath_button.replace('//*', '')}"
			return str__button_xpath_to_click
		except KeyError as exception:
			MODULE_LOGGER.error(f"Xpath Key '{exception}' not found in section {screen_name} of {xpath_collection.get_filepath()}.")
			return False

	return False
