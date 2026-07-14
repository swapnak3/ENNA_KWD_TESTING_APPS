# -*- coding: utf-8 -*-
"""Created on 23.03.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains vehicle class for TA ODP Guestuser with VIN: "BAUCZPF8521081101"
"""
from . import vin_database
from .base import Vehicle
from .. import odp_requests


class Q7GuestUser(Vehicle):
    """Interface for vehicle BAUPCA4MZ21101901.
    Generates vehicle object with vehicle specific services.

    :ivar requests: Instance of odp requests.
    """
    def __init__(self):
        """Initialize object."""

        super().__init__()

        self.vin = vin_database.GUESTUSER_VIN
        self.nickname = vin_database.GUESTUSER_NICKNAME
        self.__backend = "ODP_APPROVAL"
        self.requests = odp_requests
