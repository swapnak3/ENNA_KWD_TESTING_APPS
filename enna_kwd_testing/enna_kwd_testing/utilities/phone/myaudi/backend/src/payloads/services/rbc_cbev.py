# -*- coding: utf-8 -*-
"""Created on 07.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains payload for rbc cbev service.
"""

import datetime

from .. import interface


class Payload(interface.Payload):
    """Remote battery charging (RBC) payload for cbev vehicles."""

    def __init__(self, **kwargs):
        """Initialize payload object for rbc cbev service.

        :param dict kwargs: Keyword arguments to manipulate payload. Most of the instances attributes can be used as keyword arguments.
        """
        super().__init__()
        self.soc = "30"
        self.remaining_charging_time = "0"
        self.engine_type_one = interface.EngineType.ELECTRIC.value
        self.range_one = "450"
        self.engine_type_two = interface.EngineType.UNSUPPORTED.value
        self.range_two = "0"
        self.cruising_range_combined = self.range_one + self.range_two
        self.charging_time_target_soc = interface.RemainingChargingTimeTargetSOC.MAX_SOC.value
        self.charging_mode_selection_state = interface.ChargingModeSelectionState.IMMEDIATE.value
        self.charging_state_modification_reason = interface.ModificationReason.NONE.value
        self.charging_state_modification_state = interface.ModificationState.CAN_BE_MODIFIED.value
        self.remote_charging_max_current = "32"
        self.wireless_charging_modification_reason = interface.ModificationReason.NONE.value
        self.wireless_charging_modification_state = interface.ModificationState.CAN_BE_MODIFIED.value
        self.system_state = interface.SystemState.DEACTIVATED.value
        self.charging_state_error_code = "0"
        self.charging_rate = "117"
        # self.charging_rate = "1000"
        self.battery_condition_state = interface.BatteryConditionState.UNSUPPORTED.value
        self.charging_rate_unit = interface.ChargingRateUnit.KM_PER_H.value
        self.charging_mode = "off"
        self.charging_plug_connect_state = interface.ChargingPlugConnState.INVALID.value
        self.charging_plug_lock_state = interface.ChargingPlugLockState.INVALID.value
        self.charging_power = "2200"
        self.charging_state = interface.ChargingState.OFF.value
        self.energy_flow = interface.EnergyFlow.OFF.value
        self.ext_pwr_supply_state = interface.ExtPowerSupplyState.AVAILABLE.value
        self.flap_error_state = interface.FlapErrorState.NO_ERROR.value
        self.flap_lock_state = interface.FlapLockState.BLOCKED.value
        self.flap_state = interface.FlapState.FLAP_A_OPEN.value
        self.led_color = interface.LEDColor.NONE.value
        self.led_state = interface.LEDState.OFF.value
        self.w_charge_led_color = "green"
        self.w_charge_led_state = "off"
        self.trigger = interface.TriggerCharging.INVALID.value
        self.update_reason = interface.UpdateReason.CLAMP_15_OFF.value

        self.utc_time = datetime.datetime.now(datetime.UTC)
        self.utc = self.utc_time.strftime("%Y-%m-%dT%H:%M:%S")
        self.timestamp_instrument_cluster = self.utc
        self.timestamp_utc = self.utc

        self.target_time_day = self.utc_time.day
        self.target_time_hour = self.utc_time.hour + 2
        self.target_time_minute = self.utc_time.minute
        self.target_time_month = self.utc_time.month
        self.target_time_offset = "0"
        self.target_time_year = self.utc_time.year

        self.prepare_payload(**kwargs)

        self.payload = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n" \
                       f"<chargingStateReportRequest:chargingStateReport xmlns:chargingStateReportRequest=\"" \
                       f"http://www.vw.com/mbb/chargingStateReportRequest\" " \
                       f"xmlns:remoteBattery=\"http://www.vw.com/mbb/remoteBattery\" " \
                       f"xmlns:wirelessChargingModificationTypes=\"" \
                       f"http://www.vw.com/mbb/wirelessChargingModificationTypes\" " \
                       f"xmlns:wirelessChargingStateReportType=\"http://www.vw.com/mbb/wirelessChargingStateReportType\"" \
                       f" xmlns:wirelessChargingSystemStateType=\"http://www.vw.com/mbb/wirelessChargingSystemStateType\"" \
                       f" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"" \
                       f"http://www.vw.com/mbb/chargingStateReportRequest ../../XSD_mbb/2018.1/XSD_RBC/chargingStateReportRequest_v1_0_5.xsd \">\r\n" \
                       f"  <chargingStateReportRequest:batteryStateReport \r\n" \
                       f"  remoteBattery:SOC=\"{self.soc}\" \r\n" \
                       f"  remoteBattery:remainingChargingTime=\"{self.remaining_charging_time}\">\r\n" \
                       f"    <!-- SOC: State Of Charge in percent: % -->\r\n\t<!-- remaining Charging Time in minutes: min -->\r\n" \
                       f"    \r\n" \
                       f"    <!-- ATTENTION:\r\n\t\tSome of Attributs show comment \"UNSUPPORTED\". These values can be left on \"unsupported\", \r\n\t\t" \
                       f"as they are not relevant for the App-behavior. However do not delete these attribtues, as they\r\n\t\t" \
                       f"are mandatory regarding to the interface definition.\r\n\t-->\r\n    \r\n" \
                       f"    <remoteBattery:cruisingRangeCombined>{self.cruising_range_combined}</remoteBattery:cruisingRangeCombined>\r\n" \
                       f"    <!-- range: unit: 1km -->\r\n    \r\n" \
                       f"    <remoteBattery:cruisingRangeFirst>\r\n      \r\n" \
                       f"      <remoteBattery:engineType>{self.engine_type_one}</remoteBattery:engineType>\r\n" \
                       f"      <!-- engineType: for CBEV typeIsElectric\r\n" \
                       f"            \"gasCNG\"\r\n" \
                       f"            \"gasLPG\"\r\n" \
                       f"            \"invalid\"\r\n" \
                       f"            \"petrolDiesel\"\r\n" \
                       f"            \"petrolGasoline\"\r\n" \
                       f"            \"typeIsElectric\"\r\n" \
                       f"            \"typeIsGas\"\r\n" \
                       f"            \"typeIsPetrol\"\r\n" \
                       f"            \"unsupported\"\r\n\t\t\t-->\r\n" \
                       f"            \r\n      <remoteBattery:range>{self.range_one}</remoteBattery:range>\r\n" \
                       f"      <!-- range: unit: 1km -->\r\n      \r\n" \
                       f"    </remoteBattery:cruisingRangeFirst>\r\n" \
                       f"    <remoteBattery:cruisingRangeSecond>\r\n" \
                       f"      <remoteBattery:engineType>{self.engine_type_two}</remoteBattery:engineType>\r\n" \
                       f"      <!-- engineType: for CBEV unsupported\r\n" \
                       f"            \"gasCNG\"\r\n" \
                       f"            \"gasLPG\"\r\n" \
                       f"            \"invalid\"\r\n" \
                       f"            \"petrolDiesel\"\r\n" \
                       f"            \"petrolGasoline\"\r\n" \
                       f"            \"typeIsElectric\"\r\n" \
                       f"            \"typeIsGas\"\r\n" \
                       f"            \"typeIsPetrol\"\r\n" \
                       f"            \"unsupported\"\r\n\t\t\t" \
                       f"-->\r\n      \r\n      <remoteBattery:range>{self.range_two}</remoteBattery:range>\r\n" \
                       f"      <!-- range: unit: 1km, electric range only (displayed in app)-->\r\n" \
                       f"      \r\n    </remoteBattery:cruisingRangeSecond>\r\n" \
                       f"    <remoteBattery:remainingChargingTimeTargetSOC>{self.charging_time_target_soc}</remoteBattery:remainingChargingTimeTargetSOC>\r\n" \
                       f"    <!-- remainingChargingTimeTargetSOC: - UNSUPPORTED !!! -\r\n" \
                       f"\t\t\t\"invalid\" \"MaxSOC\" \"MinSOC\"\t\"unsupported\"\r\n\t\t\t-->\r\n" \
                       f"            \r\n  " \
                       f"</chargingStateReportRequest:batteryStateReport>\r\n" \
                       f"  <chargingStateReportRequest:chargeModeSelection>\r\n" \
                       f"    <chargingStateReportRequest:chargingModeSelectionState>{self.charging_mode_selection_state}</chargingStateReportRequest:chargingModeSelectionState>\r\n" \
                       f"     <!-- chargingModeSelectionState: \r\n" \
                       f"\t\t\t\"immediateCharging\" \"timerBasedCharging\"\r\n" \
                       f"\t\t\t-->\r\n" \
                       f"    <chargingStateReportRequest:modificationReason>{self.charging_state_modification_reason}</chargingStateReportRequest:modificationReason>\r\n" \
                       f"    <chargingStateReportRequest:modificationState>{self.charging_state_modification_state}</chargingStateReportRequest:modificationState>\r\n" \
                       f"  </chargingStateReportRequest:chargeModeSelection>\r\n" \
                       f"  <chargingStateReportRequest:chargingSettingsReport remoteBattery:chargeMaxCurrent=\"{self.remote_charging_max_current}\">\r\n" \
                       f"    <remoteBattery:wirelessChargingSystemState>\r\n" \
                       f"    <wirelessChargingSystemStateType:modificationReason>{self.wireless_charging_modification_reason}</wirelessChargingSystemStateType:modificationReason>\r\n" \
                       f"    <wirelessChargingSystemStateType:modificationState>{self.wireless_charging_modification_state}</wirelessChargingSystemStateType:modificationState>\r\n" \
                       f"    <wirelessChargingSystemStateType:systemState>{self.system_state}</wirelessChargingSystemStateType:systemState>\r\n" \
                       f"  </remoteBattery:wirelessChargingSystemState>\r\n" \
                       f"  </chargingStateReportRequest:chargingSettingsReport>\r\n" \
                       f"  <chargingStateReportRequest:chargingStateReport remoteBattery:chargingStateErrorCode=\"{self.charging_state_error_code}\">\r\n" \
                       f"    <remoteBattery:actualChargeRate>117</remoteBattery:actualChargeRate>\r\n" \
                       f"    <remoteBattery:batteryConditioningState>{self.battery_condition_state}</remoteBattery:batteryConditioningState>\r\n" \
                       f"    \t<!-- batteryConditioningState:  - UNSUPPORTED !!! -\r\n" \
                       f"            \"cooling\" \"heating\" \"invalid\" \"off\" \"unsupported\"\r\n" \
                       f"\t-->\r\n    <remoteBattery:chargeRateUnit>{self.charging_rate_unit}</remoteBattery:chargeRateUnit>\r\n" \
                       f"    <remoteBattery:chargeTargetTime>\r\n" \
                       f"      <remoteBattery:day>{self.target_time_day}</remoteBattery:day>\r\n" \
                       f"      <remoteBattery:hour>{self.target_time_hour}</remoteBattery:hour>\r\n" \
                       f"      <remoteBattery:minute>{self.target_time_minute}</remoteBattery:minute>\r\n" \
                       f"      <remoteBattery:month>{self.target_time_month}</remoteBattery:month>\r\n" \
                       f"      <remoteBattery:offset>{self.target_time_offset}</remoteBattery:offset>\r\n" \
                       f"      <remoteBattery:year>{self.target_time_year}</remoteBattery:year>\r\n" \
                       f"    </remoteBattery:chargeTargetTime>\r\n" \
                       f"    <remoteBattery:chargingMode>{self.charging_mode}</remoteBattery:chargingMode>\r\n" \
                       f"    <!-- chargingMode:\r\n" \
                       f"            \"AC\"\r\n" \
                       f"            \"DC\"\r\n" \
                       f"            \"AC_and_cond\"\r\n" \
                       f"            \"DC_and_cond\"\r\n" \
                       f"\t\t\t\"off\"\r\n\t-->\r\n" \
                       f"    <remoteBattery:chargingPlugConnState>{self.charging_plug_connect_state}</remoteBattery:chargingPlugConnState>\r\n" \
                       f"    \t<!-- chargingPlugConnState:\r\n" \
                       f"            \"connected\"\r\n" \
                       f"            \"disconnected\"\r\n" \
                       f"            \"invalid\"\r\n" \
                       f"            \"unsupported\"\r\n" \
                       f"\t-->\r\n" \
                       f"    <remoteBattery:chargingPlugLockState>{self.charging_plug_lock_state}</remoteBattery:chargingPlugLockState>\r\n" \
                       f"    \t<!-- chargingPlugLockState: \t- UNSUPPORTED !!! -\r\n" \
                       f"            \"invalid\" \"locked\" \"unlocked\" \"unsupported\"\r\n\t-->\r\n" \
                       f"    <remoteBattery:chargingPower>{self.charging_power}</remoteBattery:chargingPower>\r\n" \
                       f"      <!-- chargingPower: in kW!!\r\n\t-->\r\n" \
                       f"    <remoteBattery:chargingState>{self.charging_state}</remoteBattery:chargingState>\r\n" \
                       f"    \t<!-- chargingState:\t\t\t\r\n" \
                       f"            \"charging\"\r\n" \
                       f"            \"completed\"\r\n" \
                       f"            \"conservationCharging\"\r\n" \
                       f"            \"error\"\r\n" \
                       f"            \"invalid\"\r\n" \
                       f"            \"off\"\r\n" \
                       f"            \"unsupported\"\r\n\t-->\r\n" \
                       f"    <remoteBattery:energyFlow>{self.energy_flow}</remoteBattery:energyFlow>\r\n" \
                       f"    <!-- energyFlow: \t\t\t- UNSUPPORTED !!! - \r\n" \
                       f"            \"invalid\" \"off\" \"on\" \"unsupported\"\r\n\t-->\r\n    \r\n" \
                       f"    <remoteBattery:extPowerSupplyState>{self.ext_pwr_supply_state}</remoteBattery:extPowerSupplyState>\r\n" \
                       f"    \t<!-- extPowerSupplyState:-\r\n" \
                       f"            \"available\" \r\n" \
                       f"            \"invalid\" \r\n" \
                       f"            \"station_connected\" \r\n" \
                       f"            \"unavailable\" \r\n" \
                       f"            \"unsupported\"\r\n\t-->\r\n    \r\n" \
                       f"    <remoteBattery:flapErrorState>{self.flap_error_state}</remoteBattery:flapErrorState>\r\n" \
                       f"    <remoteBattery:flapLockState>{self.flap_lock_state}</remoteBattery:flapLockState>\r\n" \
                       f"    <remoteBattery:flapState>{self.flap_state}</remoteBattery:flapState>\r\n" \
                       f"    <remoteBattery:LED_Color>{self.led_color}</remoteBattery:LED_Color>\r\n" \
                       f"    <!-- LED_Color:\t\t\r\n" \
                       f"            \"green\"\r\n" \
                       f"            \"none\"\r\n" \
                       f"            \"red\"\r\n" \
                       f"            \"yellow\"\r\n" \
                       f"            \"blue\"  <<- CBEV intelligent charging\r\n" \
                       f"            \"white\" <<- CBEV ChargingPlan is calculated\r\n\t-->\r\n" \
                       f"    <remoteBattery:LED_State>{self.led_state}</remoteBattery:LED_State>\r\n    \t<!-- LED_State: \t\t\t\r\n" \
                       f"            \"Blink\"\t\t\t// an-aus Periode gleich lange (bei Waehlhebel nicht in P)\r\n" \
                       f"            \"Flash\"\t\t\t// lange aus, kurz an -> wenn ein Timer aktiv ist\r\n" \
                       f"            \"Off\"\r\n" \
                       f"            \"PermanentOn\"\t// Batterie voll\r\n" \
                       f"            \"Pulse\"\t\t\t// Ladevorgang aktiv\r\n\t-->\r\n    \r\n" \
                       f"    <remoteBattery:plugAutoUnlock>\r\n" \
                       f"      <remoteBattery:isAcOnceActive>false</remoteBattery:isAcOnceActive>\r\n" \
                       f"      <remoteBattery:isAcPermanentActive>false</remoteBattery:isAcPermanentActive>\r\n" \
                       f"      <remoteBattery:isDcOnceActive>false</remoteBattery:isDcOnceActive>\r\n" \
                       f"      <remoteBattery:isDcPermanentActive>true</remoteBattery:isDcPermanentActive>\r\n" \
                       f"    </remoteBattery:plugAutoUnlock>\r\n" \
                       f"    <remoteBattery:plugLockState>unsupported</remoteBattery:plugLockState>\r\n" \
                       f"\t<!-- \"invalid\" \"noPlugLocked\" \"plugAAndBLocked\" \"plugALocked\" \"plugBLocked\" \"unsupported\" -->\r\n" \
                       f"    <remoteBattery:plugState>unsupported</remoteBattery:plugState>\r\n" \
                       f"\t<!-- \"invalid\" \"noPlugConnected\" \"plugAAndBConnected\" \"plugAConnected\" \"plugBConnected\" \"unsupported\"/>-->\r\n" \
                       f"    <remoteBattery:trigger>{self.trigger}</remoteBattery:trigger>\r\n" \
                       f"    \t<!-- trigger:\t\t\t\t- unsupported !!! -\r\n" \
                       f"            \"immediately\"  \"invalid\" \"push-button\" \"timer1\" \"timer2\" \"timer3\" \"timer4\" \"unsupported\"\r\n\t-->\r\n  " \
                       f"</chargingStateReportRequest:chargingStateReport>\r\n" \
                       f"  <chargingStateReportRequest:updateReason>{self.update_reason}</chargingStateReportRequest:updateReason>\r\n" \
                       f"  <!-- trigger:\t\t\t\tupdateReason:\r\n\t\t\t" \
                       f"der Wechsel von updateReason = clamp15On zu clamp15Off triggert nach X Minuten die Eingestellte Ladeerinnerungspush. \r\n" \
                       f"\t\t\t(Vorausgesetzt Stecker nicht gesteckt und SOC unter Treshhold SOC)\r\n" \
                       f"\t-->\r\n  <chargingStateReportRequest:WirelessChargingStateReport \r\n" \
                       f"  wirelessChargingStateReportType:chargingStateErrorCode=\"0\">\r\n" \
                       f"    <wirelessChargingStateReportType:chargingState>{self.charging_state}</wirelessChargingStateReportType:chargingState>\r\n" \
                       f"    <!--     <xs:simpleType name=\"chargingStateType\">\r\n" \
                       f"    \"charging\"    \"completed\"    \"conservationCharging\"    \"error\"    \"off\"    \"running\"-->\r\n" \
                       f"    <wirelessChargingStateReportType:connectionState>inactive</wirelessChargingStateReportType:connectionState>\r\n" \
                       f"    <wirelessChargingStateReportType:errorStateZMover>noError</wirelessChargingStateReportType:errorStateZMover>\r\n" \
                       f"    <wirelessChargingStateReportType:ledColor>{self.w_charge_led_color}</wirelessChargingStateReportType:ledColor>\r\n" \
                       f"    <wirelessChargingStateReportType:ledState>{self.w_charge_led_state}</wirelessChargingStateReportType:ledState>\r\n" \
                       f"    <wirelessChargingStateReportType:panelState>unsupported</wirelessChargingStateReportType:panelState>\r\n" \
                       f"    <wirelessChargingStateReportType:temporaryDeactivation>\r\n" \
                       f"        <wirelessChargingStateReportType:modificationReason>noReason</wirelessChargingStateReportType:modificationReason>\r\n" \
                       f"        <wirelessChargingStateReportType:modificationState>canNotBeModified</wirelessChargingStateReportType:modificationState>\r\n" \
                       f"        <wirelessChargingStateReportType:temporaryDeactivationState>wirelessChargingActivated</wirelessChargingStateReportType:temporaryDeactivationState>\r\n" \
                       f"    </wirelessChargingStateReportType:temporaryDeactivation>\r\n" \
                       f"    <wirelessChargingStateReportType:wirelessChargingMode>off</wirelessChargingStateReportType:wirelessChargingMode>\r\n" \
                       f"  </chargingStateReportRequest:WirelessChargingStateReport>\r\n" \
                       f"</chargingStateReportRequest:chargingStateReport>"

        self.get_payload()

    def get_payload(self):
        """Get manipulated payload for rbc cbev service.

        :rtype: str.
        :returns: Manipulated payload.
        """
        return self.payload
