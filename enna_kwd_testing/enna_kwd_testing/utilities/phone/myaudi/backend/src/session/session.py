# -*- coding: utf-8 -*-
"""Created on 03.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Module for backend interface.
"""

import abc
import datetime
import json
import logging
import threading
import time

import requests
import urllib3

from . import auth
from . import gen_vin_certs

logger = logging.getLogger(__name__)


class BackendSession(abc.ABC):
    """Superclass for specific request and timing/blocking functionality."""

    class FetchingJobIdError(Exception): # TODO: Entfernen oder einbauen
        """Error to signalize, the job id could not be fetched from backend job list."""

    class InvalidResponseError(Exception):
        """Error to signalize, there was an invalid response from the backend for a request."""

    class InvalidPayloadError(Exception):
        """Error to signalize, the user sent an invalid payload (e.g. wrong payload type or typo in any value)."""

    cooldown_instances = {}
    service_times = {}

    def __init__(self, vin, service_type, proxies=None):
        """Initialize object.

        :param str vin: VIN for backend session.
        :param str service_type: Type of service for backend session (e.g. VSR, DWA, etc.).
        :param dict proxies: Proxies to user for backend requests (http, https).
        """

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self._auth = None
        self._vin = vin
        self._service_type = service_type
        self.__proxies = proxies
        self.__cooldown = self.__class__.service_times[service_type]

    # TODO: Outsource
    class CooldownTimer(threading.Timer):
        """Timer class implementing remaining and elapsed time."""

        def __init__(self, cooldown, callback):
            """Initialize timer object.

            :param int cooldown: Time for service cooldown.
            :param function callback: Callback function at timer finish.
            """

            super().__init__(cooldown, callback)
            self.__cooldown = cooldown
            self._start_time = datetime.datetime.now()
            self._remaining_time = None
            self._elapsed_time = None

        def get_remaining_time(self):
            """Getter returning remaining timer time.

            :rtype: int
            :return: Remaining timer time.
            """

            return self.__cooldown - (datetime.datetime.now() - self._start_time).seconds

        @property
        def remaining_time(self):
            """Getter for property remaining time.

            :rtype: int.
            :return: Remaining timer time.
            """

            self._remaining_time = self.__cooldown - (datetime.datetime.now() - self._start_time).seconds
            return self._remaining_time

        @property
        def elapsed_time(self):
            """Getter for property timer elapsed time.

            :rtype: int.
            :return: Elapsed timer time.
            """

            self._elapsed_time = (datetime.datetime.now() - self._start_time).seconds
            return self._elapsed_time

    def _start_cooldown(self):
        """Start cooldown for backend service.
        Append backend service to instance list of currently cooling down services for the specific vin.

        :rtype: bool
        :return: True
        """

        if self.__cooldown <= 0:
            return True

        timer = BackendSession.CooldownTimer(self.__cooldown, self.__finish_cooldown)
        timer.daemon = True
        timer.start()

        if self._vin not in self.__class__.cooldown_instances.keys():
            self.__class__.cooldown_instances[self._vin] = dict({self._service_type: timer})
        else:
            self.__class__.cooldown_instances[self._vin].update({self._service_type: timer})

        return True

    def __finish_cooldown(self):
        """Delete service from list of cooldown instances for specific vin.

        :rtype: bool
        :return: True
        """
        vins_cooldown_instances = self.__class__.cooldown_instances.get(self._vin)
        del vins_cooldown_instances[self._service_type]
        return True

    def __send_request(self, request_type, host, service_url_part, payload=None, header=None, cert=None):
        """Send a backend request to given url.

        :param str request_type: HTTP method (GET, PUT, POST, PATCH, etc.).
        :param str host: Host url.
        :param str service_url_part: Backend service url.
        :param str payload: Payload to send to backend.
        :param dict header: Request header.
        :param str cert: Path to certificates files (vin.crt, vin.key)
        :return: response, response.ok, response.status_code
        :rtype: requests.Response, bool, int
        :raises session.BackendSession.InvalidPayloadError: if payload could not be loaded.
        """
        logger.debug(f"Sending {request_type} request for VIN {self._vin} with service type: {self._service_type}")
        if payload is None:
            logger.error("No payload defined - Load payload before sending any request by <CLASS>.prepare_payload()")
            raise self.InvalidPayloadError("Payload for service is not loaded")
        if self._auth.token_valid:
            header["Authorization"] = f"Bearer {self._auth.token}"
        url = host + service_url_part
        request_args = (request_type, url)
        request_kwargs = {"headers": header, "data": payload, "verify": False}
        if self.__proxies:
            request_kwargs["proxies"] = self.__proxies
        if cert is not None:
            request_kwargs["cert"] = cert

        response = requests.request(*request_args, **request_kwargs)
        logger.debug(response.text)
        logger.debug(response.content)
        logger.info(f"Proceeded request with response status code {response.status_code}")

        return response, response.ok, response.status_code

    def _send_request(self, request_type, host, service_url_part, payload=None, header=None, cert=None, max_retries=3):
        """Wrapper for error handling of backend requests with retry mechanism.

        :param str request_type: HTTP method (GET, PUT, POST, PATCH, etc.).
        :param str host: Host url.
        :param str service_url_part: Backend service url.
        :param str payload: Payload to send to backend.
        :param dict header: Request header.
        :param str cert: Path to certificates files (vin.crt, vin.key)
        :param int max_retries: Maximum amount of retries in error case.
        :return: response
        :rtype: requests.Response
        :raises session.BackendSession.InvalidResponseError: if request was not successful after error handling.
        """
        for try_counter in range(0, max_retries):
            response, success, status_code = self.__send_request(request_type, host, service_url_part, payload, header, cert)
            if success:
                return response

            try:
                self.__handle_request_error(status_code, response)
            except self.InvalidResponseError:
                logger.warning("Response status code could not be handled")

        logger.error(f"Could not successfully send request after {max_retries} retries.")
        raise self.InvalidResponseError(f"Could not successfully send request after {max_retries} retries.")

    def __handle_request_error(self, status_code, response):
        """Handle request errors which´s response is not HTTP 200 or HTTP 204.
        If a solution for a specific status code is known, the function can be extended.

        :param int status_code: HTTP status code of the backend response
        :param requests.Response response: Response of the Request
        :rtype: bool
        :return: True
        :raises InvalidResponseError: if the returned status code is unknown
        """
        if status_code == 401:
            return True
        elif status_code == 503:
            wait_time_for_unreachable_server = 60
            logger.warning(f"Server is not reachable. Wait if server is reachable after {wait_time_for_unreachable_server} seconds ...")
            time.sleep(60)
            return True
        else:
            logger.critical(f"Returned status code is not handled - Status code: {status_code} - Status Message: {response.content}")
            raise self.InvalidResponseError(f"Returned status code is not handled - Status code: {status_code}")


