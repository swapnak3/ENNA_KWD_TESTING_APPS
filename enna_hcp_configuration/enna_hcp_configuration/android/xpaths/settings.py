# -*- coding: utf-8 -*-
"""Module contains xpath of settings app."""

import enna_hcp_configuration.android.xpaths
from enna_hcp_configuration.texts import TextObject
from enna_hcp_configuration.texts.android.settings import open_source_project as aosp
from . import XpathString

# pylint: disable=line-too-long, fixme
if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.com.android.car import settings
	from enna_hcp_configuration.texts.CLU55.center.de.eso.car import audi
	from enna_hcp_configuration.texts.CLU55.center.de.eso import privacymode
	from enna_hcp_configuration.texts.CLU55.center.de.eso import phone
	from enna_hcp_configuration.texts.CLU55.center.de.eso.audi import carsystemui
	from enna_hcp_configuration.texts.CLU55.center.HAR import IgniteStore
	from enna_hcp_configuration.texts.CLU46.center.technology.cariad.navi import audi as navi_audi
	from enna_hcp_configuration.texts.CLU55.center.VTM import OnlineBordbook
	from enna_hcp_configuration.texts.CLU46.center.CARI import InteriorExperience # ToDo CL55 existiert nicht in Texts

	# ToDo
	settings.texttool_globals_aosp_settings_list_item_subtext___oem_osd_settings = TextObject(xx_DE="Allgemein", bs_BA="Sistem", cs_CZ="Systém", da_DK="System", de_DE="System", el_GR="Σύστημα", en_GB="System", es_ES="Sistema", fi_FI="Järjestelmä", fr_FR="Système",
	                                                                                 hr_HR="Sustav", hu_HU="Rendszer", it_IT="Sistema", nl_NL="Systeem", no_NO="System", pl_PL="System", pt_PT="Sistema", ro_RO="Sistem", ru_RU="Система", sk_SK="Systém",
	                                                                                 sl_SI="Sistem", sr_RS="Sistem", sv_SE="System", tr_TR="Sistem", uk_UA="Система")
	# ToDo
	aosp.language_settings = TextObject(xx_DE="Languages & input", bs_BA="Jezici i unos", cs_CZ="Jazyky a zadávání", da_DK="Sprog og indtastning", de_DE="Sprachen und Eingabe", el_GR="Γλώσσες & εισαγωγή", en_GB="Languages and input", es_ES="Idiomas e introducción de texto",
	                               fi_FI="Kielet ja syöttötapa", fr_FR="Langues et saisie", hr_HR="Jezici i unos", hu_HU="Nyelvek és bevitel", it_IT="Lingue e immissione", nl_NL="Talen en invoer", no_NO="Språk og inndata",
	                               pl_PL="Języki i metody wprowadzania", pt_PT="Idiomas e entrada", ro_RO="Limbi și introducerea textului", ru_RU="Язык и ввод", sk_SK="Jazyky a vstup", sl_SI="Jeziki in vnos", sr_RS="Језици и унос",
	                               sv_SE="Språk och inmatning", tr_TR="Diller ve giriş", uk_UA="Мова й введення")

elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.com.android.car import settings
	from enna_hcp_configuration.texts.CLU53.center.de.eso.car import audi
	from enna_hcp_configuration.texts.CLU53.center.de.eso import privacymode
	from enna_hcp_configuration.texts.CLU53.center.de.eso import phone
	from enna_hcp_configuration.texts.CLU53.center.de.eso.audi import carsystemui
	from enna_hcp_configuration.texts.CLU53.center.HAR import IgniteStore
	from enna_hcp_configuration.texts.CLU46.center.technology.cariad.navi import audi as navi_audi
	from enna_hcp_configuration.texts.CLU53.center.VTM import OnlineBordbook
	from enna_hcp_configuration.texts.CLU46.center.CARI import InteriorExperience # ToDo CL53 existiert nicht in Texts
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.com.android.car import settings
	from enna_hcp_configuration.texts.CLU51.center.de.eso.car import audi
	from enna_hcp_configuration.texts.CLU51.center.de.eso import privacymode
	from enna_hcp_configuration.texts.CLU51.center.de.eso import phone
	from enna_hcp_configuration.texts.CLU51.center.de.eso.audi import carsystemui
	from enna_hcp_configuration.texts.CLU51.center.HAR import IgniteStore
	from enna_hcp_configuration.texts.CLU46.center.technology.cariad.navi import audi as navi_audi
	from enna_hcp_configuration.texts.CLU51.center.VTM import OnlineBordbook
	from enna_hcp_configuration.texts.CLU46.center.CARI import InteriorExperience # ToDo CL51 existiert nicht in Texts
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.com.android.car import settings
	from enna_hcp_configuration.texts.CLU48.center.de.eso.car import audi
	from enna_hcp_configuration.texts.CLU48.center.de.eso import privacymode
	from enna_hcp_configuration.texts.CLU48.center.de.eso import phone
	from enna_hcp_configuration.texts.CLU48.center.de.eso.audi import carsystemui
	from enna_hcp_configuration.texts.CLU48.center.HAR import IgniteStore
	from enna_hcp_configuration.texts.CLU48.center.technology.cariad.navi import audi as navi_audi
	from enna_hcp_configuration.texts.CLU48.center.VTM import OnlineBordbook
	from enna_hcp_configuration.texts.CLU48.center.CARI import InteriorExperience
