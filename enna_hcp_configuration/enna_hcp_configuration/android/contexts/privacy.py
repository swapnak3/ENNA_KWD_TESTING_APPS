# -*- coding: utf-8 -*-
"""Analyzer for the privacy App."""

#from enna_hcp_configuration.android import xpaths
from enna_hcp_configuration.android.xpaths import privacy
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import Element

POPUP_USE_ONLINE_SERVICES = Element("POPUP_use_online_services", ElementByXPathDetectorExtension([privacy.MODE_USE_ONLINE_SERVICES_TITLE]))

# MAIN = Element("main", ElementByXPathDetectorExtension([privacy.SETTINGS_PRIVACY_SETTINGS_TITLE]))
PRIVACY_SETTINGS = Element("privacy_settings", ElementByXPathDetectorExtension([privacy.SETTINGS_PRIVACY_SETTINGS_TITLE]))
OVERVIEW_SERVICES = Element("overview_services", ElementByXPathDetectorExtension([privacy.SETTINGS_OVERVIEW_SERVICES_TITLE]))
FURTHER_INFORMATIONS = Element("further_informations", ElementByXPathDetectorExtension([privacy.SETTINGS_FURTHER_INFORMATIONS_TITLE]))
MAIN_SETTINGS = Element("main_settings", ElementByXPathDetectorExtension([privacy.SETTINGS_SETTINGS_TITLE]))

POPUP_DATA_COLLECTION = Element("POPUP_data_collection", ElementByXPathDetectorExtension([privacy.MODE_DATA_COLLECTION_TITLE]))
POPUP_PRIVACY_DATA_COLLECTION_STATISTICS = Element("POPUP_privacy_data_collection_statistics", ElementByXPathDetectorExtension([privacy.POPUP_DATA_COLLECTION_STATISTICS_TITLE]))
POPUP_PRIVACY_DATA_COLLECTION_RESEARCH = Element("POPUP_privacy_data_collection_research", ElementByXPathDetectorExtension([privacy.POPUP_DATA_COLLECTION_RESEARCH_TITLE]))
POPUP_PRIVACY_DATA_COLLECTION_PERSONALIZED_EVALUATIONS = Element("POPUP_privacy_data_collection_personalized_evaluations", ElementByXPathDetectorExtension([privacy.POPUP_DATA_COLLECTION_PERSONALIZED_EVALUATIONS_TITLE]))

CONTEXT = ContextAnalyzer("privacy", AppPackageDetectorExtension(["de.eso.privacymode"]))
CONTEXT.add_elements_from_module(globals())
