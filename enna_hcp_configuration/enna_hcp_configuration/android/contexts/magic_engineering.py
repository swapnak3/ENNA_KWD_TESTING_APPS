# -*- coding: utf-8 -*-
"""Analyzer for the MAGIC-Engineering app."""

from enna_hcp_configuration.android.xpaths import magic_engineering
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import Element


# HOME = Element("home", ElementByXPathDetectorExtension([magic_engineering.HOME_TITLE, magic_engineering.HOME_COLLAPS_TITLE]))
CONNECTIVITY = Element("connectivity", ElementByXPathDetectorExtension([magic_engineering.CONNECTIVITY_TITLE]))
ACCOUNT_SERVICE = Element("account_service", ElementByXPathDetectorExtension([magic_engineering.ACCOUNT_SERVICE_TITLE]))
SERVICE_MANAGEMENT_TTS = Element("service_management_tts", ElementByXPathDetectorExtension([magic_engineering.SERVICE_MANAGEMENT_TTS_TITLE]))
SERVICE_MANAGEMENT_VTTL = Element("service_management_vttl", ElementByXPathDetectorExtension([magic_engineering.SERVICE_MANAGEMENT_VTTL_TITLE]))
MQTT = Element("mqtt", ElementByXPathDetectorExtension([magic_engineering.MQTT_TITLE]))
MAGIC_SERVICE = Element("magic_service", ElementByXPathDetectorExtension([magic_engineering.MAGIC_SERVICE_TITLE]))

CONTEXT = ContextAnalyzer("magic_engineering", AppPackageDetectorExtension(["technology.cariad.magic.engineering"]))
CONTEXT.add_elements_from_module(globals())
