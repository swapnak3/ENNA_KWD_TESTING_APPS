# -*- coding: utf-8 -*-
"""Created on 07.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains components to configure vehicles with their specific services.
"""
import abc
import datetime
import logging

from . import odp_requests
from .src.payloads import interface as base
from .. import runtime_storage
from ...exceptions import InvalidParameterException

logger = logging.getLogger(__name__)

# TODO: VSR und RBC allgemein überarbeiten
# TODO: evtl in einzelne Dateien je Dienst aufteilen?


class VSRSource(abc.ABC):
    """Base class for vehicle status report (VSR) services.

    Contains methods to manipulate vsr payload because VSR is such a complex service.
    Payload can be manipulated and will be stored while object exists.
    When payload is manipulated to desired state, it can be sent to backend.
    Defaults can be made by inherited classes by set_vsr_defaults().
    """
    def __init__(self, vin, backend):
        """Initialize object.
        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self._kwargs = dict({})

    def send_request(self):
        """Send current payload to backend."""
        odp_requests.ServiceVSR(self.__vin, self.__backend).set_status(**self._kwargs)

    def set_custom_vsr_values(self, **kwargs):
        """Manipulates payload and sends it to backend.
        Set custom vehicle status report (vsr) payload by keyword arguments

        :param dict kwargs: Keyword arguments to set custom vsr values
        """
        odp_requests.ServiceVSR(self.__vin, self.__backend).set_status(**kwargs)

    def set_all_doors_windows_open_and_lights_on(self):
        """Manipulates payload and sends it to backend.
        Manipulates:
        All doors open.
        All windows open.
        Parking lights on.
        """
        self.payload_open_all_windows()
        self.payload_open_all_doors()
        self.payload_open_frontlid()
        self.payload_open_trunk()
        self.payload_open_sunroof_full()
        self.payload_parking_lights_all_on()
        odp_requests.ServiceVSR(self.__vin, self.__backend).set_status(**self.kwargs)

    def set_all_doors_windows_closed_and_lights_off(self):
        """Manipulates payload and sends it to backend.
        Manipulates:
        All doors closed.
        All windows closed.
        Parking lights off.
        """
        self.payload_close_all_windows()
        self.payload_close_all_doors()
        self.payload_close_frontlid()
        self.payload_close_trunk()
        self.payload_close_sunroof_full()
        self.payload_parking_lights_off()
        odp_requests.ServiceVSR(self.__vin, self.__backend).set_status(**self.kwargs)

    def set_vehicle_unlocked(self):
        """Manipulates payload and sends it to backend.
        Sets vehicle state to "unlocked".
        """
        self.__unlock_vehicle()
        odp_requests.ServiceVSR(self.__vin, self.__backend).set_status(**self.kwargs)

    def set_vehicle_locked(self):
        """Manipulates payload and sends it to backend.
        Sets vehicle state to "locked".
        """
        self.payload_lock_vehicle()
        odp_requests.ServiceVSR(self.__vin, self.__backend).set_status(**self.kwargs)

    def set_doors_open_fl_and_rr(self):
        """Manipulates payload and sends it to backend.
        Sets front left and rear right door open.
        """
        self.payload_open_fl_door()
        self.payload_open_rr_door()
        odp_requests.ServiceVSR(self.__vin, self.__backend).set_status(**self.kwargs)

    def response_to_warnings_job_with_active_warnings(self):
        """Response to active vehicle status report (vsr) job.
        Activates warnings on vehicles warnings tile.
        """
        self.payload_activate_warnings()
        odp_requests.ServiceVSR(self.__vin, self.__backend).response_to_active_job(**self.kwargs)

    def response_to_warnings_job_without_active_warnings(self):
        """Response to active vehicle status report (vsr) job.
        Deactivates warnings on vehicles warnings tile.
        """
        self.payload_deactivate_warnings()
        odp_requests.ServiceVSR(self.__vin, self.__backend).response_to_active_job(**self.kwargs)

    @property
    def kwargs(self):
        """Property for keyword arguments of vehicle status report (vsr) payload.

        :return: List of kwargs
        :rtype: dict
        """
        return self._kwargs

    def __unlock_vehicle(self):
        """Manipulate payload to unlock vehicle. """
        self._kwargs.update(door_fr_locked_bool=base.DoorStateLocked.UNLOCKED.value, door_fl_locked_bool=base.DoorStateLocked.UNLOCKED.value, door_rr_locked_bool=base.DoorStateLocked.UNLOCKED.value,
                            door_rl_locked_bool=base.DoorStateLocked.UNLOCKED.value, frontlid_locked_bool=base.DoorStateLocked.UNLOCKED.value, trunk_locked_bool=base.DoorStateLocked.UNLOCKED.value)

    def payload_lock_vehicle(self):
        """Manipulate payload to lock vehicle."""
        self._kwargs.update(door_fr_locked_bool=base.DoorStateLocked.LOCKED.value, door_fl_locked_bool=base.DoorStateLocked.LOCKED.value, door_rr_locked_bool=base.DoorStateLocked.LOCKED.value,
                            door_rl_locked_bool=base.DoorStateLocked.LOCKED.value, frontlid_locked_bool=base.DoorStateLocked.LOCKED.value, trunk_locked_bool=base.DoorStateLocked.LOCKED.value)

    def payload_open_fr_door(self):
        """Manipulate payload to open front right door. """
        self._kwargs.update(door_fr_locked_bool=base.DoorStateLocked.UNLOCKED.value, door_fr_open_bool=base.DoorStateOpen.OPEN.value, door_fr_safe_bool=base.DoorStateSafe.UNSAFE.value, )

    def payload_open_fl_door(self):
        """Manipulate payload to open front left door. """
        self._kwargs.update(door_fl_locked_bool=base.DoorStateLocked.UNLOCKED.value, door_fl_open_bool=base.DoorStateOpen.OPEN.value, door_fl_safe_bool=base.DoorStateSafe.UNSAFE.value, )

    def payload_open_rr_door(self):
        """Manipulate payload to open rear right door. """
        self._kwargs.update(door_rr_locked_bool=base.DoorStateLocked.UNLOCKED.value, door_rr_open_bool=base.DoorStateOpen.OPEN.value, door_rr_safe_bool=base.DoorStateSafe.UNSAFE.value, )

    def payload_open_rl_door(self):
        """Manipulate payload to open rear left door. """
        self._kwargs.update(door_rl_locked_bool=base.DoorStateLocked.UNLOCKED.value, door_rl_open_bool=base.DoorStateOpen.OPEN.value, door_rl_safe_bool=base.DoorStateSafe.UNSAFE.value, )

    def payload_close_fr_door(self):
        """Manipulate payload to close front right door. """
        self._kwargs.update(door_fr_locked_bool=base.DoorStateLocked.LOCKED.value, door_fr_open_bool=base.DoorStateOpen.CLOSED.value, door_fr_safe_bool=base.DoorStateSafe.SAFE.value, )

    def payload_close_fl_door(self):
        """Manipulate payload to close front left door. """
        self._kwargs.update(door_fl_locked_bool=base.DoorStateLocked.LOCKED.value, door_fl_open_bool=base.DoorStateOpen.CLOSED.value, door_fl_safe_bool=base.DoorStateSafe.SAFE.value, )

    def payload_close_rr_door(self):
        """Manipulate payload to close rear right door. """
        self._kwargs.update(door_rr_locked_bool=base.DoorStateLocked.LOCKED.value, door_rr_open_bool=base.DoorStateOpen.CLOSED.value, door_rr_safe_bool=base.DoorStateSafe.SAFE.value, )

    def payload_close_rl_door(self):
        """Manipulate payload to close rear left door. """
        self._kwargs.update(door_rl_locked_bool=base.DoorStateLocked.LOCKED.value, door_rl_open_bool=base.DoorStateOpen.CLOSED.value, door_rl_safe_bool=base.DoorStateSafe.SAFE.value, )

    def payload_open_all_doors(self):
        """Manipulate payload to open all doors (front left, front right, rear left, rear right). """
        self.payload_open_rl_door()
        self.payload_open_rr_door()
        self.payload_open_fl_door()
        self.payload_open_fr_door()

    def payload_close_all_doors(self):
        """Manipulate payload to open all doors (front left, front right, rear left, rear right). """
        self.payload_close_rl_door()
        self.payload_close_rr_door()
        self.payload_close_fl_door()
        self.payload_close_fr_door()

    def payload_open_frontlid(self):
        """Manipulate payload to open front lid. """
        self._kwargs.update(frontlid_locked_bool=base.DoorStateLocked.UNLOCKED.value, frontlid_open_bool=base.DoorStateOpen.OPEN.value, frontlid_safe_bool=base.DoorStateSafe.UNSAFE.value)

    def payload_close_frontlid(self):
        """Manipulate payload to close front lid. """
        self._kwargs.update(frontlid_locked_bool=base.DoorStateLocked.LOCKED.value, frontlid_open_bool=base.DoorStateOpen.CLOSED.value, frontlid_safe_bool=base.DoorStateSafe.SAFE.value)

    def payload_open_trunk(self):
        """Manipulate payload to open trunk. """
        self._kwargs.update(trunk_locked_bool=base.DoorStateLocked.UNLOCKED.value, trunk_open_bool=base.DoorStateOpen.OPEN.value, trunk_safe_bool=base.DoorStateSafe.UNSAFE.value)

    def payload_close_trunk(self):
        """Manipulate payload to close trunk. """
        self._kwargs.update(trunk_locked_bool=base.DoorStateLocked.LOCKED.value, trunk_open_bool=base.DoorStateOpen.CLOSED.value, trunk_safe_bool=base.DoorStateSafe.SAFE.value)

    def payload_open_sunroof_full(self):
        """Manipulate payload to open sunroof. """
        self._kwargs.update(sunroof_state=base.WindowState.OPEN.value, sunroof_open_percentage="100")

    def payload_close_sunroof_full(self):
        """Manipulate payload to close sunroof. """
        self._kwargs.update(sunroof_state=base.WindowState.CLOSED.value, sunroof_open_percentage="0")

    def payload_parking_lights_left_on(self):
        """Manipulate payload to set left parking lights on. """
        self._kwargs.update(parking_light_state=base.ParkingLights.LEFT.value)

    def payload_parking_lights_right_on(self):
        """Manipulate payload to set right parking lights on. """
        self._kwargs.update(parking_light_state=base.ParkingLights.RIGHT.value)

    def payload_parking_lights_all_on(self):
        """Manipulate payload to set all parking lights on. """
        self._kwargs.update(parking_light_state=base.ParkingLights.BOTH.value)

    def payload_parking_lights_off(self):
        """Manipulate payload to set all parking lights off. """
        self._kwargs.update(parking_light_state=base.ParkingLights.OFF.value)

    def payload_open_fr_window(self):
        """Manipulate payload to open front right window. """
        self._kwargs.update(window_fr_state=base.WindowState.OPEN.value, window_fr_open_percentage="100")

    def payload_open_fl_window(self):
        """Manipulate payload to open front left window. """
        self._kwargs.update(window_fl_state=base.WindowState.OPEN.value, window_fl_open_percentage="100")

    def payload_open_rr_window(self):
        """Manipulate payload to open rear right window. """
        self._kwargs.update(window_rr_state=base.WindowState.OPEN.value, window_rr_open_percentage="100")

    def payload_open_rl_window(self):
        """Manipulate payload to open rear left window. """
        self._kwargs.update(window_rl_state=base.WindowState.OPEN.value, window_rl_open_percentage="100")

    def payload_close_fr_window(self):
        """Manipulate payload to close front right window. """
        self._kwargs.update(window_fr_state=base.WindowState.CLOSED.value, window_fr_open_percentage="0")

    def payload_close_fl_window(self):
        """Manipulate payload to close front left window. """
        self._kwargs.update(window_fl_state=base.WindowState.CLOSED.value, window_fl_open_percentage="0")

    def payload_close_rr_window(self):
        """Manipulate payload to close rear right window. """
        self._kwargs.update(window_rr_state=base.WindowState.CLOSED.value, window_rr_open_percentage="0")

    def payload_close_rl_window(self):
        """Manipulate payload to close rear left window. """
        self._kwargs.update(window_rl_state=base.WindowState.CLOSED.value, window_rl_open_percentage="0")

    def payload_open_all_windows(self):
        """Manipulate payload to open all windows (front left, front right, rear left, rear right). """
        self.payload_open_rl_window()
        self.payload_open_rr_window()
        self.payload_open_fl_window()
        self.payload_open_fr_window()

    def payload_close_all_windows(self):
        """Manipulate payload to close all windows (front left, front right, rear left, rear right). """
        self.payload_close_rl_window()
        self.payload_close_rr_window()
        self.payload_close_fl_window()
        self.payload_close_fr_window()

    def payload_activate_warnings(self):
        """Manipulate payload to activate warning messages. """
        self._kwargs.update(obdc_0203="AwICOTDQyGA9FKInoxeiIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    def payload_deactivate_warnings(self):
        """Manipulate payload to deactivate warning messages."""
        self._kwargs.update(obdc_0203="AwICOTDQyGA9FKAKAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    def payload_set_cruising_range_drive_1(self, value: str):
        """Manipulate payload to set remaining cruising range for primary drive.

        :param str value: Value for primary drive cruising range.
        """
        self._kwargs.update(range_one=value)

    def payload_set_cruising_range_combined(self, value: str):
        """Manipulate payload to set remaining cruising range for secondary drive.

        :param str value: Value for secondary drive cruising range.
        """
        self._kwargs.update(cruising_range_combined=value)

    def payload_set_mileage(self, value: str):
        """Manipulate payload to set vehicle mileage.

        :param str value: Value for vehicle mileage.
        """
        self._kwargs.update(mileage=value)

    def payload_set_service_state(self, obdc_0301, obdc_0404, obdc_040c):
        """Manipulate payload to set service intervals and upcoming service requirements.

        :param str obdc_0301: Value for VSR obdc_0301 data.
        :param str obdc_0404: Value for VSR obdc_0404 data.
        :param str obdc_040c: Value for VSR obdc_040C data.
        """
        self._kwargs.update(obdc_0301=obdc_0301, obdc_0404=obdc_0404, obdc_040C=obdc_040c)

    def payload_set_service_state_oil_level_sufficient(self):
        """Manipulates payload to set oil level sufficient"""
        self.payload_set_service_state(obdc_0301="AQMC/YPQMF7VECAA8gJCAAIgDhEBAQ==",
                                       obdc_0404="BAQC/YPQMF7VEOQH",
                                       obdc_040c="DAQC/YPQMF7VELiLAQ==")

    def payload_set_service_state_oil_level_insufficient(self):
        """Manipulates payload to set oil level insufficient (0%)"""
        self.payload_set_service_state(obdc_0301="AQMC/YPQMF7VECAAAgDiAAAgDhEBAQ==",
                                       obdc_0404="BAQC/YPQMF7VEBAE", obdc_040c="DAQC/YPQMF7VEACAAA==")

    def payload_set_service_state_adblue_level_to_max(self):
        """Manipulates payload to set adblue level to range of > 2400km """
        self.payload_set_service_state(obdc_0301="AQMC/YPQMF7VECAA8gJCAAIgDhEBAQ==",
                                       obdc_0404="BAQC/YPQMF7VEOQH", obdc_040c="DAQC/YPQMF7VELiLAQ==")

    def payload_set_service_state_adblue_level_to_sufficient(self):
        """Manipulates payload to set adblue level to range to 1400km (sufficient) """
        self.payload_set_service_state(obdc_0301="AQMC/YPQMF7VECAAUgACAAUgABEBAQ==",
                                       obdc_0404="BAQC/YPQMF7VEAgJ", obdc_040c="DAQC/YPQMF7VEHiFAQ==")

    def payload_set_service_state_adblue_level_to_min(self):
        """Manipulates payload to set adblue level to range of 0km => Engine start not possible"""
        self.payload_set_service_state(obdc_0301="AQMC/YPQMF7VECAAUgACAAUgABEBAQ==",
                                       obdc_0404="BAQC/YPQMF7VEAgJ", obdc_040c="DAQC/YPQMF7VEACAAA==")

    def payload_set_oil_change_and_inspection_to_not_calculated(self):
        """Manipulates payload to set oil change and inspection to not calculated"""
        self.payload_set_service_state(obdc_0301="AQMC/YPQMF7VEBAAAQABAAAQABEBAQ==",
                                       obdc_0404="BAQC/YPQMF7VEOQH", obdc_040c="DAQC/YPQMF7VEACAAQ==")

    def payload_set_functionality_built_in(self):
        """Manipulates payload to show that OBDC values can be displayed in-app"""
        self.payload_set_service_state(obdc_0301="AQMC/YPQMF7VEBAAAQABAAAQABEBAQ==",
                                       obdc_0404="BAQC/YPQMF7VEOQH", obdc_040c="DAQC/YPQMF7VEACAAQ==")

    @abc.abstractmethod
    def set_vsr_defaults(self):
        """Abstract method.
        Set vsr defaults for specific vehicle type of inherited class.
        """


class VSRCombustionComponent(VSRSource):
    """Vehicle status report (VSR) component for combustion vehicles. """

    def __init__(self, vin, backend):
        """Initialize object and set vsr defaults for vehicle type.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        super().__init__(vin, backend)
        self.__vin = vin
        self.__backend = backend
        self.defaults()
        self.set_vsr_defaults()

    def set_vsr_defaults(self):
        """Sends default payload to backend. """

        self.defaults()
        odp_requests.ServiceVSR(self.__vin, self.__backend).set_status(**self.kwargs)

    def defaults(self):
        """Sets vehicle status report (VSR) defaults for specific vehicle type class.
        """
        self._kwargs.update(range_two="0", engine_type_one=base.EngineType.PETROL_DIESEL.value, engine_type_two=base.EngineType.UNSUPPORTED.value)
        self.payload_set_mileage("16743")
        self.payload_set_service_state("AQMC/YPQMF7VECEB8gESABkhAREBAQ==", "BAQC/YPQMF7VEOQH", "DAQC/YPQMF7VEDKAAQ==")
        self.payload_set_cruising_range_combined("450")
        self.payload_set_cruising_range_drive_1("450")
        self.set_fuel_level("70")
        self.payload_close_all_doors()
        self.payload_close_all_windows()
        self.payload_parking_lights_off()
        self.payload_close_sunroof_full()
        self.payload_close_trunk()
        self.payload_close_frontlid()
        self.payload_deactivate_warnings()

    def set_fuel_level(self, value: str):
        """Manipulate payload to set fuel level for combustion engine.

        :param str value: Value for fuel level in percent.
        """
        self._kwargs.update(fuel_level=value)


