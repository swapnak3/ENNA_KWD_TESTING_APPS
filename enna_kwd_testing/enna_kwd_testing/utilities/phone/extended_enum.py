# -*- coding: utf-8 -*-
"""Created on xx.xx.2024.

@project: .
@author: vj28hsm: Kevin Brych.

Contains extended enumeration class
"""

from enum import Enum


class ExtendedEnum(Enum):
	"""Extended enumeration"""

	@classmethod
	def has_name(cls, name):
		"""Check if a Name is available inside an enumeration
		:param str name: name to search
		:return: True/False if name is available
		:rtype: bool
		"""
		# pylint: disable=no-member
		return name in cls._member_names_

	@classmethod
	def has_value(cls, value):
		"""Check if a Value is available inside an enumeration
		:param str value: value to search
		:return: True/False if value is available
		:rtype: bool
		"""
		return value in cls._value2member_map_
