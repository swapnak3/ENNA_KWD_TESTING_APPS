# -*- coding: utf-8 -*-
"""Created on 07.07.2022.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
Contains payload for B9PA rah timer service.
"""

import datetime

from .. import interface


class Payload(interface.Payload):
    """B9PA Remote auxiliary heating (RAH) timer service payload."""

    def __init__(self, **kwargs):
        """Initialize payload object for B9PA rah timer service.

        :param dict kwargs: Keyword arguments to manipulate payload. Most of the instances attributes can be used as keyword arguments.
        """
        super().__init__()
        self.heater_mode = interface.HeaterMode.COMFORT.value
        self.start_mode = interface.StartMode.HEATING.value
        self.timer1_state = interface.TimerState.NOT_PROGRAMMED.value
        self.timer2_state = interface.TimerState.NOT_PROGRAMMED.value

        self.utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")
        self.timestamp_instrument_cluster = self.utc
        self.car_captured_time = self.utc + "Z"

        self.timer1_time = self.utc
        self.timer2_time = self.utc

        self.prepare_payload(**kwargs)

        self.payload = f"<departureTimersAndProfilesReportRequest:departureTimersAndProfilesReport\r\n" \
                       f"departureTimersAndProfilesReportRequest:instrumentClusterTime=\"{self.timestamp_instrument_cluster}\"\r\n" \
                       f"xmlns:root=\"http://www.vw.com/mbb/departureTimersAndProfilesReportRequest\"\r\n" \
                       f"xmlns:departureTimersAndProfilesReportRequest=\"http://www.vw.com/mbb/departureTimersAndProfilesReportRequest\">\r\n" \
                       f"    <departureTimersAndProfilesReportRequest:carCapturedUTCTimestamp>{self.car_captured_time}</departureTimersAndProfilesReportRequest:carCapturedUTCTimestamp>\r\n" \
                       f"    <departureTimersAndProfilesReportRequest:climatisationSettings\r\n" \
                       f"        xmlns:remoteClima=\"http://www.vw.com/mbb/remoteClima\">\r\n" \
                       f"        <!--  comfort, economy, invalid, normal, unsupported -->\r\n" \
                       f"        <remoteClima:heaterMode>{self.heater_mode}</remoteClima:heaterMode>\r\n" \
                       f"        <!--  automatic, auxilliary, electric, invalid, unsupported -->\r\n" \
                       f"        <remoteClima:startMode>{self.start_mode}</remoteClima:startMode>\r\n" \
                       f"        <!--  heating, invalid, unsupported, ventilation -->\r\n" \
                       f"    </departureTimersAndProfilesReportRequest:climatisationSettings>\r\n" \
                       f"    <departureTimersAndProfilesReportRequest:departureTimer_singleTimer departureICT:timerID=\"1\" xmlns:departureICT=\"http://www.vw.com/mbb/departureICT\">\r\n" \
                       f"        <!-- programmed, not_programmed -->\r\n" \
                       f"        <departureICT:timerProgrammedStatus>{self.timer1_state}</departureICT:timerProgrammedStatus>\r\n" \
                       f"        <departureICT:ICTDepartureTime>{self.timer1_time}</departureICT:ICTDepartureTime>\r\n" \
                       f"    </departureTimersAndProfilesReportRequest:departureTimer_singleTimer>\r\n" \
                       f"    <departureTimersAndProfilesReportRequest:departureTimer_singleTimer departureICT:timerID=\"2\" xmlns:departureICT=\"http://www.vw.com/mbb/departureICT\">\r\n" \
                       f"        <!-- programmed, not_programmed -->\r\n" \
                       f"        <departureICT:timerProgrammedStatus>{self.timer2_state}</departureICT:timerProgrammedStatus>\r\n" \
                       f"        <departureICT:ICTDepartureTime>{self.timer2_time}</departureICT:ICTDepartureTime>\r\n" \
                       f"    </departureTimersAndProfilesReportRequest:departureTimer_singleTimer>\r\n" \
                       f"</departureTimersAndProfilesReportRequest:departureTimersAndProfilesReport>\r\n"

        self.get_payload()

    def get_payload(self):
        """Get manipulated payload for B9PA rah timer service.

        :rtype: str.
        :returns: Manipulated payload.
        """
        return self.payload
