# -*- coding: utf-8 -*-
"""Created on 17.05.2022.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
Contains vehicle class for B9PA with VIN: "BAUPSWF472205030"
"""
from . import vin_database
from .base import Vehicle
from .. import odp_requests, components


class B9PA(Vehicle):
	"""Interface for vehicle BAUPSWF472205030.
	Generates vehicle object with vehicle specific services.

	:ivar vsr_service: Instance of vsr service.
	:ivar carfinder_service: Instance of carfinder service.
	:ivar ib_update_service: Instance of installed base update service.
	:ivar rah_quickstart_service: Instance of rah quickstart service.
	:ivar rah_b9pa_timer_service: Instance of B9PA rah timer service.
	:ivar dwa_service: Instance of dwa service.
	:ivar requests: Instance of odp requests.
	"""

	def __init__(self):
		"""Initialize object."""

		super().__init__()

		self.vin = vin_database.B9PA_VIN
		self.nickname = vin_database.B9PA_NICKNAME
		self.__backend = "ODP_APPROVAL"
		self.requests = odp_requests

		self.vsr_service = components.VSRCombustionComponent(self.vin, self.__backend)
		self.carfinder_service = components.CarFinderComponent(self.vin, self.__backend)
		self.ib_update_service = components.InstalledBaseCgwClu33(self.vin, self.__backend)

		self.rah_quickstart_service = components.RAHQuickstartComponent(self.vin, self.__backend)
		self.rah_b9pa_timer_service = components.RAHB9PATimerComponent(self.vin, self.__backend)
		self.dwa_service = components.DWAComponent(self.vin, self.__backend)
