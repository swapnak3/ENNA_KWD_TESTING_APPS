# -*- coding: utf-8 -*-
"""Created on 25.05.2023.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
"""
from . import vin_database
from .base import Vehicle
from .. import odp_requests, components


class B9RahRhfAlComb1(Vehicle):
	"""Interface for vehicle BAUPSWF4823041101.
	Generates vehicle object with vehicle specific services.
	"""

	def __init__(self):
		"""Initialize object."""

		super().__init__()

		self.vin = vin_database.B9_RAH_RHF_AL_COMB_VIN
		self.nickname = vin_database.B9_RAH_RHF_AL_COMB_NICKNAME
		self.__backend = "ODP_APPROVAL"
		self.requests = odp_requests

		self.vsr_service = components.VSRCombustionComponent(self.vin, self.__backend)
		self.carfinder_service = components.CarFinderComponent(self.vin, self.__backend)
		self.ib_update_service = components.InstalledBaseCgwClu33(self.vin, self.__backend)

		self.dwa_service = components.DWAComponent(self.vin, self.__backend)
		self.rah_quickstart_service = components.RAHQuickstartComponent(self.vin, self.__backend)
		self.rah_timer_service = components.RAHTimerComponent(self.vin, self.__backend)
		self.rhf_service = components.RHFComponent(self.vin, self.__backend)
		self.speedalert_service = components.SpeedAlertComponent(self.vin, self.__backend)
		self.geofencealert_service = components.GeoFenceAlertComponent(self.vin, self.__backend)
		self.valetalert_service = components.ValetAlertComponent(self.vin, self.__backend)
