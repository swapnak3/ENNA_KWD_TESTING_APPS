# -*- coding: utf-8 -*-
"""Analyzer for the phone app."""

import enna_hcp_configuration.android.contexts
from enna_hcp_configuration.android.xpaths import phone, aem
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, \
	ElementByXPathDetectorExtension, ElementByXPathBlacklistWhitelistDetectorExtension
from enna_hcp_configuration.common.base import Element

MAIN = Element("main", ElementByXPathDetectorExtension([phone.MAIN_TITLE]))

SEARCH_DEVICES = Element("search_devices", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[phone.SEARCH_DEVICES_TITLE], must_not_exist=[phone.TEXT_UNBLOCKING_BY_PASSENGER]))
OPEN_SOURCE_SOFTWARE_NOTICE = Element("open_source_software_notice", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[phone.OPEN_SOURCE_SOFTWARE_NOTICE_TITLE], must_not_exist=[phone.TEXT_UNBLOCKING_BY_PASSENGER]))

CONNECTIONS = Element("connections", ElementByXPathDetectorExtension([phone.CONNECTION_MANAGER_TITLE]))
DEVICE_MANAGER = Element("device_manager", ElementByXPathDetectorExtension([phone.DEVICE_MANAGER_TITLE]))
BLUETOOTH_SETTINGS = Element("bluetooth_settings", ElementByXPathDetectorExtension([phone.BLUETOOTH_SETTINGS_TITLE]))
CONNECTION_BLUETOOTH = Element("connection_bluetooth", ElementByXPathDetectorExtension([phone.SETTINGS_CONNECTION_BLUETOOTH_TITLE]))
WIFI_SETTINGS = Element("wifi_settings", ElementByXPathDetectorExtension([phone.WIFI_SETTINGS_TITLE]))
VEHICLE_HOTSPOT_SETTINGS = Element("vehicle_hotspot_settings", ElementByXPathDetectorExtension([phone.VEHICLE_HOTSPOT_SETTINGS_TITLE]))
WIRELESS_CHARGING_SETTINGS = Element("wireless_charging_settings", ElementByXPathDetectorExtension(phone.WIRELESS_CHARGING_SETTINGS_TITLE))
SKELETON = Element("skeleton", ElementByXPathDetectorExtension([phone.CAR2PHONE_SKELETON_TITLE]))

POPUP_HOTSPOT_DEACTIVATION = Element("POPUP_hotspot_deactivation", ElementByXPathDetectorExtension([phone.POPUP_HOTSPOT_DEACTIVATION_IGNORE_TITLE]))
POPUP_PHONE_PERMISSIONS = Element("POPUP_phone_permissions", ElementByXPathDetectorExtension([phone.POPUP_HOTSPOT_DEACTIVATION_IGNORE_TITLE]))
POPUP_CONNECTION_BLUETOOTH_PREGRANTED_PERMISSIONS = Element("POPUP_pregranted_permissions", ElementByXPathDetectorExtension([phone.POPUP_CONNECTION_BLUETOOTH_TITLE]))

AEM_CONNECTIVITY_TEST_MENU = Element("aem_connectivity_test_menu", ElementByXPathDetectorExtension([aem.CONNECTIVITY_TEST_MENU_TITLE]))

UNBLOCK_THE_PASSENGER = Element("unblock_the_passenger", ElementByXPathDetectorExtension([phone.TEXT_UNBLOCKING_BY_PASSENGER, phone.BUTTON_CONFIRM_I_AM_PASSENGER]))

CONTEXT = ContextAnalyzer("phone", AppPackageDetectorExtension(["de.eso.phone"]))
CONTEXT.add_elements_from_module(globals())

enna_hcp_configuration.android.contexts.WAIT_SCREENS[SKELETON.name] = {"wait_time": 30}
