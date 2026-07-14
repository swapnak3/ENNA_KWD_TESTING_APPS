# -*- coding: utf-8 -*-
"""Module contains Display Touch events send via CAN."""
import logging

import enna.core.component_system.decorators

import enna_st12.instance_names

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.display_touch.interface
import enna_kwd_testing.utilities.display_touch.exceptions
import enna_kwd_testing.utilities.display_touch.helper

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.display_touch", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class ZoomInGestureNavigationMap(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to send a zoom in touch gesture."""

	def __init__(self, reporting, display_touch: enna_kwd_testing.utilities.display_touch.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna_st12.utilities.display_touch.interface.Interface display_touch: Instance of display touch interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__display_touch = display_touch

	def _action(self) -> bool:
		"""Execute action.

		Send zoom in touch gesture

		:return: True if successful, False it susan exception occurs
		:rtype: bool
		"""
		try:
			self.__display_touch.multi_finger_custom_touch(enna_kwd_testing.utilities.display_touch.helper.NAVIGATION_ZOOM_IN, update_interval=0.1)
			self._reporting.add_report_message_pass("Send zoom in gesture.")
		except enna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchError as exc:
			self._reporting.add_report_message_ta_error(f"Error by send zoom in touch event! {exc}")
			return False
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.display_touch", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class RotationNavigationMapToLeft(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to send a zoom in touch gesture."""

	def __init__(self, reporting, display_touch: enna_kwd_testing.utilities.display_touch.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna_st12.utilities.display_touch.interface.Interface display_touch: Instance of display touch interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__display_touch = display_touch

	def _action(self) -> bool:
		"""Execute action.

		Send zoom in touch gesture

		:return: True if successful, False it susan exception occurs
		:rtype: bool
		"""
		try:
			self.__display_touch.multi_finger_custom_touch(enna_kwd_testing.utilities.display_touch.helper.MAP_ROTATE_TO_LEFT, update_interval=0.1)
			self._reporting.add_report_message_pass("Send zoom in gesture.")
		except enna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchError as exc:
			self._reporting.add_report_message_ta_error(f"Error by send zoom in touch event! {exc}")
			return False
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.display_touch", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class RotationNavigationMapToRight(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to send a zoom in touch gesture."""

	def __init__(self, reporting, display_touch: enna_kwd_testing.utilities.display_touch.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna_st12.utilities.display_touch.interface.Interface display_touch: Instance of display touch interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__display_touch = display_touch

	def _action(self) -> bool:
		"""Execute action.

		Send zoom in touch gesture

		:return: True if successful, False it susan exception occurs
		:rtype: bool
		"""
		try:
			self.__display_touch.multi_finger_custom_touch(enna_kwd_testing.utilities.display_touch.helper.MAP_ROTATE_TO_RIGHT, update_interval=0.1)
			self._reporting.add_report_message_pass("Send zoom in gesture.")
		except enna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchError as exc:
			self._reporting.add_report_message_ta_error(f"Error by send zoom in touch event! {exc}")
			return False
		return True
