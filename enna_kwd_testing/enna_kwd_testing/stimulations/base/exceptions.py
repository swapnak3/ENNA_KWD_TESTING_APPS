# -*- coding: utf-8 -*-
"""Exceptions that can be thrown by classes in this package."""

import enna.core.exceptions


class BaseStimulationError(enna.core.exceptions.ENNAException):
	"""Base Exception class for base stimulation."""


class ParameterNameError(BaseStimulationError):
	"""Raise if wrong parameter name found."""


class AttributeNotDefined(BaseStimulationError):
	"""Raise if necessary attribute not define."""


class NoStimulation(BaseStimulationError):
	"""Raise if no stimulation assigned to keyword."""
