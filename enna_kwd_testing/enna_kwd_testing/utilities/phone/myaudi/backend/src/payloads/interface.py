# -*- coding: utf-8 -*-
"""Contains function to load payload to backend request session.
Enum-values, specified for the different payloads are stored in this class.
"""

import abc
import logging
import datetime

from enna_kwd_testing.utilities.phone.extended_enum import ExtendedEnum

logger = logging.getLogger(__name__)


class ServiceType(str, ExtendedEnum):
    """ Enumeration for all available Services """
    INSTALL_BASE_UPDATE_CGW_CLU_33 = "INSTALL_BASE_UPDATE_CGW_CLU_33"
    INSTALL_BASE_UPDATE_CGW_CLU_31 = "INSTALL_BASE_UPDATE_CGW_CLU_31"
    INSTALL_BASE_UPDATE_CGW_MBB_DEFAULT = "INSTALL_BASE_UPDATE_CGW_MBB_DEFAULT"
    VSR = "VSR"
    CARFINDER_VALID = "CARFINDER_VALID"
    CARFINDER_INVALID = "CARFINDER_INVALID"
    RAH_QUICKSTART = "RAH_QUICKSTART"
    RAH_TIMER = "RAH_TIMER"
    RAH_TIMER_B9PA = "RAH_TIMER_B9PA"
    RHF = "RHF"
    DWA = "DWA"
    RBC_QUICKSTART_PHEV = "RBC_QUICKSTART_PHEV"
    RBC_QUICKSTART_CBEV = "RBC_QUICKSTART_CBEV"
    SPEED_ALERT = "SPEED_ALERT"
    GEOFENCE_ALERT = "GEOFENCE_ALERT"
    VALET_ALERT = "VALET_ALERT"
    RPT_PROFILE = "RPT_PROFILE"
    RPT_TIMER = "RPT_TIMER"
    RDT = "RDT"
    RDT_EXTENDED = "RDT_EXTENDED"
    RPC = "RPC"
    RPC_EXTENDED = "RPC_EXTENDED"


class EngineType(str, ExtendedEnum):
    """ Enumeration for Engine-Type """
    ELECTRIC = "typeIsElectric"
    PETROL_DIESEL = "petrolDiesel"
    PETROL_GASOLINE = "petrolGasoline"
    UNSUPPORTED = "unsupported"
    CNG = "gasCNG"
    INVALID = "invalid"


class RemainingChargingTimeTargetSOC(str, ExtendedEnum):
    """ Enumeration for Remaining-Charging-Time-Target-SOC """
    INVALID = "invalid"
    MAX_SOC = "MaxSOC"
    MIN_SOC = "MinSOC"
    UNSUPPORTED = "unsupported"


class BatteryConditionState(str, ExtendedEnum):
    """ Enumeration for Battery-Condition-State """
    COOLING = "cooling"
    HEATING = "heating"
    INVALID = "invalid"
    OFF = "off"
    UNSUPPORTED = "unsupported"


class ChargingMode(str, ExtendedEnum):
    """ Enumeration for Charging-Mode """
    AC = "AC"
    AC_AND_COND = "AC_and_cond"
    CONDITIONING = "conditioning"
    DC = "DC"
    DC_AND_COND = "DC_and_cond"
    INVALID = "invalid"
    OFF = "off"
    UNSUPPORTED = "unsupported"


class ChargingPlugConnState(str, ExtendedEnum):
    """ Enumeration for Charging-Plug-Connection-State """
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    INVALID = "invalid"
    UNSUPPORTED = "unsupported"


class ChargingPlugLockState(str, ExtendedEnum):
    """ Enumeration for Charging-Plug-Lock-State """
    INVALID = "invalid"
    LOCKED = "locked"
    UNLOCKED = "unlocked"
    UNSUPPORTED = "unsupported"


class ChargingState(str, ExtendedEnum):
    """ Enumeration for Charging-State """
    CHARGING = "charging"
    COMPLETED = "completed"
    CONSERVATION_CHARGING = "conservationCharging"
    ERROR = "error"
    INVALID = "invalid"
    OFF = "off"
    UNSUPPORTED = "unsupported"


class EnergyFlow(str, ExtendedEnum):
    """ Enumeration for Energy-Flow """
    INVALID = "invalid"
    OFF = "off"
    ON = "on"
    UNSUPPORTED = "unsupported"


class ExtPowerSupplyState(str, ExtendedEnum):
    """ Enumeration for External-Power-Supply-State """
    AVAILABLE = "available"
    INVALID = "invalid"
    STATION_CONNECTED = "station_connected"
    UNAVAILABLE = "unavailable"
    UNSUPPORTED = "unsupported"


class LEDColor(str, ExtendedEnum):
    """ Enumeration for LED-Colors """
    GREEN = "green"
    RED = "red"
    YELLOW = "yellow"
    NONE = "none"


