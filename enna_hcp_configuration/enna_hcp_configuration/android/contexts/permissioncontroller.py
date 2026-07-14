# -*- coding: utf-8 -*-
"""Analyzer for the settings app."""

import enna_hcp_configuration.android.contexts
from enna_hcp_configuration.android.xpaths import permissioncontroller
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import Element


POPUP_NOTIFICATIONS_PERMISSION_ERLIN_LOCATION = Element("POPUP_notifications_permission_erlin_location", ElementByXPathDetectorExtension([permissioncontroller.POPUP_NOTIFICATIONS_DIALOG_ERLIN_LOCATION_TITLE]))
POPUP_NOTIFICATIONS_PERMISSION_ERLIN_SOUND = Element("POPUP_notifications_permission_erlin_sound", ElementByXPathDetectorExtension([permissioncontroller.POPUP_NOTIFICATIONS_DIALOG_ERLIN_SOUND_TITLE]))
POPUP_NOTIFICATIONS_PERMISSION_ERLIN_NOTIFICATIONS = Element("POPUP_notifications_permission_erlin_notifications", ElementByXPathDetectorExtension([permissioncontroller.POPUP_NOTIFICATIONS_DIALOG_ERLIN_NOTIFICATIONS_TITLE]))

APP_PERMISSION = Element("app_permission", ElementByXPathDetectorExtension([permissioncontroller.APP_PERMISSION_TITLE]))
APP_PERMISSION_DATA_AND_MEDIA = Element("app_permission_data_media", ElementByXPathDetectorExtension([permissioncontroller.DATA_AND_MEDIA_TITLE]))
APP_PERMISSION_MEDIACORESERVICE = Element("app_permission_mediacoreservice", ElementByXPathDetectorExtension([permissioncontroller.MEDIACORESERVICE_TITLE]))
PRIVACY_APP_PERMISSIONS = Element("privacy_app_permissions", ElementByXPathDetectorExtension([permissioncontroller.PRIVACY_APP_PERMISSIONS_TITLE]))


CONTEXT = ContextAnalyzer("permissioncontroller", AppPackageDetectorExtension(["com.android.permissioncontroller"]))
CONTEXT.add_elements_from_module(globals())

enna_hcp_configuration.android.contexts.WAIT_SCREENS[POPUP_NOTIFICATIONS_PERMISSION_ERLIN_LOCATION.name] = {"wait_time": 15}
enna_hcp_configuration.android.contexts.WAIT_SCREENS[POPUP_NOTIFICATIONS_PERMISSION_ERLIN_SOUND.name] = {"wait_time": 15}
enna_hcp_configuration.android.contexts.WAIT_SCREENS[POPUP_NOTIFICATIONS_PERMISSION_ERLIN_NOTIFICATIONS.name] = {"wait_time": 15}
