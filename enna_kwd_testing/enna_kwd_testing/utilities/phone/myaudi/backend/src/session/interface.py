# -*- coding: utf-8 -*-
"""Created on 04.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Module for specific backend interface.
"""

import abc
import json
import logging
import random
import time
import xml.parsers.expat

import xmltodict

from . import session

logger = logging.getLogger(__name__)


class Communication(abc.ABC):
    """Baseclass for communication object."""

    class FetchingJobListError(Exception):
        """Exception to raise when error at fetching jobs occurs."""

    def __init__(self, vin, service_type, backend, cooldown):
        """Initialize object, register service and cooldown time.

        :param str vin: VIN to get backend interface for.
        :param str service_type: Service type to register for VIN.
        :param str backend: Backend to use for backend interface.
        :param int cooldown: Cooldown time for service type.
        """
        session.SessionFactory().register(service_type, cooldown)
        self.transceiver = session.SessionFactory()(vin, service_type, backend, cooldown)

    @staticmethod
    @abc.abstractmethod
    def generate_random_checksum():
        """Abstract method to generate checksum. -> Required for installed base."""


class ODPInterface(Communication):
    """ODP APPROVAL backend interface."""

    ids = {}
    backend = "ODP_APPROVAL"

    def __init__(self, vin, service_type, cooldown):
        """Initialize object.

        :param str vin: VIN to get backend interface for.
        :param str service_type: Service type to register for VIN.
        :param int cooldown: Cooldown time for service type.
        """
        super().__init__(vin, service_type, self.__class__.backend, cooldown)
        self.__service_type = service_type
        self.__job_response_as_dict = None

    def __evaluate_job_list(self, response):
        """Evaluate joblist. Evaluate if job list contains job id.
        :param dict response: Job response as dict
        :rtype: bool
        :return: True if successful.
        :raises ODPInterface.FetchingJobListError: if joblist could not be fetched from backend.
        """
        logger.debug("Evaluate job list.")
        try:
            _ = response["jobList"]["job"]["@id"]
        except KeyError:
            logger.warning("Could not evaluate job list.")
            raise self.FetchingJobListError("Job list from backend was empty.")
        return True

    def __fetch_job_info(self):
        """Fetch jobs from odp approval backend."""

        logger.debug("Fetch job info.")
        service_url_part = "/mbb/jobs/v1/"
        payload = {}
        headers = {"Accept": "application/vnd.vwg.mbb.jobList_v1_1_2+xml"}
        logger.debug(f"Sending job list request for: {str(self.__class__.__name__)}")
        response = self.transceiver.send_host_request("GET", service_url_part, payload, headers)
        logger.debug(f"Response: {response}")
        data = json.dumps(xmltodict.parse(response.content))
        response_as_dict = json.loads(data)
        self.__job_response_as_dict = response_as_dict
        logger.info("Job list fetched. Job list evaluated.")
        return response_as_dict

    def __acknowledge_job_list(self):
        """Acknowledge job list to avoid fetch blocking.

        :rtype: requests.Response.
        :return: Request response.
        """
        service_url_part = "/mbb/jobs/v1/ack/"
        payload = {}
        headers = {"Content-Type": "application/vnd.vwg.jobListAcknowledge_v1_0_0+xml"}
        response = self.transceiver.send_host_request("PUT", service_url_part, payload, headers)
        logger.debug(f"Acknowledged backend job with response: {response.ok}")
        return response

    def get_valet_alert_deactivation_jobs(self, retries=3):
        """Get all job information.

        :param int retries: Max retries to perform to get job info.
        :rtype: list(list, dict).
        :return: Job info for every job id in job list.
        :raises ODPInterface.FetchingJobListError: if joblist could not be fetched.
        """
        job_dict = {}
        for retry_counter in range(0, retries):
            try:
                response = self.__fetch_job_info()
                if response:
                    jobs = self._get_valet_deactivation_job_id(response)
                    for key, value in jobs.items():
                        self.__class__.ids[key] = {"id": value}
                        self.__acknowledge_job_list()

                        job_dict[key] = self.__class__.ids[key]
                    return jobs, job_dict

            except (self.FetchingJobListError, xml.parsers.expat.ExpatError):
                self.__acknowledge_job_list()
                logger.critical(f"Jobs could not be fetched on {retry_counter + 1}. try.")
        raise self.FetchingJobListError(f"Could not fetch joblist after {retries} tries.")

    def _get_valet_deactivation_job_id(self, response):
        """Get job id for valet alert deactivation job.

        :param dict response: Job response as dict.
        :rtype: dict.
        :return: Fetched valet alert job ids.
        :raises ODPInterface.FetchingJobListError: if job ids could not be fetched."""
        valet_ids = {}
        try:
            for elem in response["jobList"]["job"]:
                if "ns1:deactivateGeoFencing" in elem.keys():
                    valet_ids["GEO"] = elem["@id"]
                else:
                    valet_ids["SPEED"] = elem["@id"]
            return valet_ids
        except (KeyError, TypeError):
            raise self.FetchingJobListError("Could not get job id.")

    def get_valet_alert_activation_jobs(self, retries=3):
        """Get all job information.

        :param int retries: Max retries to perform to get job info.
        :rtype: list(list, dict).
        :return: Job info for every job id in job list.
        :raises ODPInterface.FetchingJobListError: when joblist could not be fetched.
        """
        job_dict = {}
        for retry_counter in range(0, retries):
            try:
                response = self.__fetch_job_info()
                if response:
                    jobs = self._get_valet_activation_job_id(response)
                    for key, value in jobs.items():
                        self.__class__.ids[key] = {"id": value}

                        try:
                            if key == "SPEED":
                                self.__class__.ids[key]["job_uuid"] = self._get_valet_activation_speed_alert_uuid(response)
                        except self.FetchingJobListError:
                            logger.debug("No job uuid fetched.")
                        try:
                            if key == "GEO":
                                self.__class__.ids[key]["geo_uuid"] = self._get_valet_activation_geofence_alert_uuid(response)
                        except self.FetchingJobListError:
                            logger.debug("No geo uuid fetched.")
                        try:
                            if key == "GEO":
                                self.__class__.ids[key]["area_id"] = self._get_valet_activation_geofence_alert_area_id(response)
                        except self.FetchingJobListError:
                            logger.debug("No area id fetched.")

                        self.__acknowledge_job_list()

                        job_dict[key] = self.__class__.ids[key]
                    return jobs, job_dict

            except (self.FetchingJobListError, xml.parsers.expat.ExpatError):
                self.__acknowledge_job_list()
                logger.critical(f"Jobs could not be fetched on {retry_counter + 1}. try.")
        raise self.FetchingJobListError(f"Could not fetch joblist after {retries} tries.")

    def _get_valet_activation_job_id(self, response):
        """Get job id for valet alert activation job.

        :param dict response: Job response as dict.
        :rtype: dict.
        :return: Fetched valet alert job ids.
        :raises ODPInterface.FetchingJobListError: if joblist could not be fetched from backend.
        """
        valet_ids = {}
        try:
            for elem in response["jobList"]["job"]:
                if "ns2:activateGeoFencing" in elem.keys():
                    valet_ids["GEO"] = elem["@id"]
                else:
                    valet_ids["SPEED"] = elem["@id"]
            return valet_ids
        except (KeyError, TypeError):
            raise self.FetchingJobListError("Could not get job id.")

    def _get_valet_activation_speed_alert_uuid(self, response):
        """Get uuid id for valet alert speed alert job.

        :param dict response: Job response as dict.
        :rtype: str.
        :return: Fetched speed alert uuid id.
        :raises ODPInterface.FetchingJobListError: if joblist could not be fetched from backend.
        """
        try:
            for elem in response["jobList"]["job"]:
                if "ns3:activateSpeedAlert" in elem.keys():
                    return elem["ns3:activateSpeedAlert"]["ns3:activateSpeedAlertType"]["ns3:speedAlertDefinition"]["@ns3:uuid"]
        except (KeyError, TypeError):
            raise self.FetchingJobListError("Could not get job id.")

    def _get_valet_activation_geofence_alert_uuid(self, response):
        """Get uuid id for valet alert geo alert job.

        :param dict response: Job response as dict.
        :rtype: str.
        :return: Fetched geo alert uuid id.
        :raises ODPInterface.FetchingJobListError: if joblist could not be fetched from backend.
        """
        try:
            for elem in response["jobList"]["job"]:
                if "ns2:activateGeoFencing" in elem.keys():
                    return elem["ns2:activateGeoFencing"]["ns2:activateGeoFences"]["ns2:geoFencingDefinition"]["@ns2:uuid"]
        except (KeyError, TypeError):
            raise self.FetchingJobListError("Could not get job id.")

    def _get_valet_activation_geofence_alert_area_id(self, response):
        """Get area id for valet alert geo alert job.

        :param dict response: Job response as dict.
        :rtype: str.
        :return: Fetched geo alert area id.
        :raises ODPInterface.FetchingJobListError: if joblist could not be fetched from backend.
        """
        try:
            for elem in response["jobList"]["job"]:
                if "ns2:activateGeoFencing" in elem.keys():
                    return elem["ns2:activateGeoFencing"]["ns2:activateGeoFences"]["ns2:geoFencingDefinition"]["ns2:areaDefinition_ellipseArea"]["@ns2:area_id"]
        except (KeyError, TypeError):
            raise self.FetchingJobListError("Could not get job id.")

    def get_job(self, retries=3):
        """Get all job information.

        :param int retries: Max retries to perform to get job info.
        :rtype: list(list, dict).
        :return: Job info for every job id in job list.
        :raises ODPInterface.FetchingJobListError: if joblist could not be fetched from backend.
        """
        for retry_counter in range(0, retries):
            try:
                response = self.__fetch_job_info()
                if response:
                    job = self._get_job_id(response)
                    self.__class__.ids[job] = {}
                    try:
                        self.__class__.ids[job]["job_uuid"] = self._get_job_uuid(response)
                    except self.FetchingJobListError:
                        logger.debug("No job uuid fetched.")
                    try:
                        self.__class__.ids[job]["geo_uuid"] = self._get_geo_uuid(response)
                    except self.FetchingJobListError:
                        logger.debug("No geo uuid fetched.")
                    try:
                        self.__class__.ids[job]["area_id"] = self._get_geo_area_id(response)
                    except self.FetchingJobListError:
                        logger.debug("No area id fetched.")

                    self.__acknowledge_job_list()

                    return job, self.__class__.ids[job]

            except (self.FetchingJobListError, xml.parsers.expat.ExpatError):
                self.__acknowledge_job_list()
                logger.critical(f"Jobs could not be fetched on {retry_counter + 1}. try.")
                time.sleep(1)
        raise self.FetchingJobListError(f"Could not fetch joblist after {retries} tries.")

    def _get_job_id(self, response):
        """Get job id.

        :param dict response: Job response as dict.
        :rtype: str.
        :return: Job id.
        :raises ODPInterface.FetchingJobListError: if joblist could not be fetched from backend.
        """
        try:
            return response["jobList"]["job"]["@id"]
        except (KeyError, TypeError):
            raise self.FetchingJobListError("Could not get job id.")

    def _get_job_uuid(self, response):
        """Extract speed alert job uuid from response.

        :param dict response: Job response as dict.
        :rtype: str.
        :return: Job uuid.
        :raises ODPInterface.FetchingJobListError: if joblist could not be fetched from backend.
        """
        try:
            if isinstance(response["jobList"]["job"]["ns3:activateSpeedAlert"]["ns3:activateSpeedAlertType"]["ns3:speedAlertDefinition"], list):
                return response["jobList"]["job"]["ns3:activateSpeedAlert"]["ns3:activateSpeedAlertType"]["ns3:speedAlertDefinition"][0]["@ns3:uuid"]
            return response["jobList"]["job"]["ns3:activateSpeedAlert"]["ns3:activateSpeedAlertType"]["ns3:speedAlertDefinition"]["@ns3:uuid"]
        except (KeyError, TypeError):
            raise self.FetchingJobListError("Could not get job uuid.")

    def _get_geo_uuid(self, response):
        """Extract geofence alert geo uuid from response.

        :param dict response: Job response as dict.
        :rtype: str.
        :return: Job id.
        :raises ODPInterface.FetchingJobListError: if joblist could not be fetched from backend.
        """
        try:
            if isinstance(response["jobList"]["job"]["ns2:activateGeoFencing"]["ns2:activateGeoFences"]["ns2:geoFencingDefinition"], list):
                return response["jobList"]["job"]["ns2:activateGeoFencing"]["ns2:activateGeoFences"]["ns2:geoFencingDefinition"][0]["@ns2:uuid"]
            return response["jobList"]["job"]["ns2:activateGeoFencing"]["ns2:activateGeoFences"]["ns2:geoFencingDefinition"]["@ns2:uuid"]
        except (KeyError, TypeError):
            raise self.FetchingJobListError("Could not get geo uuid.")

    @staticmethod
    def __parse_area_ids(response):
        """Parse area ids.

        :param dict response: Job response as dict.
        :rtype: str.
        :return: Area id.
        """
        area_id = None

        for index, geofence in enumerate(response["jobList"]["job"]["ns2:activateGeoFencing"]["ns2:activateGeoFences"]["ns2:geoFencingDefinition"]):
            area_id = geofence["ns2:areaDefinition_ellipseArea"]["@ns2:area_id"]

        return area_id

    def _get_geo_area_id(self, response):
        """Extract geofence alert area id from response.

        :param dict response: Job response as dict.
        :rtype: str.
        :return: Area id.
        :raises ODPInterface.FetchingJobListError: if joblist could not be fetched from backend.
        """
        try:
            if isinstance(response["jobList"]["job"]["ns2:activateGeoFencing"]["ns2:activateGeoFences"]["ns2:geoFencingDefinition"]["ns2:areaDefinition_ellipseArea"], list):
                return response["jobList"]["job"]["ns2:activateGeoFencing"]["ns2:activateGeoFences"]["ns2:geoFencingDefinition"]["ns2:areaDefinition_ellipseArea"][0]["@ns2:area_id"]
            return response["jobList"]["job"]["ns2:activateGeoFencing"]["ns2:activateGeoFences"]["ns2:geoFencingDefinition"]["ns2:areaDefinition_ellipseArea"]["@ns2:area_id"]
        except (KeyError, TypeError):
            try:
                return self.__parse_area_ids(response)
            except (TypeError, AttributeError, KeyError):
                raise self.FetchingJobListError("Could not get geo area id.")

    @staticmethod
    def generate_random_checksum():
        """Generate random checksum between two values. Required to upload an installed base for a VIN.

        :rtype: int
        :return: checksum: Checksum to append to installed base request.
        """
        lower_limit = 10000000000000
        upper_limit = 100000000000000
        return random.randint(lower_limit, upper_limit)


def interface_factory(vin, service_type, backend, cooldown):
    """Factory to return communication object.

    :param str vin: VIN to get backend interface for.
    :param str service_type: Service type to register for VIN.
    :param str backend: Backend to get specific interface for.
    :param int cooldown: Cooldown time for service type.
    :rtype: interface.ODPInterface
    :return: Instance of ODPInterface
    """

    if backend == "ODP_APPROVAL":
        return ODPInterface(vin, service_type, cooldown)