class VSRPhevComponent(VSRSource):
    """Vehicle status report (VSR) component for phev vehicles. """

    def __init__(self, vin, backend):
        """Initialize object and set vsr defaults for vehicle type.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        super().__init__(vin, backend)
        self.__vin = vin
        self.__backend = backend
        self.defaults()
        self.set_vsr_defaults()

    def set_vsr_defaults(self):
        """Sends default payload to backend. """

        self.defaults()
        odp_requests.ServiceVSR(self.__vin, self.__backend).set_status(**self.kwargs)

    def defaults(self):
        """Sets vehicle status report (VSR) defaults for specific vehicle type class. """
        self._kwargs.update(engine_type_one=base.EngineType.PETROL_DIESEL.value, engine_type_two=base.EngineType.ELECTRIC.value)
        self.payload_set_mileage("2000")
        self.payload_set_service_state("AQMC/YPQMF7VECEB8gESABkhAREBAQ==", "BAQC/YPQMF7VEOQH", "DAQC/YPQMF7VEDKAAQ==")
        self.payload_set_cruising_range_combined("550")
        self.payload_set_cruising_range_drive_1("600")
        self.set_fuel_level("70")
        self.payload_close_all_doors()
        self.payload_close_all_windows()
        self.payload_parking_lights_off()
        self.payload_close_sunroof_full()
        self.payload_close_trunk()
        self.payload_close_frontlid()
        self.payload_deactivate_warnings()
        self.set_cruising_range_drive_2("50")

    def set_cruising_range_drive_2(self, value: str):
        """Manipulate payload to set cruising range for engine 2.

        :param str value: Value for cruising range for secondary drive.
        """
        self._kwargs.update(range_two=value)

    def set_fuel_level(self, value: str):
        """Manipulate payload to set fuel level of engine 1.

        :param str value: Value for cruising range for primary drive.
        """
        self._kwargs.update(fuel_level=value)

    def set_soc(self, value: str):
        """Manipulate payload to set state of charge (soc) in percent for engine 2.

        :param str value: Value for state of charge for secondary drive.
        """
        self._kwargs.update(soc=value)


class VSRCbevComponent(VSRSource):
    """Vehicle status report (VSR) component for cbev vehicles. """

    def __init__(self, vin, backend):
        """Initialize object and set vsr defaults for vehicle type.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        super().__init__(vin, backend)
        self.__vin = vin
        self.__backend = backend
        self.defaults()
        self.set_vsr_defaults()

    def set_vsr_defaults(self):
        """Sends default payload to backend. """
        self.defaults()
        odp_requests.ServiceVSR(self.__vin, self.__backend).set_status(**self.kwargs)

    def defaults(self):
        """Sets vehicle status report (VSR) defaults for specific vehicle type class. """
        self._kwargs.update(range_two="0", engine_type_one=base.EngineType.ELECTRIC.value, engine_type_two=base.EngineType.UNSUPPORTED.value)
        self.payload_set_mileage("2000")
        self.payload_set_service_state("AQMC/YPQMF7VECEB8gESABkhAREBAQ==", "BAQC/YPQMF7VEOQH", "DAQC/YPQMF7VEDKAAQ==")
        self.payload_set_cruising_range_combined("450")
        self.payload_set_cruising_range_drive_1("450")
        self.set_soc("70")
        self.payload_close_all_doors()
        self.payload_close_all_windows()
        self.payload_parking_lights_off()
        self.payload_close_sunroof_full()
        self.payload_close_trunk()
        self.payload_close_frontlid()
        self.payload_deactivate_warnings()

    def set_soc(self, value: str):
        """Manipulate payload to set state of charge (soc) in percent for vehicles engine.

        :param str value: Value for vehicle´s soc.
        """
        self._kwargs.update(soc=value)


