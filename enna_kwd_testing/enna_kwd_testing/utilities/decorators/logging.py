# -*- coding: utf-8 -*-
"""Created on 01.03.2022.

@project: enna_tc_connect_apps_hcp3.
@author: DYX34ZN: Jakob Kein.

Contains decorators which extend logging capabilities.
"""

import functools
import logging

import decohints

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=missing-type-doc, missing-return-doc, missing-return-type-doc, missing-param-doc, differing-param-doc, broad-except
@decohints.decohints
def logdecorator(*args):
	"""Log the start and end of the caller with the given module logger.

	If no module logger is given, the module logger of the decorator is used

	Example usage:
		@decorator()
		def add(*args):
			return sum(args)
	:param args: Logger instance
	"""
	logger_list = [x for x in args if isinstance(x, logging.Logger)]
	logger = logger_list[0] if logger_list else MODULE_LOGGER

	def inner_decorator(f):
		"""Inner decorator.

		:param f: Method to be decorated.
		:return: Decorated function.
		"""
		method_name = f.__name__

		@functools.wraps(f)
		def decorated_function(*args, **kwargs):
			"""Decorate function."""
			logger.debug(f"Start of method {method_name}")
			output = f(*args, **kwargs)
			if isinstance(output, dict):
				logger.debug(f"Return value of {method_name}: {output}")
			if isinstance(output, bool):
				logger.debug(f"Return value of {method_name}: {output}")
			logger.debug(f"End of method {method_name}")
			return output

		return decorated_function

	return inner_decorator