else:
	from enna_hcp_configuration.texts.CLU46.center.com.android.car import settings
	from enna_hcp_configuration.texts.CLU46.center.de.eso.car import audi
	from enna_hcp_configuration.texts.CLU46.center.de.eso import privacymode
	from enna_hcp_configuration.texts.CLU46.center.de.eso import phone
	from enna_hcp_configuration.texts.CLU46.center.de.eso.audi import carsystemui
	from enna_hcp_configuration.texts.CLU46.center.HAR import IgniteStore
	from enna_hcp_configuration.texts.CLU46.center.technology.cariad.navi import audi as navi_audi
	from enna_hcp_configuration.texts.CLU46.center.VTM import OnlineBordbook
	from enna_hcp_configuration.texts.CLU46.center.CARI import InteriorExperience

	# ToDo
	aosp.language_settings = TextObject(xx_UA='Мови та введення', xx_RO='Limbi și introducere de text', xx_PT='Idiomas e introdução', xx_PL='Języki i metody wprowadzania', xx_CZ='Jazyky a zadávání', xx_ES='Idiomas e introducción de texto', xx_GR='Γλώσσες και είσοδος', bs_BA="Jezici i unos", cs_CZ="Jazyky a zadávání", da_DK="Sprog og indtastning", de_DE="Sprachen und Eingabe", el_GR="Γλώσσες & εισαγωγή", en_GB="Languages and input", es_ES="Idiomas e introducción de texto",
	                               fi_FI="Kielet ja syöttötapa", fr_FR="Langues et saisie", hr_HR="Jezici i unos", hu_HU="Nyelvek és bevitel", it_IT="Lingue e immissione", nl_NL="Talen en invoer", no_NO="Språk og inndata",
	                               pl_PL="Języki i metody wprowadzania", pt_PT="Idiomas e entrada", ro_RO="Limbi și introducerea textului", ru_RU="Язык и ввод", sk_SK="Jazyky a vstup", sl_SI="Jeziki in vnos", sr_RS="Језици и унос",
	                               sv_SE="Språk och inmatning", tr_TR="Diller ve giriş", uk_UA="Мова й введення")
	# ToDo
	aosp.applications_settings = TextObject(xx_FR="Informations sur les applications", bs_BA="Informacije o aplikaciji", cs_CZ="Informace o aplikacích", da_DK="Appinfo", de_DE="App-Info", el_GR="Πληροφορίες εφαρμογής", en_GB="App info",
	                                        es_ES="Información de las aplicaciones", fi_FI="Sovellustiedot", hr_HR="Informacije o aplikaciji", hu_HU="Alkalmazásinfó", it_IT="Informazioni app", nl_NL="App-info", no_NO="App-info",
	                                        pl_PL="Informacje o aplikacjach", pt_PT="Informações do app", ro_RO="Informații despre aplicație", ru_RU="Сведения о приложениях", sk_SK="Informácie o aplikáciách", sl_SI="Podatki o aplikaciji",
	                                        sr_RS="Информације о апликацији", sv_SE="Appinformation", tr_TR="Uygulama bilgileri", uk_UA="Про додаток")


MAIN_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{settings.aosp_settings_top_level_title_text}")
SYSTEM_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{settings.texttool_globals_aosp_settings_list_item_subtext___oem_osd_settings}")
# SYSTEM_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{aosp.header_category_system}")
NOTIFICATIONS_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{carsystemui.cvaa___notification_icons}")
PRIVACY_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{privacymode.privacySettingsHeader}")
LINKED_APP_ACCOUNTS_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{settings.aosp_settings_title_text___accounts}")
# APPS_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{IgniteStore.shop_apps_tab_layout_explore_tab_label}")  # nicht in settings
APPS_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{aosp.apps_dashboard_title}")  # nicht in settings
STORAGE_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{settings.virtual_search_synonym___storage_settings_title}")
APP_FOR_DIGITAL_ASSISTANT_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{settings.aosp_settings_title_text___assistant_and_voice_settings}")

