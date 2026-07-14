# -*- coding: utf-8 -*-
"""Module contains base classes for android-based screen detection."""
import abc
import enum
import logging

import enna_hcp_configuration.android.xpaths
import enna_hcp_configuration.common.base

UNKNOWN_SCREEN_ID = "unknown"
MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=invalid-name
class HMIActionType(enum.Enum):
	"""Action type definitions for the android HMI graph. Each transition in the graph can use one of these action types.

	Pay attention regarding the difference between click_element_in_list and click_element_in_horizontal_list.
	click_element_in_list must be used for vertical scrolling within its list, click_element_in_horizontal_list for horizontal scrolling.
	"""

	click_element = enum.auto()
	click_element_in_list = enum.auto()
	click_coordinates = enum.auto()
	click_element_in_horizontal_list = enum.auto()


class ElementDetectorExtension(metaclass=abc.ABCMeta):
	"""Base class for screen element detectors."""

	@abc.abstractmethod
	def detect(self, layout):
		"""Detect an arbitrary screen element.

		:param lxml.etree.Element layout: UI layout

		:return: whether the element was detected
		:rtype: bool
		"""


class ElementByXPathDetectorExtension(ElementDetectorExtension):
	"""Screen element detection based UI element existence for a specified xpath."""

	def __init__(self, xpaths):
		"""Instantiate screen element detector.

		:param xpaths: List of xpaths that specify all UI elements that must be present to detect the screen element.
		:type xpaths: list[enna_hcp_configuration.android.xpaths.XpathString] or enna_hcp_configuration.android.xpaths.XpathString
		"""
		self._xpath_list = xpaths if isinstance(xpaths, list) else [xpaths]

	def detect(self, layout):
		"""Detect screen element based on the existence of an element in the given UI layout.

		:param lxml.etree.Element layout: UI layout
		:return: True if the element was detected else False
		:rtype: bool
		"""
		return all(layout.xpath(xpath.get()) for xpath in self._xpath_list)


class ElementByXPathBlacklistWhitelistDetectorExtension(ElementDetectorExtension):
	"""Screen element detection based UI element existence and/or non-existence for a specified xpath."""

	def __init__(self, must_exist, must_not_exist):
		"""Instantiate screen element detector.

		:param must_exist: one or multiple xpaths which specify all UI elements that must be present to detect the screen element.
		:type must_exist: list[enna_hcp_configuration.android.xpaths.XpathString] or enna_hcp_configuration.android.xpaths.XpathString
		:param must_not_exist: one or multiple xpaths which specify all UI elements that must not be present to detect the screen element.
		:type must_not_exist: list[enna_hcp_configuration.android.xpaths.XpathString] or enna_hcp_configuration.android.xpaths.XpathString
		"""
		self._must_exist_list = must_exist if isinstance(must_exist, list) else [must_exist]
		self._must_not_exist_list = must_not_exist if isinstance(must_not_exist, list) else [must_not_exist]

	def detect(self, layout):
		"""Detect screen element based on the existence and/or non-existence of an element in the given UI layout.

		:param lxml.etree.Element layout: UI layout
		:return: True if the element was detected else False
		:rtype: bool
		"""
		return all(layout.xpath(xpath.get()) for xpath in self._must_exist_list) and not any(layout.xpath(xpath.get()) for xpath in self._must_not_exist_list)


class AppPackageDetectorExtension(ElementDetectorExtension):
	"""Context detection via element existence of specific app packages.

	This detector extension will report a match if any element with one of the given packages exists.
	"""

	def __init__(self, app_packages):
		"""Instantiate context element detector.

		:param list[str] app_packages: android app package names for this context
		"""
		self._xpath_list = [f"//*[@package='{package}']" for package in app_packages]

	def detect(self, layout):
		"""Detect screen element based on the existence of an element in the given UI layout.

		:param lxml.etree.Element layout: UI layout
		:return: True if at least one element was detected else False
		:rtype: bool
		"""
		if not self._xpath_list:
			return False

		return any(layout.xpath(xpath) for xpath in self._xpath_list)