class VSRCngComponent(VSRSource):
    """Vehicle status report (VSR) component for cng gas vehicles. """

    def __init__(self, vin, backend):
        """Initialize object and set vsr defaults for vehicle type.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        super().__init__(vin, backend)
        self.__vin = vin
        self.__backend = backend
        self.defaults()
        self.set_vsr_defaults()

    def set_vsr_defaults(self):
        """Sends default payload to backend. """
        self.defaults()
        odp_requests.ServiceVSR(self.__vin, self.__backend).set_status(**self.kwargs)

    def defaults(self):
        """Sets vehicle status report (VSR) defaults for specific vehicle type class. """
        self._kwargs.update(engine_type_one=base.EngineType.CNG.value, engine_type_two=base.EngineType.PETROL_GASOLINE.value)
        self.payload_set_mileage("32001")
        self.payload_set_service_state("AQMC/YPQMF7VECEB8gESABkhAREBAQ==", "BAQC/YPQMF7VEOQH", "DAQC/YPQMF7VEDKAAQ==")
        self.payload_set_cruising_range_combined("800")
        self.payload_set_cruising_range_drive_1("400")
        self.set_cruising_range_drive_2("400")
        self.payload_close_all_doors()
        self.payload_close_all_windows()
        self.payload_parking_lights_off()
        self.payload_close_sunroof_full()
        self.payload_close_trunk()
        self.payload_close_frontlid()
        self.payload_deactivate_warnings()
        self.set_gas_level("70")
        self.set_fuel_level("70")

    def set_cruising_range_drive_2(self, value: str):
        """Manipulate payload to set cruising range for engine 2.

        :param str value: Value for cruising range for secondary drive.
        """
        self._kwargs.update(range_two=value)

    def set_gas_level(self, value: str):
        """Manipulate payload to set gas level.

        :param str value: Value for gas level.
        """
        self._kwargs.update(gas_level=value)

    def set_fuel_level(self, value: str):
        """Manipulate payload to set fuel level.

        :param str value: Value for fuel level.
        """
        self._kwargs.update(fuel_level=value)


class RAHQuickstartComponent:
    """Remote auxiliary heating (RAH) component for RAH quickstart service. """

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self.status = self.__Status(self.__vin, self.__backend)
        self.jobs = self.__Jobs(self.__vin, self.__backend)

    class __Status:
        """Contains methods to set remote auxiliary heating (RAH) state. """

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def set_state_off(self):
            """Manipulate payload to set rah state OFF and send it to backend. """
            odp_requests.ServiceRAHQuickstart(self.__vin, self.__backend).set_status(trigger=base.RAHTrigger.IMMEDIATELY.value, climatisation_state=base.ClimatisationState.OFF.value,
                                                                                     heater_source=base.HeaterSource.AUTOMATIC.value, heater_mode=base.HeaterMode.COMFORT.value,
                                                                                     start_mode=base.StartMode.HEATING.value, climatisatin_duration="0", remaining_climate_time="0")

        def set_state_on(self, duration: str, remaining: str):
            """Manipulate payload to set rah state ON with custom remaining climate time and send it to backend.

            :param str duration: Full climatisation duration.
            :param str remaining: Remaining climate time.
            """
            odp_requests.ServiceRAHQuickstart(self.__vin, self.__backend).set_status(trigger=base.RAHTrigger.IMMEDIATELY.value, climatisation_state=base.ClimatisationState.HEATING.value,
                                                                                     heater_source=base.HeaterSource.AUTOMATIC.value, heater_mode=base.HeaterMode.COMFORT.value,
                                                                                     start_mode=base.StartMode.HEATING.value, climatisatin_duration=duration,
                                                                                     remaining_climate_time=remaining)

        def set_state_error(self, error: str):
            """Manipulate payload to set an error and send it to backend.

            :raises InvalidParameterException: if Error-Code has an invalid value
            :param str error: Name of the error
            """
            if not odp_requests.ServiceRAHQuickstart.RAHErrorCodes.has_name(error):
                raise InvalidParameterException(f"Error-Code '{error}' is not available")
            odp_requests.ServiceRAHQuickstart(self.__vin, self.__backend).set_status(trigger=base.RAHTrigger.IMMEDIATELY.value, climatisation_state=base.ClimatisationState.OFF.value,
                                                                                     heater_source=base.HeaterSource.AUTOMATIC.value, heater_mode=base.HeaterMode.COMFORT.value,
                                                                                     start_mode=base.StartMode.HEATING.value,
                                                                                     climate_error_code=odp_requests.ServiceRAHQuickstart.RAHErrorCodes[error].value)

    class __Jobs:
        """Contains methods to response to active remote auxiliary heating (RAH) jobs. """

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def response_to_job_heating_on(self, duration: str, remaining: str):
            """Manipulate payload to response to active RAH job with rah state ON and custom remaining heating time.

            :param str duration: Full climatisation duration.
            :param str remaining: Remaining climate time.
            """
            odp_requests.ServiceRAHQuickstart(self.__vin, self.__backend).response_to_active_job(trigger=base.RAHTrigger.IMMEDIATELY.value, climatisation_state=base.ClimatisationState.HEATING.value,
                                                                                                 heater_source=base.HeaterSource.AUTOMATIC.value, heater_mode=base.HeaterMode.COMFORT.value,
                                                                                                 start_mode=base.StartMode.HEATING.value, climatisatin_duration=duration,
                                                                                                 remaining_climate_time=remaining)

        def response_to_job_heating_off(self):
            """Manipulate payload to response to active RAH job with rah state OFF. """
            odp_requests.ServiceRAHQuickstart(self.__vin, self.__backend).response_to_active_job(trigger=base.RAHTrigger.IMMEDIATELY.value, climatisation_state=base.ClimatisationState.OFF.value,
                                                                                                 heater_source=base.HeaterSource.AUTOMATIC.value, heater_mode=base.HeaterMode.COMFORT.value,
                                                                                                 start_mode=base.StartMode.HEATING.value, climatisatin_duration="0", remaining_climate_time="0")

        def response_to_job_with_error(self, error: str):
            """Response to active rah quickstart job with an error.

            :raises InvalidParameterException: if Error-Code has an invalid value
            :param str error: Name of the error
            """
            if not odp_requests.ServiceRAHQuickstart.RAHErrorCodes.has_name(error):
                raise InvalidParameterException(f"Error-Code '{error}' is not available")
            odp_requests.ServiceRAHQuickstart(self.__vin, self.__backend).response_to_active_job_with_error(odp_requests.ServiceRAHQuickstart.RAHErrorCodes[error])


class RAHTimerComponent:
    """Contains methods to set remote auxiliary heating (RAH) timer state. """

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self.status = self.__Status(self.__vin, self.__backend)
        self.jobs = self.__Jobs(self.__vin, self.__backend)

    class __Status:
        """Contains methods to set remote auxiliary heating (RAH) timer state. """

        def __init__(self, vin, backend):
            """Initialize object.
            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def set_all_timer_off(self):
            """Manipulate payload with all rah timer profiles OFF and send it to backend. """
            odp_requests.ServiceRAHTimer(self.__vin, self.__backend).set_status(timer1_state=base.TimerState.NOT_PROGRAMMED.value, timer2_state=base.TimerState.NOT_PROGRAMMED.value)

        def set_timer_on(self, timer_id: int, time: datetime.datetime):
            """Manipulate payload with timer profile active and expected on a custom time and send it to backend.

            :param int timer_id: Number of the timer (1 or 2)
            :param datetime.datetime time: Time to set timer too.
            """
            if timer_id not in (1, 2):
                raise InvalidParameterException("Only Timer-ID 1 or 2 is possible")

            time = time.strftime("%Y-%m-%dT%H:%M:%S")

            kwargs = {f"timer{timer_id}_state": base.TimerState.PROGRAMMED.value, f"timer{timer_id}_time": time}
            odp_requests.ServiceRAHTimer(self.__vin, self.__backend).set_status(**kwargs)

    class __Jobs:
        """Contains methods to response to active remote auxiliary heating (RAH) timer jobs. """

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def response_to_job_timer_on(self, timer_id: int, time: datetime.datetime):
            """Response to rah timer job with timer profile active and expected on a custom time.

            :param int timer_id: Number of the timer (1 or 2)
            :param datetime.datetime time: Time to set timer too.
            """
            if timer_id not in (1, 2):
                raise InvalidParameterException("Only Timer-ID 1 or 2 is possible")

            time = time.strftime("%Y-%m-%dT%H:%M:%S")
            kwargs = {f"timer{timer_id}_state": base.TimerState.PROGRAMMED.value, f"timer{timer_id}_time": time}
            odp_requests.ServiceRAHTimer(self.__vin, self.__backend).response_to_active_job(**kwargs)

        def response_to_job_timer_off(self, timer_id: int):
            """Response to rah timer job with timer profile OFF.

            :param int timer_id: Number of the timer (1 or 2)
            """
            if timer_id not in (1, 2):
                raise InvalidParameterException("Only Timer-ID 1 or 2 is possible")

            kwargs = {f"timer{timer_id}_state": base.TimerState.NOT_PROGRAMMED.value}
            odp_requests.ServiceRAHTimer(self.__vin, self.__backend).response_to_active_job(**kwargs)

        # TODO: Response to Job with error


