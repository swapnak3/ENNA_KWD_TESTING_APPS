# -*- coding: utf-8 -*-
"""Created on 07.03.2022.

@project: enna_kwd_testing.
@author: DYX34ZN: Jakob Kein.
Contains factory for vehicle (for backend requests).
"""
from .vehicles import a3_g_tron, vin_database
from .vehicles import a8_alerts
from .vehicles import a8_expired_licenses
from .vehicles import a8_phev_erw_voko
from .vehicles import b9_expired_licenses
from .vehicles import b9_rah_rhf_al_comb__1
from .vehicles import b9pa
from .vehicles import etron_ta_cbev
from .vehicles import q7
from .vehicles import q7_guestuser
from .vehicles import q7_phev_heater_source_quickstart
from .vehicles import q7_ta_honk_and_flash
from .vehicles import q7_ta_honk_and_flash2
from .vehicles import q7_ta_phev
from .vehicles import q7_ta_phev_2


def vehicle(vin):
    """Generate vehicle object by given vin.

    :param str vin: VIN to use from myaudi account.
    :rtype: backend.vehicles.<VEHICLE>
    :return: Vehicle object for given vin.
    :raises NotImplementedError: if a vin is demanded, for which no class is specified.
    """
    if vin == vin_database.Q7_VIN:
        return q7.Q7()
    elif vin == vin_database.A8_PHEV_ERW_VOKO_VIN:
        return a8_phev_erw_voko.A8PhevErwVoko()
    elif vin == vin_database.B9_RAH_RHF_AL_COMB_VIN:
        return b9_rah_rhf_al_comb__1.B9RahRhfAlComb1()
    elif vin == vin_database.B9_EXPIRED_LICENSES_VIN:
        return b9_expired_licenses.B9ExpiredLicenses()
    elif vin == vin_database.Q7_HEATER_SOURCE_QUICKSTART_VIN:
        return q7_phev_heater_source_quickstart.Q7PhevHeaterSourceQuickstart()
    elif vin == vin_database.Q7_HONK_AND_FLASH_VIN:
        return q7_ta_honk_and_flash.TaOdpQ7HonkAndFlash()
    elif vin == vin_database.B9PA_VIN:
        return b9pa.B9PA()
    elif vin == vin_database.Q7_PHEV_2_VIN:
        return q7_ta_phev_2.TaOdpQ7Phev2()
    elif vin == vin_database.A8_LICENSES_VIN:
        return a8_expired_licenses.A8ExpiredLicenses()
    elif vin == vin_database.Q7_PHEV_VIN:
        return q7_ta_phev.TaOdpQ7Phev()
    elif vin == vin_database.A8_ALERTS_AND_WARNINGS_VIN:
        return a8_alerts.TaA8AlertsAndWarning()
    elif vin == vin_database.ETRON_VIN:
        return etron_ta_cbev.TaOdpeTronCBEV()
    if vin == vin_database.Q7_HONK_AND_FLASH_2_VIN:
        return q7_ta_honk_and_flash2.TaOdpQ7HonkAndFlash2()
    elif vin == vin_database.A3_SPORTSBACK_CNG_VIN:
        return a3_g_tron.A3Gtron()
    elif vin == vin_database.GUESTUSER_VIN:
        return q7_guestuser.Q7GuestUser()
    else:
        raise NotImplementedError(f"The VIN {vin} is not implemented yet.")
