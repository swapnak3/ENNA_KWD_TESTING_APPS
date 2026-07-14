# -*- coding: utf-8 -*-
"""Created on 07.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains payload for carfinder - invalid position.
"""
import datetime

from .. import interface


class Payload(interface.Payload):
    """Carfinder invalid position payload."""

    def __init__(self, **kwargs):
        """Initialize invalid payload object for carfinder.

        :param dict kwargs: Keyword arguments to manipulate payload. Most of the instances attributes can be used as keyword arguments.
        """

        super().__init__()
        self.utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")
        self.timestamp_instrument_cluster = self.utc
        self.timestamp_utc = self.utc
        self.mileage = "12345"
        self.actuation = interface.RVSClampStateChanged.KL15OFF.value
        self.clamp_state = interface.ClampState.KLS_OFF.value
        self.prepare_payload(**kwargs)
        self.payload = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<rvsRdk:telemetricVehicleData " \
                       f"xmlns:commonTypes=\"http://www.vw.com/mbb/commonTypes\" " \
                       f"xmlns:diagnostic=\"http://www.vw.com/mbb/diagnostic\" xmlns:jobs=\"http://www.vw.com/mbb/jobMechanism\" " \
                       f"xmlns:rvsRdk=\"http://www.vw.com/mbb/rvsRdk\" xmlns:tyresState=\"http://www.vw.com/mbb/tyresState\" " \
                       f"xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" " \
                       f"xsi:schemaLocation=\"http://www.vw.com/mbb/rvsRdk ../../XSD_mbb/2018.1/TSS/rvsRdk_v1_0_1.xsd \">\r\n  \r\n\t" \
                       f"<!-- Parklicht an/aus :: (both, invalid, left, off, right, unsupported)-->\r\n\t<rvsRdk:parkingLights>left</rvsRdk:parkingLights>\r\n    \r\n\t" \
                       f"<rvsRdk:instrumentClusterTime>{self.timestamp_instrument_cluster}</rvsRdk:instrumentClusterTime>\r\n\t" \
                       f"<rvsRdk:timestamp>{self.timestamp_utc}</rvsRdk:timestamp>\r\n\t<rvsRdk:temperatureData>\r\n\t\t" \
                       f"<rvsRdk:outDoorTemperature commonTypes:state=\"invalid\">0</rvsRdk:outDoorTemperature>\r\n\t" \
                       f"</rvsRdk:temperatureData>\r\n\r\n    <rvsRdk:lastPositionDeprecated>true</rvsRdk:lastPositionDeprecated>\r\n\r\n" \
                       f"    \r\n    <!-- Trigger fuer den RVS Report (RVS_ClampStateChanged_15Off, RVS_ClampStateChanged_15On,) -->\r\n\t" \
                       f"<rvsRdk:actuation>{self.actuation}</rvsRdk:actuation>\r\n  <!--\r\n\tRVS_BEMAlertChanged, \r\n\t" \
                       f"RVS_BusSleep, \r\n\tRVS_ClampStateChanged_15Off, \r\n\tRVS_ClampStateChanged_15On, \r\n\tRVS_Relock, \r\n\t" \
                       f"RVS_RequestedByBackend, \r\n\tVHR_ConfiguredDistanceElapsed, \r\n\tVHR_ConfiguredMaintenanceDistanceElapsed, \r\n\t" \
                       f"VHR_ConfiguredTimeElapsed, \r\n\tVHR_RequestedByBackend\r\n  -->" \
                       f"\r\n\r\n\t<!--Zustand der Zuendung (clamp_15_on, clamp_S_off, clamp_S_on_clamp_15_off, invalid)-->\r\n\t" \
                       f"<rvsRdk:clampState>{self.clamp_state}</rvsRdk:clampState>\r\n      <!--\r\n\tclampState:\r\n        " \
                       f"clamp_15_on\r\n        clamp_S_off\r\n        clamp_S_on_clamp_15_off\r\n        invalid\r\n   -->\r\n\r\n\r\n" \
                       f"    \t<!--\r\n\t\t!!!!!!!!!!!!!!!!CARFINDER SIMULIEREN !!!!!!!!!!!!!!!!!!\r\n\t\tDurchzufuehrende Schritte\r\n\t\t\r\n\t\t" \
                       f"zum Senden einer gueltigen Position: \r\n\t\t\tupdate instrumentClusterTime\r\n\t\t\t\r\n\t\t\tmit gueltiger Parkdauer:" \
                       f"\r\n\t\t\t\t- actuation = RVS_ClampStateChanged_15Off\r\n\t\t\t\t- Auf Basis von \"timestamp\" wird die Parkdauer berechnet\r\n\t\t\t\t" \
                       f"- UTC Zeit!\r\n\t\t\t\t\r\n\t\t\tohne gueltiger Parkdauer (\"-\")\r\n\t\t\t\t- actuation = RVS_ClampStateChanged_15On\r\n\t" \
                       f"-->\r\n\r\n\t<!-- Kilometerstand-->\r\n\t<rvsRdk:mileage>{self.mileage}</rvsRdk:mileage>    \r\n</rvsRdk:telemetricVehicleData>"

        self.get_payload()

    def get_payload(self):
        """Get manipulated payload for carfinder invalid position.

        :rtype: str.
        :returns: Manipulated payload.
        """
        return self.payload
