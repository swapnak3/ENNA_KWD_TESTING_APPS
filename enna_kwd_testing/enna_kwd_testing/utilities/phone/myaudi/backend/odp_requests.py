# -*- coding: utf-8 -*-
"""Created on 04.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains odp request services for myaudi app.
"""

import logging

from .src.payloads.factory import payload_factory
from .src.payloads.interface import ServiceType
from .src.session.interface import interface_factory
from ...extended_enum import ExtendedEnum

logger = logging.getLogger(__name__)


class InstalledBaseCgwClu33:
    """Update installed base to reset vehicle and disable play protection."""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.INSTALL_BASE_UPDATE_CGW_CLU_33
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=30)

    def install_base(self):
        """Upload installed base type cgw clu 33.

        :rtype:list
        :return: Request response
        """
        service_url_part = f"/mbb/services/v1/uploadIB/{self.session.generate_random_checksum()}"
        headers = {"Accept": "application/vnd.vwg.mbb.servicelist_v2_0_1+xml", "Accept-Language": "en-US", "Content-Type": "text/xml"}
        payload = payload_factory(self.service_type.value)
        return self.session.transceiver.send_ib_host_request("PUT", service_url_part, payload, headers)


class InstalledBaseCgwClu31:
    """Update installed base to reset vehicle and disable play protection."""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.INSTALL_BASE_UPDATE_CGW_CLU_31
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=30)

    def install_base(self):
        """Upload installed base type cgw clu 31.

        :rtype:list
        :return: Request response
        """
        service_url_part = f"/mbb/services/v1/uploadIB/{self.session.generate_random_checksum()}"
        headers = {"Accept": "application/vnd.vwg.mbb.servicelist_v2_0_1+xml", "Accept-Language": "en-US", "Content-Type": "text/xml"}
        payload = payload_factory(self.service_type.value)
        return self.session.transceiver.send_ib_host_request("PUT", service_url_part, payload, headers)


class InstalledBaseCgwMbbDefault:
    """Update installed base to reset vehicle and disable play protection."""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.INSTALL_BASE_UPDATE_CGW_MBB_DEFAULT
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=30)

    def install_base(self):
        """Upload installed base type cgw mbb default.

        :rtype:list
        :return: Request response
        """
        service_url_part = f"/mbb/services/v1/uploadIB/{self.session.generate_random_checksum()}"
        headers = {"Accept": "application/vnd.vwg.mbb.servicelist_v2_0_1+xml", "Accept-Language": "en-US", "Content-Type": "text/xml"}
        payload = payload_factory(self.service_type.value)
        return self.session.transceiver.send_ib_host_request("PUT", service_url_part, payload, headers)


class ServiceVSR:
    """Manipulate vehicle status services."""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.VSR
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def set_status(self, **kwargs):
        """Set vehicle status.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        service_url_path = "/mbb/tss/v1/vehicleStatus/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.rvsRdk_v1_0_1+xml"}
        return self.session.transceiver.send_host_request("PUT", service_url_path, payload, headers)

    def response_to_active_job(self, **kwargs):
        """Response to vehicle status job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_path = "/mbb/tss/v1/vehicleStatus/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.rvsRdk_v1_0_1+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("PUT", service_url_path, payload, headers)


