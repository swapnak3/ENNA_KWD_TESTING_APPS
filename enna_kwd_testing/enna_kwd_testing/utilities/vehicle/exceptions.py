# -*- coding: utf-8 -*-
"""Module contains exception for errors at simulate vehicle environments."""

import enna.core.exceptions


class VehicleEnvironmentError(enna.core.exceptions.ENNAException):
	"""Base Exception for this Module"""


class VehicleSimulationError(VehicleEnvironmentError):
	"""Raise if vehicle simulation can not send to Test Environment"""


class InvalidArgument(VehicleEnvironmentError):
	"""Raise if argument for Stimulation invalid."""


class SimulationNotSupported(VehicleEnvironmentError):
	"""Raise if simulation not supported for current Test Environment."""
