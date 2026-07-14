# -*- coding: utf-8 -*-
"""Created on 29.09.2023.

@project: .
@author: SPLATZP: Pascal Platzer.

Contains helper functions for text_comparison, text.
"""
import collections
import html
import logging
import math
import re
from collections import Counter
from typing import Any

from enna_kwd_testing.utilities.text_tool.get_text import get_text_from_texttool_csv

MODULE_LOGGER = logging.getLogger(__name__)

# pylint: disable=too-many-positional-arguments
def get_cosine(vec1: dict, vec2: dict) -> float:
	"""Get cosine.

	:param vec1: vector 1 to get cosine for
	:type vec1: dict
	:param vec2: vector 2 to get cosine for
	:type vec2: dict
	:return: cosine
	:rtype: cosine
	"""
	intersection = set(vec1.keys()) & set(vec2.keys())
	numerator = sum([vec1[x] * vec2[x] for x in intersection])  # pylint: disable = consider-using-generator

	sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])  # pylint: disable = consider-using-generator
	sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])  # pylint: disable = consider-using-generator
	denominator = math.sqrt(sum1) * math.sqrt(sum2)

	if not denominator:
		return 0.0
	return float(numerator) / denominator


def text_to_vector(text: str) -> collections.Counter:
	"""Convert given text to vector.

	:param text: text to get vector for.
	:type text: str
	:return: converted text as vector
	:rtype: collections.Counter
	"""
	word = re.compile(r"\w+")
	words = word.findall(text)
	return Counter(words)


def match_text(text1: str, text2: str) -> float:
	"""Match 2 strings and get matching coverage in percent.

	:param text1: text 1 to match
	:type text1: str
	:param text2: text 2 to match
	:type text2: str
	:return: matching percentage
	:rtype: float
	"""
	vector1 = text_to_vector(text1)
	vector2 = text_to_vector(text2)

	cosine_result = get_cosine(vector1, vector2)
	MODULE_LOGGER.info("Matching texts:")
	MODULE_LOGGER.info(f"Text 1: {text1}")
	MODULE_LOGGER.info(f"Text 2: {text2}")
	MODULE_LOGGER.info(f"Matching Result: {cosine_result}")
	return cosine_result


def text_comparison(android_hmi, xpath_text_car_s: str, comparison_text_s: str = None, text_id: str = None,
					property_values: list = None, language="de_DE", texttool_source: str = "Panorama") -> bool | tuple[bool, str | bytes | Any, str] | tuple[bool, None, str]:
	"""compare text with id or text.

		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: android_hmi interface
		:param xpath_text_car_s: (str) the xpath to find the text in the car (e.g. getxpath("key", "arg"))
		:param property_values: (list) values (e.g. [1,2,3,4])
		:param comparison_text_s: (str) the text to compare
		:param text_id: (str) the text id to compare
		:param texttool_source: (str) the texttool source e.g. AudiApps
		:param str language: (str) the language to compare (e.g. "de_DE")
		:return: text as string
		:rtype: str | bool
		:raises TypeError:
	"""

	try:
		default_text = ""

		if comparison_text_s is not None:
			default_text = comparison_text_s

		if text_id is not None:
			# the .replace("\\n", "\n") is used due to an import error \n from Excel,
			# otherwise the line break would not be displayed
			default_text = get_text_from_texttool_csv(text_id, language_s=language, str_filename=texttool_source).replace("\\n", "\n")

		value_number = 1
		try:
			if property_values is not None:
				for value in property_values:
					default_text = default_text.replace(f"%{value_number}", value)
					value_number += 1
		except ValueError as exception:
			MODULE_LOGGER.exception(exception)
			return False

		android_hmi.wait_for_element_visible(xpath_text_car_s, max_time=7)
		text_car_s = html.unescape(
			android_hmi.layout.value.xpath(xpath_text_car_s)[0].attrib["text"].replace("\u200B", ""))

		if text_car_s != default_text:
			return False, text_car_s, default_text
		return True, None, default_text

	except ValueError as exception:
		MODULE_LOGGER.exception(exception)
		return False


def text_comparison_list(android_hmi, xpath_text_car_s: str, comparison_text_s: str = None,
						 text_id: str = None, language="de_DE", texttool_source: str = "Panorama") -> bool | tuple[bool, list[str | bytes], str | bool] | tuple[
	bool, None, str | bool]:
	"""compare text with id or text in a list of elments.

		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: android_hmi interface
		:param xpath_text_car_s: (str) the xpath to find the text in the car (e.g. getxpath("key", "arg"))
		:param comparison_text_s: (str) the text to compare
		:param text_id: (str) the text id to compare
		:param texttool_source: (str) the texttool source e.g. AudiApps
		:param str language: (str) the language to compare (e.g. "de_DE")
		:return: text as string
		:rtype: str | bool
		:raises TypeError:
	"""

	try:
		default_text = ""
		result_items_list = []

		if comparison_text_s is not None:
			default_text = comparison_text_s

		try:
			if text_id is not None:
				default_text = get_text_from_texttool_csv(text_id, language_s=language, str_filename=texttool_source).replace("\\n", "\n")
		except ValueError as exception:
			MODULE_LOGGER.exception(exception)

		android_hmi.wait_for_element_visible(xpath_text_car_s, max_time=7)
		list_items = android_hmi.layout.value.xpath(xpath_text_car_s)
		for index in enumerate(list_items):
			result_items_list.append(html.unescape(list_items[index[0]].attrib["text"].replace("\u200B", "")))
		if default_text not in result_items_list:
			return False, result_items_list, default_text
		return True, None, default_text

	except ValueError as exception:
		MODULE_LOGGER.exception(exception)
		return False


def get_text(text_id: str = None, property_values: list = None, language="de_DE", texttool_source: str = "Panorama") -> str | bool:
	"""compare text with id or text.
		:param property_values:
		:param text_id: (str) the text id to compare
		:param texttool_source: (str) the texttool source e.g. AudiApps
		:return: default_text
		:param str language: (str) the language to compare (e.g. "de_DE")
		:return: text as string
		:rtype: str | bool
	"""

	try:
		# the .replace("\\n", "\n") is used due to an import error \n from Excel,
		# otherwise the line break would not be displayed
		try:
			default_text = get_text_from_texttool_csv(text_id, language_s=language, str_filename=texttool_source).replace("\\n", "\n")
		except AttributeError as exception:
			MODULE_LOGGER.exception(exception)
			return False

		value_number = 1
		if property_values is not None:
			for value in property_values:
				default_text = default_text.replace(f"%{value_number}", value)
				value_number += 1

		return default_text

	except ValueError as exception:
		MODULE_LOGGER.exception(exception)
		return False
