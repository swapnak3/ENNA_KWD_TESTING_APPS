# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""

from enna_hcp_configuration.android.contexts import launcher as contexts_launcher
from enna_hcp_configuration.android.contexts import legal as contexts_legal
from enna_hcp_configuration.android.contexts import obb as contexts_obb
from enna_hcp_configuration.android.contexts import privacy as contexts_privacy
from enna_hcp_configuration.android import xpaths
from enna_hcp_configuration.android.xpaths import obb as xpaths_obb
from enna_hcp_configuration.android.base import HMIActionType


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_obb.MAIN, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_obb.INIT, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_obb.INIT_REQUEST, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_obb.WARNING_LAMPS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	graph.add_transition(contexts_obb.MAIN, contexts_obb.SEARCH, (HMIActionType.click_element, [xpaths_obb.SEARCH_BUTTON]))
	graph.add_transition(contexts_obb.MAIN, contexts_obb.SETTINGS, (HMIActionType.click_element, [xpaths_obb.SETTINGS_BUTTON]))
	graph.add_transition(contexts_obb.MAIN, contexts_obb.CHAPTERS, (HMIActionType.click_element_in_list, [xpaths_obb.MAIN_CHAPTERS_BUTTON, xpaths_obb.MAIN_LIST_CONTAINER]))
	graph.add_transition(contexts_obb.MAIN, contexts_obb.SUPPLEMENTS, (HMIActionType.click_element_in_list, [xpaths_obb.MAIN_SUPPLEMENTS_BUTTON, xpaths_obb.MAIN_LIST_CONTAINER]))
	graph.add_transition(contexts_obb.MAIN, contexts_obb.FAQ, (HMIActionType.click_element_in_list, [xpaths_obb.MAIN_FAQ_BUTTON, xpaths_obb.MAIN_LIST_CONTAINER]))
	graph.add_transition(contexts_obb.MAIN, contexts_obb.WARNING_LAMPS, (HMIActionType.click_element_in_list, [xpaths_obb.MAIN_WARNING_LAMPS_BUTTON, xpaths_obb.MAIN_LIST_CONTAINER]))
	graph.add_transition(contexts_obb.MAIN, contexts_obb.INDEX_SEARCH, (HMIActionType.click_element_in_list, [xpaths_obb.MAIN_INDEX_BUTTON, xpaths_obb.MAIN_LIST_CONTAINER]))
	graph.add_transition(contexts_obb.MAIN, contexts_obb.INFO, (HMIActionType.click_element_in_list, [xpaths_obb.MAIN_INFO_BUTTON, xpaths_obb.MAIN_LIST_CONTAINER]))

	graph.add_transition(contexts_obb.CHAPTERS, contexts_obb.CHAPTERS_DISPLAYS_AND_CONTROLS, (HMIActionType.click_element, [xpaths_obb.CHAPTERS_DISPLAYS_AND_CONTROLS_BUTTON]))  # Hinweg chapters -> displays and controls
	graph.add_transition(contexts_obb.CHAPTERS_DISPLAYS_AND_CONTROLS, contexts_obb.CHAPTERS, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))  # Rückweg displays and controls => chapters

	graph.add_transition(contexts_obb.CHAPTERS, contexts_obb.CHAPTERS_QUICK_REFERENCE, (HMIActionType.click_element, [xpaths_obb.CHAPTERS_QUICK_REFERENCE_BUTTON]))  # Hinweg chapters → kurz und bündig
	graph.add_transition(contexts_obb.CHAPTERS_QUICK_REFERENCE, contexts_obb.CHAPTERS, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))  # Rückweg kurz und bündig → chapters

	graph.add_transition(contexts_obb.CHAPTERS_DISPLAYS_AND_CONTROLS, contexts_obb.CHAPTERS_INSTRUMENT_CLUSTER, (HMIActionType.click_element, [xpaths_obb.CHAPTERS_INSTRUMENT_CLUSTER_BUTTON]))
	graph.add_transition(contexts_obb.CHAPTERS_INSTRUMENT_CLUSTER, contexts_obb.CHAPTERS_DISPLAYS_AND_CONTROLS, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))

	graph.add_transition(contexts_obb.CHAPTERS_INSTRUMENT_CLUSTER, contexts_obb.CHAPTERS_OVERVIEW_AND_CONTROLS, (HMIActionType.click_element, [xpaths_obb.CHAPTERS_OVERVIEW_AND_CONTROLS_BUTTON]))
	graph.add_transition(contexts_obb.CHAPTERS_OVERVIEW_AND_CONTROLS, contexts_obb.CHAPTERS_INSTRUMENT_CLUSTER, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))

	graph.add_transition(contexts_obb.CHAPTERS, contexts_obb.CHAPTERS_SETTING_OFF, (HMIActionType.click_element, [xpaths_obb.CHAPTERS_SETTING_OFF_BUTTON]))
	graph.add_transition(contexts_obb.CHAPTERS_SETTING_OFF, contexts_obb.CHAPTERS, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))

	graph.add_transition(contexts_obb.CHAPTERS_SETTING_OFF, contexts_obb.CHAPTERS_SITTING_CORRECTLY_AND_SAFELY, (HMIActionType.click_element, [xpaths_obb.CHAPTERS_SITTING_CORRECTLY_AND_SAFELY_BUTTON]))
	graph.add_transition(contexts_obb.CHAPTERS_SITTING_CORRECTLY_AND_SAFELY, contexts_obb.CHAPTERS_SETTING_OFF, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))

	graph.add_transition(contexts_obb.CHAPTERS_SITTING_CORRECTLY_AND_SAFELY, contexts_obb.CHAPTERS_FRONT_SEATS, (HMIActionType.click_element, [xpaths_obb.CHAPTERS_FRONT_SEATS_BUTTON]))
	graph.add_transition(contexts_obb.CHAPTERS_FRONT_SEATS, contexts_obb.CHAPTERS_SITTING_CORRECTLY_AND_SAFELY, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))

	graph.add_transition(contexts_obb.CHAPTERS, contexts_obb.CHAPTERS_DRIVER_ASSIST_SYSTEMS, (HMIActionType.click_element, [xpaths_obb.CHAPTERS_DRIVER_ASSIST_SYSTEMS_BUTTON]))
	graph.add_transition(contexts_obb.CHAPTERS_DRIVER_ASSIST_SYSTEMS, contexts_obb.CHAPTERS, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))

	graph.add_transition(contexts_obb.CHAPTERS_DRIVER_ASSIST_SYSTEMS, contexts_obb.CHAPTERS_COMBINED_ASSIST_FUNCTIONS, (HMIActionType.click_element, [xpaths_obb.CHAPTERS_COMBINED_ASSIST_FUNCTIONS_BUTTON]))
	graph.add_transition(contexts_obb.CHAPTERS_COMBINED_ASSIST_FUNCTIONS, contexts_obb.CHAPTERS_DRIVER_ASSIST_SYSTEMS, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))

	graph.add_transition(contexts_obb.CHAPTERS_COMBINED_ASSIST_FUNCTIONS, contexts_obb.CHAPTERS_ADAPTIVE_CRUISE_ASSIST, (HMIActionType.click_element, [xpaths_obb.CHAPTERS_ADAPTIVE_CRUISE_ASSIST_BUTTON]))
	graph.add_transition(contexts_obb.CHAPTERS_ADAPTIVE_CRUISE_ASSIST, contexts_obb.CHAPTERS_COMBINED_ASSIST_FUNCTIONS, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))

	graph.add_transition(contexts_obb.WARNING_LAMPS, contexts_obb.SPEED_ASSIST_SYSTEMS, (HMIActionType.click_element, [xpaths_obb.ADAPTIVE_CRUISE_ASSIST_ICON]))
	graph.add_transition(contexts_obb.SPEED_ASSIST_SYSTEMS, contexts_obb.WARNING_LAMPS, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))
	graph.add_transition(contexts_obb.SPEED_ASSIST_SYSTEMS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	graph.add_transition(contexts_obb.CHAPTERS, contexts_obb.MAIN, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))
	graph.add_transition(contexts_obb.FAQ, contexts_obb.MAIN, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))
	graph.add_transition(contexts_obb.SUPPLEMENTS, contexts_obb.MAIN, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))
	graph.add_transition(contexts_obb.WARNING_LAMPS, contexts_obb.MAIN, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))
	graph.add_transition(contexts_obb.INFO, contexts_obb.MAIN, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))
	graph.add_transition(contexts_obb.INDEX_SEARCH, contexts_obb.MAIN, (HMIActionType.click_element, [xpaths_obb.HOME_BUTTON]))
	graph.add_transition(contexts_obb.SEARCH, contexts_obb.MAIN, (HMIActionType.click_element, [xpaths_obb.HOME_BUTTON]))
	graph.add_transition(contexts_obb.SEARCH, contexts_obb.SEARCH_RESULTS, (HMIActionType.click_coordinates, [1645, 760]))
	graph.add_transition(contexts_obb.SEARCH_RESULTS, contexts_obb.MAIN, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))

	graph.add_transition(contexts_obb.SETTINGS, contexts_obb.MAIN, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))
	graph.add_transition(contexts_obb.SETTINGS, contexts_obb.SEARCH, (HMIActionType.click_element, [xpaths_obb.SEARCH_BUTTON]))
	graph.add_transition(contexts_obb.SETTINGS, contexts_obb.SETTINGS_CHANGE_LANGUAGE, (HMIActionType.click_element, [xpaths_obb.SETTINGS_CHANGE_LANGUAGE_BUTTON]))
	graph.add_transition(contexts_obb.SETTINGS, contexts_legal.ABOUT_US, (HMIActionType.click_element, [xpaths_obb.SETTINGS_ABOUT_US_BUTTON]))
	graph.add_transition(contexts_obb.SETTINGS, contexts_legal.DATA_PROTECTION_NOTES, (HMIActionType.click_element, [xpaths_obb.SETTINGS_DATA_PROTECTION_NOTES_BUTTON]))
	graph.add_transition(contexts_obb.SETTINGS, contexts_obb.SETTINGS_OSSN, (HMIActionType.click_element, [xpaths_obb.SETTINGS_OSSN_BUTTON]))

	graph.add_transition(contexts_obb.SEARCH, contexts_obb.SETTINGS, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))
	graph.add_transition(contexts_obb.SETTINGS_CHANGE_LANGUAGE, contexts_obb.SETTINGS, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))
	# graph.add_transition(contexts_legal.ABOUT_US, contexts_obb.SETTINGS, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))  # steht im legal
	# graph.add_transition(contexts_legal.DATA_PROTECTION_NOTES, contexts_obb.SETTINGS, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))  # steht im legal
	graph.add_transition(contexts_obb.SETTINGS_OSSN, contexts_obb.SETTINGS, (HMIActionType.click_element, [xpaths_obb.BACK_BUTTON]))

	graph.add_transition(contexts_obb.PRIVACY_MODE, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_obb.PRIVACY_MODE, contexts_privacy.PRIVACY_SETTINGS, (HMIActionType.click_element, [xpaths_obb.PRIVACY_MODE_BUTTON]))
