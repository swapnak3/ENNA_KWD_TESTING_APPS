# -*- coding: utf-8 -*-
"""Created on 17.05.2022.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
Contains vehicle class for TA ODP Q7 PHEV 2 with VIN: "BAUPSW4MZ2204140"
"""
from . import vin_database
from .base import Vehicle
from .. import odp_requests, components


class TaOdpQ7Phev2(Vehicle):
	"""Interface for vehicle BAUPSW4MZ2204140.
	Generates vehicle object with vehicle specific services.

	:ivar vsr_service: Instance of vsr service.
	:ivar carfinder_service: Instance of carfinder service.
	:ivar ib_update_service: Instance of installed base update service.
	:ivar dwa_service: Instance of dwa service.
	:ivar rbc_quickstart: Instance of rbc quickstart service.
	:ivar rdt_service: Instance of RDT service
	:ivar rdt_extended_service: Instance of RDT-Extended service
	:ivar rpc_service: Instance of RPC Service
	:ivar rpc_extended_service: Instance of RPC-Extended service
	:ivar requests: Instance of odp requests.
	"""

	def __init__(self):
		"""Initialize object."""

		super().__init__()

		self.vin = vin_database.Q7_PHEV_2_VIN
		self.nickname = vin_database.Q7_PHEV_2_NICKNAME
		self.__backend = "ODP_APPROVAL"
		self.requests = odp_requests

		self.vsr_service = components.VSRPhevComponent(self.vin, self.__backend)
		self.carfinder_service = components.CarFinderComponent(self.vin, self.__backend)
		self.ib_update_service = components.InstalledBaseCgwClu33(self.vin, self.__backend)

		self.dwa_service = components.DWAComponent(self.vin, self.__backend)
		self.rbc_quickstart = components.RBCQuickstartPHEV(self.vin, self.__backend)
		self.rdt_service = components.RDT(self.vin, self.__backend)
		self.rdt_extended_service = components.RDTExtended(self.vin, self.__backend)
		self.rpc_service = components.RPC(self.vin, self.__backend)
		self.rpc_extended_service = components.RPCExtended(self.vin, self.__backend)