# TODO: Outsource into superclass

class BackendInterface(BackendSession):
    """Class to authenticate for specific backend."""

    class ServiceNotRegisteredException(Exception):
        """Exception to raise when service is not registered to class."""

    def __init__(self, vin, service_type, proxies, brand="", grant_type="", scope="", host="", cookie="", token_host="", ib_host=""):
        """Initialize object.

        :param str vin: VIN for backend session.
        :param str service_type: Service type to instantiate backend session for.
        :param dict proxies: Proxies to use for backend requests (http, https).
        :param str brand: Vehicle brand. (AU, etc.)
        :param str grant_type: Grant type.
        :param str scope: Scope.
        :param str host: Backend host url.
        :param str cookie: Cookie for authentication.
        :param str token_host: Authentication host url.
        :param str ib_host: Installed base host url.
        """
        super().__init__(vin, service_type, proxies)
        self.__brand = brand
        self.__grant_type = grant_type
        self.__scope = scope
        self.__host = host
        self.__token_host = token_host
        self.__ib_host = ib_host
        self.__cookie = cookie
        self.__service_type = service_type
        self.__vin = vin
        self._authenticate()

    def send_ib_host_request(self, request_type, service_url_part, payload=None, header=None, cert=None, max_retries=3):
        """Send host request to installed base host url.

        :param str request_type: HTTP method (GET, PUT, POST, PATCH, etc.).
        :param str service_url_part: Backend service url.
        :param str payload: Payload to send to backend.
        :param dict header: Request header.
        :param str cert: Path to certificates files (vin.crt, vin.key)
        :param int max_retries: Maximum amount of retries in error case.
        :return: response
        :rtype: requests.Response
        """
        return self._send_request(request_type, self.__ib_host, service_url_part, payload, header, cert, max_retries)

    def send_auth_host_request(self, request_type, service_url_part, payload=None, header=None, cert=None, max_retries=3):
        """Send host request to token host url.

        :param str request_type: HTTP method (GET, PUT, POST, PATCH, etc.).
        :param str service_url_part: Backend service url.
        :param str payload: Payload to send to backend.
        :param dict header: Request header.
        :param str cert: Path to certificates files (vin.crt, vin.key)
        :param int max_retries: Maximum amount of retries in error case.
        :return: response
        :rtype: requests.Response
        """
        return self._send_request(request_type, self.__token_host, service_url_part, payload, header, cert, max_retries)

    def send_host_request(self, request_type, service_url_part, payload=None, header=None, cert=None, max_retries=3):
        """Send host request to service url.

        :param str request_type: HTTP method (GET, PUT, POST, PATCH, etc.).
        :param str service_url_part: Backend service url.
        :param str payload: Payload to send to backend.
        :param dict header: Request header.
        :param str cert: Path to certificates files (vin.crt, vin.key)
        :param int max_retries: Maximum amount of retries in error case.
        :return: response
        :rtype: requests.Response
        """
        if self.__vin in self.cooldown_instances:

            while self._service_type in self.cooldown_instances[self.__vin]:
                timer = self.cooldown_instances[self.__vin][self.__service_type]
                logger.info(f"Waiting for cooldown: {timer.elapsed_time} seconds. Remaining time: {timer.remaining_time}")
                time.sleep(5)

        if not self._auth.token_valid:
            self._authenticate()

        response = self._send_request(request_type, self.__host, service_url_part, payload, header, cert, max_retries)

        self._start_cooldown()
        return response

    def __authenticate(self):
        """Get authentication token for backend.
        Save authentication to authentication object.
        """
        logger.info(f"Authenticate for VIN: {self._vin}.")
        cert_path = gen_vin_certs.change_vin(self._vin)
        service_url_part = f"/mbbcoauth/cai/oauth2/v1/requestToken/token?brand={self.__brand}&grant_type={self.__grant_type}&scope={self.__scope}"
        payload = {}
        headers = {"Cookie": self.__cookie}
        certs = (f"{cert_path}vin.crt", f"{cert_path}vin.key")

        response = self.send_auth_host_request("GET", service_url_part, payload, header=headers, cert=certs)

        mbbcoauth_token = json.loads(response.text)["access_token"]
        expiring_time = json.loads(response.text)["expires_in"]
        logger.debug("Got authentication token")
        # self._auth.set_authentication(expiring_time, mbbcoauth_token)
        self._auth.token = mbbcoauth_token
        self._auth.token_time = expiring_time
        logger.debug("Save authentication to auth obj.")

    def _authenticate(self):
        """Wrapper for backend authentication.
        Evaluates if a new token is required or an already existing can be used.

        :return: True
        :rtype: bool
        """
        self._auth = auth.auth_factory(self._vin)
        if not self._auth.token_valid:
            self.__authenticate()
        return True


