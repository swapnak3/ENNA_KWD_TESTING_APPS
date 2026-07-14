# -*- coding: utf-8 -*-
"""Module contains base class for text handling over multiple languages."""
import enna_hcp_configuration.android.xpaths


class NotSupportedLanguageError(Exception):
	"""Raise if language not supported of MMI text."""


class NotTextTypeError(Exception):
	"""Raise if not text type"""


class TextObject:
	"""Class for handling MMI Text in all languages."""

	def __init__(self, **kwargs) -> None:
		"""Instanced a new object for text handling.

		:param kwargs: overhand language code as key and text as value e.g. de_DE="deutsch", en_GB="english", ...
		"""
		self._text_for_all_languages = kwargs
		for key in self._text_for_all_languages:
			self._text_for_all_languages[key]=self._text_for_all_languages[key].replace("%1","")

	def get(self, language: str = enna_hcp_configuration.android.xpaths.LANG) -> str:
		"""Get text in expected language.

		:param language: language code and country code e.g. de_DE
		:return: text
		:raise NotSupportedLanguageError: if language not found
		:raise NotTextTypeError: if text value not a string
		"""
		try:
			text = self._text_for_all_languages[language]
		except KeyError:
			raise NotSupportedLanguageError(f"This '{language}' is not supported! Currently are follow languages supported: {self._text_for_all_languages.keys()}.")
		if not isinstance(text, str):
			raise NotTextTypeError(f"Text value '{text}' is not a string!")
		return text

	def __str__(self) -> str:
		"""Get xpath text property for all languages.

		:return: text expression for all languages
		"""
		expression_parts = []
		for text in self._text_for_all_languages.values():
			# pylint: disable=consider-ternary-expression
			if "'" in text:
				expression_part = f"contains(@text,\"{text}\")" # change quotes if text include single quote
			else:
				expression_part = f"contains(@text,'{text}')"

			if expression_part not in expression_parts: # do not append double texts
				expression_parts.append(expression_part)

		expression = " or ".join(expression_parts)

		return f"[{expression}]"