class RAHB9PATimerComponent:
    """Contains methods to set B9PA remote auxiliary heating (RAH) timer state. """

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self.status = self.__Status(self.__vin, self.__backend)
        self.jobs = self.__Jobs(self.__vin, self.__backend)

    class __Status:
        """Contains methods to set B9PA remote auxiliary heating (RAH) timer state. """

        def __init__(self, vin, backend):
            """Initialize object.
            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def set_all_timer_off(self):
            """Manipulate payload with all B9PA rah timer profiles OFF and send it to backend. """
            odp_requests.ServiceRAHTimerB9PA(self.__vin, self.__backend).set_status(timer1_state=base.TimerState.NOT_PROGRAMMED.value, timer2_state=base.TimerState.NOT_PROGRAMMED.value)

        def set_timer_on(self, timer_id: int, time: datetime.datetime):
            """Manipulate payload with timer profile active and expected on a custom time and send it to backend.

            :param int timer_id: Number of the timer (1 or 2)
            :param datetime.datetime time: Time to set timer too.
            """
            if timer_id not in (1, 2):
                raise InvalidParameterException("Only Timer-ID 1 or 2 is possible")

            time = time.strftime("%Y-%m-%dT%H:%M:%S")
            kwargs = {f"timer{timer_id}_state": base.TimerState.PROGRAMMED.value, f"timer{timer_id}_time": time}
            odp_requests.ServiceRAHTimerB9PA(self.__vin, self.__backend).set_status(**kwargs)

    class __Jobs:
        """Contains methods to response to active B9PA remote auxiliary heating (RAH) timer jobs. """

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def response_to_job_timer_on(self, timer_id: int, time: datetime.datetime, heater_mode: str, start_mode: str):
            """Response to rah timer job with timer profile active and expected on a custom time.

            :param int timer_id: Number of the timer (1 or 2)
            :param datetime.datetime time: Time to set timer  too.
            :param str heater_mode: Heater Mode of the RAH
            :param str start_mode: Starting Mode of the RAH
            """
            if timer_id not in (1, 2):
                raise InvalidParameterException("Only Timer-ID 1 or 2 is possible")

            if not base.HeaterMode.has_name(heater_mode):
                raise InvalidParameterException(f"Heater-Mode '{heater_mode}' is not available")
            if not base.StartMode.has_name(start_mode):
                raise InvalidParameterException(f"Start-Mode '{start_mode}' is not available")

            time = time.strftime("%Y-%m-%dT%H:%M:%S")
            kwargs = {f"timer{timer_id}_state": base.TimerState.PROGRAMMED.value, f"timer{timer_id}_time": time}
            odp_requests.ServiceRAHTimerB9PA(self.__vin, self.__backend).response_to_active_job(**kwargs, heater_mode=base.HeaterMode[heater_mode].value, start_mode=base.StartMode[start_mode].value)

        def response_to_job_timer_off(self, timer_id: int):
            """Response to rah timer job with timer profile OFF.

            :param int timer_id: Number of the timer (1 or 2)
            """
            if timer_id not in (1, 2):
                raise InvalidParameterException("Only Timer-ID 1 or 2 is possible")

            kwargs = {f"timer{timer_id}_state": base.TimerState.NOT_PROGRAMMED.value}
            odp_requests.ServiceRAHTimerB9PA(self.__vin, self.__backend).response_to_active_job(**kwargs)

        # TODO: Response to Job with error


class RHFComponent:
    """Contains methods to access remote honk and flash (RHF) service. """

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self.jobs = self.__Jobs(self.__vin, self.__backend)

    class __Jobs:
        """Contains methods to response to active remote honk and flash (RHF) jobs. """

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def response_to_job_start_honk_and_flash(self, flash_state: str, honk_state: str):
            """Response to active rhf job with success.

            :param str flash_state: State of Flash
            :param str honk_state: State of Honk
            """
            if not base.RHFFlashState.has_name(flash_state):
                raise InvalidParameterException(f"Flash-State '{flash_state}' is not available")
            if not base.RHFHonkState.has_name(honk_state):
                raise InvalidParameterException(f"Honk-State '{honk_state}' is not available")

            odp_requests.ServiceRHF(self.__vin, self.__backend).response_to_active_job(flash_state=base.RHFFlashState[flash_state].value, honk_state=base.RHFHonkState[honk_state].value)

        def response_to_job_with_error(self, error: str):
            """Response to active rhf job with an error.

            :raises InvalidParameterException: if Error-Code has an invalid value
            :param str error: Name of the error
            """
            if not odp_requests.ServiceRHF.RHFErrorCodes.has_name(error):
                raise InvalidParameterException(f"Error-Code '{error}' is not available")
            odp_requests.ServiceRHF(self.__vin, self.__backend).response_to_active_job_with_error(odp_requests.ServiceRHF.RHFErrorCodes[error])


class CarFinderComponent:
    """Contains methods to set a valid gps location for the vehicle. """

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend

    def set_mock_location_from_config(self):
        """Manipulate payload to set geolocation to mock location from environment_config. """
        odp_requests.ServiceCarFinderValidPosition(self.__vin, self.__backend).set_position(longitude=runtime_storage.MOCK_LOCATION["longitude"].replace(".", ""),
                                                                                            latitude=runtime_storage.MOCK_LOCATION["latitude"]. replace(".", ""),
                                                                                            altitude=runtime_storage.MOCK_LOCATION["altitude"])

    def set_geo_location_schlueterstr_ingolstadt(self):
        """Manipulate payload to set geolocation to schlueterstr. 5, Ingolstadt and send it to backend. """
        odp_requests.ServiceCarFinderValidPosition(self.__vin, self.__backend).set_position(longitude="11398262", latitude="48769970")

    def set_geo_location_wankelstr_gaimersheim(self):
        """Manipulate payload to set geolocation to Wankelstr. 1, Gaimersheim and send it to backend. """
        odp_requests.ServiceCarFinderValidPosition(self.__vin, self.__backend).set_position(longitude="11398262", latitude="48769970")

    def set_geo_location(self, longitude: str, latitude: str):
        """Manipulate payload to set geolocation to custom values and send it to backend.

        :param str longitude: Longitude value of geolocation with length of 8 digits.
        :param str latitude: Latitude value of geolocation with length of 8 digits.
        """
        odp_requests.ServiceCarFinderValidPosition(self.__vin, self.__backend).set_position(longitude=longitude, latitude=latitude)

    def set_invalid_position(self):
        """Set invalid (unknown) position for vehicle. """
        odp_requests.ServiceCarFinderInValidPosition(self.__vin, self.__backend).set_invalid_position()


class DWAComponent:
    """Contains methods to trigger a Diebstahl warn anlage (dwa) alarm. """

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self.__vin = vin
        self.jobs = self.__Jobs(self.__vin, self.__backend)

    class __Jobs:
        """Contains methods to trigger a dwa (Diebstahl warn anlage) alarm. """

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def trigger_alarm(self, alarm_reason: str):
            """Trigger a dwa alarm with a specific alarm reason.

            :raises InvalidParameterException: if Alarm-Reason has an invalid value
            """
            if not odp_requests.ServiceDWA.DwaAlarmReasons.has_name(alarm_reason):
                raise InvalidParameterException(f"Alarm-Reason '{alarm_reason}' is not available")
            odp_requests.ServiceDWA(self.__vin, self.__backend).trigger_alarm(alarm_type=odp_requests.ServiceDWA.DwaAlarmReasons[alarm_reason])

        # TODO: trigger alarm with error


class InstalledBaseCgwClu33:
    """Contains methods to upload installed base to vehicle. """

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend

    def upload_installed_base(self):
        """Upload installed base to vehicle / Disable Play Protection."""
        odp_requests.InstalledBaseCgwClu33(self.__vin, self.__backend).install_base()


class InstalledBaseCgwClu31:
    """Contains methods to upload installed base to vehicle. """

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend

    def upload_installed_base(self):
        """Upload installed base to vehicle / Disable Play Protection."""
        odp_requests.InstalledBaseCgwClu31(self.__vin, self.__backend).install_base()


class InstalledBaseCgwMBBDefault:
    """Contains methods to upload installed base to vehicle. """

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend

    def upload_installed_base(self):
        """Upload installed base to vehicle / Disable Play Protection."""
        odp_requests.InstalledBaseCgwMbbDefault(self.__vin, self.__backend).install_base()


class SpeedAlertComponent:
    """Contains methods to access speed alert service."""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self._speed_alert = None
        self.jobs = self.__Jobs(self.__vin, self.__backend, outer=self)
        self.violations = self.__Violations(self.__vin, self.__backend, outer=self)

    @property
    def speed_alert(self):
        """Property speed_alert.

        :return: Speed-Alert-Service
        :rtype: ServiceSpeedAlert
        """
        return self._speed_alert

    @speed_alert.setter
    def speed_alert(self, alert):
        """Setter for property speed_alert.

        :param ServiceSpeedAlert alert: New alert to set
        """
        self._speed_alert = alert

    class __Jobs:
        """Contains methods to response to active speed alert service jobs."""

        def __init__(self, vin, backend, outer):
            """Initialize object.
            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            :param SpeedAlertComponent outer: SpeedAlertComponent, storing active speed alert profile uuid.
            """
            self.__vin = vin
            self.__backend = backend
            self.__outer = outer

        def response_to_profile_activation_job(self):
            """Response successful to a speed alert profile activation job."""
            self.__outer.speed_alert = odp_requests.ServiceSpeedAlert(self.__vin, self.__backend)
            self.__outer.speed_alert.response_to_profile_activation_job()

        def response_to_profile_deactivation_job(self):
            """Response successful to a speed alert profile deactivation job."""
            odp_requests.ServiceSpeedAlert(self.__vin, self.__backend).response_to_profile_deactivation_job()

        # TODO: response_to_job_with_error

    class __Violations:
        """Violate an active speed alert profile."""

        def __init__(self, vin, backend, outer):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            :param SpeedAlertComponent outer: SpeedAlertComponent, storing active speed alert profile uuid.
            """
            self.__vin = vin
            self.__backend = backend
            self.__outer = outer

        def trigger_violation(self, alert_state: str):
            """Start speed alert violation.

            :raises InvalidParameterException: if Alert-State has an invalid value
            :param str alert_state: Alert-State which should be triggered
            """
            if not odp_requests.ServiceSpeedAlert.AlertState.has_name(alert_state):
                raise InvalidParameterException(f"Alert-State '{alert_state}' is not available")
            self.__outer.speed_alert.trigger_alert_violation(odp_requests.ServiceSpeedAlert.AlertState[alert_state])


