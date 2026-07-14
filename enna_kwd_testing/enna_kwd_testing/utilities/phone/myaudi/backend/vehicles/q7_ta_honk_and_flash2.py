# -*- coding: utf-8 -*-
"""Created on 07.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains vehicle class for TA ODP Q7 Honk and Flash 2 with VIN: "BAUBER4MZ21032502"
"""
from . import vin_database
from .base import Vehicle

from .. import odp_requests, components


class TaOdpQ7HonkAndFlash2(Vehicle):
	"""Interface for vehicle BAUBER4MZ21032502.
	Generates vehicle object with vehicle specific services.

	:ivar vsr_service: Instance of vsr service.
	:ivar carfinder_service: Instance of carfinder service.
	:ivar ib_update_service: Instance of installed base update service.
	:ivar rah_quickstart_service: Instance of rah quickstart service.
	:ivar rah_timer_service: Instance of rah timer service.
	:ivar rhf_service: Instance of rhf service.
	:ivar requests: Instance of odp requests.
	"""
	def __init__(self):
		"""Initialize object."""

		super().__init__()

		self.vin = vin_database.Q7_HONK_AND_FLASH_2_VIN
		self.nickname = vin_database.Q7_HONK_AND_FLASH_2_NICKNAME
		self.__backend = "ODP_APPROVAL"
		self.requests = odp_requests

		self.vsr_service = components.VSRCombustionComponent(self.vin, self.__backend)
		self.carfinder_service = components.CarFinderComponent(self.vin, self.__backend)
		self.ib_update_service = components.InstalledBaseCgwClu33(self.vin, self.__backend)

		self.rah_quickstart_service = components.RAHQuickstartComponent(self.vin, self.__backend)
		self.rah_timer_service = components.RAHTimerComponent(self.vin, self.__backend)
		self.rhf_service = components.RHFComponent(self.vin, self.__backend)
