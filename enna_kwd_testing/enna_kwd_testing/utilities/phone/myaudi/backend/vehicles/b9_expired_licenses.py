# -*- coding: utf-8 -*-
"""Created on 25.05.2023.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
"""
from . import vin_database
from .base import Vehicle
from .. import odp_requests


class B9ExpiredLicenses(Vehicle):
	"""Interface for vehicle BAUPSWF4823041102.
	Generates vehicle object with vehicle specific services.

	:ivar requests: Instance of odp requests.
	"""
	def __init__(self):
		"""Initialize object."""

		super().__init__()

		self.vin = vin_database.B9_EXPIRED_LICENSES_VIN
		self.nickname = vin_database.B9_EXPIRED_LICENSES_NICKNAME
		self.__backend = "ODP_APPROVAL"
		self.requests = odp_requests
