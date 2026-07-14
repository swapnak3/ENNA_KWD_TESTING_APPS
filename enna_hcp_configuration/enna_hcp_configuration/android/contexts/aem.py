# -*- coding: utf-8 -*-
"""Analyzer for the Android Engineering Menu."""

from enna_hcp_configuration.android.xpaths import aem
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import Element

MAIN = Element("main", ElementByXPathDetectorExtension([aem.MAIN_TITLE]))
SEARCH = Element("search", ElementByXPathDetectorExtension([aem.LIST,aem.KEYBOARD]))
POWER_MODING_CLIENT_SETTINGS = Element("power_moding_client_settings", ElementByXPathDetectorExtension([aem.VEHICLE_POWERMODING_CLIENT_SETTINGS_TITLE]))

CONTEXT = ContextAnalyzer("aem", AppPackageDetectorExtension(["de.eso.aem", "com.harman.vehicle.powermoding"]))
CONTEXT.add_elements_from_module(globals())
