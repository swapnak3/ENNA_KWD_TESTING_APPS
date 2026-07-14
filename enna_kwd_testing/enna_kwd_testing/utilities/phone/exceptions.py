# -*- coding: utf-8 -*-
"""Exceptions that can be thrown by classes in this package."""

import enna.core.exceptions


class PhoneInterfaceException(enna.core.exceptions.ENNAException):
	"""Base Exception for phone interface."""


class NoDeviceConnectedException(PhoneInterfaceException):
	"""Is raised if no device is connected or device is disconnected."""


class InvalidArgumentException(PhoneInterfaceException):
	"""Is raised if one or more arguments have invalid types or values."""


class ElementNotPresentException(PhoneInterfaceException):
	"""Is raised if an element is not present in the UI layout."""


class ElementNotEnabledException(PhoneInterfaceException):
	"""Is raised if an element is not enabled."""


class FileNotFoundException(PhoneInterfaceException):
	"""Is raised if a file is not found at the given path."""


class InvalidParameterException(PhoneInterfaceException):
	"""Is raised if a parameter value is not available inside a specific backend-service."""


class NoVehicleDefinedException(PhoneInterfaceException):
	"""Is raised if no vehicle is defined for running functions inside the myaudi app"""
