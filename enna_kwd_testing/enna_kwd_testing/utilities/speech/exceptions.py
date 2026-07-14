# -*- coding: utf-8 -*-
"""Exceptions that can be thrown by classes in this package."""

import enna.core.exceptions


class SpeechError(enna.core.exceptions.ENNAException):
	"""Base Exception class for package Speech."""


class RecognitionRequestError(SpeechError):
	"""Raise if a error by a request for recognition for a speech."""


class SpeechInputError(SpeechError):
	"""Raise if a error by use listener."""


class SpeechOutputError(SpeechError):
	"""Raise if a error by speech output."""
