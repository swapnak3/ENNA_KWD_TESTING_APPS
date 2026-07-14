# -*- coding: utf-8 -*-
"""Created on 07.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains payload for rah timer service.
"""

import datetime

from .. import interface


class Payload(interface.Payload):
    """Remote auxiliary heating (RAH) timer service payload."""

    def __init__(self, **kwargs):
        """Initialize payload object for rah timer service.

        :param dict kwargs: Keyword arguments to manipulate payload. Most of the instances attributes can be used as keyword arguments.
        """
        super().__init__()
        # TODO: Remove unused parameter
        self.climate_error_code = "0"
        self.remaining_climate_time = "0"
        self.climatisation_duration = "0"
        self.heater_mode = interface.HeaterMode.COMFORT.value
        self.heater_source = interface.HeaterSource.AUTOMATIC.value
        self.start_mode = interface.StartMode.HEATING.value
        self.climatisation_state = interface.ClimatisationState.OFF.value
        self.trigger = interface.RAHTrigger.IMMEDIATELY.value
        self.timer1_state = interface.TimerState.NOT_PROGRAMMED.value
        self.timer2_state = interface.TimerState.NOT_PROGRAMMED.value
        self.timer3_state = interface.TimerState.NOT_PROGRAMMED.value

        self.utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")
        self.timestamp_instrument_cluster = self.utc
        self.timestamp_utc = self.utc

        self.timer1_time = self.utc
        self.timer2_time = self.utc
        self.timer3_time = "2018-01-11T12:56:00"  # Necessary for Testing timer in the past

        self.prepare_payload(**kwargs)

        self.payload = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<tns:departureTimersAndProfilesReport\r\n" \
                       f"    tns:instrumentClusterTime=\"{self.timestamp_instrument_cluster}\" \r\n" \
                       f"    xmlns:tns=\"http://www.vw.com/mbb/departureTimersAndProfilesReportRequest\"\r\n" \
                       f"    xmlns:remoteClima=\"http://www.vw.com/mbb/remoteClima\"\r\n" \
                       f"    xmlns:departure=\"http://www.vw.com/mbb/departure\">\r\n" \
                       f"    <tns:climatisationSettings>\r\n\t\t<!-- comfort, economy, invalid, normal, unsupported -->\r\n" \
                       f"        <remoteClima:heaterMode>{self.heater_mode}</remoteClima:heaterMode>\r\n" \
                       f"    </tns:climatisationSettings>\r\n" \
                       f"    <tns:departureTimer_singleTimer departure:timerID=\"1\">\r\n" \
                       f"        <!-- programmed, not_programmed -->\r\n\t\t" \
                       f"<departure:timerProgrammedStatus>{self.timer1_state}</departure:timerProgrammedStatus>\r\n" \
                       f"        <departure:UTCDepartureTime>{self.calc_timestamp_with_utc_offset(self.timer1_time)}</departure:UTCDepartureTime>\r\n" \
                       f"    </tns:departureTimer_singleTimer>\r\n" \
                       f"    <tns:departureTimer_singleTimer departure:timerID=\"2\">\r\n\t\t" \
                       f"<!-- programmed, not_programmed -->\r\n" \
                       f"        <departure:timerProgrammedStatus>{self.timer2_state}</departure:timerProgrammedStatus>\r\n" \
                       f"        <departure:UTCDepartureTime>{self.calc_timestamp_with_utc_offset(self.timer2_time)}</departure:UTCDepartureTime>\r\n" \
                       f"    </tns:departureTimer_singleTimer>\r\n" \
                       f"     <tns:departureTimer_singleTimer departure:timerID=\"3\">\r\n\t\t" \
                       f"<!-- _Timer3InvalidTest !!! Timer weiter zuruck in Vergangenheit durfen App nicht crashen lassen-->\r\n" \
                       f"        <departure:timerProgrammedStatus>{self.timer3_state}</departure:timerProgrammedStatus>\r\n" \
                       f"        <departure:UTCDepartureTime>{self.calc_timestamp_with_utc_offset(self.timer3_time)}</departure:UTCDepartureTime>\r\n" \
                       f"    </tns:departureTimer_singleTimer>\r\n</tns:departureTimersAndProfilesReport>"

        self.get_payload()

    def get_payload(self):
        """Get manipulated payload for rah timer service.

        :rtype: str.
        :returns: Manipulated payload.
        """
        return self.payload