class LEDState(str, ExtendedEnum):
    """ Enumeration for LED-States """
    BLINK = "Blink"
    FLASH = "Flash"
    OFF = "Off"
    PERMANENT_ON = "PermanentOn"
    PULSE = "Pulse"


class TriggerCharging(str, ExtendedEnum):
    """ Enumeration for Trigger-Charging """
    IMMEDIATELY = "immediately"
    INVALID = "invalid"
    PUSHBUTTON = "push-button"
    TIMER1 = "timer1"
    TIMER2 = "timer2"
    TIMER3 = "timer3"
    TIMER4 = "timer4"
    UNSUPPORTED = "unsupported"


class ParkingLights(str, ExtendedEnum):
    """ Enumeration for Parking-Lights """
    OFF = "off"
    BOTH = "both"
    LEFT = "left"
    RIGHT = "right"
    INVALID = "invalid"
    UNSUPPORTED = "unsupported"


class DoorStateLocked(str, ExtendedEnum):
    """ Enumeration for Door-State-Locked """
    LOCKED = "true"
    UNLOCKED = "false"


class DoorStateOpen(str, ExtendedEnum):
    """ Enumeration for Door-State-Open """
    OPEN = "true"
    CLOSED = "false"


class DoorStateSafe(str, ExtendedEnum):
    """ Enumeration for Door-State-Safe """
    SAFE = "true"
    UNSAFE = "false"


class DoorStateUnavailable(str, ExtendedEnum):
    """ Enumeration for Door-State-Unavailable """
    INVALID = "invalid"
    VALID = "valid"
    UNSUPPORTED = "unsupported"


class WindowState(str, ExtendedEnum):
    """ Enumeration for Window-State """
    CLOSED = "closed"
    OPEN = "open"
    INVALID = "invalid"
    UNSUPPORTED = "unsupported"


class RVSClampStateChanged(str, ExtendedEnum):
    """ Enumeration for RVS-Clamp-State-Changed """
    KL15OFF = "RVS_ClampStateChanged_15Off"
    KL15ON = "RVS_ClampStateChanged_15On"


class ClampState(str, ExtendedEnum):
    """ Enumeration for Clamp-State """
    KL15_ON = "clamp_15_on"
    KLS_OFF = "clamp_S_off"
    KLS_ON_KL15_OFF = "clamp_S_on_clamp_15_off"
    INVALID = "invalid"


class TyrePressureUnit(str, ExtendedEnum):
    """ Enumeration for Tyre-Pressure-Unit """
    BAR = "Bar"


class TyrePressureState(str, ExtendedEnum):
    """ Enumeration for Tyre-Pressure-State """
    INVALID = "invalid"


class FuelLevelCalculated(str, ExtendedEnum):
    """ Enumeration for Fuel-LEvel-Calculated """
    CALCULATED = "true"
    NOT_CALCULATED = "false"


class ParkingBrake(str, ExtendedEnum):
    """ Enumeration for Parking-Brake """
    ON = "true"
    OFF = "false"


class GeoCoordinatesINSchlueterStr5(str, ExtendedEnum):
    """ Coordinates for Mock-Location """
    LONGITUDE = "11398262"
    LATITUDE = "48769970"


class HeaterMode(str, ExtendedEnum):
    """ Enumeration for Heater-Mode """
    COMFORT = "comfort"
    ECONOMY = "economy"
    INVALID = "invalid"
    NORMAL = "normal"
    UNSUPPORTED = "unsupported"


class HeaterSource(str, ExtendedEnum):
    """ Enumeration for Heater-Source """
    AUTOMATIC = "automatic"
    AUXILIARY = "auxilliary"
    ELECTRIC = "electric"
    UNSUPPORTED = "unsupported"
    VENTILATION = "ventilation"


class StartMode(str, ExtendedEnum):
    """ Enumeration for Start-Mode """
    HEATING = "heating"
    INVALID = "invalid"
    UNSUPPORTED = "unsupported"
    VENTILATION = "ventilation"


class ClimatisationState(str, ExtendedEnum):
    """ Enumeration for Climatisation-State """
    HEATING = "heating"
    VENTILATION = "ventilation"
    COOLING = "cooling"
    OFF = "off"
    INVALID = "invalid"
    COMPLETED = "completed"


class RAHTrigger(str, ExtendedEnum):
    """ Enumeration for RAH-Trigger """
    IMMEDIATELY = "immediately"
    INVALID = "invalid"
    PUSH_BUTTON = "push-button"
    TIMER1 = "timer1"
    TIMER2 = "timer2"
    UNSUPPORTED = "unsupported"


class TimerState(str, ExtendedEnum):
    """ Enumeration for Timer-State """
    PROGRAMMED = "programmed"
    NOT_PROGRAMMED = "not_programmed"


class ChargingModeSelectionState(str, ExtendedEnum):
    """ Enumeration for Charging-Mode-Selection-State """
    IMMEDIATE = "immediateCharging"
    TIMER = "timerBasedCharging"


