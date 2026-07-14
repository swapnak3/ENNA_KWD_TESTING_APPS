# -*- coding: utf-8 -*-
"""Created on 10.05.2022.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
Contains payload for RDT (Remote Departure Timer) service
"""
import datetime

from .. import interface


class Payload(interface.Payload):
    """ RDT (Remote Departure Timer) payload """

    def __init__(self, **kwargs):
        """Initialize payload object for RDT service

        :param kwargs: Arbitrary keyword arguments.
        """

        super().__init__()

        self.utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")
        self.timestamp_instrument_cluster = self.utc
        self.car_captured_utc_timestamp = (datetime.datetime.now(datetime.UTC) - datetime.timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%S")

        self.profile1_departure_heater_source = interface.HeaterSource.AUTOMATIC.value
        self.profile1_active_night_rate = interface.ActiveNightRate.FALSE.value
        self.profile1_departure_charge = interface.DepartureChargeState.FALSE.value
        self.profile1_departure_climate = interface.DepartureClimateState.FALSE.value
        self.profile1_departure_start_time_hour = "4"
        self.profile1_departure_end_time_hour = "5"

        self.profile2_departure_heater_source = interface.HeaterSource.AUTOMATIC.value
        self.profile2_active_night_rate = interface.ActiveNightRate.FALSE.value
        self.profile2_departure_charge = interface.DepartureChargeState.FALSE.value
        self.profile2_departure_climate = interface.DepartureClimateState.FALSE.value
        self.profile2_departure_start_time_hour = "4"
        self.profile2_departure_end_time_hour = "5"

        self.profile3_departure_heater_source = interface.HeaterSource.AUTOMATIC.value
        self.profile3_active_night_rate = interface.ActiveNightRate.FALSE.value
        self.profile3_departure_charge = interface.DepartureChargeState.FALSE.value
        self.profile3_departure_climate = interface.DepartureClimateState.FALSE.value
        self.profile3_departure_start_time_hour = "4"
        self.profile3_departure_end_time_hour = "5"

        self.profile4_departure_heater_source = interface.HeaterSource.AUTOMATIC.value
        self.profile4_active_night_rate = interface.ActiveNightRate.FALSE.value
        self.profile4_departure_charge = interface.DepartureChargeState.FALSE.value
        self.profile4_departure_climate = interface.DepartureClimateState.FALSE.value
        self.profile4_departure_start_time_hour = "4"
        self.profile4_departure_end_time_hour = "5"

        self.profile5_departure_heater_source = interface.HeaterSource.AUTOMATIC.value
        self.profile5_active_night_rate = interface.ActiveNightRate.FALSE.value
        self.profile5_departure_charge = interface.DepartureChargeState.FALSE.value
        self.profile5_departure_climate = interface.DepartureClimateState.FALSE.value
        self.profile5_departure_start_time_hour = "4"
        self.profile5_departure_end_time_hour = "5"

        self.profile6_departure_heater_source = interface.HeaterSource.AUTOMATIC.value
        self.profile6_active_night_rate = interface.ActiveNightRate.FALSE.value
        self.profile6_departure_charge = interface.DepartureChargeState.FALSE.value
        self.profile6_departure_climate = interface.DepartureClimateState.FALSE.value
        self.profile6_departure_start_time_hour = "4"
        self.profile6_departure_end_time_hour = "5"

        self.profile7_departure_heater_source = interface.HeaterSource.AUTOMATIC.value
        self.profile7_active_night_rate = interface.ActiveNightRate.FALSE.value
        self.profile7_departure_charge = interface.DepartureChargeState.FALSE.value
        self.profile7_departure_climate = interface.DepartureClimateState.FALSE.value
        self.profile7_departure_start_time_hour = "4"
        self.profile7_departure_end_time_hour = "5"

        self.profile8_departure_heater_source = interface.HeaterSource.AUTOMATIC.value
        self.profile8_active_night_rate = interface.ActiveNightRate.FALSE.value
        self.profile8_departure_charge = interface.DepartureChargeState.FALSE.value
        self.profile8_departure_climate = interface.DepartureClimateState.FALSE.value
        self.profile8_departure_start_time_hour = "4"
        self.profile8_departure_end_time_hour = "5"

        self.timer1_programmed_status = interface.TimerProgrammedStatus.NOT_PROGRAMMED.value
        self.timer1_departure_time = "2022-04-06T04:34:13"
        self.timer2_programmed_status = interface.TimerProgrammedStatus.NOT_PROGRAMMED.value
        self.timer2_weekday_bitmask = "96"
        self.timer2_hour = "6"
        self.timer2_minute = "30"
        self.timer3_programmed_status = interface.TimerProgrammedStatus.NOT_PROGRAMMED.value
        self.timer3_departure_time = "2022-04-06T04:34:13"
        self.timer4_programmed_status = interface.TimerProgrammedStatus.NOT_PROGRAMMED.value
        self.timer4_departure_time = "2022-04-06T04:34:13"

        self.prepare_payload(**kwargs)
        self.payload = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n" \
                       f"<departureTimersAndProfilesReportRequest:departureTimersAndProfilesReport\r\n" \
                       f"departureTimersAndProfilesReportRequest:instrumentClusterTime=\"{self.timestamp_instrument_cluster}\"\r\n" \
                       f"xmlns:commonTypes=\"http://www.vw.com/mbb/commonTypes\"\r\n" \
                       f"xmlns:departure=\"http://www.vw.com/mbb/departure\"\r\n" \
                       f"xmlns:departureTimersAndProfilesReportRequest=\"http://www.vw.com/mbb/departureTimersAndProfilesReportRequest\"\r\n" \
                       f"xmlns:remoteClima=\"http://www.vw.com/mbb/remoteClima\"\r\n" \
                       f"xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\r\n" \
                       f"xsi:schemaLocation=\"http://www.vw.com/mbb/departureTimersAndProfilesReportRequest ../../XSD_files/XSD_RDT/departureTimersAndProfilesReportRequest_v1_0_1.xsd \">\r\n" \
                       f"<!-- Cluster-Time aktualisieren! -->\r\n" \
                       f"  <departureTimersAndProfilesReportRequest:carCapturedUTCTimestamp>{self.car_captured_utc_timestamp}</departureTimersAndProfilesReportRequest:carCapturedUTCTimestamp>\r\n" \
                       f"\r\n" \
                       f"  <!-- ### PROFILE DEFINITIONS ### -->\r\n" \
                       f"\r\n" \
                       f"  <!-- PROFILE 1 (Timer Laden 1) -->\r\n" \
                       f"  <departureTimersAndProfilesReportRequest:departureProfile\r\n" \
                       f"   departure:chargeMaxCurrent=\"32\" \r\n" \
                       f"   departure:profileId=\"1\" \r\n" \
                       f"   departure:profileName=\"Timerladen1\" \r\n" \
                       f"   departure:targetChargeLevel=\"100\">\r\n" \
                       f"    <departure:heaterSource>{self.profile1_departure_heater_source}</departure:heaterSource>\r\n" \
                       f"    <departure:nightRate\r\n" \
                       f"        departure:activateNightRate=\"{self.profile1_active_night_rate}\">\r\n" \
                       f"        <departure:UTCEndTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile1_departure_end_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\"/>\r\n" \
                       f"        <departure:UTCStartTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile1_departure_start_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\"/>\r\n" \
                       f"    </departure:nightRate>\r\n" \
                       f"    <departure:operation\r\n" \
                       f"    departure:charge=\"{self.profile1_departure_charge}\"\r\n" \
                       f"    departure:climate=\"{self.profile1_departure_climate}\"\r\n" \
                       f"    departure:windowHeating=\"false\"/>\r\n" \
                       f"  </departureTimersAndProfilesReportRequest:departureProfile>\r\n" \
                       f"\r\n" \
                       f"  <!-- PROFILE 2 (Timer Laden 2) -->\r\n" \
                       f"  <departureTimersAndProfilesReportRequest:departureProfile \r\n" \
                       f"   departure:chargeMaxCurrent=\"32\" \r\n" \
                       f"   departure:profileId=\"2\"	\r\n" \
                       f"   departure:profileName=\"Timerladen2\" \r\n" \
                       f"   departure:targetChargeLevel=\"100\">\r\n" \
                       f"    <departure:heaterSource>{self.profile2_departure_heater_source}</departure:heaterSource>\r\n" \
                       f"    <departure:nightRate\r\n" \
                       f"    departure:activateNightRate=\"{self.profile2_active_night_rate}\">\r\n" \
                       f"    <departure:UTCEndTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile2_departure_end_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\" />\r\n" \
                       f"        <departure:UTCStartTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile2_departure_start_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\" />\r\n" \
                       f"    </departure:nightRate>\r\n" \
                       f"    <departure:operation\r\n" \
                       f"    departure:charge=\"{self.profile2_departure_charge}\"\r\n" \
                       f"    departure:climate=\"{self.profile2_departure_climate}\"\r\n" \
                       f"    departure:windowHeating=\"false\"/>\r\n" \
                       f"  </departureTimersAndProfilesReportRequest:departureProfile>\r\n" \
                       f"\r\n" \
                       f"  <!-- PROFILE 3 (Timer Klimatisieren 1) -->\r\n" \
                       f"  <departureTimersAndProfilesReportRequest:departureProfile \r\n" \
                       f"   departure:chargeMaxCurrent=\"32\" \r\n" \
                       f"   departure:profileId=\"3\" \r\n" \
                       f"   departure:profileName=\"Timerklimatisieren1\" \r\n" \
                       f"   departure:targetChargeLevel=\"100\">\r\n" \
                       f"    <departure:heaterSource>{self.profile3_departure_heater_source}</departure:heaterSource>\r\n" \
                       f"    <departure:nightRate\r\n" \
                       f"        departure:activateNightRate=\"{self.profile3_active_night_rate}\">\r\n" \
                       f"        <departure:UTCEndTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile3_departure_end_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\"/>\r\n" \
                       f"        <departure:UTCStartTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile3_departure_start_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\"/>\r\n" \
                       f"    </departure:nightRate>\r\n" \
                       f"    <departure:operation\r\n" \
                       f"    departure:charge=\"{self.profile3_departure_charge}\"\r\n" \
                       f"    departure:climate=\"{self.profile3_departure_climate}\"\r\n" \
                       f"    departure:windowHeating=\"false\"/>\r\n" \
                       f"  </departureTimersAndProfilesReportRequest:departureProfile>\r\n" \
                       f"\r\n" \
                       f"  <!-- PROFILE 4 (Timer Klimatisieren 2) -->\r\n" \
                       f"  <departureTimersAndProfilesReportRequest:departureProfile \r\n" \
                       f"   departure:chargeMaxCurrent=\"32\" \r\n" \
                       f"   departure:profileId=\"4\"	\r\n" \
                       f"   departure:profileName=\"Timerklimatisieren2\" \r\n" \
                       f"   departure:targetChargeLevel=\"100\">\r\n" \
                       f"    <departure:heaterSource>{self.profile4_departure_heater_source}</departure:heaterSource>\r\n" \
                       f"    <departure:nightRate\r\n" \
                       f"        departure:activateNightRate=\"{self.profile4_active_night_rate}\">\r\n" \
                       f"        <departure:UTCEndTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile4_departure_end_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\"/>\r\n" \
                       f"        <departure:UTCStartTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile4_departure_start_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\"/>\r\n" \
                       f"    </departure:nightRate>\r\n" \
                       f"    <departure:operation\r\n" \
                       f"    departure:charge=\"{self.profile4_departure_charge}\"\r\n" \
                       f"    departure:climate=\"{self.profile4_departure_climate}\"\r\n" \
                       f"    departure:windowHeating=\"false\"/>\r\n" \
                       f"  </departureTimersAndProfilesReportRequest:departureProfile>\r\n" \
                       f"\r\n" \
                       f"  <!-- PROFILE 5 (Sofort Laden) -->\r\n" \
                       f"  <departureTimersAndProfilesReportRequest:departureProfile \r\n" \
                       f"   departure:chargeMaxCurrent=\"32\" \r\n" \
                       f"   departure:profileId=\"5\"	\r\n" \
                       f"   departure:profileName=\"Sofortladen\" \r\n" \
                       f"   departure:targetChargeLevel=\"100\">\r\n" \
                       f"    <departure:heaterSource>{self.profile5_departure_heater_source}</departure:heaterSource>\r\n" \
                       f"    <departure:nightRate\r\n" \
                       f"        departure:activateNightRate=\"{self.profile5_active_night_rate}\">\r\n" \
                       f"        <departure:UTCEndTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile5_departure_end_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\"/>\r\n" \
                       f"        <departure:UTCStartTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile5_departure_start_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\"/>\r\n" \
                       f"    </departure:nightRate>\r\n" \
                       f"    <departure:operation\r\n" \
                       f"    departure:charge=\"{self.profile5_departure_charge}\"\r\n" \
                       f"    departure:climate=\"{self.profile5_departure_climate}\"\r\n" \
                       f"    departure:windowHeating=\"false\"/>\r\n" \
                       f"  </departureTimersAndProfilesReportRequest:departureProfile>\r\n" \
                       f"\r\n" \
                       f"  <!-- PROFILE 6 (Sofort Klimatisieren) -->\r\n" \
                       f"  <departureTimersAndProfilesReportRequest:departureProfile \r\n" \
                       f"   departure:chargeMaxCurrent=\"32\" \r\n" \
                       f"   departure:profileId=\"6\"	\r\n" \
                       f"   departure:profileName=\"Sofortklimatisieren\" \r\n" \
                       f"   departure:targetChargeLevel=\"100\">\r\n" \
                       f"    <departure:heaterSource>{self.profile6_departure_heater_source}</departure:heaterSource>\r\n" \
                       f"    <departure:nightRate\r\n" \
                       f"        departure:activateNightRate=\"{self.profile6_active_night_rate}\">\r\n" \
                       f"        <departure:UTCEndTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile6_departure_end_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\"/>\r\n" \
                       f"        <departure:UTCStartTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile6_departure_start_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\"/>\r\n" \
                       f"    </departure:nightRate>\r\n" \
                       f"    <departure:operation\r\n" \
                       f"    departure:charge=\"{self.profile6_departure_charge}\"\r\n" \
                       f"    departure:climate=\"{self.profile6_departure_climate}\"\r\n" \
                       f"    departure:windowHeating=\"false\"/>\r\n" \
                       f"  </departureTimersAndProfilesReportRequest:departureProfile>\r\n" \
                       f"\r\n" \
                       f"  <!-- PROFILE 7 () -->\r\n" \
                       f"  <departureTimersAndProfilesReportRequest:departureProfile \r\n" \
                       f"   departure:chargeMaxCurrent=\"16\" \r\n" \
                       f"   departure:profileId=\"7\"	\r\n" \
                       f"   departure:profileName=\"BapMiniSim_Default\" \r\n" \
                       f"   departure:targetChargeLevel=\"0\">\r\n" \
                       f"    <departure:heaterSource>{self.profile7_departure_heater_source}</departure:heaterSource>\r\n" \
                       f"    <departure:nightRate\r\n" \
                       f"        departure:activateNightRate=\"{self.profile7_active_night_rate}\">\r\n" \
                       f"        <departure:UTCEndTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile7_departure_end_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\"/>\r\n" \
                       f"        <departure:UTCStartTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile7_departure_start_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\"/>\r\n" \
                       f"    </departure:nightRate>\r\n" \
                       f"    <departure:operation\r\n" \
                       f"    departure:charge=\"{self.profile7_departure_charge}\"\r\n" \
                       f"    departure:climate=\"{self.profile7_departure_climate}\"\r\n" \
                       f"    departure:windowHeating=\"false\"/>\r\n" \
                       f"  </departureTimersAndProfilesReportRequest:departureProfile>\r\n" \
                       f"\r\n" \
                       f"  <!-- PROFILE 8 () -->\r\n" \
                       f"  <departureTimersAndProfilesReportRequest:departureProfile \r\n" \
                       f"   departure:chargeMaxCurrent=\"16\" \r\n" \
                       f"   departure:profileId=\"8\" \r\n" \
                       f"   departure:profileName=\"BapMiniSim_Default\" \r\n" \
                       f"   departure:targetChargeLevel=\"0\">\r\n" \
                       f"    <departure:heaterSource>{self.profile8_departure_heater_source}</departure:heaterSource>\r\n" \
                       f"    <departure:nightRate\r\n" \
                       f"        departure:activateNightRate=\"{self.profile8_active_night_rate}\">\r\n" \
                       f"        <departure:UTCEndTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile8_departure_end_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\"/>\r\n" \
                       f"        <departure:UTCStartTime\r\n" \
                       f"        commonTypes:hour=\"{self.profile8_departure_start_time_hour}\"\r\n" \
                       f"        commonTypes:minute=\"0\"/>\r\n" \
                       f"    </departure:nightRate>\r\n" \
                       f"    <departure:operation\r\n" \
                       f"    departure:charge=\"{self.profile8_departure_charge}\"\r\n" \
                       f"    departure:climate=\"{self.profile8_departure_climate}\"\r\n" \
                       f"    departure:windowHeating=\"false\"/>\r\n" \
                       f"  </departureTimersAndProfilesReportRequest:departureProfile>\r\n" \
                       f"\r\n" \
                       f"  <!-- ### TIMER DEFINITIONS ### -->\r\n" \
                       f"  <!-- ### Timer 1 + 2 (RBC) can be single or cyclic, but are defined fixed here ### -->\r\n" \
                       f"  <!-- ### Timer 3 + 4 (RPC) can be only single ### -->\r\n" \
                       f"\r\n" \
                       f"  <!-- Timer 1 - SINGLE Timer (RBC) -->\r\n" \
                       f"  <departureTimersAndProfilesReportRequest:departureTimer_singleTimer \r\n" \
                       f"   departure:timerID=\"1\" \r\n" \
                       f"   departure:profileID=\"1\">\r\n" \
                       f"    <departure:timerChargeScheduleStatus>idle</departure:timerChargeScheduleStatus>\r\n" \
                       f"    <departure:timerClimateScheduleStatus>idle</departure:timerClimateScheduleStatus>\r\n" \
                       f"    <departure:timerExpiredStatus>NotExpired</departure:timerExpiredStatus>\r\n" \
                       f"    <departure:timerProgrammedStatus>{self.timer1_programmed_status}</departure:timerProgrammedStatus>\r\n" \
                       f"    <departure:UTCDepartureTime>{self.timer1_departure_time}</departure:UTCDepartureTime>\r\n" \
                       f"  </departureTimersAndProfilesReportRequest:departureTimer_singleTimer>\r\n" \
                       f"\r\n" \
                       f"  <!-- Timer 2 - CYCLIC Timer (RBC) -->\r\n" \
                       f"   <departureTimersAndProfilesReportRequest:departureTimer_cyclicTimer	\r\n" \
                       f"   departure:weekdayBitmask=\"{self.timer2_weekday_bitmask}\"\r\n" \
                       f"   departure:timerID=\"2\" \r\n" \
                       f"   departure:profileID=\"2\">\r\n" \
                       f"    <departure:timerChargeScheduleStatus>calculate</departure:timerChargeScheduleStatus>\r\n" \
                       f"    <departure:timerClimateScheduleStatus>calculate</departure:timerClimateScheduleStatus>\r\n" \
                       f"    <departure:timerExpiredStatus>NotExpired</departure:timerExpiredStatus>\r\n" \
                       f"    <departure:timerProgrammedStatus>{self.timer2_programmed_status}</departure:timerProgrammedStatus>\r\n" \
                       f"    <departure:UTCDepartureTimeCyclic \r\n" \
                       f"       commonTypes:hour=\"{self.timer2_hour}\"\r\n" \
                       f"       commonTypes:minute=\"{self.timer2_minute}\" />\r\n" \
                       f"  </departureTimersAndProfilesReportRequest:departureTimer_cyclicTimer>\r\n" \
                       f"\r\n" \
                       f"  <!-- Timer 3 (RPC)-->\r\n" \
                       f"  <departureTimersAndProfilesReportRequest:departureTimer_singleTimer \r\n" \
                       f"   departure:timerID=\"3\" \r\n" \
                       f"   departure:profileID=\"3\">\r\n" \
                       f"    <departure:timerChargeScheduleStatus>idle</departure:timerChargeScheduleStatus>\r\n" \
                       f"    <departure:timerClimateScheduleStatus>idle</departure:timerClimateScheduleStatus>\r\n" \
                       f"    <departure:timerExpiredStatus>NotExpired</departure:timerExpiredStatus>\r\n" \
                       f"    <departure:timerProgrammedStatus>{self.timer3_programmed_status}</departure:timerProgrammedStatus>\r\n" \
                       f"    <departure:UTCDepartureTime>{self.timer3_departure_time}</departure:UTCDepartureTime>\r\n" \
                       f"  </departureTimersAndProfilesReportRequest:departureTimer_singleTimer>\r\n" \
                       f"\r\n" \
                       f"  <!-- Timer 4 (RPC)-->\r\n" \
                       f"  <departureTimersAndProfilesReportRequest:departureTimer_singleTimer \r\n" \
                       f"   departure:timerID=\"4\" \r\n" \
                       f"   departure:profileID=\"4\">\r\n" \
                       f"    <departure:timerChargeScheduleStatus>idle</departure:timerChargeScheduleStatus>\r\n" \
                       f"    <departure:timerClimateScheduleStatus>idle</departure:timerClimateScheduleStatus>\r\n" \
                       f"    <departure:timerExpiredStatus>NotExpired</departure:timerExpiredStatus>\r\n" \
                       f"    <departure:timerProgrammedStatus>{self.timer4_programmed_status}</departure:timerProgrammedStatus>\r\n" \
                       f"    <departure:UTCDepartureTime>{self.timer4_departure_time}</departure:UTCDepartureTime>\r\n" \
                       f"  </departureTimersAndProfilesReportRequest:departureTimer_singleTimer>\r\n" \
                       f"\r\n" \
                       f"</departureTimersAndProfilesReportRequest:departureTimersAndProfilesReport>\r\n" \

        self.get_payload()

    def get_payload(self):
        """Get payload for RDT service.

        :rtype: str.
        :returns: Payload.
        """
        return self.payload