class GeoFenceAlertComponent:
    """Contains methods to access geofence alert service."""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self._geofence_alert = None
        self.jobs = self.__Jobs(self.__vin, self.__backend, outer=self)
        self.violations = self.__Violations(self.__vin, self.__backend, outer=self)

    @property
    def geofence_alert(self):
        """Property geofence_alert.

        :return: Geofence-Alert-Service
        :rtype: ServiceGeoFenceAlert
        """
        return self._geofence_alert

    @geofence_alert.setter
    def geofence_alert(self, alert):
        """Setter for property geo alert.

        :param ServiceGeoFenceAlert alert: New alert to set
        """
        self._geofence_alert = alert

    class __Jobs:
        """Contains methods to response to active geofence alert service jobs."""

        def __init__(self, vin, backend, outer):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            :param GeoFenceAlertComponent outer: GeoFenceAlertComponent, storing active speed alert profile uuid and area id.
            """
            self.__vin = vin
            self.__backend = backend
            self.__outer = outer

        def response_to_profile_activation_job(self):
            """Response successful to a geofence alert profile activation job."""
            self.__outer.geofence_alert = odp_requests.ServiceGeoFenceAlert(self.__vin, self.__backend)
            self.__outer.geofence_alert.response_to_profile_activation_job()

        def response_to_profile_deactivation_job(self):
            """Response successful to a geofence alert profile deactivation job."""
            odp_requests.ServiceGeoFenceAlert(self.__vin, self.__backend).response_to_profile_deactivation_job()

        # TODO: response_to_job_with_error

    class __Violations:
        """Violate an active geofence alert profile."""

        def __init__(self, vin, backend, outer):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            :param GeoFenceAlertComponent outer: GeoFenceAlertComponent, storing active speed alert profile uuid and area id.
            """
            self.__vin = vin
            self.__backend = backend
            self.__outer = outer

        def trigger_violation(self, event_type: str):
            """Start speed alert violation.

            :raises InvalidParameterException: if Event-Type has an invalid value
            :param str event_type: Event-Type which should be triggered
            """
            if not odp_requests.ServiceGeoFenceAlert.EventType.has_name(event_type):
                raise InvalidParameterException(f"Event-Type '{event_type}' is not available")
            self.__outer.geofence_alert.trigger_alert_violation(odp_requests.ServiceGeoFenceAlert.EventType[event_type])


class ValetAlertComponent:
    """Contains methods to access valet alert service."""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self._valet_alert = None
        self.jobs = self.__Jobs(self.__vin, self.__backend, outer=self)
        self.violations = self.__Violations(self.__vin, self.__backend, outer=self)

    @property
    def valet_alert(self):
        """Property valet_alert

        :return: Valet-Alert-Service
        :rtype: ServiceValetAlert
        """
        return self._valet_alert

    @valet_alert.setter
    def valet_alert(self, alert):
        """Setter for property valet_alert

        :param ServiceValetAlert alert: New alert to set
        """
        self._valet_alert = alert

    class __Jobs:
        """Contains methods to response to active valet alert jobs."""

        def __init__(self, vin, backend, outer):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            :param ValetAlertComponent outer: ValetAlertComponent, storing active valet alert id.
            """
            self.__vin = vin
            self.__backend = backend
            self.__outer = outer

        def response_to_profile_activation_job(self):
            """Response successful to active valet alert profile activation job."""
            self.__outer.valet_alert = odp_requests.ServiceValetAlert(self.__vin, self.__backend)
            self.__outer.valet_alert.response_to_profile_activation_job()

        def response_to_profile_deactivation_job(self):
            """Response successful to active valet alert profile deactivation job."""
            odp_requests.ServiceValetAlert(self.__vin, self.__backend).response_to_profile_deactivation_job()

        def response_to_profile_activation_job_with_error(self, error: str):
            """Response with error to active valet alert profile activation job.

            :raises InvalidParameterException: if Error-Code has an invalid value
            :param str error: Name of the error
            """
            if not odp_requests.ServiceValetAlert.ValetAlertErrorCodes.has_name(error):
                raise InvalidParameterException(f"Error-Code '{error}' is not available")
            odp_requests.ServiceValetAlert(self.__vin, self.__backend).response_to_profile_activation_job_with_error(odp_requests.ServiceValetAlert.ValetAlertErrorCodes[error])

        def response_to_profile_deactivation_job_with_error(self, error: str):
            """Response with error to active valet alert profile deactivation job.

            :raises InvalidParameterException: if Error-Code has an invalid value
            :param str error: Name of the error
            """
            if not odp_requests.ServiceValetAlert.ValetAlertErrorCodes.has_name(error):
                raise InvalidParameterException(f"Error-Code '{error}' is not available")
            odp_requests.ServiceValetAlert(self.__vin, self.__backend).response_to_profile_deactivation_job_with_error(odp_requests.ServiceValetAlert.ValetAlertErrorCodes[error])

    class __Violations:

        def __init__(self, vin, backend, outer):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            :param ValetAlertComponent outer: ValetAlertComponent, storing active valet alert id.
            """
            self.__vin = vin
            self.__backend = backend
            self.__outer = outer

        def trigger_speed_violation(self, alert_state: str):
            """Start speed alert violation inside the valet alert.

            :raises InvalidParameterException: if Alert-State has an invalid value
            :param str alert_state: Alert-State which should be triggered
            """
            if not odp_requests.ServiceValetAlert.SpeedAlertState.has_name(alert_state):
                raise InvalidParameterException(f"Alert-State '{alert_state}' is not available")
            self.__outer.valet_alert.trigger_speed_alert_violation(odp_requests.ServiceValetAlert.SpeedAlertState[alert_state])

        def trigger_geofence_violation(self, event_type: str):
            """Start speed alert violation inside the valet alert.

            :raises InvalidParameterException: if Event-Type has an invalid value
            :param str event_type: Event-Type which should be triggered
            """
            if not odp_requests.ServiceValetAlert.GeoFenceEventType.has_name(event_type):
                raise InvalidParameterException(f"Event-Type '{event_type}' is not available")
            self.__outer.valet_alert.trigger_geofence_alert_violation(odp_requests.ServiceValetAlert.GeoFenceEventType[event_type])


