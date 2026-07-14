# -*- coding: utf-8 -*-
"""Analyzer for the navigation app."""

import enna_hcp_configuration.android.contexts
from enna_hcp_configuration.android.xpaths import navigation
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathBlacklistWhitelistDetectorExtension, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import Element

POPUP_LOCATION_PERMISSION_KEYBOARD = Element("POPUP_location_permission_keyboard", ElementByXPathDetectorExtension([navigation.POPUP_LOCATION_PERMISSION_KEYBOARD_DIALOG_TITLE]))
POPUP_NAVIGATION_AUTHORIZATION_KEYBOARD = Element("POPUP_navigation_authorization_keyboard", ElementByXPathDetectorExtension([navigation.POPUP_KEYBOARD_AUTHORIZATION_DIALOG_TITLE]))
POPUP_NAVIGATION_AUTO_UPDATE_DATABASE = Element("POPUP_navigation_auto_update_database", ElementByXPathDetectorExtension([navigation.POPUP_DATABASE_AUTO_UPDATE_TITLE]))
POPUP_NAVIGATION_COUNTRY_CHANGED = Element("POPUP_navigation_country_changed", ElementByXPathDetectorExtension([navigation.POPUP_COUNTRY_CHANGED_TITLE]))

MAIN = Element("main", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[navigation.MAIN_TITLE],must_not_exist=[navigation.SEARCH_OVERLAY_TITLE, navigation.ABORT_ROUTE_GUIDANCE_BUTTON_TITLE]))
SETTINGS = Element("settings", ElementByXPathDetectorExtension([navigation.SETTING_TITLE]))
SETTINGS_CHARGING = Element("settings_charging", ElementByXPathDetectorExtension([navigation.SETTING_CHARGING_TITLE]))
SETTINGS_NAVIINFORMATION = Element("settings_naviinfo", ElementByXPathDetectorExtension([navigation.SETTING_NAVI_INFORMATION_TITLE]))
SETTINGS_COUNTRYINFORMATION = Element("settings_countryinfo", ElementByXPathDetectorExtension([navigation.SETTING_COUNTRY_INFORMATION_TITLE]))
NAVADAPTER_MOCK = Element("navadapter_mock", ElementByXPathDetectorExtension([navigation.GEM_NAVADAPTER_MOCK_TITLE]))
ESOMOCK = Element("esomock", ElementByXPathDetectorExtension([navigation.ESO_MOCK_TITLE]))
NAVADAPTER = Element("navadapter", ElementByXPathDetectorExtension([navigation.GEM_NAVADAPTER_TITLE]))
GEM = Element("gem", ElementByXPathDetectorExtension([navigation.GEM_TITLE]))
GUIDANCE = Element("guidance", ElementByXPathDetectorExtension([navigation.ABORT_ROUTE_GUIDANCE_BUTTON_TITLE]))
SEARCH = Element("search", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[navigation.SEARCH_OVERLAY_TITLE, navigation.FAVORITES_TITLE], must_not_exist=[navigation.SEARCH_CATEGORIES_TITLE]))
SEARCH_CATEGORIES = Element("search_categories", ElementByXPathDetectorExtension([navigation.SEARCH_CATEGORIES_TITLE]))

SEARCH_DETAILS = Element("search_details", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[navigation.SEARCH_OVERLAY_TITLE],must_not_exist=[navigation.FAVORITES_TITLE]))
TOURPLAN = Element("tourplan", ElementByXPathDetectorExtension([navigation.ROUTE_TOUR_PLAN_TITLE]))
INIT = Element("init", ElementByXPathDetectorExtension([navigation.INIT_TITLE]))
DESTINATION = Element("destination", ElementByXPathDetectorExtension([navigation.DEST_INPUT_TITLE]))
NOT_ACTIVATED = Element("not_activated", ElementByXPathDetectorExtension([navigation.NOT_ACTIVATED_TITLE]))
TRAFFIC_DETAILS = Element("traffic_details", ElementByXPathDetectorExtension([navigation.TRAFFIC_DETAILS_TITLE]))
DESTINATION_DETAILS = Element("destination_details", ElementByXPathDetectorExtension([navigation.DESTINATION_DETAILS_SCREEN_TITLE]))
POI_STACK = Element("poi_stack", ElementByXPathDetectorExtension([navigation.POI_STACK_SCREEN_TITLE]))
POI_OVERVIEW = Element("poi_overview", ElementByXPathDetectorExtension([navigation.POI_OVERVIEW_TITLE]))
ALTERNATIVE_ROUTES = Element("alternative_routes", ElementByXPathDetectorExtension([navigation.ALTERNATIVE_ROUTES_CLOSE_BUTTON_TITLE]))

CONTEXT = ContextAnalyzer("navigation", AppPackageDetectorExtension(["de.eso.audi.navi", "technology.cariad.navi.audi"]))
CONTEXT.add_elements_from_module(globals())

# Add wait screens for navigation
enna_hcp_configuration.android.contexts.WAIT_SCREENS[INIT.name] = {"wait_time": 20}
enna_hcp_configuration.android.contexts.WAIT_SCREENS[POPUP_NAVIGATION_COUNTRY_CHANGED.name] = {"wait_time": 10}
