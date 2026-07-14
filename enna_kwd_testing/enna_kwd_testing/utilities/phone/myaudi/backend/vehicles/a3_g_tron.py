# -*- coding: utf-8 -*-
"""Created on 31.03.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains vehicle class for A8 Alerts with VIN: "BAUPKC8V221081101"
"""
from . import vin_database
from .base import Vehicle
from .. import odp_requests, components


class A3Gtron(Vehicle):
	"""Interface for vehicle BAUPKC8V221081101.
	Generates vehicle object with vehicle specific services.

	:ivar vsr_service: Instance of vsr service.
	:ivar carfinder_service: Instance of carfinder service.
	:ivar ib_update_service: Instance of installed base update service.
	:ivar requests: Instance of odp requests.
	"""

	def __init__(self):
		"""Initialize object."""

		super().__init__()

		self.vin = vin_database.A3_SPORTSBACK_CNG_VIN
		self.nickname = vin_database.A3_SPORTSBACK_CNG_NICKNAME
		self.__backend = "ODP_APPROVAL"
		self.requests = odp_requests

		self.vsr_service = components.VSRCngComponent(self.vin, self.__backend)
		self.carfinder_service = components.CarFinderComponent(self.vin, self.__backend)
		self.ib_update_service = components.InstalledBaseCgwClu33(self.vin, self.__backend)
