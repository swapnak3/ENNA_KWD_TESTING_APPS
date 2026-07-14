# -*- coding: utf-8 -*-
"""Created on 25.05.2023.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
"""
from . import vin_database
from .base import Vehicle
from .. import odp_requests, components


class Q7PhevHeaterSourceQuickstart(Vehicle):
	"""Interface for vehicle BAUMLH4MZ22062701.
	Generates vehicle object with vehicle specific services.
	"""

	def __init__(self):
		"""Initialize object."""

		super().__init__()

		self.vin = vin_database.Q7_HEATER_SOURCE_QUICKSTART_VIN
		self.nickname = vin_database.Q7_HEATER_SOURCE_QUICKSTART_NICKNAME
		self.__backend = "ODP_APPROVAL"
		self.requests = odp_requests

		self.vsr_service = components.VSRCngComponent(self.vin, self.__backend)
		self.carfinder_service = components.CarFinderComponent(self.vin, self.__backend)
		self.ib_update_service = components.InstalledBaseCgwClu33(self.vin, self.__backend)

		self.rpc_service = components.RPC(self.vin, self.__backend)
		self.rpc_extended_service = components.RPCExtended(self.vin, self.__backend)
