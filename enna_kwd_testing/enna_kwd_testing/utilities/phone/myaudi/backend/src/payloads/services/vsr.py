# -*- coding: utf-8 -*-
"""Created on 04.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains payload for vsr service.
"""

import datetime

from .. import interface

NO_WARNINGS = "AwICOTDQyGA9FKAKAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
WARNINGS = "AwICOTDQyGA9FKInoxeiIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"


class Payload(interface.Payload):
    """Vehicle status report (VSR) payload."""

    def __init__(self, **kwargs):
        """Initialize vsr service payload object.

        :param dict kwargs: Keyword arguments to manipulate payload. Most of the instances attributes can be used as keyword arguments.
        """

        super().__init__()
        self.parking_light_state = interface.ParkingLights.OFF.value
        self.door_fl_locked_bool = interface.DoorStateLocked.LOCKED.value
        self.door_fl_open_bool = interface.DoorStateOpen.CLOSED.value
        self.door_fl_safe_bool = interface.DoorStateSafe.SAFE.value
        self.door_fr_locked_bool = interface.DoorStateLocked.LOCKED.value
        self.door_fr_open_bool = interface.DoorStateOpen.CLOSED.value
        self.door_fr_safe_bool = interface.DoorStateSafe.SAFE.value
        self.door_rl_locked_bool = interface.DoorStateLocked.LOCKED.value
        self.door_rl_open_bool = interface.DoorStateOpen.CLOSED.value
        self.door_rl_safe_bool = interface.DoorStateSafe.SAFE.value
        self.door_rr_locked_bool = interface.DoorStateLocked.LOCKED.value
        self.door_rr_open_bool = interface.DoorStateOpen.CLOSED.value
        self.door_rr_safe_bool = interface.DoorStateSafe.SAFE.value
        self.trunk_locked_bool = interface.DoorStateLocked.LOCKED.value
        self.trunk_open_bool = interface.DoorStateOpen.CLOSED.value
        self.trunk_safe_bool = interface.DoorStateSafe.SAFE.value
        self.frontlid_locked_bool = interface.DoorStateLocked.LOCKED.value
        self.frontlid_open_bool = interface.DoorStateOpen.CLOSED.value
        self.frontlid_safe_bool = interface.DoorStateSafe.SAFE.value
        self.conv_top_open_percentage = "0"
        self.conv_top_state = interface.DoorStateUnavailable.UNSUPPORTED.value
        self.sunroof_open_percentage = "0"
        self.sunroof_state = interface.WindowState.CLOSED.value
        self.sunroof_rear_open_percentage = "0"
        self.sunroof_rear_state = interface.WindowState.UNSUPPORTED.value
        self.window_fl_open_percentage = "0"
        self.window_fl_state = interface.WindowState.CLOSED.value
        self.window_fr_open_percentage = "0"
        self.window_fr_state = interface.WindowState.CLOSED.value
        self.window_rl_open_percentage = "0"
        self.window_rl_state = interface.WindowState.CLOSED.value
        self.window_rr_open_percentage = "0"
        self.window_rr_state = interface.WindowState.CLOSED.value
        self.actuation = interface.RVSClampStateChanged.KL15OFF.value
        self.clamp_state = interface.ClampState.KLS_OFF.value
        self.obdc_0301 = "AQMC/YPQMF7VECEB8gESABkhAREBAQ=="
        self.obdc_0404 = "BAQC/YPQMF7VEOQH"
        self.obdc_040C = "DAQC/YPQMF7VEDKAAQ=="
        self.obdc_0203 = NO_WARNINGS
        self.tyre_pressure_unit = interface.TyrePressureUnit.BAR.value
        self.tyre_fl_actual_pressure = "0"
        self.tyre_fl_diff_pressure = "0"
        self.tyre_fl_pos = "frontLeft"
        self.tyre_fl_pressure_state = interface.TyrePressureState.INVALID.value
        self.tyre_fr_actual_pressure = "0"
        self.tyre_fr_diff_pressure = "0"
        self.tyre_fr_pos = "frontRight"
        self.tyre_fr_pressure_state = interface.TyrePressureState.INVALID.value
        self.tyre_rl_actual_pressure = "0"
        self.tyre_rl_diff_pressure = "0"
        self.tyre_rl_pos = "rearLeft"
        self.tyre_rl_pressure_state = interface.TyrePressureState.INVALID.value
        self.tyre_rr_actual_pressure = "0"
        self.tyre_rr_diff_pressure = "0"
        self.tyre_rr_pos = "rearRight"
        self.tyre_rr_pressure_state = interface.TyrePressureState.INVALID.value
        self.bem = "100"
        self.current_speed = "0"
        self.fuel_level_calculated = interface.FuelLevelCalculated.NOT_CALCULATED.value
        self.parking_brake = interface.ParkingBrake.ON.value
        self.fuel_level = "70"
        self.gas_level = "0"
        self.soc = "0"
        self.cruising_range_combined = "450"
        self.engine_type_one = interface.EngineType.PETROL_DIESEL.value
        self.range_one = "450"
        self.engine_type_two = interface.EngineType.UNSUPPORTED.value
        self.range_two = "0"
        self.mileage = "16743"

        self.utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")
        self.timestamp_instrument_cluster = self.utc
        self.timestamp_utc = self.utc

        self.prepare_payload(**kwargs)

        self.vehicle_data = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<rvsRdk:telemetricVehicleData xmlns:commonTypes=\"" \
                            f"http://www.vw.com/mbb/commonTypes\" xmlns:diagnostic=\"http://www.vw.com/mbb/diagnostic\" " \
                            f"xmlns:jobs=\"http://www.vw.com/mbb/jobMechanism\" xmlns:rvsRdk=\"http://www.vw.com/mbb/rvsRdk\" " \
                            f"xmlns:tyresState=\"http://www.vw.com/mbb/tyresState\" " \
                            f"xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" " \
                            f"xsi:schemaLocation=\"http://www.vw.com/mbb/rvsRdk ../../XSD_mbb/2018.1/TSS/rvsRdk_v1_0_1.xsd " \
                            f"\">\r\n  \r\n\t<!-- Parklicht an/aus :: (both, invalid, left, off, right, unsupported)-->\r\n\t" \
                            f"<rvsRdk:parkingLights>{self.parking_light_state}</rvsRdk:parkingLights>\r\n\r\n\t<!-- " \
                            f"Zustand der Tueren\t:: (doorStateUnavailableEnum: invalid, unsupported, valid)-->\r\n\t" \
                            f"<rvsRdk:doorState " \
                            f"rvsRdk:locked=\"{self.door_fl_locked_bool}\" rvsRdk:open=\"{self.door_fl_open_bool}\" rvsRdk:safe=\"{self.door_fl_safe_bool}\">\r\n\t\t" \
                            f"<rvsRdk:doorId>FrontLeftDoor</rvsRdk:doorId>\r\n\t\t<rvsRdk:doorStateUnavailableEnum>valid</rvsRdk:doorStateUnavailableEnum>\r\n\t" \
                            f"</rvsRdk:doorState>\r\n\t" \
                            f"<rvsRdk:doorState rvsRdk:locked=\"{self.door_fr_locked_bool}\" rvsRdk:open=\"{self.door_fr_open_bool}\" rvsRdk:safe=\"{self.door_fr_safe_bool}\">\r\n\t\t" \
                            f"<rvsRdk:doorId>FrontRightDoor</rvsRdk:doorId>\r\n\t\t" \
                            f"<rvsRdk:doorStateUnavailableEnum>valid</rvsRdk:doorStateUnavailableEnum>\r\n\t" \
                            f"</rvsRdk:doorState>\r\n\t" \
                            f"<rvsRdk:doorState rvsRdk:locked=\"{self.door_rl_locked_bool}\" rvsRdk:open=\"{self.door_rl_open_bool}\" rvsRdk:safe=\"{self.door_rl_safe_bool}\">\r\n\t\t" \
                            f"<rvsRdk:doorId>RearLeftDoor</rvsRdk:doorId>\r\n\t\t<rvsRdk:doorStateUnavailableEnum>valid</rvsRdk:doorStateUnavailableEnum>\r\n\t" \
                            f"</rvsRdk:doorState>\r\n\t<rvsRdk:doorState rvsRdk:locked=\"{self.door_rr_locked_bool}\" rvsRdk:open=\"{self.door_rr_open_bool}\" rvsRdk:safe=\"{self.door_rr_safe_bool}\">\r\n\t\t" \
                            f"<rvsRdk:doorId>RearRightDoor</rvsRdk:doorId>\r\n\t\t<rvsRdk:doorStateUnavailableEnum>valid</rvsRdk:doorStateUnavailableEnum>\r\n\t" \
                            f"</rvsRdk:doorState>\r\n\t" \
                            f"<rvsRdk:doorState rvsRdk:locked=\"{self.trunk_locked_bool}\" rvsRdk:open=\"{self.trunk_open_bool}\" rvsRdk:safe=\"{self.trunk_safe_bool}\">\r\n\t\t" \
                            f"<rvsRdk:doorId>Trunk</rvsRdk:doorId>\r\n\t\t<rvsRdk:doorStateUnavailableEnum>valid</rvsRdk:doorStateUnavailableEnum>\r\n\t" \
                            f"</rvsRdk:doorState>\r\n\t" \
                            f"<rvsRdk:doorState rvsRdk:locked=\"{self.frontlid_locked_bool}\" rvsRdk:open=\"{self.frontlid_open_bool}\" rvsRdk:safe=\"{self.frontlid_safe_bool}\">\r\n\t\t" \
                            f"<rvsRdk:doorId>FrontLid</rvsRdk:doorId>\r\n\t\t<rvsRdk:doorStateUnavailableEnum>valid</rvsRdk:doorStateUnavailableEnum>\r\n\t" \
                            f"</rvsRdk:doorState>\r\n\r\n\r\n\t" \
                            f"<!-- Zustand der Fenster (closed, open, invalid, unsupported-->\r\n\t" \
                            f"<rvsRdk:windowList>\r\n\t\t" \
                            f"<rvsRdk:percentOpen>{self.conv_top_open_percentage}</rvsRdk:percentOpen>\r\n\t\t" \
                            f"<rvsRdk:windowId>ConvertibleTop</rvsRdk:windowId>\r\n\t\t" \
                            f"<rvsRdk:windowStateEnum>{self.conv_top_state}</rvsRdk:windowStateEnum>\r\n\t" \
                            f"</rvsRdk:windowList>\r\n\t<rvsRdk:windowList>" \
                            f"\r\n\t\t<rvsRdk:percentOpen>{self.sunroof_open_percentage}</rvsRdk:percentOpen>\r\n\t\t" \
                            f"<rvsRdk:windowId>Sunroof</rvsRdk:windowId>\r\n\t\t" \
                            f"<rvsRdk:windowStateEnum>{self.sunroof_state}</rvsRdk:windowStateEnum>\r\n\t" \
                            f"</rvsRdk:windowList>\r\n\t\r\n\t<rvsRdk:windowList>\r\n\t\t" \
                            f"<rvsRdk:percentOpen>{self.sunroof_rear_open_percentage}</rvsRdk:percentOpen>\r\n\t\t" \
                            f"<rvsRdk:windowId>SunroofRear</rvsRdk:windowId>\r\n\t\t" \
                            f"<rvsRdk:windowStateEnum>{self.sunroof_rear_state}</rvsRdk:windowStateEnum>\r\n\t" \
                            f"</rvsRdk:windowList>\r\n\r\n\r\n\t<rvsRdk:windowList>\r\n\t\t" \
                            f"<rvsRdk:percentOpen>{self.window_fl_open_percentage}</rvsRdk:percentOpen>\r\n\t\t" \
                            f"<rvsRdk:windowId>LeftWindow</rvsRdk:windowId>\r\n\t\t" \
                            f"<rvsRdk:windowStateEnum>{self.window_fl_state}</rvsRdk:windowStateEnum>\r\n\t" \
                            f"</rvsRdk:windowList>\r\n\t<rvsRdk:windowList>\r\n\t\t" \
                            f"<rvsRdk:percentOpen>{self.window_fr_open_percentage}</rvsRdk:percentOpen>\r\n\t\t" \
                            f"<rvsRdk:windowId>RightWindow</rvsRdk:windowId>\r\n\t\t" \
                            f"<rvsRdk:windowStateEnum>{self.window_fr_state}</rvsRdk:windowStateEnum>\r\n\t" \
                            f"</rvsRdk:windowList>\r\n\t<rvsRdk:windowList>\r\n\t\t" \
                            f"<rvsRdk:percentOpen>{self.window_rl_open_percentage}</rvsRdk:percentOpen>\r\n\t\t" \
                            f"<rvsRdk:windowId>RearLeftWindow</rvsRdk:windowId>\r\n\t\t" \
                            f"<rvsRdk:windowStateEnum>{self.window_rl_state}</rvsRdk:windowStateEnum>\r\n\t" \
                            f"</rvsRdk:windowList>\r\n\t<rvsRdk:windowList>\r\n\t\t" \
                            f"<rvsRdk:percentOpen>{self.window_rr_open_percentage}</rvsRdk:percentOpen>\r\n\t\t" \
                            f"<rvsRdk:windowId>RearRightWindow</rvsRdk:windowId>\r\n\t\t" \
                            f"<rvsRdk:windowStateEnum>{self.window_rr_state}</rvsRdk:windowStateEnum>\r\n\t" \
                            f"</rvsRdk:windowList>\r\n\r\n\t<rvsRdk:instrumentClusterTime>" \
                            f"{self.timestamp_instrument_cluster}</rvsRdk:instrumentClusterTime>\r\n\t" \
                            f"<rvsRdk:timestamp>{self.timestamp_utc}</rvsRdk:timestamp>\r\n\t" \
                            f"<rvsRdk:temperatureData>\r\n\t\t<rvsRdk:outDoorTemperature commonTypes:state=\"invalid\"" \
                            f">0</rvsRdk:outDoorTemperature>\r\n\t</rvsRdk:temperatureData>\r\n\r\n" \
                            f"    <!-- \"Carfinder Service\" can be simulated via \"setCarfinder.bat\r\n" \
                            f"    <rvsRdk:lastPositionDeprecated>true</rvsRdk:lastPositionDeprecated> -->\r\n" \
                            f"    \r\n    <!-- Trigger fuer den RVS Report " \
                            f"(RVS_ClampStateChanged_15Off, RVS_ClampStateChanged_15On,) -->\r\n\t" \
                            f"<rvsRdk:actuation>{self.actuation}</rvsRdk:actuation>\r\n\r\n\t" \
                            f"<!--Zustand der Zuendung (clamp_15_on, clamp_S_off, clamp_S_on_clamp_15_off, invalid)-->\r\n\t" \
                            f"<rvsRdk:clampState>{self.clamp_state}</rvsRdk:clampState>\r\n\r\n\t" \
                            f"<!-- \"Carfinder Service\" can be simulated via \"setCarfinder.bat\"\r\n\t" \
                            f"<rvsRdk:location commonTypes:altitude=\"0\">\r\n\t\t" \
                            f"<commonTypes:aggregatedConfidence commonTypes:precision=\"0\">\r\n\t\t\t" \
                            f"<commonTypes:trueness>fair</commonTypes:trueness>\r\n\t\t" \
                            f"</commonTypes:aggregatedConfidence>\r\n\t\t" \
                            f"<commonTypes:geoCoordinate commonTypes:latitude=\"-338672287\" " \
                            f"commonTypes:longitude=\"1512054428\"/>\r\n\t\t" \
                            f"<commonTypes:heading commonTypes:direction=\"0\"/>\r\n\t" \
                            f"</rvsRdk:location>\r\n    -->\r\n   \r\n\t<rvsRdk:obdcData diagnostic:version=\"0101\">\r\n\t\t" \
                            f"<diagnostic:dataGroup diagnostic:groupID=\"0301\">{self.obdc_0301}</diagnostic:dataGroup>     " \
                            f"<!-- (WIV) Wartungsintervalldaten -->\r\n\t\t" \
                            f"<diagnostic:dataGroup diagnostic:groupID=\"0404\">{self.obdc_0404}</diagnostic:dataGroup>" \
                            f"                     <!-- Oelfuellstandinformationen -->\r\n\t\t" \
                            f"<diagnostic:dataGroup diagnostic:groupID=\"040C\">{self.obdc_040C}</diagnostic:dataGroup>" \
                            f"                 <!-- SCR-Daten (z.B. Adblue)-->\r\n        " \
                            f"<diagnostic:dataGroup diagnostic:groupID=\"0203\"" \
                            f">{self.obdc_0203}</diagnostic:dataGroup>\r\n" \
                            f"        <!--<diagnostic:dataGroup diagnostic:groupID=\"0203\"" \
                            f">AwIEOTDQyGA9FKFgomWiNQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA</diagnostic:dataGroup>   -->\r\n" \
                            f"        <!-- aktive Kombi-Warnleuchten (nicht gefiltert) (inkl. km-Stand und Zeitpunkt des Sammelns)-->\r\n" \
                            f"        </rvsRdk:obdcData>\r\n        \r\n    <rvsRdk:tyresState>\r\n" \
                            f"        <tyresState:pressureUnit>{self.tyre_pressure_unit}</tyresState:pressureUnit>\r\n" \
                            f"        <tyresState:tyre>\r\n          <tyresState:actualPressure>{self.tyre_fl_actual_pressure}</tyresState:actualPressure>\r\n" \
                            f"          <tyresState:differentialPressure>{self.tyre_fl_diff_pressure}</tyresState:differentialPressure>\r\n" \
                            f"          <tyresState:tyrePosition>{self.tyre_fl_pos}</tyresState:tyrePosition>\r\n" \
                            f"          <tyresState:tyrePressureState>{self.tyre_fl_pressure_state}</tyresState:tyrePressureState>\r\n" \
                            f"        </tyresState:tyre>\r\n        <tyresState:tyre>\r\n" \
                            f"          <tyresState:actualPressure>{self.tyre_fr_actual_pressure}</tyresState:actualPressure>\r\n" \
                            f"          <tyresState:differentialPressure>{self.tyre_fr_diff_pressure}</tyresState:differentialPressure>\r\n" \
                            f"          <tyresState:tyrePosition>{self.tyre_fr_pos}</tyresState:tyrePosition>\r\n" \
                            f"          <tyresState:tyrePressureState>{self.tyre_fr_pressure_state}</tyresState:tyrePressureState>\r\n" \
                            f"        </tyresState:tyre>\r\n        <tyresState:tyre>\r\n" \
                            f"          <tyresState:actualPressure>{self.tyre_rl_actual_pressure}</tyresState:actualPressure>\r\n" \
                            f"          <tyresState:differentialPressure>{self.tyre_rl_diff_pressure}</tyresState:differentialPressure>\r\n" \
                            f"          <tyresState:tyrePosition>{self.tyre_rl_pos}</tyresState:tyrePosition>\r\n" \
                            f"          <tyresState:tyrePressureState>{self.tyre_rl_pressure_state}</tyresState:tyrePressureState>\r\n" \
                            f"        </tyresState:tyre>\r\n        <tyresState:tyre>\r\n" \
                            f"          <tyresState:actualPressure>{self.tyre_rr_actual_pressure}</tyresState:actualPressure>\r\n" \
                            f"          <tyresState:differentialPressure>{self.tyre_rr_diff_pressure}</tyresState:differentialPressure>\r\n" \
                            f"          <tyresState:tyrePosition>{self.tyre_rr_pos}</tyresState:tyrePosition>\r\n" \
                            f"          <tyresState:tyrePressureState>{self.tyre_rr_pressure_state}</tyresState:tyrePressureState>\r\n" \
                            f"        </tyresState:tyre>\r\n    </rvsRdk:tyresState>\r\n\r\n\t<!--        \r\n" \
                            f"        Possible Combinations of EngineType and Levels\r\n" \
                            f"        >> select a VEHICLE and set the Payload Parameters regarding to the table\r\n" \
                            f"       \r\n        Note (A)    * X >> a valid Level is sent from Car\r\n" \
                            f"                    * O >> a invalid Level is sent from Car (e.g. value is missing, or Bus init-value 65535 is sent)\r\n" \
                            f"              \r\n        Note (B)    fuelLevel ... is used for petrol-Types (petrolGasoline / petroDiesel)\r\n" \
                            f"                    gasLevel .... is used for gasCNG-Type\r\n" \
                            f"                    SOC ......... is used for typeIsElectric\r\n" \
                            f"                    \r\n" \
                            f"        Note (C)    unrelevant Parameters for App: BEM(Battery-Energy-Management), currentSpeed, parkingBrake, fuelLevelCalculated\r\n" \
                            f"        \r\n        Note (D)    cruisingRangeCombined = combined range of 1st and 2nd Engine (only if supported)\r\n" \
                            f"        \r\n        |........................................................................................|\r\n" \
                            f"        |>>> VEHICLE <<< ||  EngineType 1   ||    EngineType 2   || fuelLevel || gasLevel || SOC |\r\n" \
                            f"        |........................................................................................|\r\n" \
                            f"        |Verbr. (Diesel) ||  petrolDiesel    ||   unsupported    ||     X     ||    O     ||  O  |\r\n" \
                            f"        |Verbr. (Benzin) ||  petrolGasoline  ||   unsupported    ||     X     ||    O     ||  O  |\r\n" \
                            f"        |CNG             ||  gasCNG          ||   petrolGasoline ||     X     ||    X     ||  O  |\r\n" \
                            f"        |PHEV            ||  petrolDiesel    ||   typeIsElectric ||     X     ||    O     ||  X  |\r\n" \
                            f"        |BEV             ||  typeIsElectric  ||   unsupported    ||     O     ||    O     ||  X  |\r\n" \
                            f"        .........................................................................................|\r\n" \
                            f"    -->\r\n    \r\n\t<rvsRdk:vehicleStatusChange \r\n\trvsRdk:BEM=\"{self.bem}\" \r\n\t" \
                            f"rvsRdk:currentSpeed=\"{self.current_speed}\" \r\n\trvsRdk:fuelLevelCalculated=\"{self.fuel_level_calculated}\" \r\n\t" \
                            f"rvsRdk:parkingBrake=\"{self.parking_brake}\" \r\n    rvsRdk:fuelLevel=\"{self.fuel_level}\"\r\n" \
                            f"    rvsRdk:gasLevel=\"{self.gas_level}\"\r\n    rvsRdk:SOC=\"{self.soc}\">\r\n\t\t" \
                            f"<rvsRdk:cruisingRangeCombined>{self.cruising_range_combined}</rvsRdk:cruisingRangeCombined>\r\n" \
                            f"        \r\n        <!-- 1st Engine-->\r\n        <rvsRdk:cruisingRangeFirst>\r\n\t\t\t" \
                            f"<rvsRdk:engineType>{self.engine_type_one}</rvsRdk:engineType>\r\n\t\t\t" \
                            f"<rvsRdk:range>{self.range_one}</rvsRdk:range>\r\n\t\t</rvsRdk:cruisingRangeFirst>\r\n\t\t\r\n" \
                            f"        <!-- 2nd Engine-->\r\n        <rvsRdk:cruisingRangeSecond>\r\n\t\t\t" \
                            f"<rvsRdk:engineType>{self.engine_type_two}</rvsRdk:engineType>\r\n\t\t\t" \
                            f"<rvsRdk:range>{self.range_two}</rvsRdk:range>\r\n\t\t</rvsRdk:cruisingRangeSecond>\r\n" \
                            f"        \r\n\t</rvsRdk:vehicleStatusChange>  \r\n\r\n\t<!-- Kilometerstand-->\r\n\t" \
                            f"<rvsRdk:mileage>{self.mileage}</rvsRdk:mileage>    \r\n</rvsRdk:telemetricVehicleData>"

        self.get_payload()

    def get_payload(self):
        """Get manipulated payload for speed alert violation.

        :rtype: str.
        :returns: Manipulated payload.
        """
        return self.vehicle_data
