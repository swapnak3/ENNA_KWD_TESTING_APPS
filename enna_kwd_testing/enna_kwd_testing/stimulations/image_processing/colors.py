# -*- coding: utf-8 -*-
"""Module contains stimulation to check color states of UI elements."""
# pylint: disable=protected-access
import enum
import numpy
import cv2

import enna.core.config
import enna.core.exceptions
import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.core.image_processing.image
import enna.core.image_processing.helper

import enna_st12.instance_names
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.data_interfaces.android_hmi.helper

import enna_kwd_testing.stimulations.apps._internal


class ColorsBGR(enum.Enum):
	"""Constants of color"""
	WHITE = [255, 255, 255]
	DARK_WHITE = [225, 225, 225]
	BLACK = [0, 0, 0]
	LIGHT_BLACK = [30, 30, 30]


def _get_color_mask(image: enna.core.image_processing.image.Image, dark_threshold: list[int],
					bright_threshold: list[int]) -> numpy.ndarray:
	"""Get mask of  color is in range of threshold colors.
	If pixel color between dark and bright limit then pixel include to mask.

	:param image: image to check
	:param dark_threshold: threshold of value dark color
	:param bright_threshold: threshold of value bright color
	:return: mask for colors in image
	"""
	lower_limit = numpy.array(dark_threshold, numpy.uint8)
	upper_limit = numpy.array(bright_threshold, numpy.uint8)

	cv2_image = image.as_ndarray
	mask = cv2.inRange(cv2_image, lower_limit, upper_limit)

	# Debug: create an image to show mask for debugging
	# red_image = numpy.full(shape=image.as_ndarray.shape, fill_value=[0, 0, 255])  # create red color
	# mask_image = cv2.bitwise_and(red_image, red_image, mask=mask)
	# enna.core.image_processing.helper.save_image(enna_image=image, path=pathlib.Path("original"))
	# enna.core.image_processing.helper.save_image(enna_image=enna.core.image_processing.image.Image(mask_image), path=pathlib.Path("mask"))

	return mask


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckElementGreyOut(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Stimulation for checking element is grey out."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface,
				 android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: instance of reporting interface
		:param android_hmi: instance of interface for Android UI Automator
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)

	def _action(self) -> bool:
		"""Check element is grey out.

		:return: True is successful, else false
		"""
		try:
			self._android_hmi.wait_for_element_visible(xpath=self._xpath, max_time=1.0)
			coordinates_size = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(
				layout=self._android_hmi.layout.value, xpath=self._xpath)
			mask: list[int] = [coordinates_size["x"], coordinates_size["y"],
							   coordinates_size["x"] + coordinates_size["width"],
							   coordinates_size["y"] + coordinates_size["height"]]
			image_of_element = self._android_hmi.take_screenshot().get_roi(mask=mask)
			# pylint: disable=protected-access
			if enna.core.config.INFOTAINMENT_SYSTEM.cluster <= 43:
				# cluster 43 only check white pixels
				mask = _get_color_mask(image=image_of_element, dark_threshold=ColorsBGR.DARK_WHITE.value, bright_threshold=ColorsBGR.WHITE.value)
				if numpy.count_nonzero(mask) > 0:
					self._reporting.add_report_message_system_error(f"Element not grey out! Find {numpy.count_nonzero(mask)} white pixels.")
					return False

			else:
				# check no white pixels exist
				mask = _get_color_mask(image=image_of_element, dark_threshold=ColorsBGR.DARK_WHITE.value, bright_threshold=ColorsBGR.WHITE.value)
				if numpy.count_nonzero(mask) > 0:
					self._reporting.add_report_message_system_error(f"Element not grey out! Find {numpy.count_nonzero(mask)} white pixels.")
					return False
				# check no black pixels exist
				mask = _get_color_mask(image=image_of_element, dark_threshold=ColorsBGR.BLACK.value, bright_threshold=ColorsBGR.LIGHT_BLACK.value)
				if numpy.count_nonzero(mask) > 0:
					self._reporting.add_report_message_system_error(f"Element not grey out! Find {numpy.count_nonzero(mask)} black pixels.")
					return False

		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error(f"Element '{self._xpath}' is not found in current screen!")
			return False
		except (cv2.error, enna.core.exceptions.ImageProcessingException) as error:
			self._reporting.add_report_message_ta_error(f"Error by image processing! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_ta_error(f"Android HMI Exception! {error}")
			return False

		self._reporting.add_report_message_pass(f"Element '{self._xpath}' is grey out.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckElementNotGreyOut(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Stimulation for checking element is not grey out."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: instance of reporting interface
		:param android_hmi: instance of interface for Android UI Automator
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)

	def _action(self) -> bool:
		"""Check element is not grey out.

		:return: True is successful, else false
		"""
		try:
			self._android_hmi.wait_for_element_visible(xpath=self._xpath, max_time=1.0)
			coordinates_size = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(
				layout=self._android_hmi.layout.value, xpath=self._xpath)
			mask: list[int] = [coordinates_size["x"], coordinates_size["y"],
							   coordinates_size["x"] + coordinates_size["width"],
							   coordinates_size["y"] + coordinates_size["height"]]
			image_of_element = self._android_hmi.take_screenshot().get_roi(mask=mask)
			# pylint: disable=protected-access
			if enna.core.config.INFOTAINMENT_SYSTEM.cluster <= 43:
				# cluster 43 only check white pixels
				mask = _get_color_mask(image=image_of_element, dark_threshold=ColorsBGR.DARK_WHITE.value, bright_threshold=ColorsBGR.WHITE.value)
				if numpy.count_nonzero(mask) < 15:
					self._reporting.add_report_message_system_error(f"Element grey out! Find only {numpy.count_nonzero(mask)} white pixels.")
					return False

			else:
				# check  mininum of white or black pixels exist
				white_mask = _get_color_mask(image=image_of_element, dark_threshold=ColorsBGR.DARK_WHITE.value, bright_threshold=ColorsBGR.WHITE.value)
				black_mask = _get_color_mask(image=image_of_element, dark_threshold=ColorsBGR.BLACK.value, bright_threshold=ColorsBGR.LIGHT_BLACK.value)
				if numpy.count_nonzero(black_mask) < 15 and  numpy.count_nonzero(white_mask) < 15:
					self._reporting.add_report_message_system_error(f"Element grey out! Find only {numpy.count_nonzero(white_mask)} white and only {numpy.count_nonzero(black_mask)} black pixels.")
					return False

		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error(f"Element '{self._xpath}' is not found in current screen!")
			return False
		except (cv2.error, enna.core.exceptions.ImageProcessingException) as error:
			self._reporting.add_report_message_ta_error(f"Error by image processing! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_ta_error(f"Android HMI Exception! {error}")
			return False

		self._reporting.add_report_message_pass(f"Element '{self._xpath}' is not grey out.")
		return True
