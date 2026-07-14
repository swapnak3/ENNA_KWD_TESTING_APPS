# -*- coding: utf-8 -*-
"""Created on 04.02.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
"""
import logging

from .interface import ServiceType
from ..payloads.services import carfinder_invalid
from ..payloads.services import carfinder_valid
from ..payloads.services import dwa
from ..payloads.services import geofencealert_violation
from ..payloads.services import ib_cgw_clu_31
from ..payloads.services import ib_cgw_clu_33
from ..payloads.services import ib_cgw_mbb_default
from ..payloads.services import rah_quickstart
from ..payloads.services import rah_timer
from ..payloads.services import rah_timer_b9pa
from ..payloads.services import rbc_cbev
from ..payloads.services import rbc_phev
from ..payloads.services import rhf
from ..payloads.services import speedalert_violation
from ..payloads.services import rpt_profile_cbev
from ..payloads.services import rpt_timer_cbev
from ..payloads.services import rdt_phev
from ..payloads.services import rdt_phev_extended
from ..payloads.services import rpc
from ..payloads.services import rpc_extended
from ..payloads.services import vsr

logger = logging.getLogger(__name__)


def payload_factory(service_type, **kwargs):
    """Return payload for given service type.

    :param str service_type: Service to get payload for.
    :param dict kwargs: Keyword arguments for payload.
    :rtype: str
    :return: Manipulated Payload of the requested service-type
    """
    logger.info(f"Generating payload of type {service_type}")
    if service_type == ServiceType.INSTALL_BASE_UPDATE_CGW_CLU_33:
        return ib_cgw_clu_33.Payload().get_payload()
    elif service_type == ServiceType.INSTALL_BASE_UPDATE_CGW_CLU_31:
        return ib_cgw_clu_31.Payload().get_payload()
    elif service_type == ServiceType.INSTALL_BASE_UPDATE_CGW_MBB_DEFAULT:
        return ib_cgw_mbb_default.Payload().get_payload()
    elif service_type == ServiceType.VSR:
        return vsr.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.CARFINDER_VALID:
        return carfinder_valid.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.CARFINDER_INVALID:
        return carfinder_invalid.Payload().get_payload()
    elif service_type == ServiceType.RAH_QUICKSTART:
        return rah_quickstart.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.RAH_TIMER:
        return rah_timer.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.RAH_TIMER_B9PA:
        return rah_timer_b9pa.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.RHF:
        return rhf.Payload().get_payload()
    elif service_type == ServiceType.DWA:
        return dwa.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.RBC_QUICKSTART_PHEV:
        return rbc_phev.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.RBC_QUICKSTART_CBEV:
        return rbc_cbev.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.SPEED_ALERT:
        return speedalert_violation.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.GEOFENCE_ALERT:
        return geofencealert_violation.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.RPT_PROFILE:
        return rpt_profile_cbev.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.RPT_TIMER:
        return rpt_timer_cbev.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.RDT:
        return rdt_phev.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.RDT_EXTENDED:
        return rdt_phev_extended.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.RPC:
        return rpc.Payload(**kwargs).get_payload()
    elif service_type == ServiceType.RPC_EXTENDED:
        return rpc_extended.Payload(**kwargs).get_payload()
    else:
        return None
