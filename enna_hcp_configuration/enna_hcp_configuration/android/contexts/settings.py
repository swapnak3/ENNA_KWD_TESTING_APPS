# -*- coding: utf-8 -*-
"""Contexts for the settings app."""

from enna_hcp_configuration.android.base import ContextAnalyzer, ElementByXPathBlacklistWhitelistDetectorExtension, ElementByXPathDetectorExtension, AppPackageDetectorExtension
from enna_hcp_configuration.android.xpaths import settings as xpath_settings
from enna_hcp_configuration.common.base import Element


MAIN = Element("main", ElementByXPathDetectorExtension(xpath_settings.MAIN_TITLE))

# MAIN
SYSTEM = Element("system", ElementByXPathDetectorExtension(xpath_settings.SYSTEM_TITLE))
# CONNECTIIONS        de.eso.phone
# SOUND               de.eso.sound.audi
# DISPLAY             de.eso.car.audi
# VEHICLE_SETTINGS    de.eso.car.audi
# AUDI_ASSISTANT      technology.cariad.assistant
NOTIFICATIONS = Element("notifications", ElementByXPathDetectorExtension([xpath_settings.NOTIFICATIONS_TITLE]))
PRIVACY = Element("privacy", ElementByXPathDetectorExtension([xpath_settings.PRIVACY_TITLE]))
LINKED_APP_ACCOUNTS = Element("linked_app_accounts", ElementByXPathDetectorExtension([xpath_settings.LINKED_APP_ACCOUNTS_TITLE]))
# SECURITY            de.eso.usermanagement
# FUNCTIONS_ON_DEMAND de.eso.audi.fod
STORAGE = Element("storage", ElementByXPathDetectorExtension([xpath_settings.STORAGE_TITLE]))
# APP_FOR_DIGITAL_ASSISTANT com.android.permissioncontroller

# SYSTEM
SYSTEM_LANGUAGESINPUT_INPUT = Element("system_languagesinput_input", ElementByXPathDetectorExtension([xpath_settings.SYSTEM_LANGUAGESINPUT_TITLE]))
SYSTEM_LANGUAGESINPUT_LANGUAGES = Element("system_languagesinput_languages", ElementByXPathDetectorExtension([xpath_settings.SYSTEM_LANGUAGESINPUT_LANGUAGES_TITLE]))
SYSTEM_LANGUAGESINPUT_KEYBOARD = Element("system_languagesinput_keyboard", ElementByXPathDetectorExtension([xpath_settings.SYSTEM_LANGUAGESINPUT_KEYBOARD_TITLE]))
SYSTEM_LOCATION = Element("system_location", ElementByXPathDetectorExtension([xpath_settings.SYSTEM_LOCATION_TITLE]))
# SYSTEM_DATE_AND_TIME   de.eso.car.audi
# SYSTEM_UNITS   de.eso.car.audi
# SYSTEM_SOFTWARE_UPDATE de.eso.audi.softwareupdate
# SYSTEM_RESTORE_FACTORY_SETTINGS    de.eso.r2f
SYSTEM_ABOUT = Element("system_about", ElementByXPathDetectorExtension([xpath_settings.SYSTEM_ABOUT_TITLE, xpath_settings.LIST_ITEM_ABOUT_KERNEL_VERSION]))  # ehemals SYSTEM_INFO_TITLE
SYSTEM_OPEN_SOURCE_SOFTWARE_NOTICE = Element("system_open_source_software_notice", ElementByXPathDetectorExtension([xpath_settings.SYSTEM_OPEN_SOURCE_SOFTWARE_NOTICE_TITLE]))
SYSTEM_OPEN_SOURCE_SOFTWARE_NOTICE_TLI = Element("system_open_source_software_notice_tli", ElementByXPathDetectorExtension([xpath_settings.OPEN_SOURCE_SW_NOTICE_TLI_OSD_TITLE]))

SYSTEM_LEGAL_INFORMATION = Element("system_legal_information", ElementByXPathDetectorExtension([xpath_settings.SYSTEM_LEGAL_INFORMATION_TITLE]))
# SYSTEM_LOCAL_SYSTEM_UPDATE # geht bei CLU53 nicht
# SYSTEM_ANDROID_AUTO    com.google.android.embedded.projection

# NOTIFICATIONS

# PRIVACY
# PRIVACY_VEHICLE_RELATED_ONLINE_SERVICES   de.eso.privacymode
PRIVACY_MICROPHONE = Element("privacy_microphone", ElementByXPathDetectorExtension([xpath_settings.PRIVACY_MICROPHONE_TITLE, xpath_settings.PRIVACY_MICROPHONE_STATE_SWITCH]))
# PRIVACY_LOCATION = SYSTEM_LOCATION
# PRIVACY_APP_PERMISSIONS   com.android.permissioncontroller

# LINKED_APP_ACCOUNTS
# LINKED_APP_ACCOUNTS_ADD_ACCOUNT # Absturz keine Funktion in CLU53

# APPS
# APPS_RECENTLY_OPENED only headline

APPS = Element("apps", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[xpath_settings.APPS_TITLE], must_not_exist=[xpath_settings.APPS_APP_INFO_TITLE, xpath_settings.APPS_HIDE_SYSTEM_APPS_ON]))
APPS_APP_INFO = Element("apps_app_info", ElementByXPathBlacklistWhitelistDetectorExtension(
		must_exist=[xpath_settings.APPS_APP_INFO_TITLE, xpath_settings.APPS_HIDE_SYSTEM_APPS_ON],
		must_not_exist=[xpath_settings.APPS_HIDE_SYSTEM_APPS_OFF,
			xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_NOTIFI_TITLE,
			xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_PERMIS_TITLE,
			xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_STORAG_TITLE]))
