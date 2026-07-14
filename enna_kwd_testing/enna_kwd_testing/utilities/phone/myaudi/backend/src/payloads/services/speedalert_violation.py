# -*- coding: utf-8 -*-
"""Created on 07.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains payload for speed alert violation.
"""

import datetime

from .. import interface


class Payload(interface.Payload):
    """Speed alert violation payload."""

    def __init__(self, **kwargs):
        """Initialize payload object for speed alert violation.

        :param dict kwargs: Keyword arguments to manipulate payload. Most of the instances attributes can be used as keyword arguments.
        """
        super().__init__()
        self.uuid = None
        self.alert_state = interface.AlertState.START.value
        self.utc = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S")
        self.id = "1"
        self.timestamp_instrument_cluster = self.utc
        self.timestamp_utc = self.utc
        self.prepare_payload(**kwargs)

        self.payload = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n" \
                       f"<speedAlert:speedLimitViolationRequestType speedAlert:speedAlertID=\"{self.id}\"" \
                       f" speedAlert:speedLimitKmPerHour=\"70\" speedAlert:uuid=\"{self.uuid}\"" \
                       f" xmlns:baseSchedule=\"http://www.vw.com/mbb/baseSchedule\" xmlns:commonTypes=\"" \
                       f"http://www.vw.com/mbb/commonTypes\" xmlns:jobs=\"http://www.vw.com/mbb/jobMechanism\"" \
                       f" xmlns:speedAlert=\"http://www.vw.com/mbb/speedAlert\" xmlns:xsi=\"" \
                       f"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"" \
                       f"http://www.vw.com/mbb/speedAlert speedAlert_v1_0_0.xsd \">\r\n" \
                       f"  <speedAlert:state>{self.alert_state}</speedAlert:state> <!-- Start / End -->\r\n" \
                       f"  <speedAlert:timestamp>{self.timestamp_utc}</speedAlert:timestamp>\r\n" \
                       f"</speedAlert:speedLimitViolationRequestType>"

        self.get_payload()

    def get_payload(self):
        """Get manipulated payload for speed alert violation.

        :rtype: str.
        :returns: Manipulated payload.
        """
        return self.payload
