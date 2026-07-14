# -*- coding: utf-8 -*-
"""Created on 11.09.2023.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
"""
from . import vin_database
from .base import Vehicle
from .. import odp_requests


class Q7(Vehicle):
    """Interface for vehicle BAUSHS4MZ21032501.
    Generates vehicle object with vehicle specific services.
    """
    def __init__(self):
        """Initialize object."""

        super().__init__()

        self.vin = vin_database.Q7_VIN
        self.nickname = vin_database.Q7_NICKNAME
        self.__backend = "ODP_APPROVAL"
        self.requests = odp_requests
