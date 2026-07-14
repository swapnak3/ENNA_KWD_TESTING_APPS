# -*- coding: utf-8 -*-
"""Module contains all MyAudi Screen deeplinks."""


class Screen:
    """A container for a deeplink string which exists for different mobile OS."""

    def __init__(self, deeplink):
        """Initialize deeplink string object

        :param deeplink: The deeplink uri for the desired screen on device.
        :type deeplink: str, dict
        """
        self.data = deeplink

    def __call__(self, **kwargs):
        """Call class like a function. Get deeplink.

        :param dict kwargs: Contains keyword arguments to setup deeplink (e.g. VIN, countryCode, etc.).
        :rtype: str, dict
        :return: Deeplink or deeplinks to use by screen selector.
        """
        return self.get(**kwargs)

    def get(self, **kwargs):
        """Get the deeplink and evaluate with possible variables which select the content.
        If a required parameter is not given, the deeplink will contain "None" at the actual parameter position.

        :param kwargs: Arbitrary keyword arguments.
        :key str VIN: which should be used in the deeplink if available in uri.
        :rtype: str, dict
        :return: Formatted deeplinks.
        """
        if isinstance(self.data, str):
            return self.data.format(**kwargs)
        else:
            for key, value in self.data.items():
                self.data[key] = value.format(**kwargs)
            return self.data


SCREEN_LIST = {"DASHBOARD": Screen("/loggedIn/vehicleDashboard/{VIN}"),
               "DASHBOARD_VEH_STATUS": Screen("/loggedIn/vehicleDashboard/{VIN}/vehicleStatus"),
               "REMOTE_PARKING_ASSIST": Screen("/loggedIn/vehicleDashboard/{VIN}/remoteParkingAssistant"),
               "CHARGING": Screen("/loggedIn/vehicleDashboard/{VIN}/charging"),
               "CHARGING_TIMERS": Screen("/loggedIn/vehicleDashboard/{VIN}/charging/timers"),
               "CHARGING_SETTINGS": Screen("/loggedIn/vehicleDashboard/{VIN}/charging/settings"),
               "CLIMATE_QUICK_START_STOP": Screen("/loggedIn/vehicleDashboard/{VIN}/climatisation/quickStartOrQuickStop"),
               "CLIMATE_TIMERS": Screen("/loggedIn/vehicleDashboard/{VIN}/climatisation/timers"),
               "RAH_QUICK_START_STOP": Screen("/loggedIn/vehicleDashboard/{VIN}/remoteAuxiliaryHeating/quickStartOrQuickStop"),
               "RAH_TIMERS": Screen("/loggedIn/vehicleDashboard/{VIN}/remoteAuxiliaryHeating/timers"),
               "RHF": Screen("/loggedIn/vehicleDashboard/{VIN}/remoteHonkAndFlash"),
               "THEFT_ALARM": Screen("/loggedIn/vehicleDashboard/{VIN}/theftAlarm"),
               "GEOFENCE_ALERT": Screen("/loggedIn/vehicleDashboard/{VIN}/geofenceAlert"),
               "GEOFENCE_ALERT_VIOLATIONS": Screen("/loggedIn/vehicleDashboard/{VIN}/geofenceAlert/violations"),
               "SPEED_ALERT": Screen("/loggedIn/vehicleDashboard/{VIN}/speedAlert"),
               "SPEED_ALERT_VIOLATIONS": Screen("/loggedIn/vehicleDashboard/{VIN}/speedAlert/violations"),
               "VALET_ALERT": Screen("/loggedIn/vehicleDashboard/{VIN}/valetAlert"),
               "VALET_ALERT_VIOLATIONS": Screen("/loggedIn/vehicleDashboard/{VIN}/valetAlert/violations")}
