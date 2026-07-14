# -*- coding: utf-8 -*-
"""Module contains xpath of in car office app."""
import enna_hcp_configuration.android.xpaths
from enna_hcp_configuration.texts.CLU46.center.VTM import Calendar as calendar
from . import XpathString

if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.VTM import AudiInCarOffice as ico
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.VTM import AudiInCarOffice as ico
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.VTM import AudiInCarOffice as ico
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.VTM import AudiInCarOffice as ico
else:
	from enna_hcp_configuration.texts.CLU46.center.VTM import AudiInCarOffice as ico


# pylint: disable=line-too-long
WELCOME_TITLE = XpathString(f"//*{ico.home_screen__ico_app_tile__label}[@resource-id='com.valtech_mobility.ico.audi:id/titleTextViewRef']", context="in_car_office.welcome_signin_connecting")
WELCOME_SIGNING_CONNECTING_TITLE = XpathString("//*[contains(@content-desc,'com.valtech_mobility.ico.audi:string/ico_welcome_screen__welcome_message__text')]", context="in_car_office.welcome_signin_connecting")
WELCOME_SMARTPHONE_USE_BUTTON = XpathString(f"//*[@resource-id='com.valtech_mobility.ico.audi:id/operationPanelItemTextView']{ico.ico_welcome_screen__smartphone_mode_button__label}", context="in_car_office.welcome_signin_connecting")
WELCOME_ACCOUNT_USE_BUTTON = XpathString(f"//*[@resource-id='com.valtech_mobility.ico.audi:id/operationPanelItemTextView']{ico.ico_welcome_screen__cloud_mode_button__label}", context="in_car_office.welcome_signin_connecting")
WELCOME_SMARTPHONE_NOT_KNOWN_TITLE = XpathString(f"//*{ico.ico_calendar_no_device_connected_screen__content__text}", context="in_car_office.welcome")
WELCOME_SMARTPHONE_NOT_KNOWN_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]", context="in_car_office.welcome")
WELCOME_ACCOUNT_ACCESS_NOT_POSSIBLE_TITLE = XpathString(f"//*{ico.ico_no_online_user_screen__main_content__text}") # untested, not seen, yet
WELCOME_ACCOUNT_ACCESS_NOT_POSSIBLE_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]") # untested, not seen, yet

