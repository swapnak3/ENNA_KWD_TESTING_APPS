# -*- coding: utf-8 -*-
"""Created on 10.05.2022.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
Contains payload for RPC Extended service
"""
import datetime

from .. import interface


class Payload(interface.Payload):
    """ RPC Extended payload """

    def __init__(self, **kwargs):
        """Initialize payload object for RPC Extended service.

        :param kwargs: Arbitrary keyword arguments.
        """

        super().__init__()

        self.utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")
        self.timestamp_instrument_cluster = self.utc
        self.car_captured_utc_timestamp = (datetime.datetime.now(datetime.UTC) - datetime.timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%S")

        self.remaining_climate_time = "30"
        self.climatisation_duration = "30"

        self.climatisation_state = interface.RPCClimatisationState.HEATING.value
        self.heater_source = interface.HeaterSource.AUXILIARY.value

        self.prepare_payload(**kwargs)
        self.payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n" \
                       f"<climatisationStateReportRequest:climatisationStateReport\r\n" \
                       f" climatisationStateReportRequest:climateErrorCode=\"0\"\r\n" \
                       f" climatisationStateReportRequest:instrumentClusterTime=\"{self.timestamp_instrument_cluster}\"\r\n" \
                       f" climatisationStateReportRequest:remainingClimateTime=\"{self.remaining_climate_time}\"\r\n" \
                       f" xmlns:climatisationElementTypes=\"http://www.vw.com/mbb/climatisationElementTypes\" \r\n" \
                       f" xmlns:climatisationStateReportRequest=\"http://www.vw.com/mbb/climatisationStateReportRequest\" \r\n" \
                       f" xmlns:commonTypes=\"http://www.vw.com/mbb/commonTypes\"\r\n" \
                       f" xmlns:remoteBattery=\"http://www.vw.com/mbb/remoteBattery\"\r\n" \
                       f" xmlns:remoteClima=\"http://www.vw.com/mbb/remoteClima\"\r\n" \
                       f" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\r\n" \
                       f" xsi:schemaLocation=\"http://www.vw.com/mbb/climatisationStateReportRequest ../../XSD_mbb/2017.1/XSD_RPC/climatisationStateReportRequest_v1_0_3.xsd \">\r\n" \
                       f"\r\n" \
                       f"  <climatisationStateReportRequest:carCapturedUTCTimestamp>{self.car_captured_utc_timestamp}</climatisationStateReportRequest:carCapturedUTCTimestamp>\r\n" \
                       f"\r\n" \
                       f"  <climatisationStateReportRequest:climatisationElementStates\r\n" \
                       f"  climatisationElementTypes:extCondAvailableFL=\"true\"\r\n" \
                       f"  climatisationElementTypes:extCondAvailableFR=\"true\"\r\n" \
                       f"  climatisationElementTypes:extCondAvailableRL=\"true\"\r\n" \
                       f"  climatisationElementTypes:extCondAvailableRR=\"true\"\r\n" \
                       f"  climatisationElementTypes:isMirrorHeatingActive=\"false\">\r\n" \
                       f"    <climatisationElementTypes:zoneStates>\r\n" \
                       f"        <climatisationElementTypes:zoneState\r\n" \
                       f"            climatisationElementTypes:position=\"frontLeft\"\r\n" \
                       f"            climatisationElementTypes:isActive=\"true\" />\r\n" \
                       f"        <climatisationElementTypes:zoneState\r\n" \
                       f"            climatisationElementTypes:position=\"frontRight\"\r\n" \
                       f"            climatisationElementTypes:isActive=\"true\" />\r\n" \
                       f"        <climatisationElementTypes:zoneState\r\n" \
                       f"            climatisationElementTypes:position=\"rearLeft\"\r\n" \
                       f"            climatisationElementTypes:isActive=\"true\" />\r\n" \
                       f"        <climatisationElementTypes:zoneState\r\n" \
                       f"            climatisationElementTypes:position=\"rearRight\"\r\n" \
                       f"            climatisationElementTypes:isActive=\"true\" />\r\n" \
                       f"    </climatisationElementTypes:zoneStates>\r\n" \
                       f"  </climatisationStateReportRequest:climatisationElementStates>\r\n" \
                       f"\r\n" \
                       f"  <climatisationStateReportRequest:climatisationSettings\r\n" \
                       f"  remoteClima:climatisationDuration=\"{self.climatisation_duration}\"\r\n" \
                       f"  remoteClima:climatisationFollowupTime=\"0\"\r\n" \
                       f"  remoteClima:climatisationFollowupTimeBattery=\"0\"\r\n" \
                       f"  remoteClima:climatisationWithoutHVPower=\"true\"\r\n" \
                       f"  remoteClima:windowHeatingFront=\"true\"\r\n" \
                       f"  remoteClima:windowHeatingRear=\"true\">\r\n" \
                       f"\r\n" \
                       f"    <remoteClima:climatisationElementSettings\r\n" \
                       f"    climatisationElementTypes:isClimatisationAtUnlock=\"false\" " \
                       f"    climatisationElementTypes:isMirrorHeatingEnabled=\"false\">\r\n" \
                       f"    <climatisationElementTypes:zoneSettings>\r\n" \
                       f"        <climatisationElementTypes:zoneSetting\r\n" \
                       f"            climatisationElementTypes:position=\"frontLeft\"\r\n" \
                       f"            climatisationElementTypes:isEnabled=\"false\" />\r\n" \
                       f"        <climatisationElementTypes:zoneSetting\r\n" \
                       f"            climatisationElementTypes:position=\"frontRight\"\r\n" \
                       f"            climatisationElementTypes:isEnabled=\"false\" />\r\n" \
                       f"            <climatisationElementTypes:zoneSetting\r\n" \
                       f"            climatisationElementTypes:position=\"rearLeft\"\r\n" \
                       f"            climatisationElementTypes:isEnabled=\"true\" />\r\n" \
                       f"        <climatisationElementTypes:zoneSetting\r\n" \
                       f"            climatisationElementTypes:position=\"rearRight\"\r\n" \
                       f"            climatisationElementTypes:isEnabled=\"true\" />\r\n" \
                       f"      </climatisationElementTypes:zoneSettings>\r\n" \
                       f"    </remoteClima:climatisationElementSettings>\r\n" \
                       f"    <remoteClima:heaterMode>comfort</remoteClima:heaterMode>\r\n" \
                       f"    <remoteClima:heaterSource>{self.heater_source}</remoteClima:heaterSource>\r\n" \
                       f"    <remoteClima:startMode>heating</remoteClima:startMode>\r\n" \
                       f"    <remoteClima:targetTemperature commonTypes:state=\"valid\">2950</remoteClima:targetTemperature>\r\n" \
                       f"  </climatisationStateReportRequest:climatisationSettings>\r\n" \
                       f"\r\n" \
                       f"  <climatisationStateReportRequest:climatisationState>{self.climatisation_state}</climatisationStateReportRequest:climatisationState>\r\n" \
                       f"  <climatisationStateReportRequest:trigger>immediately</climatisationStateReportRequest:trigger>\r\n" \
                       f"</climatisationStateReportRequest:climatisationStateReport>\r\n" \

        self.get_payload()

    def get_payload(self):
        """Get payload for RPT service.

        :rtype: str.
        :returns: Payload.
        """
        return self.payload