class ModificationReason(str, ExtendedEnum):
    """ Enumeration for Modification-Reason """
    NONE = "noReason"


class ModificationState(str, ExtendedEnum):
    """ Enumeration for Modification-State """
    CAN_BE_MODIFIED = "canBeModified"


class SystemState(str, ExtendedEnum):
    """ Enumeration for System-State """
    DEACTIVATED = "deactivated"


class ChargingRateUnit(str, ExtendedEnum):
    """ Enumeration for Charging-Rate-Unit """
    KM_PER_H = "km_per_h"


class FlapErrorState(str, ExtendedEnum):
    """ Enumeration for Flap-Error-State """
    NO_ERROR = "noError"


class FlapLockState(str, ExtendedEnum):
    """ Enumeration for Flap-Lock-State """
    BLOCKED = "flapBLocked"


class FlapState(str, ExtendedEnum):
    """ Enumeration for Flap-State """
    FLAP_A_OPEN = "flapAOpen"


class UpdateReason(str, ExtendedEnum):
    """ Enumeration for Update-Reason """
    CLAMP_15_OFF = "clamp15Off"


class AlertState(str, ExtendedEnum):
    """ Enumeration for Alert-State """
    START = "Start"
    END = "End"


class RPTTimerState(str, ExtendedEnum):
    """ Enumeration for RPT-Timer-State """
    ACTIVATED = "activated"
    DEACTIVATED = "deactivated"


class ClimatisationTrigger(str, ExtendedEnum):
    """ Enumeration for Climatisation-Trigger """
    IMMEDIATELY = "immediately"
    INVALID = "invalid"
    PUSH_BUTTON = "push-button"
    TIMER1 = "timer1"
    TIMER2 = "timer2"
    TIMER3 = "timer3"
    TIMER4 = "timer4"
    UNSUPPORTED = "unsupported"


class RPCClimatisationState(str, ExtendedEnum):
    """ Enumeration for RPC-Climatisation-State """
    INVALID = "invalid"
    UNSUPPORTED = "unsupported"
    ERROR = "error"
    OFF = "off"
    COMPLETED = "completed"
    COOLING = "cooling"
    HEATING = "heating"
    HEATING_AUXILIARY = "heating_auxiliary"
    VENTILATION = "ventilation"


class MirrorHeatingActiveState(str, ExtendedEnum):
    """ Enumeration for Mirror-Heating-Active-State """
    TRUE = "true"
    FALSE = "false"


class MirrorHeatingEnabledState(str, ExtendedEnum):
    """ Enumeration for Mirror-Heating-Enabled-State """
    TRUE = "true"
    FALSE = "false"


class TimerProgrammedStatus(str, ExtendedEnum):
    """ Enumeration for Timer-Programmed-Status """
    NOT_PROGRAMMED = "not_programmed"
    PROGRAMMED = "programmed"


class ClimatisationPositionState(str, ExtendedEnum):
    """ Enumeration for Climatisation-Position-State """
    TRUE = "true"
    FALSE = "false"


class DepartureClimateState(str, ExtendedEnum):
    """ Enumeration for Departure-Climate-State """
    TRUE = "true"
    FALSE = "false"


class DepartureChargeState(str, ExtendedEnum):
    """ Enumeration for Departure-Charge-State """
    TRUE = "true"
    FALSE = "false"


class ActiveNightRate(str, ExtendedEnum):
    """ Enumeration for Night-Rates """
    TRUE = "true"
    FALSE = "false"


class GeoFencingEventType(str, ExtendedEnum):
    """ Enumeration for Geofence-Types """
    ENTER = "Enter"
    EXIT = "Exit"


class RHFHonkState(str, ExtendedEnum):
    HONK_ON = "honkOn"
    HONK_OFF = "honkOff"


class RHFFlashState(str, ExtendedEnum):
    FLASH_ON = "flashOn"
    FLASH_OFF = "flashOff"


class Payload(abc.ABC):
    """Baseclass for payloads."""

    def __init__(self):
        """Initialize object."""
        self.payload = None

    def prepare_payload(self, **kwargs):
        """Prepare payload and set keyword args to values.

        :param kwargs: Arbitrary keyword arguments.
        """
        for key, value in kwargs.items():
            if type(value) is not str:
                value = str(value)
            setattr(self, key, value)
            # logger.info("Proceeding with following payload variables:")
            # logger.info(self.__dict__)

    @abc.abstractmethod
    def get_payload(self):
        """Abstract method -> To be implemented by any payload type."""

    @staticmethod
    def calc_timestamp_with_utc_offset(utc_time=None):
        """Calculate timestamp with utc offset.

        :param str utc_time: UTC-Time which should be manipulated or None if DateTime.now() should be used
        :rtype: str
        :return: timestamp with utc offset
        """
        if utc_time is None:
            utc_time = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")

        return str(utc_time + "Z")
