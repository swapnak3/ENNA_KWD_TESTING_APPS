# -*- coding: utf-8 -*-
"""Sever of vehicle simulations for PPE/PPC Test Environment."""
import logging
import enum

import enna.core.config
import enna.core.interfaces.server
import enna.core.component_system.decorators
import enna.utilities.susan.interface
import enna.utilities.susan.exceptions

import enna_kwd_testing.utilities.vehicle.exceptions
import enna_kwd_testing.utilities.vehicle.interface


MODULE_LOGGER = logging.getLogger(__name__)


class Server(enna_kwd_testing.utilities.vehicle.interface.Interface, enna.core.interfaces.server.Server):
	"""Server for vehicle simulations of PPE Environment."""

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

	def __init__(self, instance_name: str, susan: enna.utilities.susan.interface.Interface) -> None:
		"""Constructor of instance for vehicle simulations.

		:param instance_name: name of server
		:param susan: instance of SUSAN Box interface
		"""
		enna_kwd_testing.utilities.vehicle.interface.Interface.__init__(self)
		enna.core.interfaces.server.Server.__init__(self, instance_name=instance_name)
		self.__susan = susan
		self._set_online()

	def comfort_ready_status(self, state: bool) -> None:
		"""Set Signal of Comfort Ready Status on SUSAN Box.

		:param state: on/off
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if state of Comfort Ready Status not set
		"""
		try:
			self.__susan.send(cmd=enna.utilities.susan.CommandType.UPD, group=self.Groups.TERMINAL, option=self.Options.COMFORT_READY_STATUS, value=state, wait_for_property_change=True)
			MODULE_LOGGER.debug(f"Successfully set Comfort Ready Status on SUSAN Box to {state}")
		except enna.utilities.susan.exceptions.SUSANException as error:
			msg = f"Comfort Ready Status not set to {state}! {error}"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError(msg)

	def clamp_15(self, state: bool) -> None:
		"""Set ignition state on SUSAN Box.

		:param state: on/off
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if state of ignition not set
		"""
		try:
			self.__susan.send(cmd=enna.utilities.susan.CommandType.UPD, group=self.Groups.TERMINAL, option=self.Options.CLAMP_15, value=state, wait_for_property_change=True)
			MODULE_LOGGER.debug(f"Successfully set Clamp 15 on SUSAN Box to {state}")
		except enna.utilities.susan.exceptions.SUSANException as error:
			msg = f"Clamp 15 not set to {state}! {error}"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError(msg)

	def clamp_s(self, state: bool) -> None:
		"""Set Clamp S on SUSAN Box.

		:param state: on/off
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if state of Clamp S not set
		"""
		try:
			self.__susan.send(cmd=enna.utilities.susan.CommandType.UPD, group=self.Groups.TERMINAL, option=self.Options.CLAMP_S, value=state, wait_for_property_change=True)
			MODULE_LOGGER.debug(f"Successfully set Clamp S on SUSAN Box to {state}")
		except enna.utilities.susan.exceptions.SUSANException as error:
			msg = f"Clamp S not set to {state}! {error}"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError(msg)

	def gear_selection(self, gear: str) -> None:
		"""Set gear position on SUSAN Box.

		:param gear: PARKING, DRIVE, NEUTRAL or REVERSE
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if gear not set
		:raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument: if argument not valid
		"""
		try:
			selected_gear = getattr(self.GearPositions, gear)
			self.__susan.send(cmd=enna.utilities.susan.CommandType.UPD, group=self.Groups.GEAR, option=self.Options.GEAR, value=selected_gear, wait_for_property_change=True)
			MODULE_LOGGER.debug(f"Successfully gear position on SUSAN Box to {gear}")
		except AttributeError:
			msg = f"'{gear}' not valid gear position! Valid gear positions are {self.GearPositions.__members__}."
			MODULE_LOGGER.error(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument(msg)
		except enna.utilities.susan.exceptions.SUSANException as error:
			msg = f"Gear position not set to {gear}! {error}"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError(msg)

	def vehicle_speed(self, speed: float) -> None:
		"""Set Actual Speed on SUSAN Box.

		:param speed: speed in m/s
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if vehicle speed not set
		"""
		try:
			speed_kilometer_per_hour: str = str(int(speed * 3.6))
			self.__susan.send(cmd=enna.utilities.susan.CommandType.UPD, group=self.Groups.SPEED, option=self.Options.SPEED, value=speed_kilometer_per_hour, wait_for_property_change=True)
			MODULE_LOGGER.debug(f"Successfully actual speed to {speed}.")
		except enna.utilities.susan.exceptions.SUSANException as error:
			msg = f"Actual Speed not set to {speed}! {error}"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError(msg)

	def driver_seat_occupancy(self, state: str) -> None:
		"""Set state of driver seat occupancy on SUSAN Box.

		:param state: OCCUPIED, NOT_OCCUPIED, NOT_AVAILABLE or ERROR
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if state of driver seat not set
		:raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument: if argument not valid
		"""
		try:
			selected_state = getattr(self.SeatOccupancy, state)
			self.__susan.send(cmd=enna.utilities.susan.CommandType.UPD, group=self.Groups.SEAT, option=self.Options.DRIVER_SEAT_OCCUPANCY, value=selected_state, wait_for_property_change=True)
			MODULE_LOGGER.debug(f"Successfully driver seat to {state}")
		except AttributeError:
			msg = f"'{state}' not valid state of seat occupancy! Valid states are {self.SeatOccupancy.__members__}."
			MODULE_LOGGER.error(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument(msg)
		except enna.utilities.susan.exceptions.SUSANException as error:
			msg = f"Driver Seat not set to state '{state}'! {error}"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError(msg)

	def co_driver_seat_occupancy(self, state: str) -> None:
		"""Set state of co-driver seat occupancy on SUSAN Box.

		:param state: OCCUPIED, NOT_OCCUPIED, NOT_AVAILABLE or ERROR
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if state of co-driver seat not set
		:raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument: if argument not valid
		"""
		try:
			selected_state = getattr(self.SeatOccupancy, state)
			self.__susan.send(cmd=enna.utilities.susan.CommandType.UPD, group=self.Groups.SEAT, option=self.Options.CO_DRIVER_SEAT_OCCUPANCY, value=selected_state, wait_for_property_change=True)
			MODULE_LOGGER.debug(f"Successfully co-driver seat to {state}")
		except AttributeError:
			msg = f"'{state}' not valid state of seat occupancy! Valid states are {self.SeatOccupancy.__members__}."
			MODULE_LOGGER.error(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument(msg)
		except enna.utilities.susan.exceptions.SUSANException as error:
			msg = f"Co-Driver Seat not set to state '{state}'! {error}"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError(msg)

	def display_design(self, mode: str) -> None:
		"""Set mode of display design.

		:param mode: DAY or NIGHT
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if mode of display design not set
		:raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument: if argument not valid
		"""
		try:
			selected_mode = getattr(self.DisplayMode, mode)
			self.__susan.send(cmd=enna.utilities.susan.CommandType.UPD, group=self.Groups.INTERIOR_LIGHT, option=self.Options.DISPLAY_DESIGN, value=selected_mode, wait_for_property_change=True)
			MODULE_LOGGER.debug(f"Successfully display design to mode {mode}")
		except AttributeError:
			msg = f"'{mode}' not valid mode of display design! Valid states are {self.DisplayMode.__members__}."
			MODULE_LOGGER.error(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument(msg)
		except enna.utilities.susan.exceptions.SUSANException as error:
			msg = f"Display design not set to mode '{mode}'! {error}"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError(msg)