class ContextAnalyzer:
	"""Context analyzer for a given HMI context."""

	def __init__(self, name, detector_extension):
		"""Initialize the analyzer.

		Screens are analyzed by first checking if the UI layout contains elements that belong to this context, which determined via the given detector extension.
		The given detector extension may also be None, in which case this context analyzer will not detect any screens, but will still detect popups.

		The context analyzer keeps a default unknown screen name using <context name>.unknown as the name for all screens which are part of this context, but were not detected by any screen object added to this context.

		Popups must not be part of the context to be detected.

		:param str name: the name of the context which is prepended to screens and popups detected by this analyzer.
		:param detector_extension: The detector extension which can detect this context, or None if this ContextAnalyzer should not detect any screens
		:type detector_extension: enna_hcp_configuration.android.base.ElementDetectorExtension or None
		"""
		self.name = name
		self.detector_extension = detector_extension
		self.unknown_screen_name = f"{self.name}.{UNKNOWN_SCREEN_ID}"
		self.screens = []
		self.popups = []

	def add_elements_from_module(self, elements):
		"""Add all screens and popups from a given dict of global attributes to this context.

		.. note::
			In order to correctly separate screens and popups, popup attribute names **must** begin with "POPUP_"

		:param dict elements: dict of global module attributes retrieved via ``globals()``
		"""
		for attr_name, object_ref in elements.items():
			if isinstance(object_ref, enna_hcp_configuration.common.base.Element):
				if attr_name.startswith("POPUP_"):
					self.add_popup(object_ref)
				else:
					self.add_screen(object_ref)

	def add_screen(self, screen):
		"""Add the given screen to this context.

		The screen name will be prepended with the name of this context.

		If the screen already exists in this analyzer, it will be replaced with the new element.

		:param enna_hcp_configuration.common.base.Element screen: the screen to add
		"""
		screen.name = f"{self.name}.{screen.name}"
		if screen in self.screens:
			MODULE_LOGGER.warning(f"the screen with name {screen.name} already exists, replacing it!")
			self.screens.remove(screen)
		self.screens.append(screen)

	def add_popup(self, popup):
		"""Add the given popup to this context.

		The popup name will be prepended with the name of this context.

		If the popup already exists in this analyzer, it will be replaced with the new element.

		:param enna_hcp_configuration.common.base.Element popup: the popup to add
		"""
		popup.name = f"{self.name}.{popup.name}"
		if popup in self.popups:
			MODULE_LOGGER.warning(f"the popup with name {popup.name} already exists, replacing it!")
			self.popups.remove(popup)
		self.popups.append(popup)

	def detect_screen(self, layout):
		"""Detect a screen using the given layout.

		:param lxml.etree.Element layout: the UI layout
		:return: the name of the detected screen, or the default unknown screen name. If this analyzer is not responsible for the context of the layout, None is returned
		:rtype: str or None
		"""
		if not self.detector_extension or not self.detector_extension.detect(layout):
			return None
		for screen in self.screens:
			# noinspection PyUnresolvedReferences
			screen_detected = screen.detector(layout) if callable(screen.detector) else screen.detector.detect(layout)
			if screen_detected:
				return screen.name
		return self.unknown_screen_name

	def detect_popups(self, layout):
		"""Detect all popup using the given layout.

		:param lxml.etree.Element layout: the UI layout
		:return: a list of the names of all detected popups
		:rtype: list[str]
		"""
		if not self.popups:
			return []
		detected_popups = []
		for popup in self.popups:
			# noinspection PyUnresolvedReferences
			popup_detected = popup.detector(layout) if callable(popup.detector) else popup.detector.detect(layout)
			if popup_detected:
				detected_popups.append(popup.name)
		return detected_popups


class ElementByMinOneXPathFromListDetectorExtension(ElementDetectorExtension):
	"""Screen element detection based  of UI element existence for a specified xpath.
	Minimum one element of list must exist in screen for detection.
	"""

	def __init__(self, xpaths):
		"""Instantiate screen element detector.

		:param xpaths: List of xpaths that specify UI elements. One or more element must present to detect the screen element.
		:type xpaths: list[enna_hcp_configuration.android.xpaths.XpathString] or enna_hcp_configuration.android.xpaths.XpathString
		"""
		self._xpath_list = xpaths if isinstance(xpaths, list) else [xpaths]

	def detect(self, layout):
		"""Detect screen element based on the existence of an element in the given UI layout.

		:param lxml.etree.Element layout: UI layout
		:return: True if the element was detected else False
		:rtype: bool
		"""
		return any(layout.xpath(xpath.get()) for xpath in self._xpath_list)
