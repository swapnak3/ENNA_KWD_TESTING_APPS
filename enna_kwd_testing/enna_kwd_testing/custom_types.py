# -*- coding: utf-8 -*-
"""Module contains custom types extensions for Keyword Written Testing."""

import enna.custom_types


class Language(enna.custom_types.Language):
	"""Enumeration for Languages."""
	BS_BA = "bs_BA"
	CS_CZ = "cs_CZ"
	DA_DK = "da_DK"
	DE_DE = "de_DE"
	EL_GR = "el_GR"
	EN_GB = "en_GB"
	ES_ES = "es_ES"
	FI_FI = "fi_FI"
	FR_FR = "fr_FR"
	HR_HR = "hr_HR"
	HU_HU = "hu_HU"
	IT_IT = "it_IT"
	NL_NL = "nl_NL"
	NO_NO = "no_NO"
	PL_PL = "pl_PL"
	PT_PT = "pt_PT"
	RO_RO = "ro_RO"
	RU_RU = "ru_RU"
	SK_SK = "sk_SK"
	SL_SI = "sl_SI"
	SR_RS = "sr_RS"
	SV_SE = "sv_SE"
	TR_TR = "tr_TR"
	UK_UA = "uk_UA"

class Platform(enna.custom_types.Platform):
	"""Enumeration with possible platforms for MQB(W)evo.
	We get our information from https://volkswagen-net.de/wikis/pages/viewpage.action?pageId=1074402772.
	"""
	MQBWevo = enna.core.enna_enum.AutoString()  # vehicle platform: AU38xPA/AU336

class VehicleProject(enna.custom_types.VehicleProject):
	"""Enumeration with possible vehicle projects for MQBWevo"""
	AU38x_PA = enna.core.enna_enum.AutoString()
	AU336_Q3NF = enna.core.enna_enum.AutoString()
