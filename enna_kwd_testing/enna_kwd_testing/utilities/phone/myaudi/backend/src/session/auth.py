# -*- coding: utf-8 -*-
"""Created on 02.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Authentication for backend requests.
"""

import logging
import threading

logger = logging.getLogger(__name__)


class __BackendAuthentication:
    """Stores values to access backend services."""

    instances = []

    def __init__(self, vin):
        """Initialize object.

        :param str vin: VIN authentication is for.
        """
        self._vin = vin
        self._expire_timestamp = None
        self.__token_valid = False
        self.__token_time = 0
        self.__token = None
        self.__token_timer = None

    def __save_auth_to_file(self):
        """Save authentication object to pickle file."""

        raise NotImplementedError("This is not implemented at the moment. -> To be done.")
        # os.makedirs(os.path.dirname("tmp\\auth.pkl"), exist_ok=True)
        # with open("tmp\\auth.pkl", 'a') as output:
        #     pickle.dump(self, output, -1)

    def __set_token_timer(self):
        """Set timer to signalize if backend access (token) is valid or expired.

        :return: Started Timer
        :rtype: threading.Timer
        """
        logger.info("Set token timer and set token valid.")
        thread = threading.Timer(self.__token_time, self.__set_token_invalid)
        thread.daemon = True
        thread.start()
        self.__token_valid = True
        return thread

    def __set_token_invalid(self):
        """Delete access object from instance list when token is expired."""

        logger.info("Set token invalid and delete authentication object.")
        self.__token_valid = False
        self.__class__.instances.remove(self)
        del self

    @property
    def vin(self):
        """Getter for vin property.

        :return: vin
        :rtype: str
        """
        return self._vin

    @vin.setter
    def vin(self, vin):
        """Setter for vin property.

        :raises ValueError: if the length of the VIN is not correct
        :param str vin: Value for vehicle VIN.
        """
        vin_length = 17
        if len(vin) != vin_length:
            raise ValueError(f"Length of VIN: {vin} is not correct. VIN must consist of {vin_length} letters")
        self._vin = vin

    @property
    def token_time(self):
        """Getter for property token expiring time.

        :return: Time when token expires in seconds.
        :rtype: int
        """
        return self.__token_time

    @token_time.setter
    def token_time(self, token_time):
        """Setter for token expiring time.

        :raises ValueError: if an invalid token time is given
        :param int token_time: Time when token expires in seconds.
        """
        if token_time < 0:
            raise ValueError("Not a valid token time. Token is already expired.")
        self.__token_time = token_time
        self.__token_timer = self.__set_token_timer()
        self.__class__.instances.append(self)

    @property
    def token(self):
        """Getter for property OAuth Token.

        :return: OAuth Token
        :rtype: str
        """
        return self.__token

    @token.setter
    def token(self, token):
        """Setter for OAuth Token.

        :param str token: OAuth token for objects VIN to access backend.
        """
        self.__token = token
        # self.__save_auth_to_file()

    @property
    def token_valid(self):
        """Getter for property token valid or not.

        :return: True or False
        :rtype: bool
        """
        return self.__token_valid


def auth_factory(vin):
    """Factory to return instances of Backend authentication.
    If an instance for a VIN is already existing and valid, return this instance.

    :param str vin: VIN to generate authentication object for.
    """
    logger.info(f"Get instance of BackendAuthentication for VIN: {vin}")
    for instance in __BackendAuthentication.instances:
        if instance.vin == vin:
            logger.debug(f"Instance already existing. Returning existing instance for VIN {vin}")
            return instance
    logger.debug(f"No instance existing. Generate new instance for VIN {vin}.")
    return __BackendAuthentication(vin)
