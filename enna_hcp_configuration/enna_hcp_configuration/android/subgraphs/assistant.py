# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""

from enna_hcp_configuration.android.xpaths import launcher as xpaths_launcher
from enna_hcp_configuration.android.xpaths import aem as xpaths_aem
from enna_hcp_configuration.android.xpaths import assistant as xpaths_assistant
from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import aem as contexts_aem
from enna_hcp_configuration.android.contexts import assistant as contexts_assistant
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher
from enna_hcp_configuration.android.contexts import settings as contexts_settings


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_assistant.GENERAL, contexts_assistant.PROACTIVITY, (HMIActionType.click_element, [xpaths_assistant.PROACTIVITY_BUTTON]))
	graph.add_transition(contexts_assistant.GENERAL, contexts_assistant.SMART_ROUTINES, (HMIActionType.click_element, [xpaths_assistant.SMART_ROUTINES_BUTTON]))
	graph.add_transition(contexts_assistant.GENERAL, contexts_assistant.HELP, (HMIActionType.click_element, [xpaths_assistant.HELP_BUTTON]))
	graph.add_transition(contexts_assistant.PROACTIVITY, contexts_assistant.GENERAL, (HMIActionType.click_element, [xpaths_assistant.GENERAL_BUTTON]))
	graph.add_transition(contexts_assistant.PROACTIVITY, contexts_assistant.SMART_ROUTINES, (HMIActionType.click_element, [xpaths_assistant.SMART_ROUTINES_BUTTON]))
	graph.add_transition(contexts_assistant.PROACTIVITY, contexts_assistant.HELP, (HMIActionType.click_element, [xpaths_assistant.HELP_BUTTON]))
	graph.add_transition(contexts_assistant.SMART_ROUTINES, contexts_assistant.GENERAL, (HMIActionType.click_element, [xpaths_assistant.GENERAL_BUTTON]))
	graph.add_transition(contexts_assistant.SMART_ROUTINES, contexts_assistant.PROACTIVITY, (HMIActionType.click_element, [xpaths_assistant.PROACTIVITY_BUTTON]))
	graph.add_transition(contexts_assistant.SMART_ROUTINES, contexts_assistant.HELP, (HMIActionType.click_element, [xpaths_assistant.HELP_BUTTON]))
	graph.add_transition(contexts_assistant.HELP, contexts_assistant.GENERAL, (HMIActionType.click_element, [xpaths_assistant.GENERAL_BUTTON]))
	graph.add_transition(contexts_assistant.HELP, contexts_assistant.PROACTIVITY, (HMIActionType.click_element, [xpaths_assistant.PROACTIVITY_BUTTON]))
	graph.add_transition(contexts_assistant.HELP, contexts_assistant.SMART_ROUTINES, (HMIActionType.click_element, [xpaths_assistant.SMART_ROUTINES_BUTTON]))

	# Exit assistant to app list
	graph.add_transition(contexts_assistant.GENERAL, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_assistant.PROACTIVITY, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_assistant.SMART_ROUTINES, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_assistant.HELP, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))

	# Exit assistant to settings main
	graph.add_transition(contexts_assistant.GENERAL, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_assistant.BACK_BUTTON]))
	graph.add_transition(contexts_assistant.PROACTIVITY, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_assistant.BACK_BUTTON]))
	graph.add_transition(contexts_assistant.SMART_ROUTINES, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_assistant.BACK_BUTTON]))
	graph.add_transition(contexts_assistant.HELP, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_assistant.BACK_BUTTON]))

	# Path from help to help elements
	graph.add_transition(contexts_assistant.HELP, contexts_assistant.HELP_ITEM_HINTS, (HMIActionType.click_element_in_list, [xpaths_assistant.HELP_HINTS_BUTTON, xpaths_assistant.LIST_CONTAINER]))
	graph.add_transition(contexts_assistant.HELP, contexts_assistant.HELP_ITEM_SPEECHEXCLUSIVE, (HMIActionType.click_element_in_list, [xpaths_assistant.HELP_SPEECHEXCLUSIVE_BUTTON, xpaths_assistant.LIST_CONTAINER]))
	graph.add_transition(contexts_assistant.HELP, contexts_assistant.HELP_ITEM_NAVIGATION, (HMIActionType.click_element_in_list, [xpaths_assistant.HELP_NAVIGATION_BUTTON, xpaths_assistant.LIST_CONTAINER]))
	graph.add_transition(contexts_assistant.HELP, contexts_assistant.HELP_ITEM_CAR, (HMIActionType.click_element_in_list, [xpaths_assistant.HELP_CAR_BUTTON, xpaths_assistant.LIST_CONTAINER]))
	graph.add_transition(contexts_assistant.HELP, contexts_assistant.HELP_ITEM_PHONE, (HMIActionType.click_element_in_list, [xpaths_assistant.HELP_PHONE_BUTTON, xpaths_assistant.LIST_CONTAINER]))
	graph.add_transition(contexts_assistant.HELP, contexts_assistant.HELP_ITEM_MEDIA, (HMIActionType.click_element_in_list, [xpaths_assistant.HELP_MEDIA_BUTTON, xpaths_assistant.LIST_CONTAINER]))
	graph.add_transition(contexts_assistant.HELP, contexts_assistant.HELP_ITEM_CLIMATE, (HMIActionType.click_element_in_list, [xpaths_assistant.HELP_CLIMATE_BUTTON, xpaths_assistant.LIST_CONTAINER]))
	graph.add_transition(contexts_assistant.HELP, contexts_assistant.HELP_ITEM_FAQ, (HMIActionType.click_element_in_list, [xpaths_assistant.HELP_FAQ_BUTTON, xpaths_assistant.LIST_CONTAINER]))
	graph.add_transition(contexts_assistant.HELP, contexts_assistant.HELP_ITEM_CONVERSATIONALS, (HMIActionType.click_element_in_list, [xpaths_assistant.HELP_CONVERSATIONALS_BUTTON, xpaths_assistant.LIST_CONTAINER]))
	graph.add_transition(contexts_assistant.HELP, contexts_assistant.HELP_ITEM_PLUG_AND_PLAY, (HMIActionType.click_element_in_list, [xpaths_assistant.HELP_PLUG_AND_PLAY_BUTTON, xpaths_assistant.LIST_CONTAINER]))

	# exit help elements to help
	graph.add_transition(contexts_assistant.HELP_ITEM_HINTS, contexts_assistant.HELP, (HMIActionType.click_element, [xpaths_assistant.BACK_BUTTON]))
	graph.add_transition(contexts_assistant.HELP_ITEM_SPEECHEXCLUSIVE, contexts_assistant.HELP, (HMIActionType.click_element, [xpaths_assistant.BACK_BUTTON]))
	graph.add_transition(contexts_assistant.HELP_ITEM_NAVIGATION, contexts_assistant.HELP, (HMIActionType.click_element, [xpaths_assistant.BACK_BUTTON]))
	graph.add_transition(contexts_assistant.HELP_ITEM_CAR, contexts_assistant.HELP, (HMIActionType.click_element, [xpaths_assistant.BACK_BUTTON]))
	graph.add_transition(contexts_assistant.HELP_ITEM_PHONE, contexts_assistant.HELP, (HMIActionType.click_element, [xpaths_assistant.BACK_BUTTON]))
	graph.add_transition(contexts_assistant.HELP_ITEM_MEDIA, contexts_assistant.HELP, (HMIActionType.click_element, [xpaths_assistant.BACK_BUTTON]))
	graph.add_transition(contexts_assistant.HELP_ITEM_CLIMATE, contexts_assistant.HELP, (HMIActionType.click_element, [xpaths_assistant.BACK_BUTTON]))
	graph.add_transition(contexts_assistant.HELP_ITEM_FAQ, contexts_assistant.HELP, (HMIActionType.click_element, [xpaths_assistant.BACK_BUTTON]))
	graph.add_transition(contexts_assistant.HELP_ITEM_CONVERSATIONALS, contexts_assistant.HELP, (HMIActionType.click_element, [xpaths_assistant.BACK_BUTTON]))
	graph.add_transition(contexts_assistant.HELP_ITEM_PLUG_AND_PLAY, contexts_assistant.HELP, (HMIActionType.click_element, [xpaths_assistant.BACK_BUTTON]))

	# AEM: Assistant GDA
	graph.add_transition(contexts_assistant.AEM_GDA_ONLINE_AND_CONNECTIVITY, contexts_assistant.AEM_GDA_CDFW_AND_SPEECH, (HMIActionType.click_element, [xpaths_aem.GDA_CDFW_AND_SPEECH_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_GDA_ONLINE_AND_CONNECTIVITY, contexts_assistant.AEM_GDA_DIALOG_CONFIGURATION, (HMIActionType.click_element, [xpaths_aem.GDA_DIALOG_CONFIGURATION_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_GDA_CDFW_AND_SPEECH, contexts_assistant.AEM_GDA_ONLINE_AND_CONNECTIVITY, (HMIActionType.click_element, [xpaths_aem.GDA_ONLINE_AND_CONNECTIVITY_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_GDA_CDFW_AND_SPEECH, contexts_assistant.AEM_GDA_DIALOG_CONFIGURATION, (HMIActionType.click_element, [xpaths_aem.GDA_DIALOG_CONFIGURATION_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_GDA_DIALOG_CONFIGURATION, contexts_assistant.AEM_GDA_ONLINE_AND_CONNECTIVITY, (HMIActionType.click_element, [xpaths_aem.GDA_ONLINE_AND_CONNECTIVITY_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_GDA_DIALOG_CONFIGURATION, contexts_assistant.AEM_GDA_CDFW_AND_SPEECH, (HMIActionType.click_element, [xpaths_aem.GDA_CDFW_AND_SPEECH_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_GDA_ONLINE_AND_CONNECTIVITY, contexts_aem.MAIN, (HMIActionType.click_element, [xpaths_aem.GDA_BACK_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_GDA_CDFW_AND_SPEECH, contexts_aem.MAIN, (HMIActionType.click_element, [xpaths_aem.GDA_BACK_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_GDA_DIALOG_CONFIGURATION, contexts_aem.MAIN, (HMIActionType.click_element, [xpaths_aem.GDA_BACK_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_GDA_ONLINE_AND_CONNECTIVITY, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_GDA_ONLINE_AND_CONNECTIVITY, contexts_assistant.AEM_GDA_ONLINE_AND_CONNECTIVITY_EDIT_VIN, (HMIActionType.click_element, [xpaths_aem.GDA_ONLINE_AND_CONNECTIVITY_VIN_EDIT_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_GDA_ONLINE_AND_CONNECTIVITY_EDIT_VIN, contexts_assistant.AEM_GDA_ONLINE_AND_CONNECTIVITY, (HMIActionType.click_element, [xpaths_aem.GDA_ONLINE_AND_CONNECTIVITY_VIN_EDIT_CANCEL_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_GDA_CDFW_AND_SPEECH, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_GDA_DIALOG_CONFIGURATION, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))

	# AEM: Assistant Predictions
	graph.add_transition(contexts_assistant.AEM_PSC_SETTINGS, contexts_aem.MAIN, (HMIActionType.click_element, [xpaths_aem.PREDICTION_SERVICES_AEM_BACK_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_PSC_SETTINGS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_PSC_SETTINGS, contexts_assistant.AEM_PSC_SETTINGS_PCL_SETTINGS, (HMIActionType.click_element, [xpaths_aem.PREDICTION_SERVICES_AEM_PCL_SETTINGS_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_PSC_SETTINGS_PCL_SETTINGS, contexts_assistant.AEM_PSC_SETTINGS, (HMIActionType.click_element, [xpaths_aem.PREDICTION_SERVICES_AEM_PCL_SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_PSC_SETTINGS, contexts_assistant.AEM_PSC_SETTINGS_PSC_SETTINGS, (HMIActionType.click_element, [xpaths_aem.PREDICTION_SERVICES_AEM_PSC_SETTINGS_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_PSC_SETTINGS_PSC_SETTINGS, contexts_assistant.AEM_PSC_SETTINGS, (HMIActionType.click_element, [xpaths_aem.PREDICTION_SERVICES_AEM_PSC_SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_PSC_SETTINGS, contexts_assistant.AEM_PSC_SETTINGS_SAP_SETTINGS, (HMIActionType.click_element, [xpaths_aem.PREDICTION_SERVICES_AEM_SAP_SETTINGS_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_PSC_SETTINGS_SAP_SETTINGS, contexts_assistant.AEM_PSC_SETTINGS, (HMIActionType.click_element, [xpaths_aem.PREDICTION_SERVICES_AEM_SAP_SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_PSC_SETTINGS, contexts_assistant.AEM_PSC_SETTINGS_PSC_BACKEND, (HMIActionType.click_element, [xpaths_aem.PREDICTION_SERVICES_AEM_PSC_BACKEND_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_PSC_SETTINGS_PSC_BACKEND, contexts_assistant.AEM_PSC_SETTINGS, (HMIActionType.click_element, [xpaths_aem.PREDICTION_SERVICES_AEM_PSC_BACKEND_BACK_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_PSC_SETTINGS, contexts_assistant.AEM_PSC_SETTINGS_SAP_FRONTEND, (HMIActionType.click_element, [xpaths_aem.PREDICTION_SERVICES_AEM_SAP_FRONTEND_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_PSC_SETTINGS_SAP_FRONTEND, contexts_assistant.AEM_PSC_SETTINGS, (HMIActionType.click_element, [xpaths_aem.PREDICTION_SERVICES_AEM_SAP_FRONTEND_BACK_BUTTON]))

	# AEM: Assistant Smart Services
	graph.add_transition(contexts_assistant.AEM_SMART_SERVICES, contexts_aem.MAIN, (HMIActionType.click_element, [xpaths_aem.SMART_SERVICES_BACK_BUTTON]))
	graph.add_transition(contexts_assistant.AEM_SMART_SERVICES, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
