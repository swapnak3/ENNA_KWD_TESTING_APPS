# -*- coding: utf-8 -*-
"""Created on 07.03.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains vehicle baseclass.
"""

import abc


class Vehicle(abc.ABC):
    """Baseclass for specifying vehicles."""

    def __init__(self):
        """Initialize object."""

        self.__vin = None
        self.__nickname = None

    @property
    def vin(self):
        """Getter for property vin.

        :return: VIN of the vehicle as string
        :rtype: str
        """

        return self.__vin

    @vin.setter
    def vin(self, vin):
        """Setter for property vin.

        :param str vin: New VIN to set for the vehicle
        """

        self.__vin = vin

    @property
    def nickname(self):
        """Getter for property vin.

        :return: Nickname of the vehicle as string
        :rtype: str
        """

        return self.__nickname

    @nickname.setter
    def nickname(self, nickname):
        """Setter for property nickname.

        :param str nickname: New Nickname to set for the vehicle
        """

        self.__nickname = nickname
