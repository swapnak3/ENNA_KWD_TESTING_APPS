# -*- coding: utf-8 -*-
"""Created on 07.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains payload for dwa service.

"""

import datetime

from .. import interface


class Payload(interface.Payload):
    """Diebstahl Warnanlage payload."""

    def __init__(self, **kwargs):
        """Initialize payload object for dwa service.

        :param dict kwargs: Keyword arguments to manipulate payload. Most of the instances attributes can be used as keyword arguments.
        """
        super().__init__()
        self.alarm_reason = None
        self.utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")

        self.prepare_payload(**kwargs)
        self.payload = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<!-- \r\nAlarm Reasons\r\n\r\n" \
                       f"01_DriversDoorOpen (Exterior Alarm)\r\n" \
                       f"08_CabinIRUEArmedAlarm (Interior Alarm)\r\n" \
                       f"11_TiltSensorArmedAlarm (Movement Alarm)\r\n" \
                       f"19_TrailerDisconnected (Trailer Alarm)\r\n\r\n" \
                       f"-->\r\n\r\n<dwap:DWAPushNotification xmlns:dwap=\"http://www.vw.com/mbb/dwaPushNotification\"" \
                       f" dwap:dwaActiveState=\"dwaActiveArmed\" dwap:dwaAlarmReason=\"{self.alarm_reason}\" " \
                       f"dwap:dwaAlarmState=\"dwaActiveTriggered\" dwap:dwaRestriction=\"dwaNoRestriction\" " \
                       f"dwap:mileage=\"100\">\r\n\t<dwap:utcTime>{self.utc}</dwap:utcTime>\r\n" \
                       f"</dwap:DWAPushNotification>"

        self.get_payload()

    def get_payload(self):
        """Get manipulated payload for dwa service.

        :rtype: str.
        :returns: Manipulated payload.
        """
        return self.payload
