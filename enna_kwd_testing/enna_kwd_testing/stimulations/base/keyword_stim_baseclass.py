# -*- coding: utf-8 -*-
"""Created on 04.08.2023.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.

Contains the abstract base class for a keyword.
"""
import abc
import logging

import enna.core.interfaces.testing
import enna.core.reporting.interface

import enna_kwd_testing.stimulations.base.exceptions
from enna_kwd_testing.core.logging import colors

MODULE_LOGGER = logging.getLogger(__name__)


class KeywordStimulation(enna.core.interfaces.testing.Stimulation, metaclass=abc.ABCMeta):
	"""Class containing basic behavior and attributes for a keyword in enna keyword driven testing context."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, based_on_kwd_spec_version = "default"):
		"""Initialize keyword object.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param str based_on_kwd_spec_version: Version of psw internal keyword specification the stimulation is based on.
		"""
		super().__init__(reporting=reporting)
		self._values: None | dict = None
		self.allowed_parameter_keys = []
		self._based_on_kwd_spec_version = based_on_kwd_spec_version

	def start(self) -> bool:
		"""Overwrite enna.core.interfaces.testing.Stimulation.start method to add functionality for reporting metadata of stimulation.

		:return: Merged result of stimulation. True if everything worked as expected, False otherwise
		:rtype: bool
		"""
		MODULE_LOGGER.info("EXECUTION INFO:" + colors.GREY)
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__.__name__}'")
		MODULE_LOGGER.info(f"KEYWORD MODULE: '{self.__module__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'" + colors.RESET)
		try:
			if super().start():
				MODULE_LOGGER.info("RESULT:" + colors.GREEN)
				MODULE_LOGGER.info(f"{self.__class__.__name__} | SUCCESSFULL" + colors.RESET)
				return True
		# pylint: disable=broad-except
		except Exception as exc:
			MODULE_LOGGER.error(f"Unhandled excption in {self.__class__.__name__} | {str(exc)}")
			MODULE_LOGGER.info("RESULT:" + colors.BOLD_RED)
			MODULE_LOGGER.info(f"{self.__class__.__name__} | FAILED" + colors.RESET)
			return False
		MODULE_LOGGER.info("RESULT:" + colors.BOLD_RED)
		MODULE_LOGGER.info(f"{self.__class__.__name__} | FAILED" + colors.RESET)
		return False

	@property
	def values(self) -> None | dict:
		"""Getter for property which contains the parameters for the given keyword stimulation.

		:return: Parameter values for given keyword simulation
		:rtype: None | dict
		"""
		return self._values

	@values.setter
	def values(self, value: dict):
		"""Setter for property which contains the parameters for the given keyword stimulation.

		If the field self.allowed_parameter_keys is not empty, then the given parameter keys have to be included in the _allowed_parameter_keys field as string.
		This is to ensure, that a key error is raised when the keyword is not capable of handling the given key from the test specification.
		E.g.:

		Given dict:
		{
			"state": True,
			"inpute_text": "This is my text"
		}
		Allowed keys:
		1. self.allowed_parameter_keys = []
			-> All input is accepted
		2. self.allowed_parameter_keys = ["state", "input_text"]
			-> Correct, both given keys are included in the self.allowed_parameter_keys list
		3. self.allowed_parameter_keys = ["state"]
			-> KeyError - The parameter key "input_text" is not included in the self.allowed_parameter_keys list

		:param dict value: Contains the parameters which should be proceeded within the keyword execution
		:raise enna_kwd_testing.stimulations.base.exceptions.ParameterNameError: If self.allowed_parameter_keys is not empty and any of the given keys from value parameter is not included in self.allowed_parameter_keys
		"""
		key_insensitive_items = {}
		for key, parameter_value in value.items():
			key_insensitive_items.update({key.lower(): parameter_value})
			key_insensitive_items.update({key.upper(): parameter_value})
		for key in key_insensitive_items:
			if (key not in [a.upper() for a in self.allowed_parameter_keys]) and (key not in [a.lower() for a in self.allowed_parameter_keys]) and self.allowed_parameter_keys:
				msg = f"Parameter '{key}' is not allowed in stimulation {self.__class__}!"
				MODULE_LOGGER.exception(msg)
				raise enna_kwd_testing.stimulations.base.exceptions.ParameterNameError(msg)
		self._values = key_insensitive_items

	@property
	def based_on_kwd_spec_version(self) -> str:
		"""Getter for property which contains keyword specification version which the stimulation is based on.

		:return: Version of the keyword specification on which the implemented stimulation is based.
		:rtype: str
		"""
		return self._based_on_kwd_spec_version
