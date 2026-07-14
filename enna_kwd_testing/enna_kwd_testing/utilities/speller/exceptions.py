# -*- coding: utf-8 -*-
"""Module contains all exceptions that can be thrown inside speller."""

import enna.core.exceptions


class SpellerException(enna.core.exceptions.ENNAException):
	"""Is raised if command did not succeed."""
