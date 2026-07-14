# -*- coding: utf-8 -*-
"""Module contains an abstract interface to display touching."""
import abc

import enna.core.component_system.decorators
import enna.core.interfaces
import enna.core.interfaces.component

import display_touch_simulation.touch_message


@enna.core.component_system.decorators.GenerateProxy()
class Interface(enna.core.interfaces.component.Component):
	"""Abstract Interface for display touching."""

	def __init__(self):
		"""Initialize interface."""
		self._connected = enna.core.interfaces.Data(False)

	@abc.abstractmethod
	def single_finger_touch(self, coordinate: tuple[int, int], duration: float = 0.3, update_interval: float = 0.01) -> None:
		"""Single finger display touch event.

		:param tuple coordinate: Single finger x/y coordinate on the display.
		:param float duration: Touch duration in seconds.
		:param float update_interval: Update interval in sec used to send touch coordinates continuously, default: 10ms. Value of 0 will disable sending update messages.
		:raise nna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchEventError: If an error by touch event
		"""

	@abc.abstractmethod
	def single_finger_drag(self, start_coordinate: tuple[int, int], end_coordinate: tuple[int, int], duration: float = 0.3, update_interval: float = 0.01) -> None:
		"""Single finger drag and drop.

		:param tuple start_coordinate: start point x/y coordinate for drag-drop-gesture on the display.
		:param tuple end_coordinate:  end point x/y coordinate for drag-drop-gesture on the display.
		:param float duration: drag duration in seconds.
		:param float update_interval: Update interval in sec used to send touch coordinates continuously, default: 10ms. Value of 0 will disable sending update messages.
		:raise nna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchEventError: If an error by touch event
		"""

	@abc.abstractmethod
	def two_finger_touch(self, first_finger: tuple[int, int], second_finger: tuple[int, int], duration: float = 0.3, update_interval: float = 0.01) -> None:
		"""Two finger touch.

		:param tuple first_finger: x/y coordinate of the first finger on the display.
		:param tuple second_finger: x/y coordinate of the second finger on the display.
		:param float duration: drag duration in seconds.
		:param float update_interval: Update interval in sec used to send touch coordinates continuously, default: 10ms. Value of 0 will disable sending update messages.
		:raise nna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchEventError: If an error by touch event
		"""

	@abc.abstractmethod
	def multi_finger_custom_touch(self, finger_coordinates: list[display_touch_simulation.touch_message.TouchMessage], update_interval: float = 0.01) -> None:
		"""Touch custom coordinate path with one or more finger ids.

		:param list[display_touch_simulation.touch_message.TouchMessage] finger_coordinates: Multi finger x/y coordinates on the display.
		:param float update_interval: Update interval in sec used to send custom touch coordinates, default: 10ms.
		:raise nna_kwd_testing.utilities.display_touch.exceptions.DisplayTouchEventError: If an error by touch event
		"""

	@property
	def connected(self) -> enna.core.interfaces.Data[bool]:
		"""Return state of connection.

		return: True is connected, False is disconnected.
		rtype: enna.core.interfaces.Data[bool]

		"""
