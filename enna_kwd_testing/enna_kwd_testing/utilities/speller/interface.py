# -*- coding: utf-8 -*-
"""Module for destination input."""

import abc

import enna.core.component_system.decorators
import enna.core.interfaces.component


@enna.core.component_system.decorators.GenerateProxy()
class Interface(enna.core.interfaces.component.Component):
	"""speller for text input using ime fast input."""

	def __init__(self):
		"""Initialize an Interface object for speller."""

	@abc.abstractmethod
	def enter_text(self, text="text", clear=True):
		"""Input destination in search area.

		:param bool clear: If True, clear input field before entering text
		:param str text: the text to search
		:raises enna_tc_hmi_hcp3.utilities.speller.exceptions.SpellerException: if during address input any exception occurs
		:return: execution result True or false and time stamp, when the address was entered
		:rtype: tuple(bool, str)

		"""

	@abc.abstractmethod
	def delete_text(self, key: str = "global_search", item: str = "clearTextButton"):
		"""Clear text in search area.

		:param key: key from xpath_collection for screen
		:param item: item from xpath_collection for clearTextButton
		:raises enna_tc_hmi_hcp3.utilities.speller.exceptions.SpellerException: if during address input any exception occurs
		:return: Result of operation
		:rtype: bool

		"""

	@abc.abstractmethod
	def activate_keyboard(self):
		"""Deactivate FastInputIME for android.
		Deactivating FastInputIME activates the visible keyboard.
		:return: True if successful
		:rtype: bool
		:raises enna_tc_connect_apps_hcp3.utilities.speller.exceptions.SpellerException: If FastInputIME can´t be disabled.
		"""
