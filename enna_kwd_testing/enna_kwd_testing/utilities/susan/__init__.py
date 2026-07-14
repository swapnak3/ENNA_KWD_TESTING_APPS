# -*- coding: utf-8 -*-
"""Module contains constants for SUSAN BOX interface"""

import enum

class Groups(enum.StrEnum):
	"""Constants of groups from SUSAN Box."""
	TERMINAL = "Terminal"
	SPEED = "Speed"
	GEAR = "Gear"
	SEAT = "Seat Occupancy"
	INTERIOR_LIGHT = "Interior Light"


class Options(enum.StrEnum):
	"""Constants of groups from SUSAN Box."""
	COMFORT_READY_STATUS = "Comfort Ready Status"
	CLAMP_15 = "Term15"
	CLAMP_S = "TermS"
	SPEED = "Actual Speed"
	GEAR = "Gear"
	DRIVER_SEAT_OCCUPANCY = "Driver Seat Occupancy"
	CO_DRIVER_SEAT_OCCUPANCY = "Co-Driver Seat Occupancy"
	DISPLAY_DESIGN = "Display Design"


class GearPositions(enum.StrEnum):
	"""Possible gear positions"""
	PARKING = "P"
	DRIVE = "D"
	NEUTRAL = "N"
	REVERSE = "R"
	INIT = "Init"


class SeatOccupancy(enum.StrEnum):
	"""Possible occupancy states from Seat."""
	OCCUPIED = "Occupied"
	NOT_AVAILABLE = "Not Available"
	ERROR = "Error"
	NOT_OCCUPIED = "Not Occupied"


class DisplayMode(enum.StrEnum):
	"""Possible display modes."""
	DAY = "Day"
	NIGHT = "Night"
