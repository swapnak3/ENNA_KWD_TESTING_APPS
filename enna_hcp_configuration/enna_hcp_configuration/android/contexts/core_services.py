# -*- coding: utf-8 -*-
"""Contexts for the core_services app."""

from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathDetectorExtension
from enna_hcp_configuration.android.xpaths import core_services as xpaths_core_services
from enna_hcp_configuration.common.base import Element

HOME = Element("home", ElementByXPathDetectorExtension([xpaths_core_services.HOME_TITLE, xpaths_core_services.HOME_COLLAPSE_TITLE]))
HOME_EXPAND = Element("home_expand", ElementByXPathDetectorExtension([xpaths_core_services.HOME_TITLE, xpaths_core_services.HOME_EXPAND_TITLE]))
HEALTH_CHECK = Element("health_check", ElementByXPathDetectorExtension([xpaths_core_services.HEALTH_CHECK_TITLE]))
BACKEND_SETTINGS = Element("backend_settings", ElementByXPathDetectorExtension([xpaths_core_services.BACKEND_SETTINGS_TITLE]))
CONFIGURATION = Element("configuration", ElementByXPathDetectorExtension([xpaths_core_services.CONFIGURATION_TITLE]))
PSO_LOGIN = Element("pso_login", ElementByXPathDetectorExtension([xpaths_core_services.PSO_LOGIN_TITLE]))
SERVICE_LIST_DISABLE_REASONS = Element("service_list_disable_reasons", ElementByXPathDetectorExtension([xpaths_core_services.SERVICE_LIST_DISABLE_REASONS_TITLE]))
MQTT = Element("mqtt", ElementByXPathDetectorExtension([xpaths_core_services.MQTT_TITLE]))
TOKENS = Element("tokens", ElementByXPathDetectorExtension([xpaths_core_services.TOKENS_TITLE]))
THIRD_PARTY_TRUSTSTORE = Element("third_party_truststore", ElementByXPathDetectorExtension([xpaths_core_services.THIRD_PARTY_TRUSTSTORE_TITLE]))


CONTEXT = ContextAnalyzer("core_services", AppPackageDetectorExtension(["de.esolutions.coreservices"]))
CONTEXT.add_elements_from_module(globals())
