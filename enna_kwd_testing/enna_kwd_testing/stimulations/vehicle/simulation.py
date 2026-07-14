# -*- coding: utf-8 -*-
"""Contains stimulation for simulation vehicle environment."""
import logging

import enna.core.component_system.decorators
import enna.core.reporting.interface

import enna_kwd_testing.utilities.vehicle.exceptions
import enna_kwd_testing.utilities.vehicle.interface
import enna_kwd_testing.stimulations.base.keyword_stim_baseclass


MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.vehicle")
class SwitchClamp15(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to switch clamp 15."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, vehicle:  enna_kwd_testing.utilities.vehicle.interface.Interface):
		"""Initialize stimulation.

		:param reporting: Instance of reporting interface.
		:param vehicle: Instance of interface for vehicle simulation
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__vehicle = vehicle
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Execute action.

		Set clamp 15 for target to state defined in instance attribute "values" under key "STATE".

		:return: True if successful, False it susan exception occurs
		:rtype: bool
		"""
		try:
			bool_state = bool(self.values["STATE"])
			self.__vehicle.clamp_15(state=bool_state)
		except enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError as error:
			self._reporting.add_report_message_system_error(f"{error}")
			return False
		self._reporting.add_report_message_pass(f"Set Clamp 15 state to '{bool_state}'.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.vehicle")
class SwitchClampS(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to switch clamp S."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, vehicle:  enna_kwd_testing.utilities.vehicle.interface.Interface):
		"""Initialize stimulation.

		:param reporting: Instance of reporting interface.
		:param vehicle: Instance of interface for vehicle simulation
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__vehicle = vehicle
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Execute action.

		Set clamp S for target to state defined in instance attribute "values" under key "STATE".

		:return: True if successful, False it susan exception occurs
		:rtype: bool
		"""
		try:
			bool_state = bool(self.values["STATE"])
			self.__vehicle.clamp_s(state=bool_state)
		except enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError as error:
			self._reporting.add_report_message_system_error(f"{error}")
			return False
		except enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported as error:
			self._reporting.add_report_message_info(f"{error}")
			return True
		self._reporting.add_report_message_pass(f"Set Clamp S state to '{bool_state}'.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.vehicle")
class SwitchComfortReady(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to switch comfort ready state."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, vehicle:  enna_kwd_testing.utilities.vehicle.interface.Interface):
		"""Initialize stimulation.

		:param reporting: Instance of reporting interface.
		:param vehicle: Instance of interface for vehicle simulation
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__vehicle = vehicle
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Execute action.

		Set comfort ready state for target to state defined in instance attribute "values" under key "STATE".

		:return: True if successful, False it susan exception occurs
		:rtype: bool
		"""
		try:
			bool_state = bool(self.values["STATE"])
			self.__vehicle.comfort_ready_status(state=bool_state)
		except enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError as error:
			self._reporting.add_report_message_system_error(f"{error}")
			return False
		except enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported as error:
			self._reporting.add_report_message_info(f"{error}")
			return True
		self._reporting.add_report_message_pass(f"Set Comfort Ready Status to '{bool_state}'.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.vehicle")
class SetDriveMode(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to ste drive mode."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, vehicle: enna_kwd_testing.utilities.vehicle.interface.Interface):
		"""Initialize stimulation.

		:param reporting: Instance of reporting interface.
		:param vehicle: Instance of interface for vehicle simulation
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__vehicle = vehicle
		self.allowed_parameter_keys = ["GEAR", "SPEED_IN_M_PER_S"]

	def _action(self) -> bool:
		"""Execute action.

		Set gear position and actual speed on susan box

		:return: True if successful, False it susan exception occurs
		:rtype: bool
		"""
		gear: str = self.values.get("GEAR", "PARKING")
		speed_mps: float = float(self.values.get("SPEED_IN_M_PER_S", 0.0))
		try:
			self.__vehicle.gear_selection(gear=gear)
			self.__vehicle.vehicle_speed(speed=speed_mps)
		except enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError as error:
			self._reporting.add_report_message_system_error(f"{error}")
			return False
		self._reporting.add_report_message_pass(f"Set gear to {gear} and velocity to {speed_mps} m/s.")
		return True

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.vehicle")
class SetDriverSeatOccupancy(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Setting Seat Occupancy  for Driver Seat."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, vehicle: enna_kwd_testing.utilities.vehicle.interface.Interface) -> None:
		"""Constructor for Driver Seat Occupancy Controller.

		:param vehicle: Instance of interface for vehicle simulation
		:param reporting: Instance of interface for report handler
		"""
		super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.3")
		self.__vehicle = vehicle
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Set Driver Seat Occupancy.

		:return: Get true if success, else false
		"""
		occupancy_state = self.values.get("STATE", "UNKNOWN")
		try:
			self.__vehicle.driver_seat_occupancy(state=occupancy_state)
		except enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError as error:
			self._reporting.add_report_message_system_error(f"{error}")
			return False
		except enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument as error:
			self._reporting.add_report_message_ta_error(f"{error}")
			return False
		except enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported as error:
			self._reporting.add_report_message_ta_error(f"{error}")
			return False
		self._reporting.add_report_message_pass(f"Set driver seat to state '{occupancy_state}'.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.vehicle")
class SetCoDriverSeatOccupancy(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Setting Seat Occupancy  for Co-Driver Seat."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, vehicle: enna_kwd_testing.utilities.vehicle.interface.Interface) -> None:
		"""Constructor for Co-Driver Seat Occupancy Controller.

		:param vehicle: Instance of interface for vehicle simulation
		:param reporting: Instance of interface for report handler
		"""
		super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.3")
		self.__vehicle = vehicle
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Set Co-Driver Seat Occupancy.

		:return: Get true if success, else false
		"""
		occupancy_state = self.values.get("STATE", "UNKNOWN")
		try:
			self.__vehicle.co_driver_seat_occupancy(state=occupancy_state)
		except enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError as error:
			self._reporting.add_report_message_system_error(f"{error}")
			return False
		except enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument as error:
			self._reporting.add_report_message_ta_error(f"{error}")
			return False
		except enna_kwd_testing.utilities.vehicle.exceptions.SimulationNotSupported as error:
			self._reporting.add_report_message_ta_error(f"{error}")
			return False
		self._reporting.add_report_message_pass(f"Set co-driver seat to state '{occupancy_state}'.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.vehicle")
class SetDisplayDesignMode(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Setting display design mode. Set bus signal from Day/Night-Sensor of vehicle"""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, vehicle: enna_kwd_testing.utilities.vehicle.interface.Interface) -> None:
		"""Constructor for set display design mode.

		:param vehicle: Instance of interface for vehicle simulation
		:param reporting: Instance of interface for report handler
		"""
		super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.3")
		self.__vehicle = vehicle
		self.allowed_parameter_keys = ["MODE"]

	def _action(self) -> bool:
		"""Set display design mode.

		:return: Get true if success, else false
		"""
		display_mode = self.values.get("MODE", "UNKNOWN")
		try:
			self.__vehicle.display_design(mode=display_mode)
		except enna_kwd_testing.utilities.vehicle.exceptions.VehicleSimulationError as error:
			self._reporting.add_report_message_system_error(f"{error}")
			return False
		except enna_kwd_testing.utilities.vehicle.exceptions.InvalidArgument as error:
			self._reporting.add_report_message_ta_error(f"{error}")
			return False
		self._reporting.add_report_message_pass(f"Display design set to mode '{display_mode}'.")
		return True