# TODO: Allgemein überarbeiten
class RBCQuickstartPHEV:
    """Contains methods to access remote battery charging (RBC) service for phev vehicle."""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self.status = self.__Status(self.__vin, self.__backend)
        self.jobs = self.__Jobs(self.__vin, self.__backend)

    class __Status:
        """Contains methods to set remote battery charging (RBC) status for phev vehicle."""

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def set_charging_on_1500_minutes_remaining(self, led_color=base.LEDColor.GREEN.value):
            """Manipulate payload to set charging state ON with 1500 minutes time remaining.

            :param backend.payloads.interface.Payload.LEDColor led_color: Visible color for charging state.
            """
            odp_requests.ServiceRBCPHEV(self.__vin, self.__backend).set_status(remaining_charging_time="1500", charging_plug_lock_state=base.ChargingPlugLockState.LOCKED.value,
                                                                               charging_plug_connect_state=base.ChargingPlugConnState.CONNECTED.value,
                                                                               charging_state=base.ChargingState.CHARGING.value, led_color=led_color,
                                                                               led_state=base.LEDState.PERMANENT_ON.value, trigger=base.TriggerCharging.IMMEDIATELY.value,
                                                                               charging_mode=base.ChargingMode.AC.value, engery_flow=base.EnergyFlow.ON.value,
                                                                               ext_pwr_supply_state=base.ExtPowerSupplyState.STATION_CONNECTED.value)

        def set_charging_on_invalid_charging_time(self, led_color=base.LEDColor.GREEN.value):
            """Manipulate payload to set charging state ON with invalid charging time remaining.

            :param backend.payloads.interface.Payload.LEDColor led_color: Visible color for charging state.
            """
            odp_requests.ServiceRBCPHEV(self.__vin, self.__backend).set_status(remaining_charging_time="1501", charging_plug_lock_state=base.ChargingPlugLockState.LOCKED.value,
                                                                               charging_plug_connect_state=base.ChargingPlugConnState.CONNECTED.value,
                                                                               charging_state=base.ChargingState.CHARGING.value, led_color=led_color,
                                                                               led_state=base.LEDState.PERMANENT_ON.value, trigger=base.TriggerCharging.IMMEDIATELY.value,
                                                                               charging_mode=base.ChargingMode.AC.value, engery_flow=base.EnergyFlow.ON.value,
                                                                               ext_pwr_supply_state=base.ExtPowerSupplyState.STATION_CONNECTED.value)

        def set_charging_off(self):
            """Manipulate payload to set charging state off."""
            odp_requests.ServiceRBCPHEV(self.__vin, self.__backend).set_status(remaining_charging_time="0", charging_plug_lock_state=base.ChargingPlugLockState.LOCKED.value,
                                                                               charging_plug_connect_state=base.ChargingPlugConnState.CONNECTED.value,
                                                                               charging_state=base.ChargingState.OFF.value, led_color=base.LEDColor.GREEN.value,
                                                                               led_state=base.LEDState.OFF.value, trigger=base.TriggerCharging.IMMEDIATELY.value,
                                                                               charging_mode=base.ChargingMode.AC.value, engery_flow=base.EnergyFlow.ON.value,
                                                                               ext_pwr_supply_state=base.ExtPowerSupplyState.STATION_CONNECTED.value)

        def set_charging_off_range_50_km_soc_30p(self):
            """Manipulate payload to set charging state off."""
            odp_requests.ServiceRBCPHEV(self.__vin, self.__backend).set_status(remaining_charging_time="0", charging_plug_lock_state=base.ChargingPlugLockState.LOCKED.value,
                                                                               charging_plug_connect_state=base.ChargingPlugConnState.CONNECTED.value,
                                                                               charging_state=base.ChargingState.OFF.value, led_color=base.LEDColor.GREEN.value,
                                                                               led_state=base.LEDState.OFF.value, trigger=base.TriggerCharging.IMMEDIATELY.value,
                                                                               charging_mode=base.ChargingMode.AC.value, engery_flow=base.EnergyFlow.ON.value,
                                                                               ext_pwr_supply_state=base.ExtPowerSupplyState.STATION_CONNECTED.value, range_two="50", soc="30")

        def set_charging_on_custom_time(self, remaining_time: str, led_color=base.LEDColor.GREEN.value, electric_range="30"):
            """Manipulate payload to set charging state ON with custom time remaining.

            :param str remaining_time: Time of charging which is remaining.
            :param backend.payloads.interface.Payload.LEDColor led_color: Visible color for charging state.
            :param electric_range: Remaining Range in Percent
            """
            odp_requests.ServiceRBCPHEV(self.__vin, self.__backend).set_status(remaining_charging_time=remaining_time, charging_plug_lock_state=base.ChargingPlugLockState.LOCKED.value,
                                                                               charging_plug_connect_state=base.ChargingPlugConnState.CONNECTED.value,
                                                                               charging_state=base.ChargingState.CHARGING.value, led_color=led_color,
                                                                               led_state=base.LEDState.PERMANENT_ON.value, trigger=base.TriggerCharging.IMMEDIATELY.value,
                                                                               charging_mode=base.ChargingMode.AC.value, engery_flow=base.EnergyFlow.ON.value,
                                                                               ext_pwr_supply_state=base.ExtPowerSupplyState.STATION_CONNECTED.value, range_two=electric_range)

        def set_charging_state_charging_off(self, soc=50):
            """Manipulate payload to set charging state OFF.

            :param int soc: State of charge which should be set for vehicle.
            """
            soc = str(soc)
            odp_requests.ServiceRBCPHEV(self.__vin, self.__backend).set_status(remaining_charging_time="0", charging_plug_lock_state=base.ChargingPlugLockState.LOCKED.value,
                                                                               charging_plug_connect_state=base.ChargingPlugConnState.CONNECTED.value,
                                                                               charging_state=base.ChargingState.OFF.value, led_state=base.LEDState.OFF.value,
                                                                               trigger=base.TriggerCharging.IMMEDIATELY.value, soc=soc, charging_mode=base.ChargingMode.AC.value,
                                                                               engery_flow=base.EnergyFlow.ON.value, ext_pwr_supply_state=base.ExtPowerSupplyState.STATION_CONNECTED.value)

    class __Jobs:
        """Contains methods to respond to remote battery charging (RBC) jobs for phev vehicle."""

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def response_to_job_charging_on_custom_time(self, remaining_time: str, led_color=base.LEDColor.GREEN.value):
            """Response to active rbc job with charging state ON and custom time remaining.

            :param str remaining_time: Time of charging remaining.
            :param backend.payloads.interface.Payload.LEDColor led_color: Visible color for charging state.
            """
            odp_requests.ServiceRBCPHEV(self.__vin, self.__backend).response_to_active_job(remaining_charging_time=remaining_time, charging_plug_lock_state=base.ChargingPlugLockState.LOCKED.value,
                                                                                           charging_plug_connect_state=base.ChargingPlugConnState.CONNECTED.value,
                                                                                           charging_state=base.ChargingState.CHARGING.value, led_color=led_color,
                                                                                           led_state=base.LEDState.PERMANENT_ON.value, trigger=base.TriggerCharging.IMMEDIATELY.value,
                                                                                           charging_mode=base.ChargingMode.AC.value, engery_flow=base.EnergyFlow.ON.value,
                                                                                           ext_pwr_supply_state=base.ExtPowerSupplyState.STATION_CONNECTED.value)

        def response_to_job_charging_off(self, soc=50):
            """Response to active rbc job with charging state OFF.

            :param int soc: State of charge to set for vehicle.
            """
            soc = str(soc)
            odp_requests.ServiceRBCCBEV(self.__vin, self.__backend).set_status(remaining_charging_time="0", charging_plug_lock_state=base.ChargingPlugLockState.LOCKED.value,
                                                                               charging_plug_connect_state=base.ChargingPlugConnState.CONNECTED.value,
                                                                               charging_state=base.ChargingState.OFF.value, led_state=base.LEDState.OFF.value,
                                                                               trigger=base.TriggerCharging.IMMEDIATELY.value, soc=soc)

        def response_to_job_with_error(self, error: str):
            """Response to active RBC quickstart job for PHEV vehicle with an error.

            :raises InvalidParameterException: if Error-Code has an invalid value
            :param str error: Name of the error
            """
            if not odp_requests.ServiceRBCPHEV.RBCErrorCodes.has_name(error):
                raise InvalidParameterException(f"Error-Code '{error}' is not available")
            odp_requests.ServiceRBCPHEV(self.__vin, self.__backend).response_to_active_job_with_error(odp_requests.ServiceRBCPHEV.RBCErrorCodes[error])


