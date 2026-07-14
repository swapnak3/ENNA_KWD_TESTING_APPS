# -*- coding: utf-8 -*-
"""Exceptions that can be thrown by classes in this package."""

import enna.core.exceptions


class DisplayTouchError(enna.core.exceptions.ENNAException):
	"""Base Exception Class for this package"""


class DisplayTouchConnectionError(DisplayTouchError):
	"""Raise if connection error to hardware for display touch."""


class DisplayTouchEventError(DisplayTouchError):
	"""Raise if error by a touch event."""
