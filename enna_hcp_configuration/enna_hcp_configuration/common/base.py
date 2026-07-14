# -*- coding: utf-8 -*-
"""Module contains base classes for HCP configuration."""
import logging

MODULE_LOGGER = logging.getLogger(__name__)


class ExtensionContainer:
	"""An abstract container to register extension classes.

	Registering the same extension twice is not supported.

	Extensions can be anything.
	"""

	def __init__(self, name):
		"""Initialize the container.

		:param str name: the name of this container
		"""
		self._extensions = []
		self.name = name

	def register_extension(self, extension):
		"""Register an extension.

		Each extension object can only be registered once.

		:param object extension: an extension, can be anything
		"""
		if extension not in self._extensions:
			self._extensions.append(extension)
		else:
			MODULE_LOGGER.warning(f"Extension {extension} is already registered")

	def unregister_extension(self, extension):
		"""Unregister an extension.

		Already unregistered extensions are ignored.

		:param object extension: an extension, can be anything
		"""
		if extension in self._extensions:
			self._extensions.remove(extension)

	def __iter__(self):
		"""Return a custom iterator which allows access to the extension list.

		:returns: an iterator to the extension list
		:rtype: iterator
		"""
		return iter(self._extensions)


class Element:
	"""Represent an element that consists of a name and a detector."""

	def __init__(self, name, detector_extension=None):
		"""Initialize the element.

		:param str name: name of the element
		:param detector_extension: a detector for this element
		:type detector_extension: callable or objec\
		"""
		self.name = name
		self.detector = detector_extension

	def __repr__(self):
		"""Representation of an element.

		:return: name of the element
		:rtype: str
		"""
		return self.name

	def __str__(self):
		"""Representation as str of an element.

		:return: name of the element
		:rtype: str
		"""
		return self.name

	def __eq__(self, other):
		"""Overwritten equality check allowing comparison of Element objects against a string.

		Only the element name will be used for comparison.

		:param object other: the object to compare against
		:return: if the two objects are equal
		:rtype: bool
		"""
		if isinstance(other, str):
			return self.name == other
		if isinstance(other, Element):
			return self.name == other.name
		return False

	def __hash__(self):
		"""Overwritten hash operator to enable hashing of Element objects.

		Uses the element name as the hash source.
		:return: the hash value of this object
		:rtype: int
		"""
		return hash(self.name)
