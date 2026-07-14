# -*- coding: utf-8 -*-
"""Analyzer for the Android Engineering Menu."""

from enna_hcp_configuration.android.xpaths import aem as xpath_aem
from enna_hcp_configuration.android.xpaths import assistant as xpath_assistant
from enna_hcp_configuration.android.base import ContextAnalyzer, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import  Element

GENERAL = Element("general", ElementByXPathDetectorExtension([xpath_assistant.GENERAL_SELECTED_TITLE]))
PROACTIVITY = Element("proactivity", ElementByXPathDetectorExtension([xpath_assistant.PROACTIVITY_SELECTED_TITLE]))
SMART_ROUTINES = Element("smart_routines", ElementByXPathDetectorExtension([xpath_assistant.SMART_ROUTINES_SELECTED_TITLE]))
HELP = Element("help", ElementByXPathDetectorExtension([xpath_assistant.HELP_SELECTED_TITLE]))
HELP_ITEM_HINTS = Element("help_item_hints", ElementByXPathDetectorExtension([xpath_assistant.HELP_HINTS_TITLE]))
HELP_ITEM_SPEECHEXCLUSIVE = Element("help_item_speechexclusive", ElementByXPathDetectorExtension([xpath_assistant.HELP_SPEECHEXCLUSIVE_TITLE]))
HELP_ITEM_NAVIGATION = Element("help_item_navigation", ElementByXPathDetectorExtension([xpath_assistant.HELP_NAVIGATION_TITLE]))
HELP_ITEM_CAR = Element("help_item_car", ElementByXPathDetectorExtension([xpath_assistant.HELP_CAR_TITLE]))
HELP_ITEM_PHONE = Element("help_item_phone", ElementByXPathDetectorExtension([xpath_assistant.HELP_PHONE_TITLE]))
HELP_ITEM_MEDIA = Element("help_item_media", ElementByXPathDetectorExtension([xpath_assistant.HELP_MEDIA_TITLE]))
HELP_ITEM_CLIMATE = Element("help_item_climate", ElementByXPathDetectorExtension([xpath_assistant.HELP_CLIMATE_TITLE]))
HELP_ITEM_FAQ = Element("help_item_faq", ElementByXPathDetectorExtension([xpath_assistant.HELP_FAQ_TITLE]))
HELP_ITEM_CONVERSATIONALS = Element("help_item_conversationals", ElementByXPathDetectorExtension([xpath_assistant.HELP_CONVERSATIONALS_TITLE]))
HELP_ITEM_PLUG_AND_PLAY = Element("help_item_plug_and_play", ElementByXPathDetectorExtension([xpath_assistant.HELP_PLUG_AND_PLAY_TITLE]))

# no subgraphes for
DELETE_ROUTINE_DATA = Element("delete_routine_data", ElementByXPathDetectorExtension([xpath_assistant.DELETE_ROUTINE]))
PHONE_RECOMMENDATIONS_TOGGLE = Element("phone_recommendations_toggle", ElementByXPathDetectorExtension([xpath_assistant.PROACTIVE_RECOMMENDATIONS_TITLE]))


# AEM: GDA Developer Settings for GDA
AEM_GDA_ONLINE_AND_CONNECTIVITY = Element("aem_gda_online_and_connectivity", ElementByXPathDetectorExtension([xpath_aem.GDA_ONLINE_AND_CONNECTIVITY_TITLE]))
AEM_GDA_ONLINE_AND_CONNECTIVITY_EDIT_VIN = Element("aem_gda_online_and_connectivity_edit_vin", ElementByXPathDetectorExtension([xpath_aem.GDA_ONLINE_AND_CONNECTIVITY_VIN_EDIT_TITLE]))
AEM_GDA_CDFW_AND_SPEECH = Element("aem_gda_cdfw_and_speech", ElementByXPathDetectorExtension([xpath_aem.GDA_CDFW_AND_SPEECH_TITLE]))
AEM_GDA_DIALOG_CONFIGURATION = Element("aem_gda_dialog_configuration", ElementByXPathDetectorExtension([xpath_aem.GDA_DIALOG_CONFIGURATION_TITLE]))

# AEM: Prediction Services
AEM_PSC_SETTINGS = Element("aem_psc_settings", ElementByXPathDetectorExtension([xpath_aem.PREDICTION_SERVICES_AEM_TITLE]))
AEM_PSC_SETTINGS_PCL_SETTINGS = Element("aem_psc_settings_pcl_settings", ElementByXPathDetectorExtension([xpath_aem.PREDICTION_SERVICES_AEM_PCL_SETTINGS_TITLE]))
AEM_PSC_SETTINGS_PSC_SETTINGS = Element("aem_psc_settings_psc_settings", ElementByXPathDetectorExtension([xpath_aem.PREDICTION_SERVICES_AEM_PSC_SETTINGS_TITLE]))
AEM_PSC_SETTINGS_SAP_SETTINGS = Element("aem_psc_settings_sap_settings", ElementByXPathDetectorExtension([xpath_aem.PREDICTION_SERVICES_AEM_SAP_SETTINGS_TITLE]))
AEM_PSC_SETTINGS_PSC_BACKEND = Element("aem_psc_settings_psc_backend", ElementByXPathDetectorExtension([xpath_aem.PREDICTION_SERVICES_AEM_PSC_BACKEND_TITLE]))
AEM_PSC_SETTINGS_SAP_FRONTEND = Element("aem_psc_settings_sap_frontend", ElementByXPathDetectorExtension([xpath_aem.PREDICTION_SERVICES_AEM_SAP_FRONTEND_TITLE]))

# AEM: Smart Services
AEM_SMART_SERVICES = Element("aem_smart_services", ElementByXPathDetectorExtension([xpath_aem.SMART_SERVICES_TITLE]))


CONTEXT = ContextAnalyzer("assistant", ElementByXPathDetectorExtension([xpath_assistant.ASSISTANT_PACKAGE, xpath_assistant.ASSISTANT_RESOURCES]))

CONTEXT.add_elements_from_module(globals())