EMAIL_OVERVIEW_TITLE = XpathString(f"//*[@resource-id='android:id/text1']{ico.ico_inbox_screen__title_line_inbox_tab__title}[@selected='true']", context="in_car_office.email_overview")
EMAIL_DETAILS_TITLE = XpathString("//*[contains(@content-desc,'com.valtech_mobility.ico.audi:drawable/ico_reply_sender')] and //*[@resource-id='com.valtech_mobility.ico.audi:id/titleTextView']", context="in_car_office.read_mail")
EMAIL_ANSWER_TITLE = XpathString(f"//*[{str(ico.ico_reply_templates_screen__template_get_back_to_you_later__text)[1:-1]} or {str(ico.ico_reply_templates_screen__template_better_call_me__text)[1:-1]}]", context="in_car_office.read_email_answer")
SETTINGS_GENERAL_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.ico.audi:id/toggle_main_settings'][@selected='true']", context="in_car_office.settings_general")
SETTINGS_CALENDAR_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.ico.audi:id/toggle_calendar_settings'][@selected='true']", context="in_car_office.settings_calendar")
SETTINGS_ACCOUNT_TITLE = XpathString(f"//*{ico.ico_settings_screen__edit_account__text}[@resource-id='com.valtech_mobility.ico.audi:id/titleTextViewRef']")
WELCOME_CONNECT_ACCOUNT_BUTTON = XpathString("//*[contains(@content-desc, 'OperationPanelItem-Mit deinem Account anmelden')]") # untested, not found, yet
TAB_CALENDAR_BUTTON = XpathString(f"//*{ico.ico_settings_screen__title_line_calendar_tab__title}", context="in_car_office.email_overview")
SETTINGS_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.ico.audi:id/menuActionContainer']//*[@class='android.widget.ImageButton']", context="in_car_office.email_overview")
TAB_EMAIL_BUTTON = XpathString(f"//*{ico.ico_inbox_screen__title_line_inbox_tab__title}", context="in_car_office.email_overview")
BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]", context="in_car_office.settings_general")
CLOSE_BUTTON = XpathString("//*[contains(@content-desc,'scalableOverlayTitle-closeButton')]") # untested, not found, yet
POPUP_NO_BUTTON = XpathString("//*[@resource-id='android:id/button2']")
POPUP_YES_BUTTON = XpathString("//*[@resource-id='android:id/button1']")
PRIVACY_SETTINGS_TITLE = XpathString("//*[contains(@content-desc, 'OperationPanelItem-Datenschutzeinstellungen') or contains(@content-desc, 'OperationPanelItem-Privacy settings')]") # untested, not found, yet
PRIVACY_OK_BUTTON = XpathString("//*[contains(@content-desc,'OperationPanelItem-OK')]") # untested, not found, yet
PRIVACY_PRIVACY_SETTINGS_BUTTON = XpathString("//*[contains(@content-desc, 'OperationPanelItem-Datenschutzeinstellungen') or contains(@content-desc, 'OperationPanelItem-Privacy settings')]") # untested, not found, yet
INIT_PROGRESS_BAR = XpathString("//*[@resource-id='com.valtech_mobility.ico.audi:id/initScreenProgressBar']") # untested, not found, yet
QR_CODE = XpathString("//*[@resource-id='com.valtech_mobility.ico.audi:id/qrcode']") # untested, not found, yet
SETTINGS_LIST = XpathString("//*[@resource-id='com.valtech_mobility.ico.audi:id/settings_list']", context="in_car_office.settings_general")
SETTINGS_TAB_CALENDAR_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.ico.audi:id/toggle_calendar_settings']", context="in_car_office.settings_general")
SETTINGS_TAB_GENERAL_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.ico.audi:id/toggle_main_settings']", context="in_car_office.settings_general")
SETTINGS_EDIT_ACCOUNT_BUTTON = XpathString(f"//*[@resource-id='com.valtech_mobility.ico.audi:id/listItemGrid2MainContent_textStart']{ico.ico_settings_screen__edit_account__text}/../..", context="in_car_office.settings_general")
SETTINGS_DISCONNECT_ACCOUNT_BUTTON = XpathString(f"//*[@resource-id='com.valtech_mobility.ico.audi:id/listItemGrid2MainContent_textStart']{ico.ico_settings_screen__unlink_account__text}/../..",
 												 cl53=f"//*{ico.ico_settings_screen__unlink_account__text}", context="in_car_office.settings_edit_account") # untested, not found, yet
