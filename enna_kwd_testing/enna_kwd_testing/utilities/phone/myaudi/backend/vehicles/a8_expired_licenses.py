# -*- coding: utf-8 -*-
"""Created on 23.03.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
"""
from . import vin_database
from .base import Vehicle
from .. import odp_requests


class A8ExpiredLicenses(Vehicle):
    """Interface for vehicle BAUCZPGEZ21070902.
    Generates vehicle object with vehicle specific services.

    :ivar requests: Instance of odp requests.
    """
    def __init__(self):
        """Initialize object."""

        super().__init__()

        self.vin = vin_database.A8_LICENSES_VIN
        self.nickname = vin_database.A8_LICENSES_NICKNAME
        self.__backend = "ODP_APPROVAL"
        self.requests = odp_requests
