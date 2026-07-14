# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""

from enna_hcp_configuration.android import xpaths
from enna_hcp_configuration.android.xpaths import navigation as xpaths_navigation
from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher, navigation as contexts_navigation, aem as contexts_aem


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_navigation.INIT, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_navigation.NOT_ACTIVATED, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_navigation.MAIN, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_navigation.MAIN, contexts_navigation.SETTINGS, (HMIActionType.click_element, [xpaths_navigation.SETTING_BUTTON]))
	graph.add_transition(contexts_navigation.SETTINGS, contexts_navigation.SETTINGS_CHARGING, (HMIActionType.click_element_in_list, [xpaths_navigation.SETTING_CHARGING_BUTTON, xpaths_navigation.SETTING_LIST]))
	graph.add_transition(contexts_navigation.SETTINGS_CHARGING, contexts_navigation.SETTINGS, (HMIActionType.click_element, [xpaths_navigation.SETTING_CHARGING_BACK_BUTTON]))
	graph.add_transition(contexts_navigation.SETTINGS, contexts_navigation.SETTINGS_COUNTRYINFORMATION, (HMIActionType.click_element_in_list, [xpaths_navigation.SETTING_COUNTRY_INFORMATION_BUTTON, xpaths_navigation.SETTING_LIST]))
	graph.add_transition(contexts_navigation.SETTINGS_COUNTRYINFORMATION, contexts_navigation.SETTINGS, (HMIActionType.click_element, [xpaths_navigation.SETTING_COUNTRY_INFORMATION_BACK_BUTTON]))
	graph.add_transition(contexts_navigation.MAIN, contexts_navigation.SEARCH, (HMIActionType.click_element, [xpaths_navigation.SEARCH_BUTTON]))
	graph.add_transition(contexts_navigation.SEARCH, contexts_navigation.MAIN, (HMIActionType.click_element, [xpaths_navigation.SEARCH_CLOSE]))
	graph.add_transition(contexts_navigation.SEARCH_DETAILS, contexts_navigation.SEARCH, (HMIActionType.click_element, [xpaths_navigation.SEARCH_CLOSE]))
	graph.add_transition(contexts_navigation.SEARCH, contexts_navigation.GUIDANCE, (HMIActionType.click_element, [xpaths_navigation.SEARCH_CLOSE]))
	graph.add_transition(contexts_navigation.SEARCH_DETAILS, contexts_navigation.GUIDANCE, (HMIActionType.click_element, [xpaths_navigation.SEARCH_CLOSE]))

	graph.add_transition(contexts_navigation.SEARCH, contexts_navigation.SEARCH_CATEGORIES, (HMIActionType.click_element, [xpaths_navigation.SEARCH_CATEGORIES_BUTTON]))
	graph.add_transition(contexts_navigation.SEARCH_CATEGORIES, contexts_navigation.SEARCH, (HMIActionType.click_element, [xpaths_navigation.SEARCH_CATEGORIES_CLOSE_BUTTON]))

	graph.add_transition(contexts_navigation.SETTINGS, contexts_navigation.MAIN, (HMIActionType.click_element, [xpaths_navigation.SETTING_CLOSE_BUTTON]))
	graph.add_transition(contexts_navigation.SETTINGS, contexts_navigation.GUIDANCE, (HMIActionType.click_element, [xpaths_navigation.SETTING_CLOSE_BUTTON]))
	graph.add_transition(contexts_navigation.SETTINGS, contexts_navigation.SETTINGS_COUNTRYINFORMATION, (HMIActionType.click_element_in_list, [xpaths_navigation.SETTING_COUNTRY_INFORMATION_BUTTON, xpaths_navigation.SETTING_LIST]))
	graph.add_transition(contexts_navigation.SETTINGS, contexts_navigation.SETTINGS_NAVIINFORMATION, (HMIActionType.click_element_in_list, [xpaths_navigation.SETTING_NAVI_INFORMATION_BUTTON, xpaths_navigation.SETTING_LIST]))

	graph.add_transition(contexts_navigation.GEM, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_navigation.GEM, contexts_aem.MAIN, (HMIActionType.click_element, [xpaths_navigation.GEM_CLOSE_BUTTON]))
	graph.add_transition(contexts_navigation.GEM, contexts_navigation.NAVADAPTER, (HMIActionType.click_element_in_list, [xpaths_navigation.GEM_NAVADAPTER_BUTTON, xpaths_navigation.GEM_LIST_HORIZONTAL]))
	graph.add_transition(contexts_navigation.NAVADAPTER, contexts_navigation.ESOMOCK, (HMIActionType.click_element_in_list, [xpaths_navigation.GEM_NAVADAPTER_DEMO_MOCK_BUTTON, xpaths_navigation.GEM_NAVADAPTER_LIST]))
	graph.add_transition(contexts_navigation.ESOMOCK, contexts_aem.MAIN, (HMIActionType.click_element, [xpaths_navigation.GEM_CLOSE_BUTTON]))
	graph.add_transition(contexts_navigation.NAVADAPTER, contexts_navigation.NAVADAPTER_MOCK, (HMIActionType.click_element_in_list, [xpaths_navigation.GEM_NAVADAPTER_MOCK_BUTTON, xpaths_navigation.GEM_NAVADAPTER_LIST]))
	graph.add_transition(contexts_navigation.NAVADAPTER_MOCK, contexts_aem.MAIN, (HMIActionType.click_element, [xpaths_navigation.GEM_CLOSE_BUTTON]))
	graph.add_transition(contexts_navigation.GUIDANCE, contexts_navigation.MAIN, (HMIActionType.click_element, [xpaths_navigation.ABORT_ROUTE_GUIDANCE_BUTTON_TITLE]))
	graph.add_transition(contexts_navigation.GUIDANCE, contexts_navigation.SEARCH, (HMIActionType.click_element, [xpaths_navigation.SEARCH_BUTTON]))
	graph.add_transition(contexts_navigation.GUIDANCE, contexts_navigation.TOURPLAN, (HMIActionType.click_element, [xpaths_navigation.ROUTE_INFO_DESTINATION_FLAG]))
	graph.add_transition(contexts_navigation.GUIDANCE, contexts_navigation.SETTINGS, (HMIActionType.click_element, [xpaths_navigation.SETTING_BUTTON]))
	graph.add_transition(contexts_navigation.TOURPLAN, contexts_navigation.GUIDANCE, (HMIActionType.click_element, [xpaths_navigation.ROUTE_TOUR_PLAN_CLOSE_BUTTON]))
	graph.add_transition(contexts_navigation.MAIN, contexts_navigation.SEARCH, (HMIActionType.click_element, [xpaths_navigation.SEARCH_BUTTON]))  # Hinweg main -> search
	graph.add_transition(contexts_navigation.SEARCH, contexts_navigation.SEARCH_CATEGORIES, (HMIActionType.click_element, [xpaths_navigation.SEARCH_CATEGORIES_BUTTON]))  # Hinweg search -> search_categories
	graph.add_transition(contexts_navigation.SEARCH_CATEGORIES, contexts_navigation.SEARCH, (HMIActionType.click_element, [xpaths_navigation.SEARCH_CATEGORIES_CLOSE_BUTTON]))  # Rückweg search_categories -> search
	graph.add_transition(contexts_navigation.SEARCH, contexts_navigation.MAIN, (HMIActionType.click_element, [xpaths_navigation.SEARCH_CLOSE]))  # Rückweg search -> main

	graph.add_transition(contexts_navigation.SETTINGS_COUNTRYINFORMATION, contexts_navigation.SETTINGS, (HMIActionType.click_element, [xpaths_navigation.SETTING_COUNTRY_INFORMATION_BACK_BUTTON]))
	graph.add_transition(contexts_navigation.SETTINGS_COUNTRYINFORMATION, contexts_navigation.MAIN, (HMIActionType.click_element, [xpaths_navigation.SETTING_CLOSE_BUTTON]))
	graph.add_transition(contexts_navigation.SETTINGS_COUNTRYINFORMATION, contexts_navigation.GUIDANCE, (HMIActionType.click_element, [xpaths_navigation.SETTING_CLOSE_BUTTON]))
	graph.add_transition(contexts_navigation.TRAFFIC_DETAILS, contexts_navigation.MAIN, (HMIActionType.click_element, [xpaths_navigation.DETAILS_SCREEN_CLOSE_BUTTON]))
	graph.add_transition(contexts_navigation.DESTINATION_DETAILS, contexts_navigation.MAIN, (HMIActionType.click_element, [xpaths_navigation.DETAILS_SCREEN_CLOSE_BUTTON]))
	graph.add_transition(contexts_navigation.POI_STACK, contexts_navigation.MAIN, (HMIActionType.click_element, [xpaths_navigation.POI_STACK_CLOSE_BUTTON]))
	graph.add_transition(contexts_navigation.ALTERNATIVE_ROUTES, contexts_navigation.MAIN, (HMIActionType.click_element, [xpaths_navigation.ALTERNATIVE_ROUTES_CLOSE_BUTTON_TITLE]))

	graph.add_transition(contexts_navigation.SETTINGS_NAVIINFORMATION, contexts_navigation.MAIN, (HMIActionType.click_element, [xpaths_navigation.SETTING_CLOSE_BUTTON]))
	graph.add_transition(contexts_navigation.SETTINGS_NAVIINFORMATION, contexts_navigation.GUIDANCE, (HMIActionType.click_element, [xpaths_navigation.SETTING_CLOSE_BUTTON]))
	graph.add_transition(contexts_navigation.SETTINGS_NAVIINFORMATION, contexts_navigation.SETTINGS, (HMIActionType.click_element, [xpaths_navigation.SETTING_NAVI_INFORMATION_BACK_BUTTON]))