# TODO: Allgemein überarbeiten
class RBCQuickstartCBEV:
    """Contains methods to access remote battery charging (RBC) service for cbev vehicle.
     """

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self.jobs = self.__Jobs(self.__vin, self.__backend)
        self.status = self.__SetStatus(self.__vin, self.__backend)

    class __SetStatus:
        """Contains methods to set remote battery charging (RBC) status for cbev vehicle."""

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def set_charging_on_remaining_30_min_soc_80_pwr_120000_rate_117_range_400(self, led_color=base.LEDColor.GREEN.value):
            """Set charging state ON with 30 minutes remaining time, a state of charge to 80 percent,
            charging power 120 kW, charging rate, m/s, cruising range 400 km.

            :param backend.payloads.interface.Payload.LEDColor led_color: Visible color for charging state.
            """
            range_drive_one = 400
            state_of_charge = 80
            charging_power = 120_000
            starttime = datetime.datetime.now()
            endtime = starttime + datetime.timedelta(minutes=30)
            endtime_day = endtime.day
            endtime_hour = endtime.hour
            endtime_minute = endtime.minute
            endtime_month = endtime.month
            endtime_year = endtime.year
            duration_numeric = (endtime - starttime).seconds / 60
            duration = f"{duration_numeric:02.0f}"

            odp_requests.ServiceRBCCBEV(self.__vin, self.__backend).set_status(target_time_day=endtime_day, target_time_hour=endtime_hour, target_time_minute=endtime_minute,
                                                                               target_time_month=endtime_month, target_time_year=endtime_year, remaining_charging_time=duration,
                                                                               range_one=range_drive_one, soc=state_of_charge,
                                                                               charging_plug_lock_state=base.ChargingPlugLockState.LOCKED.value,
                                                                               charging_plug_connect_state=base.ChargingPlugConnState.CONNECTED.value, charging_power=charging_power,
                                                                               charging_state=base.ChargingState.CHARGING.value, led_color=led_color,
                                                                               led_state=base.LEDState.PERMANENT_ON.value,
                                                                               charging_rate_unit=base.ChargingRateUnit.KM_PER_H.value, charging_rate=117)

        def set_charging_off_range_400_soc_80(self):
            """Set charging state off with a cruising range of 400 km and a state of charge of 80 percent."""
            range_drive_one = 400
            state_of_charge = 80
            odp_requests.ServiceRBCCBEV(self.__vin, self.__backend).set_status(remaining_charging_time=0, range_one=range_drive_one, soc=state_of_charge,
                                                                               charging_plug_lock_state=base.ChargingPlugLockState.LOCKED.value,
                                                                               charging_plug_connect_state=base.ChargingPlugConnState.CONNECTED.value,
                                                                               charging_state=base.ChargingState.OFF.value,
                                                                               led_state=base.LEDState.OFF.value, charging_rate=117)

        def set_charging_on_custom_values(self, duration: int, state_of_charge=80, range_drive_one=400, led_color=base.LEDColor.GREEN.value):
            """Set charging state ON with custom values.

            :param int duration: Time of charging remaining.
            :param int state_of_charge: Current charging state in percent.
            :param int range_drive_one: Current range of engine 1.
            :param backend.payloads.interface.Payload.LEDColor led_color: Visible color for charging state.
            """
            charging_power = 120_000
            starttime = datetime.datetime.now()
            endtime = starttime + datetime.timedelta(minutes=duration)
            endtime_day = endtime.day
            endtime_hour = endtime.hour
            endtime_minute = endtime.minute
            endtime_month = endtime.month
            endtime_year = endtime.year
            duration_numeric = (endtime - starttime).seconds / 60
            duration = f"{duration_numeric:02.0f}"
            odp_requests.ServiceRBCCBEV(self.__vin, self.__backend).set_status(target_time_day=endtime_day, target_time_hour=endtime_hour, target_time_minute=endtime_minute,
                                                                               target_time_month=endtime_month, target_time_year=endtime_year, remaining_charging_time=duration,
                                                                               range_one=range_drive_one, soc=state_of_charge,
                                                                               charging_plug_lock_state=base.ChargingPlugLockState.LOCKED.value,
                                                                               charging_plug_connect_state=base.ChargingPlugConnState.CONNECTED.value, charging_power=charging_power,
                                                                               charging_state=base.ChargingState.CHARGING.value, led_color=led_color,
                                                                               led_state=base.LEDState.PERMANENT_ON.value,
                                                                               charging_rate_unit=base.ChargingRateUnit.KM_PER_H.value, charging_rate=117)

        def set_charging_state_charging_off(self, soc=50):
            """Set charging state ON with a current state of charging of 50 percent values.

            :param int soc: Current state of charge.
            """
            soc = str(soc)
            odp_requests.ServiceRBCCBEV(self.__vin, self.__backend).set_status(remaining_charging_time="0", charging_plug_lock_state=base.ChargingPlugLockState.LOCKED.value,
                                                                               charging_plug_connect_state=base.ChargingPlugConnState.CONNECTED.value,
                                                                               charging_state=base.ChargingState.OFF.value, led_state=base.LEDState.OFF.value,
                                                                               trigger=base.TriggerCharging.IMMEDIATELY.value, soc=soc)

    class __Jobs:
        """Contains methods to response to active remote battery charging (RBC) job for cbev vehicle."""

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def response_to_job_on_custom_values(self, duration: int, state_of_charge=80, range_drive_one=400, led_color=base.LEDColor.GREEN.value):
            """Response to an active remote battery charging (RBC) job with charging ON and custom values.

            :param int duration: Remaining duration of charging.
            :param int state_of_charge: Current soc in percent.
            :param int range_drive_one: Current remaining cruising range for engine one.
            :param backend.payloads.interface.Payload.LEDColor led_color: Visible color for charging state.
            """
            charging_power = 120_000
            starttime = datetime.datetime.now()
            endtime = starttime + datetime.timedelta(minutes=duration)
            endtime_day = endtime.day
            endtime_hour = endtime.hour
            endtime_minute = endtime.minute
            endtime_month = endtime.month
            endtime_year = endtime.year
            duration_numeric = (endtime - starttime).seconds / 60
            duration = f"{duration_numeric:02.0f}"
            odp_requests.ServiceRBCCBEV(self.__vin, self.__backend).response_to_active_job(target_time_day=endtime_day, target_time_hour=endtime_hour, target_time_minute=endtime_minute,
                                                                                           target_time_month=endtime_month, target_time_year=endtime_year, remaining_charging_time=duration,
                                                                                           range_one=range_drive_one, soc=state_of_charge,
                                                                                           charging_plug_lock_state=base.ChargingPlugLockState.LOCKED.value,
                                                                                           charging_plug_connect_state=base.ChargingPlugConnState.CONNECTED.value, charging_power=charging_power,
                                                                                           charging_state=base.ChargingState.CHARGING.value, led_color=led_color,
                                                                                           led_state=base.LEDState.PERMANENT_ON.value,
                                                                                           charging_rate_unit=base.ChargingRateUnit.KM_PER_H.value, charging_rate=117)

        def response_to_job_with_error(self, error: str):
            """Response to active RBC quickstart job for CBEV with an error.

            :raises InvalidParameterException: if Error-Code has an invalid value
            :param str error: Name of the error
            """
            if not odp_requests.ServiceRBCPHEV.RBCErrorCodes.has_name(error):
                raise InvalidParameterException(f"Error-Code '{error}' is not available")
            odp_requests.ServiceRBCCBEV(self.__vin, self.__backend).response_to_active_job_with_error(odp_requests.ServiceRBCPHEV.RBCErrorCodes[error])


class RPTProfile:
    """Contains methods to access RPT (Remote Profile and Timer Programming) Profile Service"""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self.jobs = self.__Jobs(self.__vin, self.__backend)

    class __Jobs:
        """Contains methods to response to active jobs"""

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        # TODO: Define Jobs

        def response_to_job_with_error(self, error: str):
            """Response to active RPT-Profile job with an error.

            :raises InvalidParameterException: if Error-Code has an invalid value
            :param str error: Name of the error
            """
            if not odp_requests.ServiceRPTProfile.RPTProfileErrorCodes.has_name(error):
                raise InvalidParameterException(f"Error-Code '{error}' is not available")
            odp_requests.ServiceRPTProfile(self.__vin, self.__backend).response_to_active_job_with_error(odp_requests.ServiceRPTProfile.RPTProfileErrorCodes[error])


class RPTTimer:
    """Contains methods to access RPT (Remote Profile and Timer Programming) Timer Service"""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self.jobs = self.__Jobs(self.__vin, self.__backend)

    class __Jobs:
        """Contains methods to response to active jobs"""

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        # TODO: Define Jobs

        def response_to_job_with_error(self, error: str):
            """Response to active RPT-Timer job with an error.

            :raises InvalidParameterException: if Error-Code has an invalid value
            :param str error: Name of the error
            """
            if not odp_requests.ServiceRPTTimer.RPTTimerErrorCodes.has_name(error):
                raise InvalidParameterException(f"Error-Code '{error}' is not available")
            odp_requests.ServiceRPTTimer(self.__vin, self.__backend).response_to_active_job_with_error(odp_requests.ServiceRPTTimer.RPTTimerErrorCodes[error])