# TODO: Outsourcing maybe good

class SessionFactory:
    """Factory class for backend interface."""

    class BackendNotDefinedError(Exception):
        """Exception to raise when backend is not defined."""

    def __init__(self):
        """Initialize object."""

    @classmethod
    def __call__(cls, vin, service_type, backend, cooldown=None):
        """Register service for given backend.
        Return backend interface object for backend.

        :param str vin: VIN to get backend interface for.
        :param str service_type: Service type to register for VIN.
        :param str backend: Backend to use for backend interface.
        :param int cooldown: Cooldown time for service type.
        :raises BackendNotDefinedError: if no interface is available for the given backend type
        :rtype: BackendInterface.
        :return: BackendInterface object.
        """
        if backend == "ODP_APPROVAL":
            SessionFactory.register(service_type, cooldown)
            return cls.odp_request(vin, service_type)
        else:
            logger.exception("No interface for this backend type available.")
            raise cls.BackendNotDefinedError("No interface for this backend type available.")

    @classmethod
    def odp_request(cls, vin, service_type):
        """Return backend interface object.
        :param str vin: VIN to get backend interface for.
        :param str service_type: Service type to register for VIN.
        :rtype: BackendInterface.
        :return: BackendInterface object.
        """
        http_proxy = "http://proxy.in.audi.vwg:8080"
        https_proxy = "http://proxy.in.audi.vwg:8080"
        proxies = {"http": http_proxy, "https": https_proxy}
        brand = "Audi"
        grant_type = "client_credentials"
        scope = "t1_a:teltech"
        host = "https://mod3caimbbrun-3a.app.eu.dp.vwg-connect.com"
        # host = "https://caiazsrundev-3a.app.eu.dp.vwg-connect.com"
        # token_host = "https://caiazsrun-3a.app.eu.dp.vwg-connect.com"
        token_host = "https://caiazsrundev-3a.app.eu.dp.vwg-connect.com"
        ib_host = "https://mod3digestmbbrun-3a.app.eu.dp.vwg-connect.com"
        cookie = "OAUTH_COOKIE=78aa6890-136c-463d-8b7e-6cadf64180e1"

        return BackendInterface(vin, service_type, proxies, brand, grant_type, scope, host, cookie, token_host, ib_host)

    @staticmethod
    def register(service_type: str, cooldown: int):
        """Register service type to service instances of VIN.

        :param str service_type: Service type to register for VIN.
        :param int cooldown: Cooldown time for service type.
        """
        BackendInterface.service_times[service_type] = cooldown
