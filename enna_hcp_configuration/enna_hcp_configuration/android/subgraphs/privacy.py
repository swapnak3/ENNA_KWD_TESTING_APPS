# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""

from enna_hcp_configuration.android import xpaths
from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import aaam as contexts_aaam
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher
from enna_hcp_configuration.android.contexts import privacy as contexts_privacy
from enna_hcp_configuration.android.contexts import settings as contexts_settings
from enna_hcp_configuration.android.xpaths import privacy as xpaths_privacy


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_privacy.PRIVACY_SETTINGS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_privacy.PRIVACY_SETTINGS, contexts_settings.PRIVACY, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_OVERVIEW_SERVICES_BUTTON]))
	graph.add_transition(contexts_privacy.PRIVACY_SETTINGS, contexts_privacy.OVERVIEW_SERVICES, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_OVERVIEW_SERVICES_BUTTON]))
	graph.add_transition(contexts_privacy.PRIVACY_SETTINGS, contexts_privacy.FURTHER_INFORMATIONS, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_FURTHER_INFORMATIONS_BUTTON]))
	graph.add_transition(contexts_privacy.PRIVACY_SETTINGS, contexts_privacy.MAIN_SETTINGS, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_SETTINGS_BUTTON]))
	graph.add_transition(contexts_privacy.PRIVACY_SETTINGS, contexts_settings.PRIVACY, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_privacy.PRIVACY_SETTINGS, contexts_aaam.CATALOG_POPUP_DATA_PRIVACY, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_privacy.OVERVIEW_SERVICES, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_privacy.OVERVIEW_SERVICES, contexts_privacy.FURTHER_INFORMATIONS, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_FURTHER_INFORMATIONS_BUTTON]))
	graph.add_transition(contexts_privacy.OVERVIEW_SERVICES, contexts_privacy.PRIVACY_SETTINGS, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_PRIVACY_SETTINGS_BUTTON]))
	graph.add_transition(contexts_privacy.OVERVIEW_SERVICES, contexts_privacy.MAIN_SETTINGS, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_SETTINGS_BUTTON]))
	graph.add_transition(contexts_privacy.OVERVIEW_SERVICES, contexts_settings.PRIVACY, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_privacy.FURTHER_INFORMATIONS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_privacy.FURTHER_INFORMATIONS, contexts_privacy.PRIVACY_SETTINGS, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_PRIVACY_SETTINGS_BUTTON]))
	graph.add_transition(contexts_privacy.FURTHER_INFORMATIONS, contexts_privacy.OVERVIEW_SERVICES, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_OVERVIEW_SERVICES_BUTTON]))
	graph.add_transition(contexts_privacy.FURTHER_INFORMATIONS, contexts_privacy.MAIN_SETTINGS, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_SETTINGS_BUTTON]))
	graph.add_transition(contexts_privacy.FURTHER_INFORMATIONS, contexts_settings.PRIVACY, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_privacy.MAIN_SETTINGS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_privacy.MAIN_SETTINGS, contexts_privacy.PRIVACY_SETTINGS, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_privacy.MAIN_SETTINGS, contexts_privacy.OVERVIEW_SERVICES, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_privacy.MAIN_SETTINGS, contexts_privacy.FURTHER_INFORMATIONS, (HMIActionType.click_element, [xpaths_privacy.SETTINGS_BACK_BUTTON]))
