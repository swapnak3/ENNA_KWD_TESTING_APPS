# -*- coding: utf-8 -*-
"""Created on 07.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains payload for carfinder - valid position.
"""

import datetime

from .. import interface


class Payload(interface.Payload):
    """Carfinder valid position payload."""

    def __init__(self, **kwargs):
        """Initialize valid payload object for carfinder.

        :param dict kwargs: Keyword arguments to manipulate payload. Most of the instances attributes can be used as keyword arguments.
        """
        super().__init__()
        self.latitude = interface.GeoCoordinatesINSchlueterStr5.LATITUDE.value
        self.longitude = interface.GeoCoordinatesINSchlueterStr5.LONGITUDE.value
        self.altitude = "0"
        self.mileage = "12345"
        self.actuation = interface.RVSClampStateChanged.KL15OFF.value
        self.clamp_state = interface.ClampState.KLS_OFF.value
        self.utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")
        self.timestamp_instrument_cluster = self.utc
        self.timestamp_utc = self.utc
        self.prepare_payload(**kwargs)

        self.payload = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<rvsRdk:telemetricVehicleData xmlns:commonTypes=\"" \
                       f"http://www.vw.com/mbb/commonTypes\" xmlns:diagnostic=\"http://www.vw.com/mbb/diagnostic\" " \
                       f"xmlns:jobs=\"http://www.vw.com/mbb/jobMechanism\" xmlns:rvsRdk=\"http://www.vw.com/mbb/rvsRdk\" " \
                       f"xmlns:tyresState=\"http://www.vw.com/mbb/tyresState\" xmlns:xsi=\"" \
                       f"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.vw.com/mbb/rvsRdk ../../XSD_mbb/2018.1/TSS/rvsRdk_v1_0_1.xsd \"" \
                       f">\r\n  \r\n\r\n  \r\n\t<!-- Parklicht an/aus :: (both, invalid, left, off, right, unsupported)-->" \
                       f"\r\n\t<rvsRdk:parkingLights>off</rvsRdk:parkingLights>\r\n\r\n\r\n\t<rvsRdk:instrumentClusterTime>{self.timestamp_instrument_cluster}" \
                       f"</rvsRdk:instrumentClusterTime>\r\n\t" \
                       f"<rvsRdk:timestamp>{self.timestamp_utc}</" \
                       f"rvsRdk:timestamp>\r\n\t<rvsRdk:temperatureData>\r\n\t\t<rvsRdk:outDoorTemperature commonTypes:state=\"invalid\">0</rvsRdk:outDoorTemperature>" \
                       f"\r\n\t</rvsRdk:temperatureData>\r\n    \r\n    <!-- Trigger fuer den RVS Report (RVS_ClampStateChanged_15Off, RVS_ClampStateChanged_15On,) -->" \
                       f"\r\n\t<rvsRdk:actuation>{self.actuation}</rvsRdk:actuation>\r\n  " \
                       f"<!--\r\n\tRVS_BEMAlertChanged, \r\n\tRVS_BusSleep, \r\n\tRVS_ClampStateChanged_15Off, \r\n\tRVS_ClampStateChanged_15On, " \
                       f"\r\n\tRVS_Relock, \r\n\tRVS_RequestedByBackend, \r\n\tVHR_ConfiguredDistanceElapsed, \r\n\tVHR_ConfiguredMaintenanceDistanceElapsed, " \
                       f"\r\n\tVHR_ConfiguredTimeElapsed, \r\n\tVHR_RequestedByBackend\r\n  -->\r\n\r\n\t" \
                       f"<!--Zustand der Zuendung (clamp_15_on, clamp_S_off, clamp_S_on_clamp_15_off, invalid)-->" \
                       f"\r\n\t<rvsRdk:clampState>{self.clamp_state}</rvsRdk:clampState>\r\n      <!--\r\n\tclampState:\r\n        " \
                       f"clamp_15_on\r\n        clamp_S_off\r\n        clamp_S_on_clamp_15_off\r\n        invalid\r\n   -->" \
                       f"\r\n\r\n\t<!-- \"Carfinder Service\" can be simulated via \"setCarfinder.bat\"-->\r\n\t" \
                       f"<rvsRdk:location commonTypes:altitude=\"{self.altitude}\">\r\n\t\t<commonTypes:aggregatedConfidence commonTypes:precision=\"0\">\r\n\t\t\t" \
                       f"<commonTypes:trueness>fair</commonTypes:trueness>\r\n\t\t</commonTypes:aggregatedConfidence>\r\n\t\t" \
                       f"<commonTypes:geoCoordinate " \
                       f"commonTypes:longitude=\"{self.longitude}\" " \
                       f"commonTypes:latitude=\"{self.latitude}\"/>\r\n\t\t" \
                       f"<commonTypes:heading commonTypes:direction=\"0\"/>\r\n\t</rvsRdk:location>\r\n\t\t\t" \
                       f"<!-- ... -115151507, 36131516  CES Las Vegas-->\r\n            " \
                       f"<!-- valide Werte sind bis 180.xxxxxx (longitude) und 90.xxxxxx (latitude) mit jeweils 6 Nachkommastellen -->" \
                       f"\r\n\t\t\t<!-- 48743019, 11437349 Ingolstadt HBF -->\r\n            " \
                       f"<!-- 48152969, 11598718 Muenchen Englischer Garten -->" \
                       f"\r\n\t\t\t<!-- 48793517, 11406154 fuer RHF testing  Ingolstadt < 500m -->\r\n\t\t\t" \
                       f"<!-- 48794097, 11404330 fuer RHF testing  Ingolstadt > 500m -->\r\n\t\t\t" \
                       f"<!-- 48931552, 11547334 fuer RHF testing  Daheim\t < 500m-->\r\n\t\t\t" \
                       f"<!-- 48930283, 11541937 fuer RHF testing  Daheim\t > 500m-->\r\n            " \
                       f"<!-- 48790172, 11412034 RHF testing Ingolstadt <<< 500m -->\r\n            " \
                       f"<!-- -268435454, -134217726 invalid values I-CAN -->\r\n            " \
                       f"<!-- 52526751, 13376872 Berlin -->\r\n    " \
                       f"\t<!--\r\n\t\t!!!!!!!!!!!!!!!!CARFINDER SIMULIEREN !!!!!!!!!!!!!!!!!!\r\n\t\t" \
                       f"Durchzufuehrende Schritte\r\n\t\t\r\n\t\tzum Senden einer gueltigen Position: \r\n\t\t\t" \
                       f"update instrumentClusterTime\r\n\t\t\t\r\n\t\t\tmit gueltiger Parkdauer:\r\n\t\t\t\t- " \
                       f"actuation = RVS_ClampStateChanged_15Off\r\n\t\t\t\t- Auf Basis von \"timestamp\" wird die Parkdauer berechnet\r\n\t\t\t\t- " \
                       f"UTC Zeit!\r\n\t\t\t\t\r\n\t\t\tohne gueltiger Parkdauer (\"-\")\r\n\t\t\t\t- " \
                       f"actuation = RVS_ClampStateChanged_15On\r\n\t-->\r\n\r\n\t<!-- Kilometerstand-->\r\n\t" \
                       f"<rvsRdk:mileage>{self.mileage}</rvsRdk:mileage>    \r\n</rvsRdk:telemetricVehicleData>"

        self.get_payload()

    def get_payload(self):
        """Get manipulated payload for carfinder valid position.

        :rtype: str.
        :returns: Manipulated payload.
        """
        return self.payload
