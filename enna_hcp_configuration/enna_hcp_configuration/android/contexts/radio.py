# -*- coding: utf-8 -*-
"""Analyzer for the radio app."""

import enna_hcp_configuration.android.contexts
from enna_hcp_configuration.android.xpaths import radio
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import Element

# screen to intitialize
INIT = Element("init", ElementByXPathDetectorExtension([radio.INIT_TITLE]))

# screens to go
MAIN_LAST_STATIONS = Element("main_last_stations", ElementByXPathDetectorExtension([radio.MAIN_LAST_STATIONS_SELECTED_TITLE]))
MAIN_FAVORITES = Element("main_favorites", ElementByXPathDetectorExtension([radio.MAIN_FAVORITES_SELECTED_TITLE]))
MAIN_DAB_FM = Element("main_dab_fm", ElementByXPathDetectorExtension([radio.MAIN_DAB_FM_SELECTED_TITLE]))
NOW_PLAYING = Element("now_playing", ElementByXPathDetectorExtension([radio.NOW_PLAYING_TITLE]))
SEARCH = Element("search", ElementByXPathDetectorExtension([radio.SEARCH_BAR_TITLE]))
SETTINGS = Element("settings", ElementByXPathDetectorExtension([radio.SETTINGS_TITLE]))
SETTINGS_PROVIDER_INFO = Element("settings_provider_info", ElementByXPathDetectorExtension([radio.SETTINGS_PROVIDER_INFO_TITLE]))
SETTINGS_OSD = Element("settings_osd", ElementByXPathDetectorExtension([radio.SETTINGS_OSD_TITLE]))
SETTINGS_CUSTOM_BL_GEMS = Element("settings_custom_bl_gems", ElementByXPathDetectorExtension([radio.SETTINGS_CUSTOM_BL_GEMS_TITLE]))
SETTINGS_CUSTOM_BL_GEMS_GENERAL = Element("settings_custom_bl_gems_general", ElementByXPathDetectorExtension([radio.SETTINGS_CUSTOM_BL_GEMS_GENERAL_TITLE]))
SETTINGS_CUSTOM_BL_GEMS_DOMAIN_ANNOUNCEMENT = Element("settings_custom_bl_gems_domain_announcement", ElementByXPathDetectorExtension([radio.SETTINGS_CUSTOM_BL_GEMS_DOMAIN_ANNOUNCEMENT_TITLE]))
HISTORY = Element("history", ElementByXPathDetectorExtension([radio.RADIOTEXT_HISTORY_TITLE_TEXT]))

# screen only when cofigured
MAIN_AM = Element("main_am", ElementByXPathDetectorExtension([radio.MAIN_AM_SELECTED_TITLE]))

BRG = Element("brg", ElementByXPathDetectorExtension([radio.SETTINGS_BRG_TITLE]))

CONTEXT = ContextAnalyzer("radio", AppPackageDetectorExtension(["de.eso.radio", "de.eso.entertainment.ui"]))
CONTEXT.add_elements_from_module(globals())

enna_hcp_configuration.android.contexts.WAIT_SCREENS[INIT.name] = {"wait_time": 10}
