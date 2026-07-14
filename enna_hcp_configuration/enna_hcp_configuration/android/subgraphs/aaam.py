# -*- coding: utf-8 -*-
"""Module contains transitions from aaam (AudiAsAMatchmaker, themes app) to any menu"""

from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import aaam as contexts_aaam
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher
from enna_hcp_configuration.android.contexts import legal as contexts_legal
from enna_hcp_configuration.android.contexts import privacy as contexts_privacy
from enna_hcp_configuration.android.xpaths import aaam as xpaths_aaam
from enna_hcp_configuration.android.xpaths import launcher as xpaths_launcher


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_aaam.THEMES, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_aaam.SETTINGS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))

	graph.add_transition(contexts_aaam.THEMES, contexts_aaam.CATALOG, (HMIActionType.click_element, [xpaths_aaam.CATALOG_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_POPUP_DATA_PRIVACY, contexts_privacy.PRIVACY_SETTINGS, (HMIActionType.click_element, [xpaths_aaam.CATALOG_POPUP_DATA_PRIVACY_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_POPUP_DATA_PRIVACY, contexts_aaam.THEMES, (HMIActionType.click_element, [xpaths_aaam.CATALOG_POPUP_CANCEL_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_POPUP_DATA_PRIVACY, contexts_aaam.CATALOG_POPUP_FUNCTION_UNAVAILABLE, (HMIActionType.click_element, [xpaths_aaam.CATALOG_POPUP_CANCEL_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_POPUP_FUNCTION_UNAVAILABLE, contexts_aaam.THEMES, (HMIActionType.click_element, [xpaths_aaam.CATALOG_POPUP_FUNCTION_UNAVAILABLE_CANCEL_BUTTON]))

	graph.add_transition(contexts_aaam.CATALOG, contexts_aaam.THEMES, (HMIActionType.click_element, [xpaths_aaam.THEMES_BUTTON]))
	graph.add_transition(contexts_aaam.THEMES, contexts_aaam.CATALOG_INFO, (HMIActionType.click_element, [xpaths_aaam.CATALOG_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_INFO, contexts_aaam.CATALOG, (HMIActionType.click_element, [xpaths_aaam.CATALOG_INFO_TOCATALOG_BUTTON]))
	graph.add_transition(contexts_aaam.THEMES, contexts_aaam.SETTINGS, (HMIActionType.click_element, [xpaths_aaam.SETTINGS_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG, contexts_aaam.SETTINGS, (HMIActionType.click_element, [xpaths_aaam.SETTINGS_BUTTON]))
	graph.add_transition(contexts_aaam.SETTINGS, contexts_aaam.THEMES, (HMIActionType.click_element, [xpaths_aaam.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_aaam.SETTINGS, contexts_aaam.CATALOG, (HMIActionType.click_element, [xpaths_aaam.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_aaam.SETTINGS, contexts_legal.ABOUT_US, (HMIActionType.click_element_in_list, [xpaths_aaam.SETTINGS_ABOUTUS_BUTTON, xpaths_aaam.SETTINGS_RECYCLERVIEW])) #  Impressum
	graph.add_transition(contexts_aaam.SETTINGS, contexts_legal.DATA_PROTECTION_NOTES, (HMIActionType.click_element_in_list, [xpaths_aaam.SETTINGS_DATA_PROTECTION_NOTES_BUTTON, xpaths_aaam.SETTINGS_RECYCLERVIEW]))
	graph.add_transition(contexts_aaam.SETTINGS, contexts_aaam.SETTINGS_OSSN, (HMIActionType.click_element_in_list, [xpaths_aaam.SETTINGS_OSSN_BUTTON, xpaths_aaam.SETTINGS_RECYCLERVIEW]))
	graph.add_transition(contexts_aaam.SETTINGS_OSSN, contexts_aaam.SETTINGS, (HMIActionType.click_element, [xpaths_aaam.SETTINGS_BACK_BUTTON]))

	graph.add_transition(contexts_aaam.CATALOG, contexts_aaam.CATALOG_HIGHLIGHTS_MORE, (HMIActionType.click_element_in_list, [xpaths_aaam.CATALOG_HIGHLIGHTS_MORE_BUTTON, xpaths_aaam.CATALOG_LIST_CONTAINER]))
	graph.add_transition(contexts_aaam.CATALOG_HIGHLIGHTS_MORE, contexts_aaam.CATALOG, (HMIActionType.click_element, [xpaths_aaam.CATALOG_HIGHLIGHTS_BACK_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_HIGHLIGHTS_MORE, contexts_aaam.THEMES, (HMIActionType.click_element, [xpaths_aaam.THEMES_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_HIGHLIGHTS_MORE, contexts_aaam.CATALOG_HIGHLIGHTS_MORE_WHALE, (HMIActionType.click_element, [xpaths_aaam.CATALOG_HIGHLIGHTS_MORE_WHALE_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_HIGHLIGHTS_MORE_WHALE, contexts_aaam.CATALOG_HIGHLIGHTS_MORE, (HMIActionType.click_element, [xpaths_aaam.CATALOG_HIGHLIGHTS_BACK_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_HIGHLIGHTS_MORE_WHALE, contexts_aaam.CATALOG_HIGHLIGHTS_MORE_WHALE_PREVIEW, (HMIActionType.click_element, [xpaths_aaam.CATALOG_HIGHLIGHTS_MORE_WHALE_PREVIEW_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_HIGHLIGHTS_MORE_WHALE_PREVIEW, contexts_aaam.CATALOG_HIGHLIGHTS_MORE_WHALE, (HMIActionType.click_element, [xpaths_aaam.CATALOG_HIGHLIGHTS_BACK_BUTTON]))

	graph.add_transition(contexts_aaam.CATALOG, contexts_aaam.CATALOG_AUDI, (HMIActionType.click_element_in_list, [xpaths_aaam.CATALOG_AUDI_BUTTON, xpaths_aaam.CATALOG_LIST_CONTAINER]))
	graph.add_transition(contexts_aaam.CATALOG_AUDI, contexts_aaam.CATALOG, (HMIActionType.click_element, [xpaths_aaam.CATALOG_AUDI_BACK_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_AUDI, contexts_aaam.CATALOG_AUDI_AUDISPORT_MORE, (HMIActionType.click_element, [xpaths_aaam.CATALOG_AUDI_MORE_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_AUDI_AUDISPORT_MORE, contexts_aaam.CATALOG_AUDI, (HMIActionType.click_element, [xpaths_aaam.CATALOG_AUDI_BACK_BUTTON]))

	graph.add_transition(contexts_aaam.CATALOG, contexts_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE, (HMIActionType.click_element_in_list, [xpaths_aaam.CATALOG_SEASONAL_HOLIDAYS_BUTTON, xpaths_aaam.CATALOG_LIST_CONTAINER]))
	graph.add_transition(contexts_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE, contexts_aaam.CATALOG, (HMIActionType.click_element, [xpaths_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BACK_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE, contexts_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI, (HMIActionType.click_element, [xpaths_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI, contexts_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE, (HMIActionType.click_element, [xpaths_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BACK_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI, contexts_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_PREVIEW, (HMIActionType.click_element, [xpaths_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_PREVIEW_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_PREVIEW, contexts_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI, (HMIActionType.click_element, [xpaths_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BACK_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI, contexts_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_BUY, (HMIActionType.click_element, [xpaths_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_BUY_BUTTON]))
	graph.add_transition(contexts_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_BUY, contexts_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI, (HMIActionType.click_element, [xpaths_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BACK_BUTTON]))