class RDT:
    """Contains methods to access RDT (Remote Departure Timer) Service"""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self.jobs = self.__Jobs(self.__vin, self.__backend)

    class __Jobs:
        """Contains methods to response to active jobs"""

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def response_to_job_timer_off(self, timer_id: int):
            if timer_id == 1:
                timer_id_mapped = 3
            elif timer_id == 2:
                timer_id_mapped = 4
            else:
                raise InvalidParameterException("Only Timer-ID 1 or 2 is possible")

            kwargs = {f"timer{timer_id_mapped}_programmed_status": base.TimerProgrammedStatus.PROGRAMMED.value}

            odp_requests.ServiceRDT(self.__vin, self.__backend).response_to_active_job(**kwargs)

        def response_to_job_timer_on(self, timer_id: int, departure_time: datetime.datetime, heater_source: str):
            if timer_id == 1:
                timer_id_mapped = 3
            elif timer_id == 2:
                timer_id_mapped = 4
            else:
                raise InvalidParameterException("Only Timer-ID 1 or 2 is possible")

            if not base.HeaterSource.has_name(heater_source):
                raise InvalidParameterException(f"Heater-Source '{heater_source}' is not available")

            kwargs = {f"profile{timer_id_mapped}_departure_heater_source": base.HeaterSource[heater_source].value,
                      f"profile{timer_id_mapped}_departure_climate": base.DepartureClimateState.TRUE.value,
                      f"timer{timer_id_mapped}_departure_time": departure_time.strftime("%Y-%m-%dT%H:%M:%S"),
                      f"timer{timer_id_mapped}_programmed_status": base.TimerProgrammedStatus.PROGRAMMED.value}

            odp_requests.ServiceRDT(self.__vin, self.__backend).response_to_active_job(**kwargs)

        def response_to_job_with_error(self, error: str):
            """Response to active RDT job with an error.

            :raises InvalidParameterException: if Error-Code has an invalid value
            :param str error: Name of the error
            """
            if not odp_requests.ServiceRDT.RDTErrorCodes.has_name(error):
                raise InvalidParameterException(f"Error-Code '{error}' is not available")
            odp_requests.ServiceRDT(self.__vin, self.__backend).response_to_active_job_with_error(odp_requests.ServiceRDT.RDTErrorCodes[error])


class RDTExtended:
    """Contains methods to access Extended RDT (Remote Departure Timer) Service"""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self.jobs = self.__Jobs(self.__vin, self.__backend)

    class __Jobs:
        """Contains methods to response to active jobs"""

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def response_to_job_timer_on(self,
                                     timer_id: int,
                                     departure_time: datetime.datetime,
                                     heater_source: str,
                                     front_left_seat: str,
                                     front_right_seat: str,
                                     rear_left_seat: str,
                                     rear_right_seat: str):
            if timer_id == 1:
                timer_id_mapped = 3
            elif timer_id == 2:
                timer_id_mapped = 4
            else:
                raise InvalidParameterException("Only Timer-ID 1 or 2 is possible")

            if not base.HeaterSource.has_name(heater_source):
                raise InvalidParameterException(f"Heater-Source '{heater_source}' is not available")
            if not base.ClimatisationPositionState.has_name(front_left_seat):
                raise InvalidParameterException(f"Front-Left-Seat-Value '{front_left_seat}' is not available")
            if not base.ClimatisationPositionState.has_name(front_right_seat):
                raise InvalidParameterException(f"Front-Right-Seat-Value '{front_right_seat}' is not available")
            if not base.ClimatisationPositionState.has_name(rear_left_seat):
                raise InvalidParameterException(f"Rear-Left-Seat-Value '{rear_left_seat}' is not available")
            if not base.ClimatisationPositionState.has_name(rear_right_seat):
                raise InvalidParameterException(f"Rear-Right-Seat-Value '{rear_right_seat}' is not available")

            kwargs = {f"profile{timer_id_mapped}_departure_heater_source": base.HeaterSource[heater_source].value,
                      f"profile{timer_id_mapped}_departure_climate": base.DepartureClimateState.TRUE.value,
                      f"timer{timer_id_mapped}_departure_time": departure_time.strftime("%Y-%m-%dT%H:%M:%S"),
                      f"timer{timer_id_mapped}_programmed_status": base.TimerProgrammedStatus.PROGRAMMED.value}

            # TODO: Glasflächenheizung welcher Parameter?!

            odp_requests.ServiceRDTExtended(self.__vin, self.__backend).response_to_active_job(**kwargs,
                                                                                               climatisation_position_front_left_state=base.ClimatisationPositionState[front_left_seat].value,
                                                                                               climatisation_position_front_right_state=base.ClimatisationPositionState[front_right_seat].value,
                                                                                               climatisation_position_rear_left_state=base.ClimatisationPositionState[rear_left_seat].value,
                                                                                               climatisation_position_rear_right_state=base.ClimatisationPositionState[rear_right_seat].value)

        def response_to_job_with_error(self, error: str):
            """Response to active RDT-Extended job with an error.

            :raises InvalidParameterException: if Error-Code has an invalid value
            :param str error: Name of the error
            """
            if not odp_requests.ServiceRDTExtended.RDTExtendedErrorCodes.has_name(error):
                raise InvalidParameterException(f"Error-Code '{error}' is not available")
            odp_requests.ServiceRDTExtended(self.__vin, self.__backend).response_to_active_job_with_error(odp_requests.ServiceRDTExtended.RDTExtendedErrorCodes[error])


class RPC:
    """Contains methods to access RPC Service"""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self.jobs = self.__Jobs(self.__vin, self.__backend)

    class __Jobs:
        """Contains methods to response to active jobs"""

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def response_to_job_climatisation_on(self, duration: str, remaining: str, heater_source: str, climatisation_state: str):
            """Manipulate payload to response to activate climatisation

            :raises InvalidParameterException: if Heater-Source or Climatisation-State has an invalid value
            :param str duration: Climatisation duration.
            :param str remaining: Remaining Climatisation time.
            :param str heater_source: Heater Source.
            :param str climatisation_state: State of the climatisation.
            """
            if not base.HeaterSource.has_name(heater_source):
                raise InvalidParameterException(f"Heater-Source '{heater_source}' is not available")
            if not base.ClimatisationState.has_name(climatisation_state):
                raise InvalidParameterException(f"Climatisation-State {climatisation_state} is not available")
            odp_requests.ServiceRPC(self.__vin, self.__backend).response_to_active_job(climatisation_duration=duration,
                                                                                       remaining_climate_time=remaining,
                                                                                       heater_source=base.HeaterSource[heater_source].value,
                                                                                       climatisation_state=base.ClimatisationState[climatisation_state].value)

        def response_to_job_climatisation_off(self):
            """Manipulate payload to response to deactivate climatisation"""
            odp_requests.ServiceRPC(self.__vin, self.__backend).response_to_active_job(remaining_climate_time="0",
                                                                                       climatisation_duration="0",
                                                                                       heater_source=base.HeaterSource.AUTOMATIC.value,
                                                                                       climatisation_state=base.ClimatisationState.OFF.value)

        def response_to_job_with_error(self, error: str):
            """Response to active RPC job with an error.

            :raises InvalidParameterException: if Error-Code has an invalid value
            :param str error: Name of the error
            """
            if not odp_requests.ServiceRPC.RPCErrorCodes.has_name(error):
                raise InvalidParameterException(f"Error-Code '{error}' is not available")
            odp_requests.ServiceRPC(self.__vin, self.__backend).response_to_active_job_with_error(odp_requests.ServiceRPC.RPCErrorCodes[error])


class RPCExtended:
    """Contains methods to access Extended RPC Service"""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.__vin = vin
        self.__backend = backend
        self.jobs = self.__Jobs(self.__vin, self.__backend)

    class __Jobs:
        """Contains methods to response to active jobs"""

        def __init__(self, vin, backend):
            """Initialize object.

            :param str vin: VIN to access by backend session.
            :param str backend: Backend where VIN is located.
            """
            self.__vin = vin
            self.__backend = backend

        def response_to_job_climatisation_on(self, duration: str, remaining: str, heater_source: str, climatisation_state: str):
            """Manipulate payload to response to activate extended climatisation

            :raises InvalidParameterException: if Heater-Source or Climatisation-State has an invalid value
            :param str duration: Climatisation duration.
            :param str remaining: Remaining Climatisation time.
            :param str heater_source: Heater Source.
            :param str climatisation_state: State of the climatisation.
            """
            if not base.HeaterSource.has_name(heater_source):
                raise InvalidParameterException(f"Heater-Source '{heater_source}' is not available")
            if not base.ClimatisationState.has_name(climatisation_state):
                raise InvalidParameterException(f"Climatisation-State '{climatisation_state}' is not available")
            odp_requests.ServiceRPCExtended(self.__vin, self.__backend).response_to_active_job(climatisation_duration=duration,
                                                                                               remaining_climate_time=remaining,
                                                                                               heater_source=base.HeaterSource[heater_source].value,
                                                                                               climatisation_state=base.ClimatisationState[climatisation_state].value)

        def response_to_job_climatisation_off(self):
            """Manipulate payload to response to deactivate extended climatisation"""
            odp_requests.ServiceRPCExtended(self.__vin, self.__backend).response_to_active_job(remaining_climate_time="0",
                                                                                               climatisation_duration="0",
                                                                                               heater_source=base.HeaterSource.AUTOMATIC.value,
                                                                                               climatisation_state=base.ClimatisationState.OFF.value)

        def response_to_job_with_error(self, error: str):
            """Response to active RPC-Extended job with an error.

            :raises InvalidParameterException: if Error-Code has an invalid value
            :param str error: Name of the error
            """
            if not odp_requests.ServiceRPCExtended.RPCExtendedErrorCodes.has_name(error):
                raise InvalidParameterException(f"Error-Code '{error}' is not available")
            odp_requests.ServiceRPCExtended(self.__vin, self.__backend).response_to_active_job_with_error(odp_requests.ServiceRPCExtended.RPCExtendedErrorCodes[error])
