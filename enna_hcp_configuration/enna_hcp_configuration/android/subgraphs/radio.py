# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""

from enna_hcp_configuration.android import xpaths
from enna_hcp_configuration.android.xpaths import radio as xpaths_radio
from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher, radio as contexts_radio

# pylint: disable=line-too-long

def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	# From init
	graph.add_transition(contexts_radio.INIT, contexts_radio.MAIN_DAB_FM, (HMIActionType.click_element, [xpaths_radio.MAIN_DAB_FM_BUTTON]))
	graph.add_transition(contexts_radio.INIT, contexts_radio.SETTINGS, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BUTTON]))

	# From radio
	graph.add_transition(contexts_radio.INIT, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_AM, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_FAVORITES, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_DAB_FM, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_LAST_STATIONS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_radio.SETTINGS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	# From Last Stations
	graph.add_transition(contexts_radio.MAIN_LAST_STATIONS, contexts_radio.MAIN_AM, (HMIActionType.click_element, [xpaths_radio.MAIN_AM_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_LAST_STATIONS, contexts_radio.MAIN_DAB_FM, (HMIActionType.click_element, [xpaths_radio.MAIN_DAB_FM_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_LAST_STATIONS, contexts_radio.MAIN_FAVORITES, (HMIActionType.click_element, [xpaths_radio.MAIN_FAVORITES_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_LAST_STATIONS, contexts_radio.SETTINGS, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_LAST_STATIONS, contexts_radio.SEARCH, (HMIActionType.click_element, [xpaths_radio.SEARCH_BUTTON]))

	# From Favorites
	graph.add_transition(contexts_radio.MAIN_FAVORITES, contexts_radio.MAIN_AM, (HMIActionType.click_element, [xpaths_radio.MAIN_AM_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_FAVORITES, contexts_radio.MAIN_DAB_FM, (HMIActionType.click_element, [xpaths_radio.MAIN_DAB_FM_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_FAVORITES, contexts_radio.MAIN_LAST_STATIONS, (HMIActionType.click_element, [xpaths_radio.MAIN_LAST_STATIONS_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_FAVORITES, contexts_radio.SETTINGS, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_FAVORITES, contexts_radio.SEARCH, (HMIActionType.click_element, [xpaths_radio.SEARCH_BUTTON]))

	# From DAB/FM
	graph.add_transition(contexts_radio.MAIN_DAB_FM, contexts_radio.MAIN_AM, (HMIActionType.click_element, [xpaths_radio.MAIN_AM_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_DAB_FM, contexts_radio.MAIN_FAVORITES, (HMIActionType.click_element, [xpaths_radio.MAIN_FAVORITES_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_DAB_FM, contexts_radio.MAIN_LAST_STATIONS, (HMIActionType.click_element, [xpaths_radio.MAIN_LAST_STATIONS_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_DAB_FM, contexts_launcher.CHANGE_SOURCE, (HMIActionType.click_element, [xpaths_radio.CHANGESOURCE_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_DAB_FM, contexts_radio.NOW_PLAYING, (HMIActionType.click_element, [xpaths_radio.MAIN_MINI_PLAYER]))
	graph.add_transition(contexts_radio.MAIN_DAB_FM, contexts_radio.SETTINGS, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_DAB_FM, contexts_radio.SEARCH, (HMIActionType.click_element, [xpaths_radio.SEARCH_BUTTON]))

	# From AM
	graph.add_transition(contexts_radio.MAIN_AM, contexts_radio.MAIN_DAB_FM, (HMIActionType.click_element, [xpaths_radio.MAIN_DAB_FM_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_AM, contexts_radio.MAIN_FAVORITES, (HMIActionType.click_element, [xpaths_radio.MAIN_FAVORITES_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_AM, contexts_radio.MAIN_LAST_STATIONS, (HMIActionType.click_element, [xpaths_radio.MAIN_LAST_STATIONS_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_AM, contexts_radio.SETTINGS, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BUTTON]))
	graph.add_transition(contexts_radio.MAIN_AM, contexts_radio.SEARCH, (HMIActionType.click_element, [xpaths_radio.SEARCH_BUTTON]))

	# From NPS
	graph.add_transition(contexts_radio.NOW_PLAYING, contexts_radio.MAIN_DAB_FM, (HMIActionType.click_element, [xpaths_radio.NOW_PLAYING_MINIMIZE]))
	graph.add_transition(contexts_radio.NOW_PLAYING, contexts_radio.MAIN_FAVORITES, (HMIActionType.click_element, [xpaths_radio.NOW_PLAYING_MINIMIZE]))
	graph.add_transition(contexts_radio.NOW_PLAYING, contexts_radio.MAIN_LAST_STATIONS, (HMIActionType.click_element, [xpaths_radio.NOW_PLAYING_MINIMIZE]))
	graph.add_transition(contexts_radio.NOW_PLAYING, contexts_radio.MAIN_AM, (HMIActionType.click_element, [xpaths_radio.NOW_PLAYING_MINIMIZE]))

	# From settings
	graph.add_transition(contexts_radio.SETTINGS, contexts_radio.MAIN_DAB_FM, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BACK]))
	graph.add_transition(contexts_radio.SETTINGS, contexts_radio.MAIN_FAVORITES, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BACK]))
	graph.add_transition(contexts_radio.SETTINGS, contexts_radio.MAIN_LAST_STATIONS, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BACK]))
	graph.add_transition(contexts_radio.SETTINGS, contexts_radio.BRG, (HMIActionType.click_element_in_list, [xpaths_radio.SETTINGS_BROADCAST_RADIO_GEM, xpaths_radio.SETTINGS_LIST]))
	graph.add_transition(contexts_radio.SETTINGS, contexts_radio.MAIN_AM, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BACK]))
	graph.add_transition(contexts_radio.SETTINGS, contexts_radio.SETTINGS_PROVIDER_INFO, (HMIActionType.click_element_in_list, [xpaths_radio.SETTINGS_PROVIDER_INFO_BUTTON, xpaths_radio.SETTINGS_LIST]))
	graph.add_transition(contexts_radio.SETTINGS, contexts_radio.SETTINGS_OSD, (HMIActionType.click_element_in_list, [xpaths_radio.SETTINGS_OSD_BUTTON, xpaths_radio.SETTINGS_LIST]))
	graph.add_transition(contexts_radio.SETTINGS, contexts_radio.SETTINGS_CUSTOM_BL_GEMS, (HMIActionType.click_element_in_list, [xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_BUTTON, xpaths_radio.SETTINGS_LIST]))
	graph.add_transition(contexts_radio.SETTINGS_CUSTOM_BL_GEMS, contexts_radio.SETTINGS_CUSTOM_BL_GEMS_GENERAL, (HMIActionType.click_element_in_list, [xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_GENERAL_BUTTON, xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_LIST]))
	graph.add_transition(contexts_radio.SETTINGS_CUSTOM_BL_GEMS, contexts_radio.SETTINGS_CUSTOM_BL_GEMS_DOMAIN_ANNOUNCEMENT, (HMIActionType.click_element_in_list, [xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_DOMAIN_ANNOUNCEMENT_BUTTON, xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_LIST]))
	# and back
	graph.add_transition(contexts_radio.SETTINGS_PROVIDER_INFO, contexts_radio.SETTINGS, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BACK]))
	graph.add_transition(contexts_radio.SETTINGS_OSD, contexts_radio.SETTINGS, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BACK]))
	graph.add_transition(contexts_radio.SETTINGS_CUSTOM_BL_GEMS, contexts_radio.SETTINGS, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BACK]))
	graph.add_transition(contexts_radio.SETTINGS_CUSTOM_BL_GEMS_GENERAL, contexts_radio.SETTINGS_CUSTOM_BL_GEMS, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BACK]))
	graph.add_transition(contexts_radio.SETTINGS_CUSTOM_BL_GEMS_DOMAIN_ANNOUNCEMENT, contexts_radio.SETTINGS_CUSTOM_BL_GEMS, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BACK]))

	# From search
	graph.add_transition(contexts_radio.SEARCH, contexts_radio.MAIN_DAB_FM, (HMIActionType.click_element, [xpaths_radio.SEARCH_CLOSE_BUTTON]))
	graph.add_transition(contexts_radio.SEARCH, contexts_radio.MAIN_FAVORITES, (HMIActionType.click_element, [xpaths_radio.SEARCH_CLOSE_BUTTON]))
	graph.add_transition(contexts_radio.SEARCH, contexts_radio.MAIN_LAST_STATIONS, (HMIActionType.click_element, [xpaths_radio.SEARCH_CLOSE_BUTTON]))
	graph.add_transition(contexts_radio.SEARCH, contexts_radio.MAIN_AM, (HMIActionType.click_element, [xpaths_radio.SEARCH_CLOSE_BUTTON]))

	# History
	graph.add_transition(contexts_radio.HISTORY, contexts_radio.NOW_PLAYING, (HMIActionType.click_element, [xpaths_radio.RADIOTEXT_HISTORY_CLOSE_BUTTON]))
	graph.add_transition(contexts_radio.NOW_PLAYING, contexts_radio.HISTORY, (HMIActionType.click_element, [xpaths_radio.NOW_PLAY_OPEN_HISTORY_BUTTON]))

	# From Broadcast Radio GEM
	graph.add_transition(contexts_radio.BRG, contexts_radio.SETTINGS, (HMIActionType.click_element, [xpaths_radio.SETTINGS_BACK]))
