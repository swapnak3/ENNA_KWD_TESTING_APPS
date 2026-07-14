# -*- coding: utf-8 -*-
"""Contains class to handle packages from .json files."""

import json
import os
from pathlib import Path


class PackageLoader:
	"""Class containing functionality to load packages from this file."""

	def __init__(self, package_collection: Path = Path(__file__).parent / "package_collection.json"):
		"""Initialize package loader object.

		Initialize object and load the package json file to storage.

		:param Path package_collection: Path to .json file with contains a collection of packages.
		"""
		self.__path = os.path.dirname(__file__)
		with open(os.path.join(self.__path, str(package_collection)), encoding="utf-8") as self.__json_file:
			self.__data = json.load(self.__json_file)
			self.__json_file.close()

	def get_package(self, element) -> str:
		"""Resolve package by recursive call and replacing placeholders in json by correct xpath.

		:param str element: to get package for (json key)
		:return: Complete, resolved package
		:rtype: str
		"""
		return self.__data[element]
