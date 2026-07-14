# -*- coding: utf-8 -*-
"""Analyzer for the obb App. """

import enna_hcp_configuration.android.contexts
from enna_hcp_configuration.android.xpaths import obb
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathBlacklistWhitelistDetectorExtension, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import Element

# MAIN = Element("main", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[obb.SEARCH_BUTTON, obb.MAIN_TITLE, obb.SETTINGS_TITLE], must_not_exist=[obb.FUNCTION_BLOCKED_TITLE, obb.PRIVACY_MODE_TITLE]))
MAIN = Element("main", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[obb.SEARCH_BUTTON, obb.MAIN_TITLE], must_not_exist=[obb.SETTINGS_TITLE, obb.FUNCTION_BLOCKED_TITLE, obb.PRIVACY_MODE_TITLE]))
SEARCH = Element("search", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[obb.SEARCH_EDIT_TEXT_BOX_TITLE, obb.BACK_BUTTON, obb.HOME_BUTTON], must_not_exist=[obb.SEARCH_WEBCONTENT_TITLE]))
SEARCH_RESULTS = Element("search_results", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[obb.BACK_BUTTON, obb.HOME_BUTTON, obb.SEARCH_RESULT], must_not_exist=obb.NIX))
INIT = Element("init", ElementByXPathDetectorExtension([obb.INIT_TITLE]))
INIT_REQUEST = Element("init_request", ElementByXPathDetectorExtension([obb.INIT_REQUEST_TITLE]))
CHAPTERS = Element("chapters", ElementByXPathDetectorExtension([obb.CHAPTERS_TITLE]))
SUPPLEMENTS = Element("supplements", ElementByXPathDetectorExtension([obb.SUPPLEMENTS_TITLE]))
FAQ = Element("faq", ElementByXPathDetectorExtension([obb.FAQ_TITLE]))
WARNING_LAMPS = Element("warning_lamps", ElementByXPathDetectorExtension([obb.WARNING_LAMPS_TITLE]))
INDEX_SEARCH = Element("index_search", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[obb.INDEX_SEARCH_LETTER_A, obb.INDEX_SEARCH_LETTER_W, obb.INDEX_SEARCH_TEXT_TITLE], must_not_exist=[obb.NIX]))
INFO = Element("info", ElementByXPathDetectorExtension([obb.INFO_TITLE]))

BLOCKED = Element("blocked", ElementByXPathDetectorExtension([obb.FUNCTION_BLOCKED_TITLE]))

CONNECTIVITY_ERROR = Element("no_internet_connectivity", ElementByXPathDetectorExtension([obb.CONNECTIVITY_ERROR_TEXT_TITLE]))

CHAPTERS_QUICK_REFERENCE = Element("chapters_quick_reference", ElementByXPathDetectorExtension([obb.CHAPTERS_QUICK_REFERENCE_TITLE]))
CHAPTERS_DISPLAYS_AND_CONTROLS = Element("chapters_displays_and_controls", ElementByXPathDetectorExtension([obb.CHAPTERS_DISPLAYS_AND_CONTROLS_TITLE]))
CHAPTERS_SETTING_OFF = Element("chapters_setting_off", ElementByXPathDetectorExtension([obb.CHAPTERS_SETTING_OFF_TITLE]))
CHAPTERS_DRIVER_ASSIST_SYSTEMS = Element("chapters_driver_assist_systems", ElementByXPathDetectorExtension([obb.CHAPTERS_DRIVER_ASSIST_SYSTEMS_TITLE]))

CHAPTERS_INSTRUMENT_CLUSTER = Element("chapters_instrument_cluster", ElementByXPathDetectorExtension([obb.CHAPTERS_INSTRUMENT_CLUSTER_TITLE]))
CHAPTERS_OVERVIEW_AND_CONTROLS = Element("chapters_overview_and_controls", ElementByXPathDetectorExtension([obb.CHAPTERS_OVERVIEW_AND_CONTROLS_TITLE]))
CHAPTERS_SITTING_CORRECTLY_AND_SAFELY = Element("chapter_sitting_correctly_and_safely", ElementByXPathDetectorExtension([obb.CHAPTERS_SITTING_CORRECTLY_AND_SAFELY_TITLE]))
CHAPTERS_FRONT_SEATS = Element("chapters_front_seats", ElementByXPathDetectorExtension([obb.CHAPTERS_FRONT_SEATS_TITLE]))
CHAPTERS_COMBINED_ASSIST_FUNCTIONS = Element("chapters_combined_assist_functions", ElementByXPathDetectorExtension([obb.CHAPTERS_COMBINED_ASSIST_FUNCTIONS_TITLE]))
CHAPTERS_ADAPTIVE_CRUISE_ASSIST = Element("chapters_adaptive_cruise_assist", ElementByXPathDetectorExtension([obb.CHAPTERS_ADAPTIVE_CRUISE_ASSIST_TITLE]))
SPEED_ASSIST_SYSTEMS = Element("speed_assist_systems", ElementByXPathDetectorExtension([obb.ADAPTIVE_CRUISE_ASSIST_TITLE]))

FAQ_SET_OFF = Element("faq_set_off", ElementByXPathDetectorExtension([obb.FAQ_BEFORE_SET_OFF_TITLE]))
FRONT_SEATS = Element("front_seats", ElementByXPathDetectorExtension([obb.FAQ_FRONT_SEATS_TITLE]))

# settings seems to be quite a wide match. It needs to be put at the end of file, so it does not steel the attention from more precisely defined screens
SETTINGS = Element("settings", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[obb.BACK_BUTTON, obb.SETTINGS_TITLE, obb.SETTINGS_CHANGE_LANGUAGE_BUTTON], must_not_exist=[obb.INDEX_SEARCH_LETTER_A]))
SETTINGS_CHANGE_LANGUAGE = Element("settings_change_language", ElementByXPathDetectorExtension([obb.SETTINGS_CHANGE_LANGUAGE_TITLE]))
# SETTINGS_IMPRINT -> SETTINGS_AUBOUT_US = Element("about_us", ElementByXPathDetectorExtension([obb.ABOUT_US_TITLE]))  # legal.ABOUT_US
# SETTINGS_PRIVACY_POLICY -> SETTINGS_DATA_PROTECTION_NOTES = Element("data_protection_notes", ElementByXPathDetectorExtension([obb.DATA_PROTECTION_NOTES_TITLE]))  # legal.DATA_PROTECTION_NOTES
SETTINGS_OSSN = Element("settings_ossn", ElementByXPathDetectorExtension([obb.SETTINGS_OSSN_TITLE]))

PRIVACY_MODE = Element("privacy_mode", ElementByXPathDetectorExtension([obb.PRIVACY_MODE_TITLE]))

CONTEXT = ContextAnalyzer("obb", AppPackageDetectorExtension(["com.valtech_mobility.obb.audi"]))
CONTEXT.add_elements_from_module(globals())

# Add wait screens for obb
enna_hcp_configuration.android.contexts.WAIT_SCREENS[INIT.name] = {"wait_time": 30}
enna_hcp_configuration.android.contexts.WAIT_SCREENS[INIT_REQUEST.name] = {"wait_time": 30}