# SYSTEM
SYSTEM_LANGUAGESINPUT_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{aosp.language_settings}")
SYSTEM_LANGUAGESINPUT_LANGUAGES_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{str(aosp.languages_settings).replace("contains(", "").replace(",", "=").replace(")", "")}")
SYSTEM_LANGUAGESINPUT_KEYBOARD_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{settings.virtual_search_synonym___keyboard_settings}")
SYSTEM_LOCATION_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{settings.virtual_search_synonym___location_settings_title}")
# SYSTEM_ABOUT_TITLE = XpathString("//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title'][@text='about' or @text='Info']")  # kein texttool
SYSTEM_ABOUT_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{aosp.system_about_title}")
SYSTEM_OPEN_SOURCE_SOFTWARE_NOTICE_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{settings.texttool_globals_aosp_settings_list_item_text___oem_ossn_entry}")
SYSTEM_LOCATION_USE_SWITCH = XpathString("//*[@resource-id='android:id/switch_widget']")
OPEN_SOURCE_SW_NOTICE_TLI_OSD_TITLE = XpathString(clu46="//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']/.//*[@content-desc='###technology.cariad.trafficlightinformation:string/title_activity_osd_text']",
                                                  clu53="//*[@resource-id='technology.cariad.trafficlightinformation:id/titleTextViewRef'][@content-desc='###technology.cariad.trafficlightinformation:string/title_activity_osd_text']")
SYSTEM_LEGAL_INFORMATION_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{phone.connection_mgr__main_menu__legal_information__text}")

# NOTIFICATIONS

# PRIVACY
PRIVACY_MICROPHONE_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{settings.virtual_search_synonym___microphone_settings_title}")
PRIVACY_MICROPHONE_STATE_SWITCH = XpathString("//*[@content-desc='###microphone_state_switch']")

# LINKED_APP_ACCOUNTS_ADD_ACCOUNT

# APPS
APPS_APP_INFO_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{aosp.applications_settings}")
APPS_HIDE_SYSTEM_APPS = XpathString("//*[contains(@content-desc,'all_applications_settings_hide_system_switch')]/.//*[@resource-id='android:id/switch_widget']")
APPS_HIDE_SYSTEM_APPS_OFF = XpathString("//*[contains(@content-desc,'all_applications_settings_hide_system_switch')]/.//*[@resource-id='android:id/switch_widget'][@checked='false']")
APPS_HIDE_SYSTEM_APPS_ON = XpathString("//*[contains(@content-desc,'all_applications_settings_hide_system_switch')]/.//*[@resource-id='android:id/switch_widget'][@checked='true']")

APPS_APP_INFO_ENTRY = XpathString("//*[contains(@content-desc, 'applications_settings_screen_entry') or contains(@content-desc, 'recent_apps_view_all')]")
APPS_APP_HIDE_SYSTEM_APPS_TOGGLE = XpathString("//*[contains(@content-desc,'all_applications_settings_hide_system_switch')][@package='com.android.car.settings']")

APPS_APP_INFO_VIEWALL_APP_DET_NOTIFI_TITLE = XpathString("//*[@content-desc='###application_details_notifications']")
APPS_APP_INFO_VIEWALL_APP_DET_PERMIS_TITLE = XpathString("//*[@content-desc='###application_details_permissions']")
APPS_APP_INFO_VIEWALL_APP_DET_STORAG_TITLE = XpathString("//*[@content-desc='###application_details_storage']")
APPS_APP_INFO_VIEWALL_ENTITY_HEADER_ICON = XpathString("//*[@resource-id='com.android.car.settings:id/entity_header_icon']")
APPS_APP_INFO_VIEWALL_ENTITY_HEADER_TITLE = XpathString("//*[@resource-id='com.android.car.settings:id/entity_header_title']")

