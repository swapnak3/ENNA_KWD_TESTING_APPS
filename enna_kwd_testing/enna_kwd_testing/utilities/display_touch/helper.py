# -*- coding: utf-8 -*-
"""Module contains helper functions to calculate multi display touch events."""

import logging
import math

from display_touch_simulation.touch_message import FingerTouchInformation, TouchMessage, TouchState


MODULE_LOGGER = logging.getLogger(__name__)


def calculate_finger_linear_touch_points(start_coordinates: tuple[int, int], end_coordinates: tuple[int, int], steps: int =20, finger_id: int = 1) -> list[FingerTouchInformation]:
	"""Calculate a linear way of touch point between start and end coordinates.

	:param tuple start_coordinates: x/y start point of finger way
	:param tuple end_coordinates: x/y end point of finger way
	:param int steps: count of point to calculating
	:param int finger_id: number of finger
	:return: list with finger touch information  of linear way from this finger.
	:rtype: list[FingerTouchInformation]
	"""
	x = start_coordinates[0]
	y = start_coordinates[1]
	diff_x = (end_coordinates[0] - x) / steps
	diff_y = (end_coordinates[1]- y) / steps
	finger_touches = [FingerTouchInformation(finger_id, TouchState.TOUCH_START, x, y, 0)]
	for step in range(steps - 1):
		x += diff_x
		y += diff_y
		finger_touches.append(FingerTouchInformation(finger_id, TouchState.TOUCH_UPDATE, int(x), int(y), 0))
		MODULE_LOGGER.debug(f"{step}: Coordinate = ({x}, {y})")

	finger_touches.append(FingerTouchInformation(finger_id, TouchState.TOUCH_RELEASE, end_coordinates[0], end_coordinates[1], 0))
	return finger_touches


def calculate_tow_fingers_linear_gesture(first_finger_start: tuple[int, int], first_finger_end: tuple[int, int], second_finger_start: tuple[int, int], second_finger_end: tuple[int, int], steps=20) -> list[TouchMessage]:
	"""Create touch message list for a linear two finger gesture.

	:param tuple first_finger_start: x/y start point of first finger
	:param tuple first_finger_end: x/y end point of first finger
	:param tuple second_finger_start: x/y start point of second finger
	:param tuple second_finger_end: x/y end point of second finger
	:param int steps: number of touch messages
	:return: list of touch messages for this gesture
	:rtype: list[TouchMessage]
	"""

	first_finger_touches = calculate_finger_linear_touch_points(first_finger_start, first_finger_end, steps=steps, finger_id=1)
	second_finger_touches = calculate_finger_linear_touch_points(second_finger_start, second_finger_end, steps=steps, finger_id=2)
	touch_messages = []
	for i, _ in enumerate(first_finger_touches):
		if i == len(first_finger_touches) - 1:
			touch_messages.append(TouchMessage(touch_data=[first_finger_touches[i], second_finger_touches[i]], command=0x10, update_finger_count=2, total_finger_count=0))
		else:
			touch_messages.append(TouchMessage(touch_data=[first_finger_touches[i], second_finger_touches[i]], command=0x10, update_finger_count=2, total_finger_count=2))

	return touch_messages


def calculate_90degree_rotation_gesture(middle: tuple[int, int], radius: int, turn_right: bool = False) -> list[TouchMessage]:
	"""Generate touch points for a two finger rotation gesture.
	First finger is in a middle point from circle.
	Second finger rotate to 90 degrees.

	:param tuple middle: x/y coordinates from middle point of circle
	:param int radius: radius from circle
	:param bool turn_right: If true then rotate gesture to right. Default gesture rotate to left.
	:return: list of touch messages for this gesture
	:rtype: list[TouchMessage]
	"""

	steps: int = 10
	angle_step: float =  math.pi / (2 * steps)
	current_angle: float = 0.0

	x: int = middle[0]
	y: int = middle[1]

	if turn_right:
		angle_step *= -1

	touches: list = [

	TouchMessage( touch_data=[
		FingerTouchInformation(finger_id=1, finger_touch_state=TouchState.TOUCH_START, x_coordinate=x, y_coordinate=y, z_coordinate=0),
		FingerTouchInformation(finger_id=2, finger_touch_state=TouchState.TOUCH_START, x_coordinate=x + int(radius * math.sin(current_angle)), y_coordinate=y + int(radius * math.cos(current_angle)), z_coordinate=0)
		],
		command=0x10,
		update_finger_count=2,
		total_finger_count=2)
	]

	for _ in range(steps):
		current_angle += angle_step
		touches.append(TouchMessage(touch_data=[
			FingerTouchInformation(finger_id=1, finger_touch_state=TouchState.TOUCH_UPDATE, x_coordinate=x, y_coordinate=y, z_coordinate=0),
			FingerTouchInformation(finger_id=2, finger_touch_state=TouchState.TOUCH_UPDATE, x_coordinate=x + int(radius * math.sin(current_angle)), y_coordinate=y + int(radius * math.cos(current_angle)), z_coordinate=0)
			],
			command=0x10,
			update_finger_count=2,
			total_finger_count=2)
		)

	touches.append(TouchMessage(touch_data=[
		FingerTouchInformation(finger_id=1, finger_touch_state=TouchState.TOUCH_RELEASE, x_coordinate=x, y_coordinate=y, z_coordinate=0),
		FingerTouchInformation(finger_id=2, finger_touch_state=TouchState.TOUCH_RELEASE, x_coordinate=x + int(radius * math.sin(current_angle)), y_coordinate=y + int(radius * math.cos(current_angle)), z_coordinate=0)
		],
		command=0x10,
		update_finger_count=2,
		total_finger_count=0)
	)

	return touches


NAVIGATION_ZOOM_IN = calculate_tow_fingers_linear_gesture((1200, 350), (1200, 150), (1200, 400), (1200,600), steps=20)
MAP_ROTATE_TO_LEFT = calculate_90degree_rotation_gesture((1200, 500), 250, turn_right=False)
MAP_ROTATE_TO_RIGHT = calculate_90degree_rotation_gesture((1200, 500), 250, turn_right=True)
