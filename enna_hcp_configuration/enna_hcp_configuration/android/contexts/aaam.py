# -*- coding: utf-8 -*-
"""Contexts for the themes app (AudiAsAMatchmaker, com.valtech_mobility.aaam.audi package)."""

from enna_hcp_configuration.android.base import ContextAnalyzer, ElementByXPathBlacklistWhitelistDetectorExtension, ElementByXPathDetectorExtension, AppPackageDetectorExtension
from enna_hcp_configuration.android.xpaths import aaam as xpaths_aaam
from enna_hcp_configuration.common.base import Element


THEMES = Element("themes", ElementByXPathDetectorExtension([xpaths_aaam.THEMES_TITLE]))  # AAAM_OVERVIEW
CATALOG = Element("catalog", ElementByXPathDetectorExtension([xpaths_aaam.CATALOG_TITLE, xpaths_aaam.CATALOG_LIST_CONTAINER]))  # AAAM_CATALOG
CATALOG_INFO = Element("catalog_info", ElementByXPathDetectorExtension([xpaths_aaam.CATALOG_INFO_TITLE]))  # AAAM_CATALO_INFO

SETTINGS = Element("settings", ElementByXPathDetectorExtension([xpaths_aaam.SETTINGS_TITLE]))  # AAAM_SETTINGS
SETTINGS_OSSN = Element("settings_ossn", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[xpaths_aaam.SETTINGS_OSSN_TITLE], must_not_exist=[xpaths_aaam.SETTINGS_OSSN_TITLE_BLOCKING_DISCLAIMER])) # AAAM_OSSN
SETTINGS_OSSN_BLOCKING_DISCLAIMER = Element("settings_ossn_blocking_disclaimer", ElementByXPathDetectorExtension(xpaths_aaam.SETTINGS_OSSN_TITLE_BLOCKING_DISCLAIMER)) # AAAM_OSSN

CONSENT_TO_ADVERTISING = Element("consent_to_advertising", ElementByXPathDetectorExtension([xpaths_aaam.CONSENT_TO_ADVERTISING_TITLE]))  # AAAM_CONSENT_TO_ADVERTISING

CATALOG_POPUP_DATA_PRIVACY = Element("catalog_popup_data_privacy", ElementByXPathDetectorExtension([xpaths_aaam.CATALOG_POPUP_DATA_PRIVACY_TITLE]))
CATALOG_POPUP_FUNCTION_UNAVAILABLE = Element("catalog_popup_function_unavailable", ElementByXPathDetectorExtension([xpaths_aaam.CATALOG_POPUP_FUNCTION_UNAVAILABLE_TITLE]))

CATALOG_HIGHLIGHTS_MORE = Element("catalog_highlights_more", ElementByXPathDetectorExtension([xpaths_aaam.CATALOG_HIGHLIGHTS_MORE_TITLE]))  # AAAM_CATALOG_HIGHLIGHTS_MORE
CATALOG_HIGHLIGHTS_MORE_WHALE = Element("catalog_highlights_more_whale", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[xpaths_aaam.CATALOG_HIGHLIGHTS_MORE_WHALE_TITLE],
                                                                                                                 must_not_exist=[xpaths_aaam.CATALOG_HIGHLIGHTS_MORE_WHALE_PREVIEW_TEXT]))  # AAAM_CATALOG_HIGHLIGHTS_MORE_WHALE
CATALOG_HIGHLIGHTS_MORE_WHALE_PREVIEW = Element("catalog_highlights_more_whale_preview", ElementByXPathDetectorExtension([xpaths_aaam.CATALOG_HIGHLIGHTS_MORE_WHALE_PREVIEW_TITLE, xpaths_aaam.CATALOG_HIGHLIGHTS_MORE_WHALE_PREVIEW_TEXT]))

CATALOG_AUDI = Element("catalog_audi", ElementByXPathDetectorExtension([xpaths_aaam.CATALOG_AUDI_TITLE, xpaths_aaam.CATALOG_AUDI_MORE_BUTTON]))
CATALOG_AUDI_AUDISPORT_MORE = Element("catalog_audi_audisport_more", ElementByXPathDetectorExtension([xpaths_aaam.CATALOG_AUDI_AUDISPORT_MORE_TITLE, xpaths_aaam.CATALOG_AUDI_AUDISPORT_MORE_WEBVIEW_TITLE]))

CATALOG_SEASONAL_HOLIDAYS_MORE = Element("catalog_seasonal_holidays_more", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[xpaths_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_TITLE],
                                                                                                                             must_not_exist=[xpaths_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_PREVIEW_BUTTON]))
CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI = Element("catalog_seasonal_holidays_more_bonsai", ElementByXPathDetectorExtension([xpaths_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_TITLE,
                                                                                                                          xpaths_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_PREVIEW_BUTTON]))
CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_PREVIEW = Element("catalog_seasonal_holidays_more_bonsai_preview", ElementByXPathDetectorExtension([xpaths_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_PREVIEW_TITLE]))
CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_BUY = Element("catalog_seasonal_holidays_more_bonsai_buy", ElementByXPathDetectorExtension([xpaths_aaam.CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_BUY_TITLE]))


CONTEXT = ContextAnalyzer("aaam", AppPackageDetectorExtension(["com.valtech_mobility.aaam.audi"]))
CONTEXT.add_elements_from_module(globals())
