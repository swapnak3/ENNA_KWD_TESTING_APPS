# -*- coding: utf-8 -*-
"""Sever of vehicle simulations for MQBw Baseline Test Environment."""
import logging
import enum
import time

import enna.core.config
import enna.core.interfaces.server
import enna.core.component_system.decorators
import enna.data_interfaces.adb.interface
import enna.data_interfaces.adb.exceptions

import enna_kwd_testing.utilities.vehicle.exceptions
import enna_kwd_testing.utilities.vehicle.interface

MODULE_LOGGER = logging.getLogger(__name__)


class Server(enna_kwd_testing.utilities.vehicle.interface.Interface, enna.core.interfaces.server.Server):
	"""Server for vehicle simulations of PPE Environment."""

	class Properties(enum.StrEnum):
		"""Constants of Vehicle Property IDs"""
		IGNITION = "0x11400409"
		GEAR_SELECTION = "0x11400400"
		SPEED = "0x11600207"
		DISPLAY_MODE = "0x11200407"

	class IgnitionStates(enum.StrEnum):
		"""Constants ignition states"""
		OFF = "2"
		ON = "4"

	class GearPositions(enum.StrEnum):
		"""Possible gear positions"""
		PARKING = "4"
		DRIVE = "8"
		NEUTRAL = "1"
		REVERSE = "2"
		INIT = "0"

	class DisplayMode(enum.StrEnum):
		"""Possible display modes."""
		DAY = "false"
		NIGHT = "true"

	def __init__(self, instance_name: str, adb: enna.data_interfaces.adb.interface.Interface) -> None:
		"""Constructor of instance for vehicle simulations.

		:param instance_name: name of server
		:param adb: instance of android debug bridge interface
		"""
		enna_kwd_testing.utilities.vehicle.interface.Interface.__init__(self)
		enna.core.interfaces.server.Server.__init__(self, instance_name=instance_name)
		self.__car_inject = "dumpsys activity service com.android.car inject-vhal-event"
		self.__adb = adb
		self._set_online()
		self._current_speed: float = 1000.0
		self._current_gear: str = ""

	def comfort_ready_status(self, state: bool) -> None:
		"""Set Signal of Comfort Ready Status.

		:param state: on/off
		:raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported: if not supported for Test environment
		"""
		msg = "Comfort Ready can not simulate on MQBw environment."
		MODULE_LOGGER.exception(msg)
		raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported(msg)

	def clamp_15(self, state: bool) -> None:
		"""Set ignition state on Android VehicleHAL.

		:param state: on/off
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if state of ignition not set
		"""
		try:
			ignition_state = self.IgnitionStates.ON if state else self.IgnitionStates.OFF
			inject = f"{self.__car_inject} {self.Properties.IGNITION} {ignition_state}"
			self.__adb.execute_shell_command(command=inject, timeout=10.0)
			MODULE_LOGGER.exception(f"Successfully set Clamp 15 to {state}")
		except enna.data_interfaces.adb.exceptions.ADBException as error:
			msg = f"Clamp 15 not set to {state}! {error}"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError(msg)

	def clamp_s(self, state: bool) -> None:
		"""Set Signal of Clamp S.

		:param state: on/off
		:raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported: if not supported for Test environment
		"""
		msg = "Clamp S can not simulate on MQBw environment."
		MODULE_LOGGER.exception(msg)
		raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported(msg)

	def gear_selection(self, gear: str) -> None:
		"""Set gear position on Android VehicleHAL.

		:param gear: PARKING, DRIVE, NEUTRAL or REVERSE
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if gear not set
		:raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument: if argument not valid
		"""
		self._current_gear = "" # reset current gear
		log_gear_positions = {
			"PARKING": "GEAR_PARK",
			"DRIVE": "GEAR_DRIVE",
			"NEUTRAL": "GEAR_NEUTRAL",
			"REVERSE": "GEAR_REVERSE",
			"INIT": "GEAR_UNKNOWN"
		}
		try:
			self.__adb.start_logcat_reading()
			self.__adb.register("GEAR_POSITION", self.__callback_gear)
			selected_gear = getattr(self.GearPositions, gear)
			inject = f"{self.__car_inject} {self.Properties.GEAR_SELECTION} {selected_gear}"
			self.__adb.execute_shell_command(command=inject, timeout=10.0)
			# waiting updating gear position is verified on logcat message
			timeout = time.time() + 5.0
			while time.time() < timeout:
				if self._current_gear == log_gear_positions[gear]:
					MODULE_LOGGER.debug(f"Update to gear position {gear} is verified.")

			MODULE_LOGGER.debug(f"Successfully gear position to {gear}")
			self.__adb.stop_logcat_reading()
		except AttributeError:
			msg = f"'{gear}' not valid gear position! Valid gear positions are {self.GearPositions.__members__}."
			MODULE_LOGGER.error(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument(msg)
		except enna.data_interfaces.adb.exceptions.ADBException as error:
			msg = f"Gear position not set to {gear}! {error}"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError(msg)

	def vehicle_speed(self, speed: float) -> None:
		"""Set vehicle velocity on Android VehicleHAL.

		:param speed: speed in m/s
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if vehicle speed not set
		"""
		self._current_speed = 1000.0 # reset current speed value
		current_equal_expected: bool = False
		try:
			self.__adb.start_logcat_reading()
			self.__adb.register("CURRENT_SPEED", self.__callback_speed)
			inject = f"{self.__car_inject} {self.Properties.SPEED} {speed}"
			self.__adb.execute_shell_command(command=inject, timeout=10.0)

			# waiting if speed reading on logcat
			timeout = time.time() + 5.0
			while time.time() < timeout:
				if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 55: # In Cluster 55 the log message contains km/h instead of m/s, so value needs to be recalculated to m/s
					self._current_speed /= 3.6
				if speed - 0.05 < self._current_speed < speed + 0.05:
					current_equal_expected = True
					break
			self.__adb.stop_logcat_reading()
		except enna.data_interfaces.adb.exceptions.ADBException as error:
			msg = f"Speed not set to {speed}! {error}"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError(msg)

		# raise exception is speed not verified on logcat message
		if not current_equal_expected:
			msg = f"Speed value {speed} is not reading on logcat inner 5.0 seconds!"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError(msg)
		MODULE_LOGGER.debug(f"Successfully set speed  to {speed}")


	def driver_seat_occupancy(self, state: str) -> None:
		"""Set state of driver seat occupancy.

		:param state: OCCUPIED, NOT_OCCUPIED, NOT_AVAILABLE or ERROR
		:raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported: if not supported for Test environment
		"""
		msg = "Driver Seat Occupancy can not simulate on MQBw environment."
		MODULE_LOGGER.exception(msg)
		raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported(msg)

	def co_driver_seat_occupancy(self, state: str) -> None:
		"""Set state of co-driver seat occupancy.

		:param state: OCCUPIED, NOT_OCCUPIED, NOT_AVAILABLE or ERROR
		:raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported: if not supported for Test environment
		"""
		msg = "Co-Driver Seat Occupancy can not simulate on MQBw environment."
		MODULE_LOGGER.exception(msg)
		raise enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported(msg)

	def display_design(self, mode: str) -> None:
		"""Set mode of display design on Android VehicleHAL.

		:param mode: DAY or NIGHT
		:raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError: if mode of display design not set
		:raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument: if argument not valid
		"""
		try:
			selected_mode = getattr(self.DisplayMode, mode)
			inject = f"{self.__car_inject} {self.Properties.DISPLAY_MODE} {selected_mode}"
			self.__adb.execute_shell_command(command=inject, timeout=10.0)
			MODULE_LOGGER.debug(f"Successfully display design to mode {mode}")
		except AttributeError:
			msg = f"'{mode}' not valid mode of display design! Valid states are {self.DisplayMode.__members__}."
			MODULE_LOGGER.error(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument(msg)
		except enna.data_interfaces.adb.exceptions.ADBException as error:
			msg = f"Display design not set to mode '{mode}'! {error}"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError(msg)

	def __callback_speed(self, message: enna.core.interfaces.Data) -> None:
		"""Set attribute current speed if value this reading from logcat.

		:param message: logcat message
		"""
		MODULE_LOGGER.debug(f"Logcat: {message.value}")
		self._current_speed = float(message.value['extractedParameters']['current_speed'])

	def __callback_gear(self, message: enna.core.interfaces.Data) -> None:
		"""Set attribute current gear if value this reading from logcat.

		:param message: logcat message
		"""
		MODULE_LOGGER.debug(f"Logcat: {message.value}")
		self._current_gear = message.value['extractedParameters']['gear_position']
