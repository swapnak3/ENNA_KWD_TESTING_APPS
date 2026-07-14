# -*- coding: utf-8 -*-
"""Analyzer for the media app."""

from enna_hcp_configuration.android.xpaths import media
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathBlacklistWhitelistDetectorExtension, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import Element

POPUP_MISSING_PERMISSION = Element("POPUP_missing_permission", ElementByXPathDetectorExtension([media.POPUP_MISSING_PERMISSION_DIALOG]))
POPUP_STORAGE_PERMISSION = Element("POPUP_storage_permission", ElementByXPathDetectorExtension([media.POPUP_STORAGE_PERMISSION_DIALOG]))

MAIN = Element("main", ElementByXPathDetectorExtension([media.MAIN_TITLE]))
SEARCH = Element("search", ElementByXPathDetectorExtension([media.SEARCH_X, media.SEARCH_ENTRY_FIELD_TITLE]))
SETTINGS = Element("settings", ElementByXPathDetectorExtension([media.SETTINGS_TOP_BAR_TITLE]))
SWITCHAPPS = Element("switchapps", ElementByXPathDetectorExtension([media.APPS_SCREEN_CONTENT_TITLE]))
RECENTS = Element("recents", ElementByXPathDetectorExtension([media.RECENTS_TITLE]))
ARTISTS = Element("artists", ElementByXPathDetectorExtension([media.ARTISTS_TITLE]))
ALBUMS = Element("albums", ElementByXPathDetectorExtension([media.ALBUMS_TITLE]))
TRACKS = Element("tracks", ElementByXPathDetectorExtension([media.TRACKS_TITLE]))
PLAYLISTS = Element("playlists", ElementByXPathDetectorExtension([media.PLAYLISTS_TITLE]))
GENRES = Element("genres", ElementByXPathDetectorExtension([media.GENRES_TITLE]))
VIDEOS = Element("videos", ElementByXPathDetectorExtension([media.VIDEOS_TITLE]))
FOLDERS = Element("folders", ElementByXPathDetectorExtension([media.FOLDERS_TITLE]))
ALL = Element("all", ElementByXPathDetectorExtension([media.ALL_TITLE]))
NOW_PLAYING = Element("now_playing", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[media.NP_TITLE, media.NP_SEEK_BAR_TITLE], must_not_exist=[media.NP_VIDEO_SS_FS_TITLE]))
NOW_PLAYING_VIDEO_SS = Element("now_playing_video_ss", ElementByXPathDetectorExtension([media.NP_VIDEO_SS_INTERACTION_FOREGROUND_TITLE, media.NP_VIDEO_SS_FS_TITLE]))
NOW_PLAYING_VIDEO_FS = Element("now_playing_video_fs", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[media.NP_VIDEO_SS_FS_TITLE], must_not_exist=[media.NP_VIDEO_SS_INTERACTION_FOREGROUND_TITLE]))
PLAYLIST = Element("playlist", ElementByXPathDetectorExtension([media.GENERIC_PLAYLIST_TITLE]))
ERROR = Element("error", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[media.ERROR_TITLE], must_not_exist=[media.PERMISSION_REQUEST_TEXT_TITLE]))
PERMISSION_REQUEST = Element("permission_request", ElementByXPathDetectorExtension([media.PERMISSION_REQUEST_TEXT_TITLE]))
FORMATS = Element("formats", ElementByXPathDetectorExtension([media.FORMATS_TITLE]))

CONTEXT = ContextAnalyzer("media", AppPackageDetectorExtension(["com.android.car.media", "com.harman.mediacoreservice"]))
CONTEXT.add_elements_from_module(globals())
