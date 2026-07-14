# -*- coding: utf-8 -*-
"""Exceptions that can be thrown by classes in this package."""

import enna.core.exceptions


class ElementNotFound(enna.core.exceptions.ENNAException):
	"""Raise if element not found in xpath collection."""
