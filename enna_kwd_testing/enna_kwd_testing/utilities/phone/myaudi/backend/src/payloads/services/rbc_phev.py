# -*- coding: utf-8 -*-
"""Created on 07.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains payload for rbc phev service.
"""

import datetime

from .. import interface


class Payload(interface.Payload):
    """Remote battery charging (RBC) payload for phev vehicles."""

    def __init__(self, **kwargs):
        """Initialize payload object for rbc phev service.

        :param dict kwargs: Keyword arguments to manipulate payload. Most of the instances attributes can be used as keyword arguments.
        """
        super().__init__()
        self.soc = "30"
        self.remaining_charging_time = "0"
        self.cruising_range_combined = "480"
        self.engine_type_one = interface.EngineType.PETROL_DIESEL.value
        self.range_one = "450"
        self.engine_type_two = interface.EngineType.ELECTRIC.value
        self.range_two = "30"
        self.remote_charging_max_current = "32"
        self.charging_state_error_code = "0"
        self.battery_condition_state = interface.BatteryConditionState.UNSUPPORTED.value
        self.charging_mode = "off"
        self.charging_plug_connect_state = interface.ChargingPlugConnState.INVALID.value
        self.charging_plug_lock_state = interface.ChargingPlugLockState.INVALID.value
        self.charging_state = "off"
        self.energy_flow = "off"
        self.ext_pwr_supply_state = interface.ExtPowerSupplyState.INVALID.value
        self.led_color = interface.LEDColor.NONE.value
        self.led_state = interface.LEDState.OFF.value
        self.trigger = interface.TriggerCharging.INVALID.value

        self.utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")
        self.timestamp_instrument_cluster = self.utc
        self.timestamp_utc = self.utc
        self.prepare_payload(**kwargs)

        self.payload = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<chargingStateReportRequest:chargingStateReport \r\n" \
                       f"xmlns:chargingStateReportRequest=\"http://www.vw.com/mbb/chargingStateReportRequest\" \r\n" \
                       f"xmlns:remoteBattery=\"http://www.vw.com/mbb/remoteBattery\" \r\nxmlns:rvs=\"http://www.vw.com/mbb/rvs\" \r\n" \
                       f"xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" \r\nxsi:schemaLocation=\"" \
                       f"http://www.vw.com/mbb/chargingStateReportRequest ../../XSD_files/XSD_RBC/chargingStateReportRequest_v1_0_0.xsd \">\r\n" \
                       f"  <chargingStateReportRequest:batteryStateReport \r\n  remoteBattery:SOC=\"{self.soc}\" \r\n  " \
                       f"remoteBattery:remainingChargingTime=\"{self.remaining_charging_time}\">\r\n\t" \
                       f"<!-- SOC: State Of Charge in percent: % -->\r\n\t" \
                       f"<!-- remaining Charging Time in minutes: min -->\r\n\t\r\n\t\r\n\t" \
                       f"<!-- ATTENTION:\r\n\t\t" \
                       f"Some of Attributs show comment \"UNSUPPORTED\". These values can be left on \"unsupported\", \r\n\t\t" \
                       f"as they are not relevant for the App-behavior. However do not delete these attribtues, as they\r\n\t\t" \
                       f"are mandatory regarding to the interface definition.\r\n\t-->\r\n  \r\n" \
                       f"    <remoteBattery:cruisingRangeCombined>{self.cruising_range_combined}</remoteBattery:cruisingRangeCombined>\r\n\t" \
                       f"<!-- range: unit: 1km -->\r\n\t\r\n    <remoteBattery:cruisingRangeFirst>\t\r\n\t\r\n      " \
                       f"<rvs:engineType>{self.engine_type_one}</rvs:engineType>\r\n\t  " \
                       f"<!-- engineType: for e-tron (hybrid) this is combustion (petrolDiesel / petrolGasoline) type, relevant for RTS Services\r\n" \
                       f"            \"gasCNG\"\r\n            \"gasLPG\"\r\n            \"invalid\"\r\n            \"petrolDiesel\"\r\n            \"petrolGasoline\"\r\n" \
                       f"            \"typeIsElectric\"\r\n            \"typeIsGas\"\r\n            \"typeIsPetrol\"\r\n            \"unsupported\"\r\n\t\t\t-->\r\n\t\t\t\r\n" \
                       f"      <rvs:range>{self.range_one}</rvs:range>\r\n\t  <!-- range: unit: 1km -->\r\n    " \
                       f"</remoteBattery:cruisingRangeFirst>\r\n    <remoteBattery:cruisingRangeSecond>\r\n\t\r\n      " \
                       f"<rvs:engineType>{self.engine_type_two}</rvs:engineType>\r\n\t  " \
                       f"<!-- engineType: for e-tron (hybrid) this is Electric type, relevant for RTS Services\r\n" \
                       f"            \"gasCNG\"\r\n            \"gasLPG\"\r\n            \"invalid\"\r\n            \"petrolDiesel\"\r\n" \
                       f"            \"petrolGasoline\"\r\n            \"typeIsElectric\"\r\n            \"typeIsGas\"\r\n" \
                       f"            \"typeIsPetrol\"\r\n            \"unsupported\"\r\n\t\t\t-->\r\n\t\t\t\r\n" \
                       f"      <rvs:range>{self.range_two}</rvs:range>\r\n\t  " \
                       f"<!-- range: unit: 1km, electric range only (displayed in app)-->\r\n\t\t\t\r\n" \
                       f"    </remoteBattery:cruisingRangeSecond>\r\n" \
                       f"    <remoteBattery:remainingChargingTimeTargetSOC>invalid</remoteBattery:remainingChargingTimeTargetSOC>\r\n\t" \
                       f"<!-- remainingChargingTimeTargetSOC: - UNSUPPORTED !!! -\r\n\t\t\t\"invalid\" \"MaxSOC\" \"MinSOC\"\t\"unsupported\"\r\n\t\t\t-->\r\n\t\t\t\r\n" \
                       f"  </chargingStateReportRequest:batteryStateReport>\r\n  <chargingStateReportRequest:chargingSettingsReport \r\n" \
                       f"  remoteBattery:chargeMaxCurrent=\"{self.remote_charging_max_current}\"/>\r\n  <chargingStateReportRequest:chargingStateReport \r\n" \
                       f"  remoteBattery:chargingStateErrorCode=\"{self.charging_state_error_code}\">\r\n    " \
                       f"<remoteBattery:batteryConditioningState>{self.battery_condition_state}</remoteBattery:batteryConditioningState>\r\n\t" \
                       f"<!-- batteryConditioningState:  - UNSUPPORTED !!! -\r\n            \"cooling\" \"heating\" \"invalid\" \"off\" \"unsupported\"\r\n\t-->\r\n" \
                       f"    <remoteBattery:chargingMode>{self.charging_mode}</remoteBattery:chargingMode>\r\n\t<!-- chargingMode:\t\t\t\t- unsupported !!! -\r\n" \
                       f"            \"AC\" \"AC_and_cond\" \"conditioning\" \"DC\" \"DC_and_cond\" \"invalid\" \"off\" \"unsupported\"\r\n\t-->\r\n\t\r\n" \
                       f"    <remoteBattery:chargingPlugConnState>{self.charging_plug_connect_state}</remoteBattery:chargingPlugConnState>\r\n\t<!-- chargingPlugConnState:\r\n" \
                       f"            \"connected\"\r\n            \"disconnected\"\r\n            \"invalid\"\r\n            \"unsupported\"\r\n\t-->\r\n\t\r\n" \
                       f"    <remoteBattery:chargingPlugLockState>{self.charging_plug_lock_state}</remoteBattery:chargingPlugLockState>\r\n\t" \
                       f"<!-- chargingPlugLockState: \t- UNSUPPORTED !!! -\r\n            \"invalid\" \"locked\" \"unlocked\" \"unsupported\"\r\n\t-->\r\n\t\r\n" \
                       f"    <remoteBattery:chargingState>{self.charging_state}</remoteBattery:chargingState>\r\n\t" \
                       f"<!-- chargingState:\t\t\t\r\n            \"charging\"\r\n            \"completed\"\r\n            \"conservationCharging\"\r\n" \
                       f"            \"error\"\r\n            \"invalid\"\r\n            \"off\"\r\n            \"unsupported\"\r\n\t-->\r\n\t\r\n" \
                       f"    <remoteBattery:energyFlow>{self.energy_flow}</remoteBattery:energyFlow>\r\n\t<!-- energyFlow: \t\t\t- UNSUPPORTED !!! - \r\n" \
                       f"            \"invalid\" \"off\" \"on\" \"unsupported\"\r\n\t-->\r\n\t\r\n" \
                       f"    <remoteBattery:extPowerSupplyState>{self.ext_pwr_supply_state}</remoteBattery:extPowerSupplyState>\r\n\t" \
                       f"<!-- extPowerSupplyState:-\r\n            \"available\" \r\n            \"invalid\" \r\n" \
                       f"            \"station_connected\" \r\n            \"unavailable\" \r\n            \"unsupported\"\r\n\t-->\r\n\t\r\n" \
                       f"    <remoteBattery:LED_Color>{self.led_color}</remoteBattery:LED_Color>\r\n\t<!-- LED_Color:\t\t\r\n" \
                       f"            \"green\"\r\n            \"none\"\r\n            \"red\"\r\n            \"yellow\"\r\n\t-->\r\n\t\r\n" \
                       f"    <remoteBattery:LED_State>{self.led_state}</remoteBattery:LED_State> \r\n\t<!-- LED_State: \t\t\t\r\n" \
                       f"            \"Blink\"\t\t\t// an-aus Periode gleich lange (bei Waehlhebel nicht in P)\r\n" \
                       f"            \"Flash\"\t\t\t// lange aus, kurz an -> wenn ein Timer aktiv ist\r\n" \
                       f"            \"Off\"\r\n            \"PermanentOn\"\t// Batterie voll\r\n" \
                       f"            \"Pulse\"\t\t\t// Ladevorgang aktiv\r\n\t-->\r\n\t\r\n" \
                       f"    <remoteBattery:trigger>{self.trigger}</remoteBattery:trigger>\r\n\t<!-- trigger:\t\t\t\t- unsupported !!! -\r\n" \
                       f"            \"immediately\"  \"invalid\" \"push-button\" \"timer1\" \"timer2\" \"timer3\" \"timer4\" \"unsupported\"\r\n\t-->\r\n\t\r\n" \
                       f"  </chargingStateReportRequest:chargingStateReport>\r\n</chargingStateReportRequest:chargingStateReport>"

        self.get_payload()

    def get_payload(self):
        """Get manipulated payload for rbc phev service.

        :rtype: str.
        :returns: Manipulated payload.
        """
        return self.payload