APPS_APP_INFO_VIEWALL_AUDI_ASSISTANT_TITLE = XpathString(f"//*[@content-desc='###application_details_app']/.//*{settings.aosp_settings_top_level_list_item_text___oem_digital_assistant_settings}")
APPS_APP_INFO_VIEWALL_CAR_TITLE = XpathString(f"//*[@content-desc='###application_details_app']/.//*{str(audi.texttool_globals_application_label___app_name_car).replace("contains(", "").replace("text,", "text=").replace("')", "\u200B'")}")     # //*[contains(@text,'Fahrzeug\u200B')]
APPS_APP_INFO_VIEWALL_CAR2PHONE_TITLE = XpathString(f"//*[@content-desc='###application_details_app']/.//*{phone.connection_mgr__main_menu__car_2_phone__text}")
APPS_APP_INFO_VIEWALL_EXPERIENCES_TITLE = XpathString(f"//*[@content-desc='###application_details_app']/.//*{InteriorExperience.app_name}")
APPS_APP_INFO_VIEWALL_LEGAL_TITLE = XpathString(f"//*[@content-desc='###application_details_app']/.//*{IgniteStore.shop_apps_details_list_item_text_legal_item}")
APPS_APP_INFO_VIEWALL_NAVIGATION_TITLE = XpathString(f"//*[@content-desc='###application_details_app']/.//*{navi_audi.texttool_globals_application_label___app_name}")
APPS_APP_INFO_VIEWALL_OBB_TITLE = XpathString(f"//*[@content-desc='###application_details_app']/.//*{OnlineBordbook.home_screen__bordbook_app_tile__label}")
APPS_APP_INFO_VIEWALL_PRIVACY_SETTINGS_TITLE = XpathString(f"//*[@content-desc='###application_details_app']/.//*{privacymode.texttool_globals_application_label___app_name}")
APPS_APP_INFO_VIEWALL_TLI_TITLE = XpathString(f"//*[@content-desc='###application_details_app']/.//*{str(audi.texttool_custom_fas_main_setting___traffic_light_information).replace("contains(", "").replace("text,", "text=").replace("')", "\u200B'")}")

APPS_NAVIGATION_SCREEN_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/entity_header_title']{navi_audi.texttool_globals_application_label___app_name}")
APPS_STORAGE_TOOLBAR_TITLE = XpathString(f"//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title']{settings.virtual_search_synonym___storage_settings_title}")

STORAGE_MUSIC_AND_AUDIO_TITLE = XpathString("//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title'][@text='Music and audio' or @text='Musik und Audio']")
STORAGE_OTHER_APPS_TITLE = XpathString("//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_title'][@text='Other apps' or @text='Weitere Apps']")

BACK_BUTTON = XpathString("//*[@resource-id='com.android.car.settings:id/car_ui_toolbar_nav_icon_container']/./*[@resource-id='com.android.car.settings:id/car_ui_toolbar_nav_icon']")
LIST_CONTAINER = XpathString("//*[@scrollable='true']") # or @resource-id='com.android.car.settings:id/settings_recycler_view']")
PRIVACY_LIST_CONTAINER = XpathString("//*[@class='androidx.recyclerview.widget.RecyclerView']")

LIST_ITEM_AUDI_ASSISTANT = XpathString("//*[contains(@content-desc, '###oem_digital_assistant_settings_entry') or @content-desc='###technology.cariad.assistant']")

LIST_ITEM_SYSTEM = XpathString("//*[contains(@content-desc, '###system_settings_entry')]")
#LIST_ITEM_SYSTEM = XpathString("//android.widget.FrameLayout[@resource-id='com.android.car.settings:id/top_level_recycler_view']/android.widget.FrameLayout[@resource-id='com.android.car.settings:id/car_ui_recycler_view']/androidx.recyclerview.widget.RecyclerView[@resource-id='com.android.car.settings:id/car_ui_internal_recycler_view']/android.widget.FrameLayout[@content-desc='###system_settings_entry']")
#LIST_ITEM_SYSTEM = XpathString("//android.widget.FrameLayout[@resource-id='com.android.car.settings:id/settings_recycler_view']/android.widget.FrameLayout[@resource-id='com.android.car.settings:id/car_ui_recycler_view']/androidx.recyclerview.widget.RecyclerView[@resource-id='com.android.car.settings:id/car_ui_internal_recycler_view']/android.widget.FrameLayout[@content-desc='###system_settings_entry']")
LIST_ITEM_SYSTEM_TEXT = XpathString(f"{LIST_ITEM_SYSTEM}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_SYSTEM_LEADING_ICON = XpathString(f"{LIST_ITEM_SYSTEM}//*[@resource-id='android:id/icon']")
LIST_ITEM_SYSTEM_SUBMENU_ICON = XpathString(f"{LIST_ITEM_SYSTEM}//*[@index='2'][@resource-id='android:id/widget_frame']")
LIST_ITEM_CONNECTIONS = XpathString("//*[contains(@content-desc, '###connection_settings_entry')]")
LIST_ITEM_CONNECTIONS_TEXT = XpathString(f"{LIST_ITEM_CONNECTIONS}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_CONNECTIONS_LEADING_ICON = XpathString(f"{LIST_ITEM_CONNECTIONS}//*[@resource-id='android:id/icon']")
LIST_ITEM_CONNECTIONS_SUBMENU_ICON = XpathString(f"{LIST_ITEM_CONNECTIONS}//*[@index='2'][@resource-id='android:id/widget_frame']")
LIST_ITEM_SOUND = XpathString("//*[contains(@content-desc, '###sound_settings_entry')]")
LIST_ITEM_SOUND_TEXT = XpathString(f"{LIST_ITEM_SOUND}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_SOUND_LEADING_ICON = XpathString(f"{LIST_ITEM_SOUND}//*[@resource-id='android:id/icon']")
LIST_ITEM_SOUND_SUBMENU_ICON = XpathString(f"{LIST_ITEM_SOUND}//*[@index='2'][@resource-id='android:id/widget_frame']")
LIST_ITEM_DISPLAY = XpathString("//*[contains(@content-desc, '###display_settings_entry')]")
LIST_ITEM_DISPLAY_TEXT = XpathString(f"{LIST_ITEM_DISPLAY}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_DISPLAY_LEADING_ICON = XpathString(f"{LIST_ITEM_DISPLAY}//*[@resource-id='android:id/icon']")
LIST_ITEM_DISPLAY_SUBMENU_ICON = XpathString(f"{LIST_ITEM_DISPLAY}//*[@index='2'][@resource-id='android:id/widget_frame']")
LIST_ITEM_VEHICLE_SETTINGS = XpathString("//*[contains(@content-desc, '###vehicle_settings_entry')]")
LIST_ITEM_VEHICLE_SETTINGS_TEXT = XpathString(f"{LIST_ITEM_VEHICLE_SETTINGS}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_VEHICLE_SETTINGS_LEADING_ICON = XpathString(f"{LIST_ITEM_VEHICLE_SETTINGS}//*[@resource-id='android:id/icon']")
LIST_ITEM_VEHICLE_SETTINGS_SUBMENU_ICON = XpathString(f"{LIST_ITEM_VEHICLE_SETTINGS}//*[@index='2'][@resource-id='android:id/widget_frame']")
LIST_ITEM_AUDI_ASSISTANT_TEXT = XpathString(f"{LIST_ITEM_AUDI_ASSISTANT}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_AUDI_ASSISTANT_LEADING_ICON = XpathString(f"{LIST_ITEM_AUDI_ASSISTANT}//*[@resource-id='android:id/icon']")
LIST_ITEM_AUDI_ASSISTANT_SUBMENU_ICON = XpathString(f"{LIST_ITEM_AUDI_ASSISTANT}//*[@index='2'][@resource-id='android:id/widget_frame']")
LIST_ITEM_NOTIFICATIONS = XpathString("//*[contains(@content-desc, '###notifications_settings_entry')]")
LIST_ITEM_NOTIFICATIONS_TEXT = XpathString(f"{LIST_ITEM_NOTIFICATIONS}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_NOTIFICATIONS_LEADING_ICON = XpathString(f"{LIST_ITEM_NOTIFICATIONS}//*[@resource-id='android:id/icon']")
LIST_ITEM_NOTIFICATIONS_SUBMENU_ICON = XpathString(f"{LIST_ITEM_NOTIFICATIONS}//*[@index='2'][@resource-id='android:id/widget_frame']")
LIST_ITEM_PRIVACY = XpathString("//*[contains(@content-desc, '###privacy_settings_entry')]")
LIST_ITEM_PRIVACY_TEXT = XpathString(f"{LIST_ITEM_PRIVACY}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_PRIVACY_LEADING_ICON = XpathString(f"{LIST_ITEM_PRIVACY}//*[@resource-id='android:id/icon']")
LIST_ITEM_PRIVACY_SUBMENU_ICON = XpathString(f"{LIST_ITEM_PRIVACY}//*[@index='2'][@resource-id='android:id/widget_frame']")
LIST_ITEM_LINKED_APP_ACCOUNTS = XpathString("//*[contains(@content-desc, '###eso_accounts_settings_entry')]")
LIST_ITEM_LINKED_APP_ACCOUNTS_TEXT = XpathString(f"{LIST_ITEM_LINKED_APP_ACCOUNTS}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_LINKED_APP_ACCOUNTS_LEADING_ICON = XpathString(f"{LIST_ITEM_LINKED_APP_ACCOUNTS}//*[@resource-id='android:id/icon']")
LIST_ITEM_LINKED_APP_ACCOUNTS_SUBMENU_ICON = XpathString(f"{LIST_ITEM_LINKED_APP_ACCOUNTS}//*[@index='2'][@resource-id='android:id/widget_frame']")
LIST_ITEM_SECURITY = XpathString("//*[contains(@content-desc, '###security_settings_entry')]")
LIST_ITEM_SECURITY_TEXT = XpathString(f"{LIST_ITEM_SECURITY}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_SECURITY_LEADING_ICON = XpathString(f"{LIST_ITEM_SECURITY}//*[@resource-id='android:id/icon']")
LIST_ITEM_SECURITY_SUBMENU_ICON = XpathString(f"{LIST_ITEM_SECURITY}//*[@index='2'][@resource-id='android:id/widget_frame']")
LIST_ITEM_FUNCTIONS_ON_DEMAND = XpathString("//*[contains(@content-desc, '###fod_settings_entry')]")
LIST_ITEM_FUNCTIONS_ON_DEMAND_TEXT = XpathString(f"{LIST_ITEM_FUNCTIONS_ON_DEMAND}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_FUNCTIONS_ON_DEMAND_LEADING_ICON = XpathString(f"{LIST_ITEM_FUNCTIONS_ON_DEMAND}//*[@resource-id='android:id/icon']")
LIST_ITEM_FUNCTIONS_ON_DEMAND_SUBMENU_ICON = XpathString(f"{LIST_ITEM_FUNCTIONS_ON_DEMAND}//*[@index='2'][@resource-id='android:id/widget_frame']")
LIST_ITEM_APPS = XpathString("//*[contains(@content-desc, '###apps_settings_entry')]")
LIST_ITEM_APPS_TEXT = XpathString(f"{LIST_ITEM_APPS}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_APPS_LEADING_ICON = XpathString(f"{LIST_ITEM_APPS}//*[@resource-id='android:id/icon']")
LIST_ITEM_APPS_SUBMENU_ICON = XpathString(f"{LIST_ITEM_APPS}//*[@index='2'][@resource-id='android:id/widget_frame']")
LIST_ITEM_STORAGE = XpathString("//*[contains(@content-desc, '###storage_settings_entry')]")
LIST_ITEM_STORAGE_TEXT = XpathString(f"{LIST_ITEM_STORAGE}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_STORAGE_LEADING_ICON = XpathString(f"{LIST_ITEM_STORAGE}//*[@resource-id='android:id/icon']")
LIST_ITEM_STORAGE_SUBMENU_ICON = XpathString(f"{LIST_ITEM_STORAGE}//*[@index='2'][@resource-id='android:id/widget_frame']")
LIST_ITEM_APP_FOR_DIGITAL_ASSISTANT = XpathString("//*[contains(@content-desc, '###assistant_and_voice_settings_entry')]")
LIST_ITEM_APP_FOR_DIGITAL_ASSISTANT_TEXT = XpathString(f"{LIST_ITEM_APP_FOR_DIGITAL_ASSISTANT}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_APP_FOR_DIGITAL_ASSISTANT_LEADING_ICON = XpathString(f"{LIST_ITEM_APP_FOR_DIGITAL_ASSISTANT}//*[@resource-id='android:id/icon']")
LIST_ITEM_APP_FOR_DIGITAL_ASSISTANT_SUBMENU_ICON = XpathString(f"{LIST_ITEM_APP_FOR_DIGITAL_ASSISTANT}//*[@index='2'][@resource-id='android:id/widget_frame']")

#LIST_ITEM_SYSTEM_LANGUAGESINPUT = XpathString("//android.widget.FrameLayout[@resource-id='com.android.car.settings:id/settings_recycler_view']/android.widget.FrameLayout[@resource-id='com.android.car.settings:id/car_ui_recycler_view']/androidx.recyclerview.widget.RecyclerView[@resource-id='com.android.car.settings:id/car_ui_internal_recycler_view']/android.widget.FrameLayout[@content-desc='###language_settings_entry']")
LIST_ITEM_SYSTEM_LANGUAGESINPUT = XpathString("//*[contains(@content-desc, '###languages_and_input_settings')]")
LIST_ITEM_SYSTEM_LANGUAGESINPUT_TEXT = XpathString(f"{LIST_ITEM_SYSTEM_LANGUAGESINPUT}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_SYSTEM_LANGUAGESINPUT_SUBMENU_ICON = XpathString(f"{LIST_ITEM_SYSTEM_LANGUAGESINPUT}//*[contains(@class, 'android.widget.ImageView')]")
LIST_ITEM_SYSTEM_LANGUAGESINPUT_LANGUAGES = XpathString("//*[contains(@content-desc, '###language_settings_entry')]")
LIST_ITEM_SYSTEM_LANGUAGESINPUT_KEYBOARD = XpathString("//*[contains(@content-desc, '###keyboard_entry')]")
LIST_ITEM_SYSTEM_LOCATION = XpathString("//*[contains(@content-desc, '###location_settings_entry')]")
LIST_ITEM_SYSTEM_LOCATION_TEXT = XpathString(f"{LIST_ITEM_SYSTEM_LOCATION}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_SYSTEM_LOCATION_SUBMENU_ICON = XpathString(f"{LIST_ITEM_SYSTEM_LOCATION}//*[contains(@class, 'android.widget.ImageView')]")
LIST_ITEM_SYSTEM_DATE_AND_TIME = XpathString("//*[contains(@content-desc, '###date_time_settings_entry')]")
LIST_ITEM_SYSTEM_DATE_AND_TIME_TEXT = XpathString(f"{LIST_ITEM_SYSTEM_DATE_AND_TIME}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_SYSTEM_DATE_AND_TIME_SUBMENU_ICON = XpathString(f"{LIST_ITEM_SYSTEM_DATE_AND_TIME}//*[contains(@class, 'android.widget.ImageView')]")
LIST_ITEM_SYSTEM_UNITS = XpathString("//*[contains(@content-desc, '###units_settings_entry')]")
LIST_ITEM_SYSTEM_UNITS_TEXT = XpathString(f"{LIST_ITEM_SYSTEM_UNITS}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_SYSTEM_UNITS_SUBMENU_ICON= XpathString(f"{LIST_ITEM_SYSTEM_UNITS}//*[contains(@class, 'android.widget.ImageView')]")
LIST_ITEM_SYSTEM_SOFTWARE_UPDATE = XpathString("//*[contains(@content-desc, '###system_update_settings')]")
LIST_ITEM_SYSTEM_SOFTWARE_UPDATE_TEXT = XpathString(f"{LIST_ITEM_SYSTEM_SOFTWARE_UPDATE}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_SYSTEM_SOFTWARE_UPDATE_SUBMENU_ICON = XpathString(f"{LIST_ITEM_SYSTEM_SOFTWARE_UPDATE}//*[contains(@class, 'android.widget.ImageView')]")
LIST_ITEM_SYSTEM_RESTORE_FACTORY_SETTINGS = XpathString("//*[contains(@content-desc, '###r2f_settings_entry')]")
LIST_ITEM_SYSTEM_RESTORE_FACTORY_SETTINGS_TEXT = XpathString(f"{LIST_ITEM_SYSTEM_RESTORE_FACTORY_SETTINGS}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_SYSTEM_RESTORE_FACTORY_SETTINGS_SUBMENU_ICON = XpathString(f"{LIST_ITEM_SYSTEM_RESTORE_FACTORY_SETTINGS}//*[contains(@class, 'android.widget.ImageView')]")
LIST_ITEM_SYSTEM_ABOUT = XpathString("//*[contains(@content-desc, '###about_settings_entry')]")
LIST_ITEM_SYSTEM_OPEN_SOURCE_SOFTWARE_NOTICE = XpathString("//*[contains(@content-desc, '###oem_ossn')]")
LIST_ITEM_OPEN_SOURCE_SW_NOTICE_TLI = XpathString("//*[contains(@content-desc, 'com.android.settings.category.ia.about_legal/technology.cariad.tli.app.osd.OsdTextActivity')]")
LIST_ITEM_SYSTEM_LEGAL_INFORMATION = XpathString("//*[@content-desc='###legal_information_entry']")
LIST_ITEM_SYSTEM_LEGAL_INFORMATION_TEXT = XpathString(f"{LIST_ITEM_SYSTEM_LEGAL_INFORMATION}//*[contains(@class, 'android.widget.TextView')]")
LIST_ITEM_SYSTEM_LEGAL_INFORMATION_SUBMENU_ICON = XpathString(f"{LIST_ITEM_SYSTEM_LEGAL_INFORMATION}//*[contains(@class, 'android.widget.ImageView')]")
LIST_ITEM_SYSTEM_LOCAL_SYSTEM_UPDATE = XpathString("//*[@content-desc='###com.android.settings.category.ia.system/com.android.car.systemupdater.SystemUpdaterActivity']")
LIST_ITEM_SYSTEM_ANDROID_AUTO = XpathString("//*[@content-desc='###com.android.settings.category.ia.system/com.google.android.apps.auto.aareceiver.settings.SettingsActivity']")

LIST_ITEM_OEM_PRIVACY_SETTINGS = XpathString("//*[contains(@content-desc, '###oem_privacy_settings_entry')]")

LIST_ITEM_SUMMARY_LANGUAGE = XpathString("//*[@content-desc='###language_settings_entry']/.//*[@resource-id='android:id/summary'][@class='android.widget.TextView'][@package='com.android.car.settings']")
LIST_ITEM_ABOUT_KERNEL_VERSION = XpathString("//*[contains(@content-desc, '###kernel_version')]")

# APP-INFO
APPS_APP_INFO_LIST_ITEM_MEDIA = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'com.android.car.media')]")
APPS_APP_INFO_LIST_ITEM_MEDIA_ICON = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'com.android.car.media')]//*[@resource-id='android:id/icon']")
APPS_APP_INFO_LIST_ITEM_MEDIA_TEXT = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'com.android.car.media')]//*[@resource-id='android:id/title']")
APPS_APP_INFO_LIST_ITEM_MEDIA_SECONDARY = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'com.harman.car.media.secondary')]")
APPS_APP_INFO_LIST_ITEM_MEDIA_SECONDARY_ICON = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'com.harman.car.media.secondary')]//*[@resource-id='android:id/icon']")
APPS_APP_INFO_LIST_ITEM_MEDIA_SECONDARY_TEXT = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'com.harman.car.media.secondary')]//*[@resource-id='android:id/title']")
APPS_APP_INFO_LIST_ITEM_MEDIA_CORE = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'com.harman.mediacoreservice')]")
APPS_APP_INFO_LIST_ITEM_MEDIA_CORE_ICON = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'com.harman.mediacoreservice')]//*[@resource-id='android:id/icon']")
APPS_APP_INFO_LIST_ITEM_MEDIA_CORE_TEXT = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'com.harman.mediacoreservice')]//*[@resource-id='android:id/title']")
APPS_APP_INFO_LIST_ITEM_RADIO = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.radio')]")
APPS_APP_INFO_LIST_ITEM_RADIO_ICON = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.radio')]//*[@resource-id='android:id/icon']")
APPS_APP_INFO_LIST_ITEM_RADIO_TEXT = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.radio')]//*[@resource-id='android:id/title']")
APPS_APP_INFO_LIST_ITEM_RPC = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.audi.remoteproductionclient')]")
APPS_APP_INFO_LIST_ITEM_RPC_ICON = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.audi.remoteproductionclient')]//*[@resource-id='android:id/icon']")
APPS_APP_INFO_LIST_ITEM_RPC_TEXT = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.audi.remoteproductionclient')]//*[@resource-id='android:id/title']")
APPS_APP_INFO_LIST_ITEM_SOFTWAREPDATE = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.audi.softwareupdate')]")
APPS_APP_INFO_LIST_ITEM_SOFTWAREPDATE_ICON = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.audi.softwareupdate')]//*[@resource-id='android:id/icon']")
APPS_APP_INFO_LIST_ITEM_SOFTWAREPDATE_TEXT = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.audi.softwareupdate')]//*[@resource-id='android:id/title']")
APPS_APP_INFO_LIST_ITEM_SOUND = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.sound.audi')]")
APPS_APP_INFO_LIST_ITEM_SOUND_ICON = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.sound.audi')]//*[@resource-id='android:id/icon']")
APPS_APP_INFO_LIST_ITEM_SOUND_TEXT = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.sound.audi')]//*[@resource-id='android:id/title']")
APPS_APP_INFO_LIST_ITEM_VIDEO = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.video')]")
APPS_APP_INFO_LIST_ITEM_VIDEO_ICON = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.video')]//*[@resource-id='android:id/icon']")
APPS_APP_INFO_LIST_ITEM_VIDEO_TEXT = XpathString(f"{LIST_CONTAINER}//*[contains(@content-desc, 'de.eso.video')]//*[@resource-id='android:id/title']")

# APPS APP-INFO VIEWALL
APPS_APP_INFO_VIEWALL_AUDI_ASSISTANT_LIST_ITEM = XpathString("//*[contains(@content-desc, '###oem_digital_assistant_settings_entry') or @content-desc='###technology.cariad.assistant']")
APPS_APP_INFO_VIEWALL_CAR_LIST_ITEM = XpathString("//*[@content-desc='###de.eso.car.audi']")
APPS_APP_INFO_VIEWALL_CAR2PHONE_LIST_ITEM = XpathString("//*[@content-desc='###technology.cariad.hcp3.car2phone.audi']")

APPS_APP_INFO_VIEWALL_EXPERIENCES_LIST_ITEM = XpathString(clu46="//*[@content-desc='###technology.cariad.interiorexperience.audi.experiences']",
														  clu55="//*[@content-desc='###technology.cariad.interiorexperience.icc.mqb.audi.experiences']")
APPS_APP_INFO_VIEWALL_LEGAL_LIST_ITEM = XpathString("//*[@content-desc='###com.valtech_mobility.legal.audi']")
APPS_APP_INFO_VIEWALL_NAVIGATION_LIST_ITEM = XpathString("//*[@content-desc='###technology.cariad.navi.audi']")
APPS_APP_INFO_VIEWALL_OBB_LIST_ITEM = XpathString("//*[@content-desc='###com.valtech_mobility.obb.audi']")
APPS_APP_INFO_VIEWALL_OEM_PRIVACY_SETTINGS_LIST_ITEM = XpathString("//*[@content-desc='###de.eso.privacymode']")
APPS_APP_INFO_VIEWALL_TLI_LIST_ITEM = XpathString("//*[@content-desc='###technology.cariad.trafficlightinformation']")
APPS_APP_INFO_VIEWALL_STORAGE_LIST_ITEM = XpathString("//*[contains(@content-desc, '###storage_settings_entry')]")


# for settings.SetSystemAppPermission
MAIN_LIST = XpathString("//*[contains(@resource-id,'car_ui_internal_recycler_view')]")
PERMISSIONS = XpathString("//*[@content-desc='###application_details_permissions']")
UNKNOWN = XpathString("//*[@content-desc='###de.eso.aem']")
AEM = XpathString("//*[@content-desc='###de.eso.aem']")
ANDROID_AUTO = XpathString("//*[@content-desc='###com.harman.connectivity.androidauto']")
APPLE_CARPLAY = XpathString("//*[@content-desc='###com.harman.connectivity.carplay.app']")
ATX = XpathString("//*[@content-desc='###com.github.uiautomator']")
AUDI_ASSISTANT = XpathString("//*[@content-desc='###technology.cariad.assistant']")
CAR = XpathString("//*[@content-desc='###de.eso.car.audi']")
EXPERIENCES = XpathString(clu46="//*[@content-desc='###technology.cariad.interiorexperience.audi.experiences']",
                          clu55="//*[@content-desc='###technology.cariad.interiorexperience.icc.mqb.audi.experiences']")
NAVIGATION = XpathString("//*[@content-desc='###technology.cariad.navi.audi']")
THEMES = XpathString("//*[@content-desc='###com.valtech_mobility.aaam.audi']")
