# -*- coding: utf-8 -*-
"""Created on 08.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains vehicle class for A8 Alerts with VIN: "BAUCZPF8521070901"
"""
from . import vin_database
from .base import Vehicle
from .. import odp_requests, components


class TaA8AlertsAndWarning(Vehicle):
	"""Interface for vehicle BAUCZPF8521070901.
	Generates vehicle object with vehicle specific services.

	:ivar vsr_service: Instance of vsr service.
	:ivar carfinder_service: Instance of carfinder service.
	:ivar ib_update_service: Instance of installed base update service.
	:ivar speedalert_service: Instance of speed alert service.
	:ivar geofencealert_service: Instance of rbc geofence alert service.
	:ivar valetalert_service: Instance of rbc valet alert service.
	:ivar requests: Instance of odp requests.
	"""

	def __init__(self):
		"""Initialize object."""

		super().__init__()

		self.vin = vin_database.A8_ALERTS_AND_WARNINGS_VIN
		self.nickname = vin_database.A8_ALERTS_AND_WARNINGS_NICKNAME
		self.__backend = "ODP_APPROVAL"
		self.requests = odp_requests

		self.vsr_service = components.VSRCombustionComponent(self.vin, self.__backend)
		self.carfinder_service = components.CarFinderComponent(self.vin, self.__backend)
		self.ib_update_service = components.InstalledBaseCgwClu33(self.vin, self.__backend)

		self.speedalert_service = components.SpeedAlertComponent(self.vin, self.__backend)
		self.geofencealert_service = components.GeoFenceAlertComponent(self.vin, self.__backend)
		self.valetalert_service = components.ValetAlertComponent(self.vin, self.__backend)