EMAIL_FILTER_TITLE = XpathString("//*[contains(@content-desc, 'com.valtech_mobility.ico.audi:string/ico_inbox_screen__title_line_popup_filter_unread')]", context="in_car_office.email_overview_filter_open")
EMAIL_ARROW_DROPDOWN_TITLE = XpathString("//*[contains(@content-desc,'com.valtech_mobility.ico.audi:drawable/black_listarrow_right_animatable') or contains(@content-desc,'com.valtech_mobility.ico.audi:drawable/black_listarrow_down_animatable')]") # untested, not found, yet
EMAIL_INBOX_SLIDE_OUT_TITLE = XpathString("//*[contains(@content-desc,'com.valtech_mobility.ico.audi:string/ico_reply_slide_out__titleline__title')]") # untested, not found, yet
SCREEN_CALENDAR_TITLE = XpathString(f"//*[@resource-id='android:id/text1']{ico.ico_settings_screen__title_line_calendar_tab__title}[@selected='true']", context="in_car_office.calendar")
CALENDAR_NO_EVENT_SELECTED_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.ico.audi:id/text_events_amount']", context="in_car_office.calendar")
CALENDAR_ALL_DAY_EVENTS_TITLE = XpathString(f"//*[@resource-id='com.valtech_mobility.ico.audi:id/titleTextViewRef']{calendar.calendar_allday_events_screen__all_day_events__title}", context="in_car_office.calendar_all_day_events")
#CALENDAR_EVENT_CONTACTS_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.ico.audi:id/titleTextViewRef'][contains(@text,'Contact participants') or contains(@text,'Teilnehmer kontaktieren')]")
CALENDAR_EVENT_CONTACTS_TITLE = XpathString(f"//*[@resource-id='com.valtech_mobility.ico.audi:id/titleTextViewRef']{ico.calendar_allday_events_screen__all_day_events__title if enna_hcp_configuration.android.xpaths.CLUSTER == 'clu53' else calendar.calendar_allday_events_screen__all_day_events__title}", context="in_car_office.calendar_all_day_events")
SETTINGS_UNLINK_ACCOUNT_DIALOG_TITLE = XpathString(f"//*{ico.ico_settings_screen__unlink_account__dialog_msg}", context="in_car_office.unlink_account_dialog")
SETTINGS_OSD_TITLE = XpathString(f"//*[@resource-id='com.valtech_mobility.ico.audi:id/titleTextViewRef']{ico.ico_settings_screen__open_source_licences__text}", context="in_car_office.settings_osd")
# SETTINGS_OSD_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]")
DAY_NO_EVENTS_TITLE = XpathString(f"//*{ico.calendar_day_no_events_all_day_events_available_text if enna_hcp_configuration.android.xpaths.CLUSTER == 'clu53' else calendar.calendar_day_no_events_no_all_day_events_available_text}", context="in_car_office.calendar_event_selected")
BLOCKING_DISCLAIMER = XpathString("//*[contains(@content-desc,'com.valtech_mobility.ico.audi:string/calendar_source_blocking_toast__blocking__text')]") # untested, not found yet
EMAIL_FILTER_BUTTON = XpathString("//*[contains(@content-desc,'inboxSourceSelectionButton')]", context="in_car_office.email_overview")
ANSWER_EMAIL_BUTTON = XpathString("//*[contains(@content-desc,'com.valtech_mobility.ico.audi:drawable/ico_reply_sender')]", context="in_car_office.read_mail")

NAVIGATION_BAR_FAVORITE = XpathString("//*[contains(@content-desc, 'com.valtech_mobility.ico.audi/com.valtech_mobility.ico.MainActivity')][contains(@resource-id,'navigation_bar_favorite')]")

MESSAGING_SHOW_ALL_ATTACHMENTS = XpathString("//*[contains(@content-desc, 'com.valtech_mobility.ico.audi:drawable/ico_messaging_attachment')]")
MESSAGING_OPTIONS_READ = XpathString(f"//*{str(ico.ico_inbox_screen__email_start_readout_button__content_description).replace('@text', '@content-desc')}[@resource-id='com.valtech_mobility.ico.audi:id/listItemButton_0']")
MESSAGING_OPTIONS_MORE = XpathString(f"//*{str(ico.ico_inbox_screen__email_options_button__content_description).replace('@text', '@content-desc')}[@resource-id='com.valtech_mobility.ico.audi:id/listItemButton_1']")

MESSAGING_OPTIONS_REPLY_SENDER = XpathString("//*[contains(@content-desc, 'com.valtech_mobility.ico.audi:drawable/ico_reply_sender')][@resource-id='com.valtech_mobility.ico.audi:id/operationPanelItemImageView']")
MESSAGING_OPTIONS_REPLY_ALL = XpathString("//*[contains(@content-desc, 'com.valtech_mobility.ico.audi:drawable/ico_reply_all')][@resource-id='com.valtech_mobility.ico.audi:id/operationPanelItemImageView']")
