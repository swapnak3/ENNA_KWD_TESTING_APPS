# -*- coding: utf-8 -*-
"""Analyzer for the Traffic Lights Information debug app."""

import enna_hcp_configuration.android.contexts
from enna_hcp_configuration.android.xpaths import in_car_office
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathBlacklistWhitelistDetectorExtension, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import Element

WELCOME = Element("welcome", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[in_car_office.WELCOME_TITLE], must_not_exist=[in_car_office.WELCOME_SIGNING_CONNECTING_TITLE, in_car_office.WELCOME_SMARTPHONE_NOT_KNOWN_TITLE, in_car_office.WELCOME_ACCOUNT_ACCESS_NOT_POSSIBLE_TITLE]))  # pylint: disable=line-too-long # noqa
WELCOME_SIGNING_CONNECTING = Element("welcome_signin_connecting", ElementByXPathDetectorExtension([in_car_office.WELCOME_SIGNING_CONNECTING_TITLE]))
WELCOME_SIGNING_CONNECTING_SMARTPHONE_NOT_KNOWN = Element("welcome_signin_connecting_smartphone_not_known", ElementByXPathDetectorExtension([in_car_office.WELCOME_SMARTPHONE_NOT_KNOWN_TITLE]))
WELCOME_SIGNING_CONNECTING_ACCOUNT_ACCESS_NOT_POSSIBLE = Element("welcome_signin_connecting_account_access_not_possible", ElementByXPathDetectorExtension([in_car_office.WELCOME_ACCOUNT_ACCESS_NOT_POSSIBLE_TITLE]))

LINKING_TO_EMAIL_ACOUNT = Element("linking_to_email_account", ElementByXPathDetectorExtension([in_car_office.QR_CODE]))

EMAIL_OVERVIEW = Element("email_overview", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[in_car_office.EMAIL_OVERVIEW_TITLE], must_not_exist=[in_car_office.EMAIL_FILTER_TITLE]))
EMAIL_OVERVIEW_FILTER = Element("email_overview_filter_open", ElementByXPathDetectorExtension([in_car_office.EMAIL_FILTER_TITLE]))
EMAIL_OVERVIEW_SLIDE_OUT = Element("email_overview_slide_out", ElementByXPathDetectorExtension([in_car_office.EMAIL_INBOX_SLIDE_OUT_TITLE]))

READ_MAIL = Element("read_mail", ElementByXPathDetectorExtension([in_car_office.EMAIL_DETAILS_TITLE, in_car_office.EMAIL_ARROW_DROPDOWN_TITLE]))
READ_MAIL_ANSWER = Element("read_email_answer", ElementByXPathDetectorExtension([in_car_office.EMAIL_ANSWER_TITLE]))

CALENDAR = Element("calendar", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[in_car_office.SCREEN_CALENDAR_TITLE, in_car_office.CALENDAR_NO_EVENT_SELECTED_TITLE], must_not_exist=[in_car_office.DAY_NO_EVENTS_TITLE]))
CALENDAR_EVENT_SELECTED = Element("calendar_event_selected", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[in_car_office.SCREEN_CALENDAR_TITLE], must_not_exist=[in_car_office.CALENDAR_NO_EVENT_SELECTED_TITLE]))
CALENDAR_NO_EVENTS = Element("calendar_no_events", ElementByXPathDetectorExtension([in_car_office.SCREEN_CALENDAR_TITLE, in_car_office.DAY_NO_EVENTS_TITLE]))
CALENDAR_ALL_DAY_EVENTS = Element("calendar_all_day_events", ElementByXPathDetectorExtension([in_car_office.CALENDAR_ALL_DAY_EVENTS_TITLE]))
CALENDAR_EVENT_CONTACTS = Element("calendar_event_contacts", ElementByXPathDetectorExtension([in_car_office.CALENDAR_EVENT_CONTACTS_TITLE]))

SETTINGS_GENERAL = Element("settings_general", ElementByXPathDetectorExtension([in_car_office.SETTINGS_GENERAL_TITLE]))
SETTINGS_CALENDAR = Element("settings_calendar", ElementByXPathDetectorExtension([in_car_office.SETTINGS_CALENDAR_TITLE]))
SETTINGS_EDIT_ACCOUNT = Element("settings_edit_account", ElementByXPathDetectorExtension([in_car_office.SETTINGS_ACCOUNT_TITLE]))
SETTINGS_OSD = Element("settings_osd", ElementByXPathDetectorExtension([in_car_office.SETTINGS_OSD_TITLE]))
UNLINK_ACCOUNT_DIALOG = Element("unlink_account_dialog", ElementByXPathDetectorExtension([in_car_office.SETTINGS_UNLINK_ACCOUNT_DIALOG_TITLE]))
#SETTINGS_OSD_BUTTON_ON = Element("settings_osd_button_on", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[in_car_office.SETTINGS_OSD_BUTTON_ON], must_not_exist=[in_car_office.BLOCKING_DISCLAIMER]))

BLOCKING_DISCLAIMER = Element("blocking_disclaimer", ElementByXPathDetectorExtension([in_car_office.BLOCKING_DISCLAIMER]))

PRIVACY_SETTINGS = Element("privacy_settings", ElementByXPathDetectorExtension([in_car_office.PRIVACY_SETTINGS_TITLE]))
LOADING = Element("loading", ElementByXPathDetectorExtension([in_car_office.INIT_PROGRESS_BAR]))

CONTEXT = ContextAnalyzer("in_car_office", AppPackageDetectorExtension(["com.valtech_mobility.ico.audi"]))
CONTEXT.add_elements_from_module(globals())

# Add wait screens for in car office
enna_hcp_configuration.android.contexts.WAIT_SCREENS[LOADING.name] = {"wait_time": 30}
