# -*- coding: utf-8 -*-
"""Contains class to handle data from .json files."""

import json
import os


class JsonLoader:
	"""Class containing functionality to load data from json file."""

	def __init__(self, path_to_json_data):
		"""Initialize adb commands loader object.

		Initialize object and load the adb commands json file to storage.

		:param Path path_to_json_data: Path to .json file.
		"""
		self.__path = os.path.dirname(__file__)
		with open(os.path.join(self.__path, str(path_to_json_data)), encoding="utf-8") as self.__json_file:
			self.__data = json.load(self.__json_file)
			self.__json_file.close()

	def get_value(self, element) -> str:
		"""Resolve values by recursive call and replacing placeholders in json by correct xpath.

		:param str element: to get values for (json key)
		:return: Complete, resolved value
		:rtype: str
		"""
		return self.__data[element]
