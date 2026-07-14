# -*- coding: utf-8 -*-
"""Created on 07.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains payload for geofence alert violation.
"""

import datetime

from .. import interface


class Payload(interface.Payload):
    """Geofence Alert violation payload."""

    def __init__(self, **kwargs):
        """Initialize payload object for geofence alert violation.

        :param dict kwargs: Keyword arguments to manipulate payload. Most of the instances attributes can be used as keyword arguments.
        """
        super().__init__()
        self.geo_uuid = None
        self.area_id = None
        self.id = "1"
        self.event_type = interface.GeoFencingEventType.EXIT.value
        self.utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")
        self.timestamp_instrument_cluster = self.utc
        self.timestamp_utc = self.utc
        self.prepare_payload(**kwargs)

        self.payload = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n\r\n" \
                       f"<geoFencing:geoFenceViolationRequestType geoFencing:geoFenceId=\"{self.id}\" geoFencing:uuid=\"{self.geo_uuid}\"" \
                       f" xmlns:root=\"http://www.vw.com/mbb/geoFencing\" xmlns:geoFencing=\"" \
                       f"http://www.vw.com/mbb/geoFencing\"> \r\n<geoFencing:geoFencingAreaViolated geoFencing:area_id=\"{self.area_id}\" /> \r\n" \
                       f"<geoFencing:geoFencingEventType>{self.event_type}</geoFencing:geoFencingEventType>  <!-- Enter / Exit -->\r\n" \
                       f"<geoFencing:location commonTypes:altitude=\"426\" xmlns:commonTypes=\"http://www.vw.com/mbb/commonTypes\"> \r\n" \
                       f"<commonTypes:aggregatedConfidence commonTypes:precision=\"100\"> \r\n" \
                       f"<commonTypes:trueness>fair</commonTypes:trueness>\r\n" \
                       f"</commonTypes:aggregatedConfidence> \r\n" \
                       f"<commonTypes:geoCoordinate commonTypes:latitude=\"48810455\" commonTypes:longitude=\"11511094\" /> \r\n" \
                       f"<commonTypes:heading commonTypes:direction=\"90\" /> \r\n" \
                       f"</geoFencing:location> \r\n<geoFencing:utcTime>{self.timestamp_utc}</geoFencing:utcTime> \r\n" \
                       f"</geoFencing:geoFenceViolationRequestType>"

        self.get_payload()

    def get_payload(self):
        """Get manipulated payload for geofence alert violation.

        :rtype: str.
        :returns: Manipulated payload.
        """
        return self.payload
