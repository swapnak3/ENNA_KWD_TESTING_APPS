# -*- coding: utf-8 -*-
"""Module contains xpath of legal app."""
import enna_hcp_configuration.android.xpaths
from . import XpathString

if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.VTM import Legal as legal
	from enna_hcp_configuration.texts.CLU55.center.de.eso import privacymode
	from enna_hcp_configuration.texts.CLU55.center.VTM import OnlineLogbookHCP3App as olb
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.VTM import Legal as legal
	from enna_hcp_configuration.texts.CLU53.center.de.eso import privacymode
	from enna_hcp_configuration.texts.CLU53.center.VTM import OnlineLogbookHCP3App as olb
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.VTM import Legal as legal
	from enna_hcp_configuration.texts.CLU51.center.de.eso import privacymode
	from enna_hcp_configuration.texts.CLU51.center.VTM import OnlineLogbookHCP3App as olb
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.VTM import Legal as legal
	from enna_hcp_configuration.texts.CLU48.center.de.eso import privacymode
	from enna_hcp_configuration.texts.CLU48.center.VTM import OnlineLogbookHCP3App as olb
else:
	from enna_hcp_configuration.texts.CLU46.center.VTM import Legal as legal
	from enna_hcp_configuration.texts.CLU46.center.de.eso import privacymode
	from enna_hcp_configuration.texts.CLU46.center.VTM import OnlineLogbookHCP3App as olb


# pylint: disable=line-too-long, fixme
OVERVIEW_TITLE = XpathString(f"//*[@resource-id='com.valtech_mobility.legal.audi:id/titleTextViewRef']{legal.home_screen__legal_app_tile__label}")
OVERVIEW_LIST_CONTAINER = XpathString(clu46="//*[@resource-id='com.valtech_mobility.legal.audi:id/list_items']", clu53="//*[@resource-id='com.valtech_mobility.legal.audi:id/layout_legal_info_overview']")

ABOUT_US_TITLE = XpathString(f"//*[@resource-id='com.valtech_mobility.legal.audi:id/titleTextViewRef']{privacymode.settings_entry_imprint}")
WEBVIEW_CONTENT_CONTAINER = XpathString("//*[@class='android.webkit.WebView']")
# DATA_PROTECTION_NOTES_TITLE = XpathString(f"//*[@resource-id='com.valtech_mobility.legal.audi:id/titleTextViewRef']{privacymode.settings_entry_legal_disclaimer}")
DATA_PROTECTION_NOTES_TITLE = XpathString(f"//*[@resource-id='com.valtech_mobility.legal.audi:id/titleTextViewRef']{str(privacymode.settings_entry_legal_disclaimer).replace("Datenschutzhinweise", "Datenschutzinformation Connect")}")  # ToDo TextTool
SETTINGS_TITLE = XpathString(f"//*[@resource-id='com.valtech_mobility.legal.audi:id/titleTextViewRef']{privacymode.settings_title}")
SETTINGS_OPEN_SOURCE_SOFTWARE_NOTICE_TITLE = XpathString(f"//*[@resource-id='com.valtech_mobility.legal.audi:id/titleTextViewRef']{privacymode.settings_entry_os_disclaimer}")
QR_CODE_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.legal.audi:id/qrcode']")
SKELETON_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.legal.audi:id/skeleton']")
VIDEO_PLAYER_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.legal.audi:id/playerView']")
FUNCTION_BLOCKED_TITLE = XpathString(f"//*{privacymode.texttool_globals_toast___hmisdk__toast_blocking_text}")
PRIVACY_MODE_INFO_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.legal.audi:id/textAndButtonsScreenContainer']/.//*[@resource-id='com.valtech_mobility.legal.audi:id/textView1']")
TITLE_LINE_CONTAINER = XpathString("//*[@resource-id='com.valtech_mobility.legal.audi:id/interactionContainer']")
WEBVIEW_BLOCKING = XpathString("//*[@resource-id='com.valtech_mobility.legal.audi:id/container_webview_blocking']")

SETTINGS_BACK_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.legal.audi:id/actionButtons']/..//*[@class='android.widget.ImageButton']")
PRIVACY_MODE_INFO_SETTINGS_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.legal.audi:id/operationPanel']/..//*[@index='2']")
PRIVACY_MODE_INFO_OK_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.legal.audi:id/operationPanel']/..//*[@index='1']")
IMPRINT_BUTTON = XpathString(f"//*[@resource-id='com.valtech_mobility.legal.audi:id/listItemGrid2MainContent_textStart']{privacymode.settings_entry_imprint}")
# DATA_PROTECTION_NOTES_BUTTON = XpathString(f"//*[@resource-id='com.valtech_mobility.legal.audi:id/listItemGrid2MainContent_textStart']{privacymode.settings_entry_legal_disclaimer}")
DATA_PROTECTION_NOTES_BUTTON = XpathString(f"//*[@resource-id='com.valtech_mobility.legal.audi:id/listItemGrid2MainContent_textStart']{str(privacymode.settings_entry_legal_disclaimer).replace("Datenschutzhinweise", "Datenschutzinformation Connect")}")  # ToDo TextTool
SETTINGS_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.legal.audi:id/menuActionContainer']/..//*[@class='android.widget.ImageButton']")
OPEN_SOURCE_SOFTWARE_NOTICE_BUTTON = XpathString("//*[contains(@content-desc, 'com.valtech_mobility.legal.audi:string/legal_settings_screen__open_source_license__title')]")

DATAPRIVACY_BUTTON = XpathString(f"//*{olb.logbook_settings_screen__data_protection_information__text}")
