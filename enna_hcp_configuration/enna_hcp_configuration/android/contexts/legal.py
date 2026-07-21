# -*- coding: utf-8 -*-
"""Analyzer for the legal App."""

import enna_hcp_configuration.android.contexts

from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathBlacklistWhitelistDetectorExtension, ElementByXPathDetectorExtension
from enna_hcp_configuration.android.xpaths import legal as xpaths_legal
from enna_hcp_configuration.common.base import Element

OVERVIEW = Element("overview", ElementByXPathDetectorExtension([xpaths_legal.OVERVIEW_TITLE, xpaths_legal.OVERVIEW_LIST_CONTAINER]))
ABOUT_US = Element("about_us", ElementByXPathDetectorExtension([xpaths_legal.ABOUT_US_TITLE, xpaths_legal.WEBVIEW_CONTENT_CONTAINER]))
DATA_PROTECTION_NOTES = Element("data_protection_notes", ElementByXPathDetectorExtension([xpaths_legal.DATA_PROTECTION_NOTES_TITLE, xpaths_legal.WEBVIEW_CONTENT_CONTAINER]))

SETTINGS = Element("settings", ElementByXPathDetectorExtension([xpaths_legal.SETTINGS_TITLE]))
SETTINGS_OPEN_SOURCE_SOFTWARE_NOTICE = Element("settings_open_source_software_notice", ElementByXPathDetectorExtension([xpaths_legal.SETTINGS_OPEN_SOURCE_SOFTWARE_NOTICE_TITLE]))

QR_CODE = Element("qr_code", ElementByXPathDetectorExtension([xpaths_legal.QR_CODE_TITLE]))
SKELETON = Element("skeleton", ElementByXPathDetectorExtension([xpaths_legal.SKELETON_TITLE]))
VIDEO_PLAYER = Element("video_player", ElementByXPathDetectorExtension([xpaths_legal.VIDEO_PLAYER_TITLE]))

BLOCKED = Element("blocked", ElementByXPathDetectorExtension([xpaths_legal.FUNCTION_BLOCKED_TITLE]))
PRIVACY_MODE_INFO = Element("privacy_mode_info", ElementByXPathDetectorExtension([xpaths_legal.PRIVACY_MODE_INFO_TITLE]))

EMPTY = Element("empty", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[xpaths_legal.TITLE_LINE_CONTAINER, xpaths_legal.WEBVIEW_BLOCKING], must_not_exist=xpaths_legal.WEBVIEW_CONTENT_CONTAINER))

CONTEXT = ContextAnalyzer("legal", AppPackageDetectorExtension(["com.valtech_mobility.legal.audi"]))
CONTEXT.add_elements_from_module(globals())

# enna_hcp_configuration.android.contexts.WAIT_SCREENS[QR_CODE.name] = {"wait_time": 3}
enna_hcp_configuration.android.contexts.WAIT_SCREENS[SKELETON.name] = {"wait_time": 30}
enna_hcp_configuration.android.contexts.WAIT_SCREENS[EMPTY.name] = {"wait_time": 3}
