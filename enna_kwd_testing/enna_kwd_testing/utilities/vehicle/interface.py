# -*- coding: utf-8 -*-
"""The interface of vehicle simulations."""
import abc

import enna.core.component_system.decorators
import enna.core.interfaces.component


@enna.core.component_system.decorators.GenerateProxy()
class Interface(enna.core.interfaces.component.Component):
	"""Abstract interface for controlling test portal."""


	@abc.abstractmethod
	def comfort_ready_status(self, state: bool) -> None:
		"""Set Signal of Comfort Ready Status.

		:param state: on/off
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if state of Comfort Ready Status not set
		:raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported: if not supported for Test environment
		"""

	@abc.abstractmethod
	def clamp_15(self, state: bool) -> None:
		"""Set ignition state. (Clamp 15)

		:param state: on/off
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if state of ignition not set
		:raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported: if not supported for Test environment
		"""

	@abc.abstractmethod
	def clamp_s(self, state: bool) -> None:
		"""Set clamp S.

		:param state: on/off
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if state of Clamp S not set
		:raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported: if not supported for Test environment
		"""

	@abc.abstractmethod
	def gear_selection(self, gear: str) -> None:
		"""Set gear position.

		:param gear: PARKING, DRIVE, NEUTRAL or REVERSE
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if gear not set
		:raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument: if argument not valid
		:raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported: if not supported for Test environment
		"""

	@abc.abstractmethod
	def vehicle_speed(self, speed: float) -> None:
		"""Set vehicle velocity.

		:param speed: speed in m/s
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if vehicle speed not set
		:raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported: if not supported for Test environment
		"""

	@abc.abstractmethod
	def driver_seat_occupancy(self, state: str) -> None:
		"""Set state of driver seat occupancy.

		:param state: OCCUPIED, NOT_OCCUPIED, NOT_AVAILABLE or ERROR
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if state of driver seat not set
		:raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument: if argument not valid
		:raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported: if not supported for Test environment
		"""

	@abc.abstractmethod
	def co_driver_seat_occupancy(self, state: str) -> None:
		"""Set state of co-driver seat occupancy.

		:param state: OCCUPIED, NOT_OCCUPIED, NOT_AVAILABLE or ERROR
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if state of co-driver seat not set
		:raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument: if argument not valid
		:raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported: if not supported for Test environment
		"""

	@abc.abstractmethod
	def display_design(self, mode: str) -> None:
		"""Set mode of display design.

		:param mode: DAY or NIGHT
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if mode of display design not set
		:raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument: if argument not valid
		:raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported: if not supported for Test environment
		"""
