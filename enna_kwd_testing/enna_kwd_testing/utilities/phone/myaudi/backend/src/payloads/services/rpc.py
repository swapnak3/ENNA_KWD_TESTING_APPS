# -*- coding: utf-8 -*-
"""Created on 10.05.2022.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
Contains payload for RPC service
"""
import datetime

from .. import interface


class Payload(interface.Payload):
    """ RPC payload """

    def __init__(self, **kwargs):
        """Initialize payload object for RPC service.

        :param kwargs: Arbitrary keyword arguments.
        """
        super().__init__()

        self.utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")
        self.timestamp_instrument_cluster = self.utc

        self.remaining_climate_time = "30"
        self.climatisation_duration = "30"
        self.climatisation_state = interface.RPCClimatisationState.HEATING.value
        self.heater_source = interface.HeaterSource.AUXILIARY.value

        self.prepare_payload(**kwargs)

        self.payload = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n" \
                       f"<climatisationStateReportRequest:climatisationStateReport \r\n" \
                       f" climatisationStateReportRequest:climateErrorCode=\"0\"\r\n" \
                       f" climatisationStateReportRequest:instrumentClusterTime=\"{self.timestamp_instrument_cluster}\" \r\n" \
                       f" climatisationStateReportRequest:remainingClimateTime=\"{self.remaining_climate_time}\"\r\n" \
                       f" xmlns:climatisationElementTypes=\"http://www.vw.com/mbb/climatisationElementTypes\" " \
                       f" xmlns:climatisationStateReportRequest=\"http://www.vw.com/mbb/climatisationStateReportRequest\" " \
                       f" xmlns:commonTypes=\"http://www.vw.com/mbb/commonTypes\"\r\n" \
                       f" xmlns:remoteBattery=\"http://www.vw.com/mbb/remoteBattery\"\r\n" \
                       f" xmlns:remoteClima=\"http://www.vw.com/mbb/remoteClima\"\r\n" \
                       f" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\r\n" \
                       f" xsi:schemaLocation=\"http://www.vw.com/mbb/climatisationStateReportRequest ../../XSD_mbb/2017.1/XSD_RPC/climatisationStateReportRequest_v1_0_3.xsd \">\r\n" \
                       f"   <climatisationStateReportRequest:climatisationSettings\r\n" \
                       f"     remoteClima:climatisationDuration=\"{self.climatisation_duration}\"\r\n" \
                       f"     remoteClima:climatisationFollowupTime=\"5\"\r\n" \
                       f"     remoteClima:climatisationFollowupTimeBattery=\"5\"\r\n" \
                       f"     remoteClima:climatisationWithoutHVPower=\"true\">\r\n" \
                       f"   <remoteClima:heaterSource>{self.heater_source}</remoteClima:heaterSource>\r\n" \
                       f"   </climatisationStateReportRequest:climatisationSettings>\r\n" \
                       f"   <climatisationStateReportRequest:climatisationState>{self.climatisation_state}</climatisationStateReportRequest:climatisationState>\r\n" \
                       f"<climatisationStateReportRequest:trigger>immediately</climatisationStateReportRequest:trigger>\r\n" \
                       f"</climatisationStateReportRequest:climatisationStateReport>"

        self.get_payload()

    def get_payload(self):
        """Get payload for RPT service.

        :rtype: str.
        :returns: Payload.
        """
        return self.payload
