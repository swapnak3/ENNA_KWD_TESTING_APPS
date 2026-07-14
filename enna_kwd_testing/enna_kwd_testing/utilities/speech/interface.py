# -*- coding: utf-8 -*-
"""Module contains a abstract interface to speech handling."""

import abc

import enna.core.component_system.decorators
import enna.core.interfaces
import enna.core.interfaces.component


@enna.core.component_system.decorators.GenerateProxy()
class Interface(enna.core.interfaces.component.Component):
	"""Abstract Interface to a speech to text and text to speech."""

	def __init__(self):
		"""Initialize interface."""
		self._current_phrase = enna.core.interfaces.Data("")
		self._all_phrases = enna.core.interfaces.Data("")

	@abc.abstractmethod
	def start_listening(self):
		"""Start listing at microphone. Start thread to recognize speech."""

	@abc.abstractmethod
	def stop_listening(self, timeout=10) -> str:
		"""Stop listing at microphone.

		:param float timeout: time out to end listing in seconds
		:return: all recognized phrases
		:rtype: str
		"""

	@abc.abstractmethod
	def speak(self, text: str):
		"""Speak a text. Output via sound card.

		:param str text: Text output to speak
		"""

	@abc.abstractmethod
	def driver_speak(self, text: str) -> None:
		"""Driver speak a text. Output via sound card on left channel.

		:param str text: Text output to speak
		"""

	@abc.abstractmethod
	def co_driver_speak(self, text: str) -> None:
		"""Co-Driver speak a text. Output via sound card on right channel.

		:param str text: Text output to speak
		"""

	@property
	def current_phrase(self):
		"""Get current recognized speech phrase.

		:return: Current recognized phrase
		:rtype: enna.core.interfaces.Data
		"""
		return self._current_phrase

	@property
	def all_phrases(self):
		"""Get all recognized speech phrases.

		:return: All recognized phrases
		:rtype: enna.core.interfaces.Data
		"""
		return self._all_phrases
