# -*- coding: utf-8 -*-
# pylint: disable=too-many-statements
"""Module contains transitions for a sub graph of the android HMI."""

from enna_hcp_configuration.android import xpaths
from enna_hcp_configuration.android.xpaths import media as xpaths_media
from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher, media as contexts_media


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	# From contexts_media.MAIN:
	graph.add_transition(contexts_media.MAIN, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_media.MAIN, contexts_media.SEARCH, (HMIActionType.click_element, [xpaths_media.SEARCH_BUTTON]))
	graph.add_transition(contexts_media.MAIN, contexts_media.SETTINGS, (HMIActionType.click_element, [xpaths_media.SETTINGS_BUTTON]))
	graph.add_transition(contexts_media.MAIN, contexts_media.SWITCHAPPS, (HMIActionType.click_element, [xpaths_media.SWITCHAPPS_BUTTON]))
	graph.add_transition(contexts_media.MAIN, contexts_media.RECENTS, (HMIActionType.click_element_in_list, [xpaths_media.MAIN_RECENTS_BUTTON, xpaths_media.GENERIC_LIST]))
	graph.add_transition(contexts_media.MAIN, contexts_media.ARTISTS, (HMIActionType.click_element_in_list, [xpaths_media.MAIN_ARTISTS_BUTTON, xpaths_media.GENERIC_LIST]))
	graph.add_transition(contexts_media.MAIN, contexts_media.ALBUMS, (HMIActionType.click_element_in_list, [xpaths_media.MAIN_ALBUMS_BUTTON, xpaths_media.GENERIC_LIST]))
	graph.add_transition(contexts_media.MAIN, contexts_media.TRACKS, (HMIActionType.click_element_in_list, [xpaths_media.MAIN_TRACKS_BUTTON, xpaths_media.GENERIC_LIST]))
	graph.add_transition(contexts_media.MAIN, contexts_media.PLAYLISTS, (HMIActionType.click_element_in_list, [xpaths_media.MAIN_PLAYLISTS_BUTTON, xpaths_media.GENERIC_LIST]))
	graph.add_transition(contexts_media.MAIN, contexts_media.GENRES, (HMIActionType.click_element_in_list, [xpaths_media.MAIN_GENRES_BUTTON, xpaths_media.GENERIC_LIST]))
	graph.add_transition(contexts_media.MAIN, contexts_media.VIDEOS, (HMIActionType.click_element_in_list, [xpaths_media.MAIN_VIDEOS_BUTTON, xpaths_media.GENERIC_LIST]))
	graph.add_transition(contexts_media.MAIN, contexts_media.FOLDERS, (HMIActionType.click_element_in_list, [xpaths_media.MAIN_FOLDERS_BUTTON, xpaths_media.GENERIC_LIST]))

	# From contexts_media.SEARCH
	graph.add_transition(contexts_media.SEARCH, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_media.SEARCH, contexts_media.MAIN, (HMIActionType.click_element, [xpaths_media.SEARCH_X]))
	graph.add_transition(contexts_media.SEARCH, contexts_media.RECENTS, (HMIActionType.click_element, [xpaths_media.SEARCH_X]))
	graph.add_transition(contexts_media.SEARCH, contexts_media.ARTISTS, (HMIActionType.click_element, [xpaths_media.SEARCH_X]))
	graph.add_transition(contexts_media.SEARCH, contexts_media.ALBUMS, (HMIActionType.click_element, [xpaths_media.SEARCH_X]))
	graph.add_transition(contexts_media.SEARCH, contexts_media.TRACKS, (HMIActionType.click_element, [xpaths_media.SEARCH_X]))
	graph.add_transition(contexts_media.SEARCH, contexts_media.PLAYLISTS, (HMIActionType.click_element, [xpaths_media.SEARCH_X]))
	graph.add_transition(contexts_media.SEARCH, contexts_media.GENRES, (HMIActionType.click_element, [xpaths_media.SEARCH_X]))
	graph.add_transition(contexts_media.SEARCH, contexts_media.VIDEOS, (HMIActionType.click_element, [xpaths_media.SEARCH_X]))
	graph.add_transition(contexts_media.SEARCH, contexts_media.FOLDERS, (HMIActionType.click_element, [xpaths_media.SEARCH_X]))

	# From contexts_media.RESENTS
	graph.add_transition(contexts_media.RECENTS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_media.RECENTS, contexts_media.MAIN, (HMIActionType.click_element, [xpaths_media.BACK_BUTTON]))
	graph.add_transition(contexts_media.RECENTS, contexts_media.SEARCH, (HMIActionType.click_element, [xpaths_media.SEARCH_BUTTON]))
	graph.add_transition(contexts_media.RECENTS, contexts_media.SETTINGS, (HMIActionType.click_element, [xpaths_media.SETTINGS_BUTTON]))
	graph.add_transition(contexts_media.RECENTS, contexts_media.SWITCHAPPS, (HMIActionType.click_element, [xpaths_media.SWITCHAPPS_BUTTON]))
	graph.add_transition(contexts_media.RECENTS, contexts_media.NOW_PLAYING, (HMIActionType.click_element, [xpaths_media.NPS_MINIMIZED]))

	# From contexts_media.ARTISTS
	graph.add_transition(contexts_media.ARTISTS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_media.ARTISTS, contexts_media.MAIN, (HMIActionType.click_element, [xpaths_media.BACK_BUTTON]))
	graph.add_transition(contexts_media.ARTISTS, contexts_media.SEARCH, (HMIActionType.click_element, [xpaths_media.SEARCH_BUTTON]))
	graph.add_transition(contexts_media.ARTISTS, contexts_media.SETTINGS, (HMIActionType.click_element, [xpaths_media.SETTINGS_BUTTON]))
	graph.add_transition(contexts_media.ARTISTS, contexts_media.SWITCHAPPS, (HMIActionType.click_element, [xpaths_media.SWITCHAPPS_BUTTON]))
	graph.add_transition(contexts_media.ARTISTS, contexts_media.NOW_PLAYING, (HMIActionType.click_element, [xpaths_media.NPS_MINIMIZED]))

	# From contexts_media.ALBUMS
	graph.add_transition(contexts_media.ALBUMS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_media.ALBUMS, contexts_media.MAIN, (HMIActionType.click_element, [xpaths_media.BACK_BUTTON]))
	graph.add_transition(contexts_media.ALBUMS, contexts_media.SEARCH, (HMIActionType.click_element, [xpaths_media.SEARCH_BUTTON]))
	graph.add_transition(contexts_media.ALBUMS, contexts_media.SETTINGS, (HMIActionType.click_element, [xpaths_media.SETTINGS_BUTTON]))
	graph.add_transition(contexts_media.ALBUMS, contexts_media.SWITCHAPPS, (HMIActionType.click_element, [xpaths_media.SWITCHAPPS_BUTTON]))
	graph.add_transition(contexts_media.ALBUMS, contexts_media.NOW_PLAYING, (HMIActionType.click_element, [xpaths_media.NPS_MINIMIZED]))

	# From contexts_media.TRACKS
	graph.add_transition(contexts_media.TRACKS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_media.TRACKS, contexts_media.MAIN, (HMIActionType.click_element, [xpaths_media.BACK_BUTTON]))
	graph.add_transition(contexts_media.TRACKS, contexts_media.SEARCH, (HMIActionType.click_element, [xpaths_media.SEARCH_BUTTON]))
	graph.add_transition(contexts_media.TRACKS, contexts_media.SETTINGS, (HMIActionType.click_element, [xpaths_media.SETTINGS_BUTTON]))
	graph.add_transition(contexts_media.TRACKS, contexts_media.SWITCHAPPS, (HMIActionType.click_element, [xpaths_media.SWITCHAPPS_BUTTON]))
	graph.add_transition(contexts_media.TRACKS, contexts_media.NOW_PLAYING, (HMIActionType.click_element, [xpaths_media.NPS_MINIMIZED]))

	# From contexts_media.PLAYLISTS
	graph.add_transition(contexts_media.PLAYLISTS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_media.PLAYLISTS, contexts_media.MAIN, (HMIActionType.click_element, [xpaths_media.BACK_BUTTON]))
	graph.add_transition(contexts_media.PLAYLISTS, contexts_media.SEARCH, (HMIActionType.click_element, [xpaths_media.SEARCH_BUTTON]))
	graph.add_transition(contexts_media.PLAYLISTS, contexts_media.SETTINGS, (HMIActionType.click_element, [xpaths_media.SETTINGS_BUTTON]))
	graph.add_transition(contexts_media.PLAYLISTS, contexts_media.SWITCHAPPS, (HMIActionType.click_element, [xpaths_media.SWITCHAPPS_BUTTON]))
	graph.add_transition(contexts_media.PLAYLISTS, contexts_media.NOW_PLAYING, (HMIActionType.click_element, [xpaths_media.NPS_MINIMIZED]))

	# From contexts_media.GENRES
	graph.add_transition(contexts_media.GENRES, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_media.GENRES, contexts_media.MAIN, (HMIActionType.click_element, [xpaths_media.BACK_BUTTON]))
	graph.add_transition(contexts_media.GENRES, contexts_media.SEARCH, (HMIActionType.click_element, [xpaths_media.SEARCH_BUTTON]))
	graph.add_transition(contexts_media.GENRES, contexts_media.SETTINGS, (HMIActionType.click_element, [xpaths_media.SETTINGS_BUTTON]))
	graph.add_transition(contexts_media.GENRES, contexts_media.SWITCHAPPS, (HMIActionType.click_element, [xpaths_media.SWITCHAPPS_BUTTON]))
	graph.add_transition(contexts_media.GENRES, contexts_media.NOW_PLAYING, (HMIActionType.click_element, [xpaths_media.NPS_MINIMIZED]))

	# From contexts_media.VIDEOS
	graph.add_transition(contexts_media.VIDEOS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_media.VIDEOS, contexts_media.MAIN, (HMIActionType.click_element, [xpaths_media.BACK_BUTTON]))
	graph.add_transition(contexts_media.VIDEOS, contexts_media.SEARCH, (HMIActionType.click_element, [xpaths_media.SEARCH_BUTTON]))
	graph.add_transition(contexts_media.VIDEOS, contexts_media.SETTINGS, (HMIActionType.click_element, [xpaths_media.SETTINGS_BUTTON]))
	graph.add_transition(contexts_media.VIDEOS, contexts_media.SWITCHAPPS, (HMIActionType.click_element, [xpaths_media.SWITCHAPPS_BUTTON]))
	graph.add_transition(contexts_media.VIDEOS, contexts_media.NOW_PLAYING, (HMIActionType.click_element, [xpaths_media.NPS_MINIMIZED]))

	# From contexts_media.FOLDERS
	graph.add_transition(contexts_media.FOLDERS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_media.FOLDERS, contexts_media.MAIN, (HMIActionType.click_element, [xpaths_media.BACK_BUTTON]))
	graph.add_transition(contexts_media.FOLDERS, contexts_media.SEARCH, (HMIActionType.click_element, [xpaths_media.SEARCH_BUTTON]))
	graph.add_transition(contexts_media.FOLDERS, contexts_media.SETTINGS, (HMIActionType.click_element, [xpaths_media.SETTINGS_BUTTON]))
	graph.add_transition(contexts_media.FOLDERS, contexts_media.SWITCHAPPS, (HMIActionType.click_element, [xpaths_media.SWITCHAPPS_BUTTON]))
	graph.add_transition(contexts_media.FOLDERS, contexts_media.NOW_PLAYING, (HMIActionType.click_element, [xpaths_media.NPS_MINIMIZED]))
	graph.add_transition(contexts_media.FOLDERS, contexts_media.ALL, (HMIActionType.click_element_in_list, [xpaths_media.FOLDERS_ALL_BUTTON, xpaths_media.FOLDERS_LIST]))

	# From contexts_media.ALL
	graph.add_transition(contexts_media.ALL, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_media.ALL, contexts_media.SEARCH, (HMIActionType.click_element, [xpaths_media.SEARCH_BUTTON]))
	graph.add_transition(contexts_media.ALL, contexts_media.SETTINGS, (HMIActionType.click_element, [xpaths_media.SETTINGS_BUTTON]))
	graph.add_transition(contexts_media.ALL, contexts_media.SWITCHAPPS, (HMIActionType.click_element, [xpaths_media.SWITCHAPPS_BUTTON]))
	graph.add_transition(contexts_media.ALL, contexts_media.NOW_PLAYING, (HMIActionType.click_element, [xpaths_media.NPS_MINIMIZED]))
	graph.add_transition(contexts_media.ALL, contexts_media.FOLDERS, (HMIActionType.click_element, [xpaths_media.BACK_BUTTON]))

	# From contexts_media.NOW_PLAYING
	graph.add_transition(contexts_media.NOW_PLAYING, contexts_media.MAIN, (HMIActionType.click_element, [xpaths_media.NP_MINIMIZE_BUTTON]))
	graph.add_transition(contexts_media.NOW_PLAYING, contexts_media.RECENTS, (HMIActionType.click_element, [xpaths_media.NP_MINIMIZE_BUTTON]))
	graph.add_transition(contexts_media.NOW_PLAYING, contexts_media.ARTISTS, (HMIActionType.click_element, [xpaths_media.NP_MINIMIZE_BUTTON]))
	graph.add_transition(contexts_media.NOW_PLAYING, contexts_media.ALBUMS, (HMIActionType.click_element, [xpaths_media.NP_MINIMIZE_BUTTON]))
	graph.add_transition(contexts_media.NOW_PLAYING, contexts_media.TRACKS, (HMIActionType.click_element, [xpaths_media.NP_MINIMIZE_BUTTON]))
	graph.add_transition(contexts_media.NOW_PLAYING, contexts_media.PLAYLISTS, (HMIActionType.click_element, [xpaths_media.NP_MINIMIZE_BUTTON]))
	graph.add_transition(contexts_media.NOW_PLAYING, contexts_media.GENRES, (HMIActionType.click_element, [xpaths_media.NP_MINIMIZE_BUTTON]))
	graph.add_transition(contexts_media.NOW_PLAYING, contexts_media.VIDEOS, (HMIActionType.click_element, [xpaths_media.NP_MINIMIZE_BUTTON]))
	graph.add_transition(contexts_media.NOW_PLAYING, contexts_media.FOLDERS, (HMIActionType.click_element, [xpaths_media.NP_MINIMIZE_BUTTON]))
	graph.add_transition(contexts_media.NOW_PLAYING, contexts_media.PLAYLIST, (HMIActionType.click_element, [xpaths_media.NP_PLAYLIST_BUTTON]))

	# From contexts_media.PLAYLIST
	graph.add_transition(contexts_media.PLAYLIST, contexts_media.NOW_PLAYING, (HMIActionType.click_element, [xpaths_media.NP_PLAYLIST_BUTTON_SELECTED]))

	# From contexts_media.NOW_PLAYING_VIDEO_SS
	graph.add_transition(contexts_media.NOW_PLAYING_VIDEO_SS, contexts_media.PLAYLIST, (HMIActionType.click_element, [xpaths_media.NP_VIDEO_SS_PLAYLIST_BUTTON]))
	graph.add_transition(contexts_media.NOW_PLAYING_VIDEO_SS, contexts_media.NOW_PLAYING_VIDEO_FS, (HMIActionType.click_element, [xpaths_media.NP_VIDEO_SS_FULLSCREEN_BUTTON]))

	# From contexts_media.NOW_PLAYING_VIDEO_FS
	graph.add_transition(contexts_media.NOW_PLAYING_VIDEO_FS, contexts_media.NOW_PLAYING_VIDEO_SS, (HMIActionType.click_element, [xpaths_media.NP_VIDEO_SS_FS_TITLE]))

	# From contexts_media.formats
	graph.add_transition(contexts_media.FORMATS, contexts_media.FOLDERS, (HMIActionType.click_element, [xpaths_media.BACK_BUTTON]))

	graph.add_transition(contexts_media.PERMISSION_REQUEST, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_media.ERROR, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