class ServiceCarFinderValidPosition:
    """Manipulate vehicle gps location."""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.CARFINDER_VALID
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def set_position(self, **kwargs):
        """Set valid vehicle location.

        :param kwargs: dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        service_url_path = "/mbb/tss/v1/vehicleStatus/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.rvsRdk_v1_0_1+xml"}
        return self.session.transceiver.send_host_request("PUT", service_url_path, payload, headers)


class ServiceCarFinderInValidPosition:
    """Manipulate vehicle location to set an unknown location."""

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.CARFINDER_INVALID
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def set_invalid_position(self):
        """Set invalid vehicle location.

        :rtype: list
        :return: Request response
        """
        service_url_path = "/mbb/tss/v1/vehicleStatus/"
        payload = payload_factory(self.service_type.value)
        headers = {"Content-Type": "application/vnd.vwg.mbb.rvsRdk_v1_0_1+xml"}
        return self.session.transceiver.send_host_request("PUT", service_url_path, payload, headers)


class ServiceRAHQuickstart:
    """Manipulate state of remote auxiliary heating (RAH)."""

    class RAHErrorCodes(str, ExtendedEnum):
        """Enum containing possible Error-Codes for RAH Quickstart service."""

        VEH_TECHNICAL_ERROR = "1"
        RAH_ERROR = "9"
        FUEL_LEVEL_INSUFFICIENT = "13"
        IGNITION_ON = "5"

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.RAH_QUICKSTART
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def set_status(self, **kwargs):
        """Public method to set the status of the RAH for a testcase.
        Should only be used for Precondition purposes and not for testcase-action.
        Actions of testcases have to be triggered and responded as job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        service_url_part = "/mbb/rs/v1/status/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.climatisationStateReportRequest_v1_0_3+xml"}
        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)

    def response_to_active_job(self, **kwargs):
        """Response to active remote auxiliary heating (RAH) job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = "/mbb/rs/v1/status/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.climatisationStateReportRequest_v1_0_3+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)

    def response_to_active_job_with_error(self, error: RAHErrorCodes):
        """Response to active remote auxiliary heating (RAH) job with an Error-Code.
        :param backend.odp_requests.ServiceRAHQuickstart.RAHErrorCodes error: Error-Code to send to backend.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = f"/mbb/rs/v1/status/clima/error/{error.value}"
        payload = {}
        headers = {"Content-Type": "application/vnd.vwg.mbb.climatisationStateReportRequest_v1_0_3+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)


class ServiceRAHTimer:
    """Manipulate timers for remote auxiliary heating (RAH) service."""

    class RAHErrorCodes(str, ExtendedEnum):
        """Enum containing possible RAHErrorCodes."""

        VEH_TECHNICAL_ERROR = "1"
        RAH_ERROR = "9"
        FUEL_LEVEL_INSUFFICIENT = "13"
        IGNITION_ON = "5"

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.RAH_TIMER
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def set_status(self, **kwargs):
        """Public method to set the status of the RAH-Timer for a testcase.
        Should only be used for Precondition purposes and not for testcase-action.
        Actions of testcases have to be triggered and responded as job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        service_url_part = "/mbb/rs/v1/status/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.DepartureTimersAndProfilesReportRequest_v1_0_0+xml"}
        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)

    def response_to_active_job(self, **kwargs):
        """Response to remote auxiliary heating (RAH) job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = "/mbb/rs/v1/status/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.DepartureTimersAndProfilesReportRequest_v1_0_0+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)


class ServiceRAHTimerB9PA:
    """Manipulate B9PA timers for remote auxiliary heating (RAH) service."""

    class RAHB9PAErrorCodes(str, ExtendedEnum):
        """Enum containing possible B9PA RAHErrorCodes."""

        FUEL_LEVEL_INSUFFICIENT = "13"
        IGNITION_ON = "5"

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.RAH_TIMER_B9PA
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def set_status(self, **kwargs):
        """Public method to set the status of the RAH-Timer (B9PA) for a testcase.
        Should only be used for Precondition purposes and not for testcase-action.
        Actions of testcases have to be triggered and responded as job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        service_url_part = "/mbb/rs/v1/status/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.DepartureTimersAndProfilesReportRequest_v1_0_4+xml"}

        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)

    def response_to_active_job(self, **kwargs):
        """Response to B9PA remote auxiliary heating (RAH) job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = "/mbb/rs/v1/status/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.DepartureTimersAndProfilesReportRequest_v1_0_4+xml", "X-RelatedJobId": job_id}

        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)

    def response_to_active_job_with_error(self, error: RAHB9PAErrorCodes):
        """Response to an active B9PA RAH Timer job with an Error-Code.

        :param backend.odp_requests.ServiceRAHTimerB9PA.RAHB9PAErrorCodes error: Error-Code to send to backend.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        payload = payload_factory(self.service_type.value)
        service_url_part = f"/mbb/rs/v1/status/clima/error/{error.value}"
        headers = {"Content-Type": "application/vnd.vwg.mbb.climatisationStateReportRequest_v1_0_3+xml", "X-RelatedJobId": job_id}

        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)


class ServiceRHF:
    """Access remote honk and flash (RHF) service."""

    class RHFErrorCodes(str, ExtendedEnum):
        """Enum containing possible Error-Codes for remote honk and flash (RHF) service."""

        TECHNICAL_ERROR = "14"
        TTL_EXPIRED = "98"
        NO_RESPONSE = "94"
        LOCK_STATUS_CHANGED = "11"
        HIGHER_PRIO_FUNCT_ACTIVE = "10"
        HORN_ACTIVATED = "9"
        CONV_TOP_NOT_LOCKED = "8"
        TRUNK_OPEN = "7"
        ENGINE_HOOD_OPEN = "6"
        CLAMP15_ON = "4"
        CLAMPS_ON = "3"
        DOOR_OPEN = "5"

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.RHF
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def response_to_active_job(self, **kwargs):
        """Response to remote honk and flash (RHF) job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = "/mbb/rhf/v1/status/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.honkAndFlash_v1_0_0+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def response_to_active_job_with_error(self, error: RHFErrorCodes):
        """Response to an active remote honk and flash (RHF) job with an Error-Code.

        :param backend.odp_requests.ServiceRHF.RHFErrorCodes error: Error-Code to send to backend.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        payload = payload_factory(self.service_type.value)
        service_url_part = f"/mbb/rhf/v1/error/?num={error.value}"
        headers = {"Content-Type": "application/vnd.vwg.mbb.honkAndFlash_v1_0_0+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)


class ServiceDWA:
    """Trigger diebstahl warn anlage (dwa) alarms."""

    class DwaAlarmReasons(str, ExtendedEnum):
        """Enum containing possible alarm reasons."""

        NO_REASON = "00_NoAlarmReason"
        EXTERIOR = "01_DriversDoorOpen"
        INTERIOR = "08_CabinIRUEArmedAlarm"
        MOVEMENT = "11_TiltSensorArmedAlarm"
        TRAILER = "19_TrailerDisconnected"

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.cooldown = 180
        self.service_type = ServiceType.DWA
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=self.cooldown)

    def trigger_alarm(self, alarm_type: DwaAlarmReasons):
        """Trigger a Diebstahl warn anlage (dwa) alarm.

        :param backend.odp_requests.ServiceDWA.DwaAlarmReasons alarm_type: Alarm reason to trigger dwa alarm for.
        :rtype: list
        :return: Request response
        """
        kwargs = {"alarm_reason": f"{alarm_type.value}"}
        service_url_part = "/mbb/dwap/v1/notification/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.dwaPushNotification_v1_0_0+xml"}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)


class ServiceRBCPHEV:
    """Manipulate charging state with remote battery charging (RBC) service for PHEV vehicle."""

    class RBCErrorCodes(str, ExtendedEnum):
        """Enum containing possible Error-Codes for remote battery charging (RBC) job responses."""

        UNKNOWN_ERROR = "1"
        TIMEOUT = "2"
        REJECTED = "3"
        SYNC_CONFLICT = "4"
        IGNITION_ON = "5"
        AUTO_PLUG_LOCK_FAIL = "6"
        NO_EXT_PWR_SUPPLY = "7"
        DEVICE_ERROR = "8"
        WRONG_GEAR = "9"
        CONSERVATION_CHARGE_RUNNING = "10"
        PLUG_NOT_CONNECTED = "11"
        BATTERY_TEMP_LOW = "12"
        BATTERY_TEMP_LOW_AWC = "13"
        GENERAL_CONTROL_DEVICE_AWC = "14"
        INTERNAL_ERROR_AWC = "15"
        EXTERNAL_ERROR_AWC = "16"
        METAL_OBJECT_DETECTED = "17"
        NO_EXT_PWR_SUPPLY_AWC = "18"
        WRONG_GEAR_AWC = "19"
        BOTH_FLAPS_OPEN_PLUG_CONNECTED = "25"

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.RBC_QUICKSTART_PHEV
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def set_status(self, **kwargs):
        """Public method to set the status of the RBC-PHEV for a testcase.
        Should only be used for Precondition purposes and not for testcase-action.
        Actions of testcases have to be triggered and responded as job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        service_url_part = "/mbb/rbc/v1/chargingStateReport/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.chargingStateReportRequest_v1_0_0+xml"}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def response_to_active_job(self, **kwargs):
        """Response to active remote battery charging (RBC) job for PHEV vehicle.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = "/mbb/rbc/v1/chargingStateReport/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.chargingStateReportRequest_v1_0_0+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def response_to_active_job_with_error(self, error: RBCErrorCodes):
        """Response to active remote battery charging (RBC) job for PHEV vehicle with an Error-Code.

        :param backend.odp_requests.ServiceRBCPHEV.RBCErrorCodes error: Error-Code to send as job response.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = f"/mbb/rbc/v1/error/?num={error.value}"
        payload = {}
        headers = {"Content-Type": "application/vnd.vwg.mbb.chargingStateReportRequest_v1_0_0+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)


class ServiceRBCCBEV:
    """Manipulate charging state with remote battery charging (RBC) service for CBEV vehicle."""

    class RBCErrorCodes(str, ExtendedEnum):
        """Enum containing possible Error-Codes for remote battery charging (RBC) job responses."""

        UNKNOWN_ERROR = "1"
        TIMEOUT = "2"
        REJECTED = "3"
        SYNC_CONFLICT = "4"
        IGNITION_ON = "5"
        AUTO_PLUG_LOCK_FAIL = "6"
        NO_EXT_PWR_SUPPLY = "7"
        DEVICE_ERROR = "8"
        WRONG_GEAR = "9"
        CONSERVATION_CHARGE_RUNNING = "10"
        PLUG_NOT_CONNECTED = "11"
        BATTERY_TEMP_LOW = "12"
        BATTERY_TEMP_LOW_AWC = "13"
        GENERAL_CONTROL_DEVICE_AWC = "14"
        INTERNAL_ERROR_AWC = "15"
        EXTERNAL_ERROR_AWC = "16"
        METAL_OBJECT_DETECTED = "17"
        NO_EXT_PWR_SUPPLY_AWC = "18"
        WRONG_GEAR_AWC = "19"
        BOTH_FLAPS_OPEN_PLUG_CONNECTED = "25"

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.RBC_QUICKSTART_CBEV
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def set_status(self, **kwargs):
        """Public method to set the status of the RBC-CBEV for a testcase.
        Should only be used for Precondition purposes and not for testcase-action.
        Actions of testcases have to be triggered and responded as job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        service_url_part = "/mbb/rbc/v1/chargingStateReport/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.chargingStateReportRequest_v1_0_5+xml"}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def response_to_active_job(self, **kwargs):
        """Response to active remote battery charging (RBC) job for CBEV vehicle.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = "/mbb/rbc/v1/chargingStateReport/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.chargingStateReportRequest_v1_0_5+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def response_to_active_job_with_error(self, error: RBCErrorCodes):
        """Response to active remote battery charging (RBC) job for CBEV vehicle with an Error-Code.
        :param backend.odp_requests.ServiceRBCCBEV.RBCErrorCodes error: Error-Code to send as job response.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = f"/mbb/rbc/v1/error/?num={error.value}"
        payload = {}
        headers = {"Content-Type": "application/vnd.vwg.mbb.chargingStateReportRequest_v1_0_5+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)


class ServiceSpeedAlert:
    """Access speed alert service."""

    class AlertState(str, ExtendedEnum):
        """Enum containing possible alert states for speed alert violations."""

        START = "Start"
        END = "End"

    def __init__(self, vin, backend):
        """Initialize object.

         :param str vin: VIN to access by backend session.
         :param str backend: Backend where VIN is located.
         """
        self.service_type = ServiceType.SPEED_ALERT
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)
        self.active_alert_job_id = None
        self.active_alert_job_uuid = None

    def response_to_profile_activation_job(self):
        """Response to a profile activation job for speed alert service.

        :rtype: list
        :return: Request response
        """
        job_response_as_dict = self.session.get_job()
        self.active_alert_job_id = job_response_as_dict[0]
        self.active_alert_job_uuid = job_response_as_dict[1]["job_uuid"]
        service_url_part = "/mbb/speedalert/v1/error/?num=noError"
        payload = ""
        headers = {"Content-Type": "application/vnd.vwg.mbb.rvsRdk_v1_0_1+xml", "X-RelatedJobId": self.active_alert_job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def response_to_profile_deactivation_job(self):
        """Response to a profile deactivation job for speed alert service.

        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = "/mbb/speedalert/v1/error/?num=noError"
        payload = ""
        headers = {"Content-Type": "application/vnd.vwg.mbb.rvsRdk_v1_0_1+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def trigger_alert_violation(self, alert_state: AlertState):
        """Trigger speed alert violation for an active profile.

        :param backend.odp_requests.ServiceSpeedAlert.AlertState alert_state: Start or End speed violation.
        :rtype: list
        :return: Request response
        """
        kwargs = {"uuid": self.active_alert_job_uuid, "alert_state": alert_state.value}
        service_url_part = "/mbb/speedalert/v1/violation/"
        headers = {"Content-Type": "application/vnd.vwg.mbb.speedAlert_v1_0_0+xml", "X-RelatedJobId": self.active_alert_job_id}
        payload = payload_factory(self.service_type.value, **kwargs)
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)


class ServiceGeoFenceAlert:
    """Access geofence alert service."""

    class EventType(str, ExtendedEnum):
        """Enum containing possible event types for geofence alert violations."""
        ENTER = "Enter"
        EXIT = "Exit"

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.GEOFENCE_ALERT
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)
        self.active_alert_job_id = None
        self.active_alert_job_geo_uuid = None
        self.active_alert_job_area_id = None

    def response_to_profile_activation_job(self):
        """Response to a profile activation job for geofence alert service.

        :rtype: list
        :return: Request response
        """
        job_response_as_dict = self.session.get_job()
        self.active_alert_job_id = job_response_as_dict[0]
        self.active_alert_job_geo_uuid = job_response_as_dict[1]["geo_uuid"]
        self.active_alert_job_area_id = job_response_as_dict[1]["area_id"]
        service_url_part = "/mbb/geofencing/v1/error/?num=noError"
        payload = ""
        headers = {"Content-Type": "application/vnd.vwg.mbb.rvsRdk_v1_0_1+xml", "X-RelatedJobId": self.active_alert_job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def response_to_profile_deactivation_job(self):
        """Response to a profile deactivation job for geofence alert service.

        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = "/mbb/geofencing/v1/error/?num=noError"
        payload = ""
        headers = {"Content-Type": "application/vnd.vwg.mbb.rvsRdk_v1_0_1+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def trigger_alert_violation(self, event_type: EventType):
        """Trigger speed alert violation for an active profile.

        :param event_type: backend.odp_requests.ServiceGeofenceAlert.AlertState event_type: Exit or enter geofence.
        :rtype: list
        :return: Request response
        """
        kwargs = {"geo_uuid": self.active_alert_job_geo_uuid, "area_id": self.active_alert_job_area_id, "event_type": event_type.value}
        service_url_part = "/mbb/geofencing/v1/violation/"
        headers = {"Content-Type": "application/vnd.vwg.mbb.geoFencing_v1_0_0+xml", "X-RelatedJobId": self.active_alert_job_id}
        payload = payload_factory(self.service_type.value, **kwargs)
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)


class ServiceValetAlert:
    """Access valet alert service."""

    class GeoFenceEventType(str, ExtendedEnum):
        """Enum containing possible event types for valet alert geofence alert service."""

        ENTER = "Enter"
        EXIT = "Exit"

    class SpeedAlertState(str, ExtendedEnum):
        """Enum containing possible alert state types for valet alert speed alert service."""

        START = "Start"
        END = "End"

    class ValetAlertErrorCodes(str, ExtendedEnum):
        """Enum containing possible error types for valet alert service."""

        ERROR5 = 5

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.vin = vin
        self.backend = backend
        self.service_type = ServiceType.VALET_ALERT
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)
        self.__active_speed_alert_job_id = None
        self.__active_geofence_alert_job_id = None
        self.__active_speed_alert_uuid = None
        self.__active_geofence_alert_uuid = None
        self.__active_geofence_alert_area_id = None

    def response_to_profile_activation_job(self):
        """Response to a profile activation job for valet alert service.

        :rtype: list(list)
        :return: Request response
        """
        jobs, ids = self.session.get_valet_alert_activation_jobs()
        self.__active_speed_alert_job_id = jobs["SPEED"]
        self.__active_geofence_alert_job_id = jobs["GEO"]
        self.__active_speed_alert_uuid = ids["SPEED"]["job_uuid"]
        self.__active_geofence_alert_uuid = ids["GEO"]["geo_uuid"]
        self.__active_geofence_alert_area_id = ids["GEO"]["area_id"]

        service_url_part = "/mbb/valetalert/v1/geoFenceError/error?num=noError"
        payload = ""
        headers = {"Content-Type": "application/xml", "X-RelatedJobId": self.__active_geofence_alert_job_id}
        response = self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

        service_url_part = "/mbb/valetalert/v1/speedAlertError/error?num=noError"
        payload = ""
        headers = {"Content-Type": "application/xml", "X-RelatedJobId": self.__active_speed_alert_job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers), response

    def response_to_profile_activation_job_with_error(self, error: ValetAlertErrorCodes):
        """Response to a profile job with error for valet alert service.

        :rtype: list(list)
        :return: Request response
        """
        jobs, ids = self.session.get_valet_alert_activation_jobs()
        self.__active_speed_alert_job_id = jobs["SPEED"]
        self.__active_geofence_alert_job_id = jobs["GEO"]

        service_url_part = f"/mbb/valetalert/v1/geoFenceError/error?num={error.value}"
        payload = ""
        headers = {"Content-Type": "application/xml", "X-RelatedJobId": self.__active_geofence_alert_job_id}
        response = self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

        service_url_part = f"/mbb/valetalert/v1/speedAlertError/error?num={error.value}"
        payload = ""
        headers = {"Content-Type": "application/xml", "X-RelatedJobId": self.__active_speed_alert_job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers), response

    def response_to_profile_deactivation_job(self):
        """Response to a profile deactivation job for valet alert service.

        :rtype: list
        :return: Request response
        """
        jobs, ids = self.session.get_valet_alert_deactivation_jobs()
        self.__active_speed_alert_job_id = jobs["SPEED"]
        self.__active_geofence_alert_job_id = jobs["GEO"]

        service_url_part = "/mbb/valetalert/v1/geoFenceError/error?num=noError"
        payload = ""
        headers = {"Content-Type": "application/xml", "X-RelatedJobId": self.__active_geofence_alert_job_id}
        response = self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

        service_url_part = "/mbb/valetalert/v1/speedAlertError/error?num=noError"
        payload = ""
        headers = {"Content-Type": "application/xml", "X-RelatedJobId": self.__active_speed_alert_job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers), response

    def response_to_profile_deactivation_job_with_error(self, error: ValetAlertErrorCodes):
        """Response to a profile job with error for valet alert service.

        :rtype: list
        :return: Request response
        """
        jobs, ids = self.session.get_valet_alert_deactivation_jobs()
        self.__active_speed_alert_job_id = jobs["SPEED"]
        self.__active_geofence_alert_job_id = jobs["GEO"]

        service_url_part = f"/mbb/valetalert/v1/geoFenceError/error?num={error.value}"
        payload = ""
        headers = {"Content-Type": "application/xml", "X-RelatedJobId": self.__active_geofence_alert_job_id}
        response = self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

        service_url_part = f"/mbb/valetalert/v1/speedAlertError/error?num={error.value}"
        payload = ""
        headers = {"Content-Type": "application/xml", "X-RelatedJobId": self.__active_speed_alert_job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers), response

    def trigger_geofence_alert_violation(self, event_type: GeoFenceEventType):
        """Trigger valet alert speed alert violation for an active profile.

        :param event_type: backend.odp_requests.ServiceValetAlert.GeoFenceEventType event_type: Exit or enter geofence.
        :rtype: list
        :return: Request response
        """
        kwargs = {"geo_uuid": self.__active_geofence_alert_uuid, "id": "0", "area_id": self.__active_geofence_alert_area_id, "event_type": event_type.value}
        service_url_part = "/mbb/valetalert/v1/geoFenceViolation/"
        headers = {"Content-Type": "application/vnd.vwg.mbb.geoFencing_v1_0_0+xml", "X-RelatedJobId": self.__active_geofence_alert_job_id}
        payload = payload_factory("GEOFENCE_ALERT", **kwargs)
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def trigger_speed_alert_violation(self, alert_state: SpeedAlertState):
        """Trigger valet alert speed alert violation for an active profile.

        :param backend.odp_requests.ServiceValetAlert.SpeedAlertState alert_state: Start or end speed violation.
        :rtype: list
        :return: Request response
        """
        kwargs = {"uuid": self.__active_speed_alert_uuid, "id": "0", "alert_state": alert_state.value}
        service_url_part = "/mbb/valetalert/v1/speedAlertViolation/"
        headers = {"Content-Type": "application/vnd.vwg.mbb.speedAlert_v1_0_0+xml", "X-RelatedJobId": self.__active_speed_alert_job_id}
        payload = payload_factory("SPEED_ALERT", **kwargs)
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)


class ServiceRPTProfile:
    """Access RPT Profile service."""

    class RPTProfileErrorCodes(str, ExtendedEnum):
        """Enum containing possible error-codes the service."""
        GENERAL_ERROR_UNKNOWN_REASON = 1
        ECU_RESPONSE_TIMEOUT_EXPIRED = 2
        ECU_REPORTED_ERROR = 3
        SYNC_CONFLICT_DETECTED_TIMESTAMP_CHECK = 4

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.RPT_PROFILE
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def response_to_active_job(self, **kwargs):
        """Response to active job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = "/mbb/profiletimer/v1/profileStateReport/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.rptProfileStateReport_v1_0_2+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def response_to_active_job_with_error(self, error: RPTProfileErrorCodes):
        """Response to active Job with an Error-Code.
        :param backend.odp_requests.ServiceRPTProfile.RPTProfileErrorCodes error: Error-Code to send as job response.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = f"/mbb/profiletimer/v1/errorReport/?num={error.value}"
        payload = {}
        headers = {"Content-Type": "application/vnd.vwg.mbb.rptProfileStateReport_v1_0_2+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)


class ServiceRPTTimer:
    """Access RPT Timer service."""

    class RPTTimerErrorCodes(str, ExtendedEnum):
        """Enum containing possible error-codes the service."""
        GENERAL_ERROR_UNKNOWN_REASON = 1
        ECU_RESPONSE_TIMEOUT_EXPIRED = 2
        ECU_REPORTED_ERROR = 3
        SYNC_CONFLICT_DETECTED_TIMESTAMP_CHECK = 4

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.RPT_TIMER
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def response_to_active_job(self, **kwargs):
        """Response to active job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = "/mbb/profiletimer/v1/timerStateReport/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.rptTimerStateReport_v1_0_0+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def response_to_active_job_with_error(self, error: RPTTimerErrorCodes):
        """Response to active Job with an Error-Code.
        :param backend.odp_requests.ServiceRPTTimer.RPTTimerErrorCodes error: Error-Code to send as job response.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = f"/mbb/profiletimer/v1/errorReport/?num={error.value}"
        payload = {}
        headers = {"Content-Type": "application/vnd.vwg.mbb.rptTimerStateReport_v1_0_0+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)


class ServiceRDT:
    """Access RDT service."""

    class RDTErrorCodes(str, ExtendedEnum):
        """Enum containing possible error-codes the service."""
        GENERAL_ERROR_UNKNOWN_REASON = 1
        ECU_RESPONSE_TIMEOUT_EXPIRED = 2
        ECU_REPORTED_ERROR = 3
        SYNC_CONFLICT_DETECTED_TIMESTAMP_CHECK = 4

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.RDT
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def response_to_active_job(self, **kwargs):
        """Response to active job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = "/mbb/rdt/v1/departureTimersAndProfilesReport/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.departureTimersAndProfilesReportRequest_v1_0_1+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def response_to_active_job_with_error(self, error: RDTErrorCodes):
        """Response to active Job with an Error-Code.
        :param backend.odp_requests.ServiceRDT.RDTErrorCodes error: Error-Code to send as job response.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = f"/mbb/rdt/v1/departureTimeError/?num={error.value}"
        payload = {}
        headers = {"Content-Type": "application/vnd.vwg.mbb.departureTimersAndProfilesReportRequest_v1_0_1+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)


class ServiceRDTExtended:
    """Access RDT Extended service."""

    class RDTExtendedErrorCodes(str, ExtendedEnum):
        """Enum containing possible error-codes the service."""
        GENERAL_ERROR_UNKNOWN_REASON = 1
        ECU_RESPONSE_TIMEOUT_EXPIRED = 2
        ECU_REPORTED_ERROR = 3
        SYNC_CONFLICT_DETECTED_TIMESTAMP_CHECK = 4

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.RDT_EXTENDED
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def response_to_active_job(self, **kwargs):
        """Response to active job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = "/mbb/rdt/v1/departureTimersAndProfilesReport/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.departureTimersAndProfilesReportRequest_v1_0_3+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def response_to_active_job_with_error(self, error: RDTExtendedErrorCodes):
        """Response to active Job with an Error-Code.
        :param backend.odp_requests.ServiceRDT.RDTErrorCodes error: Error-Code to send as job response.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = f"/mbb/rdt/v1/departureTimeError/?num={error.value}"
        payload = {}
        headers = {"Content-Type": "application/vnd.vwg.mbb.departureTimersAndProfilesReportRequest_v1_0_3+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)


class ServiceRPC:
    """Access RPC service."""

    class RPCErrorCodes(str, ExtendedEnum):
        """Enum containing possible error-codes the service."""
        GENERAL_ERROR_UNKNOWN_REASON = 1
        ECU_RESPONSE_TIMEOUT_EXPIRED = 2
        ECU_REPORTED_ERROR = 3
        SYNC_CONFLICT_DETECTED_TIMESTAMP_CHECK = 4
        IGNITION_ON = 5
        CHARGE_PLUG_NOT_CONNECTED_LOCKED = 6
        OPEN_DOORS = 7
        EXTERNAL_POWER_SUPPLY_NOT_AVAILABLE = 8
        GENERAL_CONTROL_DEVICE_ERROR = 9
        BATTERY_LOW = 10
        GEAR_NOT_IN_PARKING_POSITION = 11
        RUNNING_REDUCED_POWER = 12
        AUXILIARY_HEATER_NO_FUEL = 13
        AUXILIARY_HEATER_MAX_OPERATIONS_IN_SEQUENCE = 14
        CHARGING_HAS_PRIORITY = 15
        BATTERY_CONDITIONING_HAS_PRIORITY = 16

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.RPC
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def response_to_active_job(self, **kwargs):
        """Response to active job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = "/mbb/rpc/v1/stateReport/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.climatisationStateReportRequest_v1_0_0+xml", "x-relatedJobId": job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def response_to_active_job_with_error(self, error: RPCErrorCodes):
        """Response to active Job with an Error-Code.
        :param backend.odp_requests.ServiceRPC.RPCErrorCodes error: Error-Code to send as job response.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = f"/mbb/rpc/v1/error/?num={error.value}"
        payload = {}
        # TODO: No-Content-Type necessary?!
        headers = {"X-BRAND": "Audi", "X-COUNTRY": "Germany", "x-relatedJobId": job_id}
        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)


class ServiceRPCExtended:
    """Access RPC Extended service."""

    class RPCExtendedErrorCodes(str, ExtendedEnum):
        """Enum containing possible error-codes the service."""
        GENERAL_ERROR_UNKNOWN_REASON = 1
        ECU_RESPONSE_TIMEOUT_EXPIRED = 2
        ECU_REPORTED_ERROR = 3
        SYNC_CONFLICT_DETECTED_TIMESTAMP_CHECK = 4
        IGNITION_ON = 5
        CHARGE_PLUG_NOT_CONNECTED_LOCKED = 6
        OPEN_DOORS = 7
        EXTERNAL_POWER_SUPPLY_NOT_AVAILABLE = 8
        GENERAL_CONTROL_DEVICE_ERROR = 9
        BATTERY_LOW = 10
        GEAR_NOT_IN_PARKING_POSITION = 11
        RUNNING_REDUCED_POWER = 12
        AUXILIARY_HEATER_NO_FUEL = 13
        AUXILIARY_HEATER_MAX_OPERATIONS_IN_SEQUENCE = 14
        CHARGING_HAS_PRIORITY = 15
        BATTERY_CONDITIONING_HAS_PRIORITY = 16

    def __init__(self, vin, backend):
        """Initialize object.

        :param str vin: VIN to access by backend session.
        :param str backend: Backend where VIN is located.
        """
        self.service_type = ServiceType.RPC_EXTENDED
        self.session = interface_factory(vin, self.service_type.value, backend, cooldown=0)

    def response_to_active_job(self, **kwargs):
        """Response to active job.

        :param dict kwargs: Keyword arguments to manipulate payload with desired values.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = "/mbb/rpc/v1/stateReport/"
        payload = payload_factory(self.service_type.value, **kwargs)
        headers = {"Content-Type": "application/vnd.vwg.mbb.climatisationStateReportRequest_v1_0_3+xml", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("POST", service_url_part, payload, headers)

    def response_to_active_job_with_error(self, error: RPCExtendedErrorCodes):
        """Response to active Job with an Error-Code.
        :param backend.odp_requests.ServiceRPCExtended.RPCExtendedErrorCodes error: Error-Code to send as job response.
        :rtype: list
        :return: Request response
        """
        job_id = self.session.get_job()[0]
        service_url_part = f"/mbb/rpc/v1/error/?num={error.value}"
        payload = {}
        # TODO: No-Content-Type necessary?!
        headers = {"X-BRAND": "Audi", "X-COUNTRY": "Germany", "X-RelatedJobId": job_id}
        return self.session.transceiver.send_host_request("PUT", service_url_part, payload, headers)
