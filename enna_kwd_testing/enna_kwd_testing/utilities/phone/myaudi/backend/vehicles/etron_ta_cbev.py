# -*- coding: utf-8 -*-
"""Created on 10.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains vehicle class for TA ODP etron CBEV with VIN: "BAUCZPGEZ21070902"
"""
from . import vin_database
from .base import Vehicle
from .. import odp_requests, components


class TaOdpeTronCBEV(Vehicle):
	"""Interface for vehicle BAUCZPGEZ21070902.
	Generates vehicle object with vehicle specific services.

	:ivar vsr_service: Instance of vsr service.
	:ivar carfinder_service: Instance of carfinder service.
	:ivar dwa_service: Instance of dwa service.
	:ivar ib_update_service: Instance of installed base update service.
	:ivar rbc_quickstart: Instance of rbc quickstart service.
	:ivar rpt_profile_service: Instance of RPT-Profile service
	:ivar rpt_timer_service: Instance of RPT-Timer service
	:ivar rpc_service: Instance of RPC Service
	:ivar rpc_extended_service: Instance of RPC-Extended service
	:ivar requests: Instance of odp requests.
	"""

	def __init__(self):
		"""Initialize object."""

		super().__init__()

		self.vin = vin_database.ETRON_VIN
		self.nickname = vin_database.ETRON_NICKNAME
		self.__backend = "ODP_APPROVAL"
		self.requests = odp_requests

		self.vsr_service = components.VSRCbevComponent(self.vin, self.__backend)
		self.carfinder_service = components.CarFinderComponent(self.vin, self.__backend)
		self.ib_update_service = components.InstalledBaseCgwClu33(self.vin, self.__backend)

		self.dwa_service = components.DWAComponent(self.vin, self.__backend)
		self.rbc_quickstart = components.RBCQuickstartCBEV(self.vin, self.__backend)
		self.rpt_profile_service = components.RPTProfile(self.vin, self.__backend)
		self.rpt_timer_service = components.RPTTimer(self.vin, self.__backend)
		self.rpc_service = components.RPC(self.vin, self.__backend)
		self.rpc_extended_service = components.RPCExtended(self.vin, self.__backend)