APPS_APP_INFO_VIEWALL  = Element("apps_app_info_viewall", ElementByXPathBlacklistWhitelistDetectorExtension(
		must_exist=[xpath_settings.APPS_APP_INFO_TITLE, xpath_settings.APPS_HIDE_SYSTEM_APPS_OFF],
		must_not_exist=[xpath_settings.APPS_HIDE_SYSTEM_APPS_ON,
						xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_NOTIFI_TITLE,
						xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_PERMIS_TITLE,
						xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_STORAG_TITLE]))

# APPS PERMISSION_MANAGER
# APPS_DEFAULT_APPS
# APPS_UNUSED_APPS
# APPS_PERFORMANCE_IMPACTING_APPS
# APPS_SPECIAL_APP_ACCESS
# APPS_DEFAULT_NOTIFICATION_SOUND # switch
APPS_APP_INFO_VIEWALL_AUDI_ASSISTANT = Element("apps_app_info_viewall_audi_assistant", ElementByXPathDetectorExtension([xpath_settings.APPS_APP_INFO_VIEWALL_AUDI_ASSISTANT_TITLE,
	xpath_settings.APPS_APP_INFO_VIEWALL_ENTITY_HEADER_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_NOTIFI_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_PERMIS_TITLE]))
APPS_APP_INFO_VIEWALL_CAR = Element("apps_app_info_viewall_car", ElementByXPathDetectorExtension([xpath_settings.APPS_APP_INFO_VIEWALL_CAR_TITLE,
	xpath_settings.APPS_APP_INFO_VIEWALL_ENTITY_HEADER_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_NOTIFI_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_PERMIS_TITLE]))
APPS_APP_INFO_VIEWALL_CAR2PHONE = Element("apps_app_info_viewall_car2phone", ElementByXPathDetectorExtension([xpath_settings.APPS_APP_INFO_VIEWALL_CAR2PHONE_TITLE,
	xpath_settings.APPS_APP_INFO_VIEWALL_ENTITY_HEADER_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_NOTIFI_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_PERMIS_TITLE]))
APPS_APP_INFO_VIEWALL_EXPERIENCES = Element("apps_app_info_viewall_experiences", ElementByXPathDetectorExtension([xpath_settings.APPS_APP_INFO_VIEWALL_EXPERIENCES_TITLE,
	xpath_settings.APPS_APP_INFO_VIEWALL_ENTITY_HEADER_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_NOTIFI_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_PERMIS_TITLE]))
APPS_APP_INFO_VIEWALL_LEGAL = Element("apps_app_info_viewall_legal", ElementByXPathDetectorExtension([xpath_settings.APPS_APP_INFO_VIEWALL_LEGAL_TITLE,
	xpath_settings.APPS_APP_INFO_VIEWALL_ENTITY_HEADER_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_NOTIFI_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_PERMIS_TITLE]))
APPS_APP_INFO_VIEWALL_NAVIGATION = Element("apps_app_info_viewall_navigation", ElementByXPathDetectorExtension([xpath_settings.APPS_APP_INFO_VIEWALL_NAVIGATION_TITLE,
	xpath_settings.APPS_APP_INFO_VIEWALL_ENTITY_HEADER_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_NOTIFI_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_PERMIS_TITLE]))
APPS_APP_INFO_VIEWALL_OBB = Element("apps_app_info_viewall_obb", ElementByXPathDetectorExtension([xpath_settings.APPS_APP_INFO_VIEWALL_OBB_TITLE,
	xpath_settings.APPS_APP_INFO_VIEWALL_ENTITY_HEADER_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_NOTIFI_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_PERMIS_TITLE]))
APPS_APP_INFO_VIEWALL_PRIVACY_SETTINGS = Element("apps_app_info_viewall_privacy_settings", ElementByXPathDetectorExtension([xpath_settings.APPS_APP_INFO_VIEWALL_PRIVACY_SETTINGS_TITLE,
	xpath_settings.APPS_APP_INFO_VIEWALL_ENTITY_HEADER_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_NOTIFI_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_PERMIS_TITLE]))
APPS_APP_INFO_VIEWALL_TLI = Element("apps_app_info_viewall_tli", ElementByXPathDetectorExtension([xpath_settings.APPS_APP_INFO_VIEWALL_TLI_TITLE,
	xpath_settings.APPS_APP_INFO_VIEWALL_ENTITY_HEADER_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_NOTIFI_TITLE, xpath_settings.APPS_APP_INFO_VIEWALL_APP_DET_PERMIS_TITLE]))

# STORAGE
STORAGE_MUSIC_AND_AUDIO = Element("storage_music_and_audio", ElementByXPathDetectorExtension([xpath_settings.STORAGE_MUSIC_AND_AUDIO_TITLE]))
STORAGE_OTHER_APPS = Element("storage_other_apps", ElementByXPathDetectorExtension([xpath_settings.STORAGE_OTHER_APPS_TITLE]))
# STORAGE_FILES  # auf diesem Gerät wird die Dateiverwaltung nicht unterstützt
# STORAGE_SYSTEM  # System enthält Dateien für die Ausführung der Android-Version 13

# Moved to the end of the file because of greedy behaviour to make apps_app_info screen detectable
# APPS = Element("apps", ElementByXPathDetectorExtension([xpath_settings.APPS_TITLE]))
# APPS = Element("apps", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[xpath_settings.APPS_TITLE], must_not_exist=[xpath_settings.APPS_APP_INFO_TITLE, xpath_settings.APPS_HIDE_SYSTEM_APPS_ON]))

CONTEXT = ContextAnalyzer("settings", AppPackageDetectorExtension(["com.android.car.settings"]))
CONTEXT.add_elements_from_module(globals())
