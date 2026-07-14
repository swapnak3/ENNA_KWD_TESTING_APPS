# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""

from enna_hcp_configuration.android import xpaths
from enna_hcp_configuration.android.xpaths import aem as xpaths_aem
from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import aem as contexts_aem, phone as contexts_phone, launcher as contexts_launcher, navigation as contexts_navigation, ignite_store as contexts_ignite_store
from enna_hcp_configuration.android.contexts import emergencycall as contexts_emergency_call
from enna_hcp_configuration.android.contexts import assistant as contexts_assistant


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_aem.MAIN, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_aem.SEARCH, contexts_aem.MAIN, (HMIActionType.click_element, [xpaths_aem.SEARCH_BACK_BUTTON]))
	graph.add_transition(contexts_aem.MAIN, contexts_ignite_store.AEM_IGNITE_STORE_ENGINEERING_MENUE, (HMIActionType.click_element_in_list, [xpaths_aem.IGNITE_STORE_ENGINEERING_MENU_BUTTON, xpaths_aem.LIST]))
	graph.add_transition(contexts_aem.MAIN, contexts_aem.POWER_MODING_CLIENT_SETTINGS, (HMIActionType.click_element_in_list, [xpaths_aem.VEHICLE_POWERMODING_CLIENT_SETTINGS_BUTTON, xpaths_aem.LIST]))
	graph.add_transition(contexts_aem.POWER_MODING_CLIENT_SETTINGS, contexts_aem.MAIN, (HMIActionType.click_element, [xpaths_aem.VEHICLE_POWERMODING_CLIENT_SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_aem.POWER_MODING_CLIENT_SETTINGS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_aem.MAIN, contexts_emergency_call.AEM_ECALL_SETTINGS, (HMIActionType.click_element_in_list, [xpaths_aem.ECALL_TEST_MENU_BUTTON, xpaths_aem.LIST]))
	graph.add_transition(contexts_aem.MAIN, contexts_phone.AEM_CONNECTIVITY_TEST_MENU, (HMIActionType.click_element_in_list, [xpaths_aem.CONNECTIVITY_TEST_MENU_BUTTON, xpaths_aem.LIST]))
	graph.add_transition(contexts_aem.MAIN, contexts_assistant.AEM_GDA_ONLINE_AND_CONNECTIVITY, (HMIActionType.click_element_in_list, [xpaths_aem.GDA_BUTTON, xpaths_aem.LIST]))
	graph.add_transition(contexts_aem.MAIN, contexts_assistant.AEM_GDA_CDFW_AND_SPEECH, (HMIActionType.click_element_in_list, [xpaths_aem.GDA_BUTTON, xpaths_aem.LIST]))
	graph.add_transition(contexts_aem.MAIN, contexts_assistant.AEM_GDA_DIALOG_CONFIGURATION, (HMIActionType.click_element_in_list, [xpaths_aem.GDA_BUTTON, xpaths_aem.LIST]))
	graph.add_transition(contexts_aem.MAIN, contexts_assistant.AEM_PSC_SETTINGS, (HMIActionType.click_element_in_list, [xpaths_aem.PREDICTION_SERVICES_AEM_BUTTON, xpaths_aem.LIST]))
	graph.add_transition(contexts_aem.MAIN, contexts_assistant.AEM_SMART_SERVICES, (HMIActionType.click_element_in_list, [xpaths_aem.SMART_SERVICES_BUTTON, xpaths_aem.LIST]))
	graph.add_transition(contexts_aem.MAIN, contexts_navigation.GEM, (HMIActionType.click_element_in_list, [xpaths_aem.NAV_GEM, xpaths_aem.LIST]))
