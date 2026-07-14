# -*- coding: utf-8 -*-
"""Module contains class of display touching"""

import logging
import display_touch_simulation.touch
import display_touch_simulation.touch_message
import display_touch_simulation.exceptions
from display_touch_simulation.implementations.hcp3.touch import HCP3TouchConfig
from display_touch_simulation.implementations.one_infotainment.touch import OneInfotainmentTouchConfig

import display_touch_simulation.interface
import enna.core.config
import enna.core.exceptions
import enna.core.interfaces.server

import enna_st12.instance_names

import enna_kwd_testing.utilities.display_touch.interface
import enna_kwd_testing.utilities.display_touch.exceptions




MODULE_LOGGER = logging.getLogger(__name__)

INSTANCE_CONFIG = enna.core.config.get_instance_config(__name__)

class Server(enna_kwd_testing.utilities.display_touch.interface.Interface, enna.core.interfaces.server.Server):
	"""Class of sent display touch events."""

	def __init__(self, instance_name: str) -> None:
		"""Constructor of class.

		:param str instance_name: Name of instance to initialize server for.
		:raise enna.core.exceptions.ConfigurationException: If wrong system for implementation configured.
		:raise enna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchConnectionError: If an error by connection to hardware of display touch
		"""
		enna_kwd_testing.utilities.display_touch.interface.Interface.__init__(self)
		enna.core.interfaces.server.Server.__init__(self, instance_name=instance_name)
		self.__read_configuration(instance_name=instance_name)

		try:
			# self.__touch = display_touch_simulation.touch.Touch(implementation=self.__system)
			self.__touch = display_touch_simulation.touch.Touch(implementation=self.__system, config=self.__config)
		except display_touch_simulation.exceptions.TouchCanError as exc:
			msg = f"No connection to Vector Box! {exc}"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchConnectionError(msg) from exc
		except NotImplementedError as exc:
			msg = f"No implementation found for system '{self.__system}'! {exc}"
			MODULE_LOGGER.exception(msg)
			raise enna.core.exceptions.ConfigurationException(msg)

		self._connected = enna.core.interfaces.Data(True)
		self._signal_property("connected", self.connected)
		self._set_online()

	def __read_configuration(self, instance_name: str) -> None:
		"""Reading configuration of instance.

		:param str instance_name: name of display touch instance
		:raise enna.core.exceptions.ConfigurationException: if instance name invalid
		"""
		self.__system = INSTANCE_CONFIG[instance_name].get("infotainment_system", "hcp3")
		self.__channel = INSTANCE_CONFIG[instance_name].get("channel", 0)
		self.__baud_rate = INSTANCE_CONFIG[instance_name].get("baud_rate", 500000)
		self.__app_name = INSTANCE_CONFIG[instance_name].get("app_name", "Touch")
		self.__vkms_key = INSTANCE_CONFIG[instance_name].get("vkms_key", None)

		if instance_name == enna_st12.instance_names.AndroidHMI.CENTER:
			self.__display = display_touch_simulation.DisplayTypes.DISPLAY_TYPE_TOP_OR_CENTER
		elif instance_name == enna_st12.instance_names.AndroidHMI.PASSENGER:
			self.__display = display_touch_simulation.DisplayTypes.DISPLAY_TYPE_PID
		else:
			msg = f"No valid display type exist for instance_name '{instance_name}'! Valid display type are '{enna_st12.instance_names.AndroidHMI.CENTER}' or  '{enna_st12.instance_names.AndroidHMI.CENTER}'."
			MODULE_LOGGER.exception(msg)
			raise enna.core.exceptions.ConfigurationException(msg)

		if self.__system == "hcp3":
			self.__config = HCP3TouchConfig(channel=self.__channel, bitrate=self.__baud_rate, application_name=self.__app_name, display_type=self.__display, vkms_key=self.__vkms_key)
		elif self.__system == "one_infotainment":
			self.__config = OneInfotainmentTouchConfig(channel=self.__channel, bitrate=self.__baud_rate, application_name=self.__app_name, display_type=self.__display, vkms_key=self.__vkms_key)
		else:
			msg = f"No valid config for system '{self.__system}'!"
			MODULE_LOGGER.exception(msg)
			raise  enna.core.exceptions.ConfigurationException(msg)


	def single_finger_touch(self, coordinate: tuple[int, int], duration: float = 0.3, update_interval: float = 0.01) -> None:
		"""Single finger display touch event.

		:param tuple coordinate: Single finger x/y coordinate on the display.
		:param float duration: Touch duration in seconds.
		:param float update_interval: Update interval in sec used to send touch coordinates continuously, default: 10ms. Value of 0 will disable sending update messages.
		:raise nna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchEventError: If an error by touch event
		"""
		try:
			self.__touch.single_finger_touch(coordinate=coordinate, duration=duration, update_interval=update_interval)
		except (NotImplementedError, display_touch_simulation.exceptions.TouchCanError) as exc:
			msg = f"Touch event error by single touch! {exc}"
			raise enna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchEventError(msg)

	def single_finger_drag(self, start_coordinate: tuple[int, int], end_coordinate: tuple[int, int], duration: float = 0.3, update_interval: float = 0.01) -> None:
		"""Single finger drag and drop.

		:param tuple start_coordinate: start point x/y coordinate for drag-drop-gesture on the display.
		:param tuple end_coordinate:  end point x/y coordinate for drag-drop-gesture on the display.
		:param float duration: drag duration in seconds.
		:param float update_interval: Update interval in sec used to send touch coordinates continuously, default: 10ms. Value of 0 will disable sending update messages.
		:raise nna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchEventError: If an error by touch event
		"""
		try:
			self.__touch.single_finger_drag(start_coordinate=start_coordinate, end_coordinate=end_coordinate, duration=duration, update_interval=update_interval)
		except (NotImplementedError, display_touch_simulation.exceptions.TouchCanError) as exc:
			msg = f"Touch event error by drag and drop! {exc}"
			raise enna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchEventError(msg)

	def two_finger_touch(self, first_finger: tuple[int, int], second_finger: tuple[int, int], duration: float = 0.3, update_interval: float = 0.01) -> None:
		"""Two finger touch.

		:param tuple first_finger: x/y coordinate of the first finger on the display.
		:param tuple second_finger: x/y coordinate of the second finger on the display.
		:param float duration: drag duration in seconds.
		:param float update_interval: Update interval in sec used to send touch coordinates continuously, default: 10ms. Value of 0 will disable sending update messages.
		:raise nna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchEventError: If an error by touch event
		"""
		try:
			self.__touch.two_finger_touch(first_finger=first_finger, second_finger=second_finger, duration=duration, update_interval=update_interval)
		except (NotImplementedError, display_touch_simulation.exceptions.TouchCanError) as exc:
			msg = f"Touch event error by two finger touch! {exc}"
			raise enna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchEventError(msg)

	def multi_finger_custom_touch(self, finger_coordinates: list[display_touch_simulation.touch_message.TouchMessage], update_interval: float = 0.01) -> None:
		"""Touch custom coordinate path with one or more finger ids.

		:param list[display_touch_simulation.touch_message.TouchMessage] finger_coordinates: Multi finger x/y coordinates on the display.
		:param float update_interval: Update interval in sec used to send custom touch coordinates, default: 10ms.
		:raise nna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchEventError: If an error by touch event
		"""
		try:
			self.__touch.multi_finger_custom_touch(finger_coordinates=finger_coordinates, update_interval=update_interval)
		except (NotImplementedError, display_touch_simulation.exceptions.TouchCanError) as exc:
			msg = f"Touch event error by multi custom finger touch! {exc}"
			raise enna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchEventError(msg)
