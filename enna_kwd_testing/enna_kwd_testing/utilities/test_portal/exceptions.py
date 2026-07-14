# -*- coding: utf-8 -*-
"""Module contains all exceptions for this module."""

import enna.core.exceptions


class PortalBaseException(enna.core.exceptions.ENNAException):
	"""Base Exception for all errors in Test Portal issues."""

class PortalConnectionError(PortalBaseException):
	"""Raise if an error by connection to Test Portal."""

class PortalMockNotFound(PortalBaseException):
	"""Raise if mock not found in vehicle."""
