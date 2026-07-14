# -*- coding: utf-8 -*-
"""Created on 04.08.2023.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.

Contains exceptions in context of the dependency factories and stimulation factories
"""
import enna.core.exceptions


class TestSpecificationException(enna.core.exceptions.ENNAException):
	"""Contains exceptions which is thrown when an error in the given test specification occurs."""
