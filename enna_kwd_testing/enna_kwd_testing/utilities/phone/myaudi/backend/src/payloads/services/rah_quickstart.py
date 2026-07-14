# -*- coding: utf-8 -*-
"""Created on 07.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains payload for rah quickstart service.
"""

import datetime

from .. import interface


class Payload(interface.Payload):
    """Remote auxiliary heating (RAH) quickstart service payload."""

    def __init__(self, **kwargs):
        """Initialize payload object for rah quickstart service.

        :param dict kwargs: Keyword arguments to manipulate payload. Most of the instances attributes can be used as keyword arguments.
        """
        super().__init__()
        self.climate_error_code = "0"
        self.remaining_climate_time = "0"
        self.climatisation_duration = "30"
        self.heater_mode = interface.HeaterMode.COMFORT.value
        self.heater_source = interface.HeaterSource.AUTOMATIC.value
        self.start_mode = interface.StartMode.HEATING.value
        self.climatisation_state = interface.ClimatisationState.HEATING.value
        self.trigger = interface.RAHTrigger.INVALID.value

        self.utc = datetime.datetime.now(datetime.UTC)
        self.timestamp_instrument_cluster = datetime.datetime.now().strftime("%Y-%m-%dT%I:%M:%S")
        self.timestamp_utc_z = self.calc_timestamp_with_utc_offset()
        self.prepare_payload(**kwargs)

        self.payload = f"<?xml version=\'1.0\' encoding=\'UTF-8\'?>\r\n" \
                       f"<climatisationStateReportRequest:climatisationStateReport xmlns:climatisationElementTypes=\"" \
                       f"http://www.vw.com/mbb/climatisationElementTypes\" xmlns:climatisationStateReportRequest=\"" \
                       f"http://www.vw.com/mbb/climatisationStateReportRequest\" xmlns:remoteBattery=\"" \
                       f"http://www.vw.com/mbb/remoteBattery\" xmlns:remoteClima=\"http://www.vw.com/mbb/remoteClima\"" \
                       f" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" climatisationStateReportRequest:climateErrorCode=\"{self.climate_error_code}\"" \
                       f" climatisationStateReportRequest:instrumentClusterTime=\"{self.timestamp_instrument_cluster}\"" \
                       f" climatisationStateReportRequest:remainingClimateTime=\"{self.remaining_climate_time}\" xsi:schemaLocation=\"" \
                       f"http://www.vw.com/mbb/climatisationStateReportRequest ../../XSD_mbb/2018.1/XSD_RAH/climatisationStateReportRequest_v1_0_3.xsd \">\r\n" \
                       f"  <climatisationStateReportRequest:carCapturedUTCTimestamp>{self.timestamp_utc_z}</climatisationStateReportRequest:carCapturedUTCTimestamp>\r\n" \
                       f"  <climatisationStateReportRequest:climatisationSettings remoteClima:climatisationDuration=\"{self.climatisation_duration}\"> \r\n" \
                       f"    <remoteClima:heaterMode>{self.heater_mode}</remoteClima:heaterMode>\r\n" \
                       f"    <!-- \"comfort\" \"economy\" \"invalid\" \"normal\" \"unsupported\"-->\r\n" \
                       f"    <remoteClima:heaterSource>{self.heater_source}</remoteClima:heaterSource>\r\n" \
                       f"    <!--  \"automatic\" \"auxilliary\" \"electric\" \"invalid\" \"unsupported\"/>-->\r\n" \
                       f"    <remoteClima:startMode>{self.start_mode}</remoteClima:startMode>\r\n" \
                       f"    <!--  \"heating\" \"invalid\" \"unsupported\" \"ventilation\" -->\r\n" \
                       f"  </climatisationStateReportRequest:climatisationSettings>\r\n" \
                       f"  <climatisationStateReportRequest:climatisationState>{self.climatisation_state}</climatisationStateReportRequest:climatisationState>\r\n" \
                       f"  <!-- Gultige Werte nur \"heating\", \"ventilation\", \"off\" oder \"invalid\" & \"completed\" vgl. " \
                       f"KPM 7348835 2017-11-24, Schuler:  (Erganzung in Mail vom 29.11. 11:03\r\n" \
                       f"  (cooling, und heating_auxiliary gibt es bei RAH Audi nicht)-->\r\n" \
                       f"  <climatisationStateReportRequest:trigger>{self.trigger}</climatisationStateReportRequest:trigger>\r\n" \
                       f"  <!-- \"immediately\" \"invalid\" \"push-button\" \"timer1\" \"timer2\" \"unsupported\"-->\r\n" \
                       f"</climatisationStateReportRequest:climatisationStateReport>"

        self.get_payload()

    def get_payload(self):
        """Get manipulated payload for rah quickstart service.

        :rtype: str.
        :returns: Manipulated payload.
        """
        return self.payload
