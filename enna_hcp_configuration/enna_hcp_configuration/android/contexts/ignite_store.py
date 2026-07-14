# -*- coding: utf-8 -*-
"""Analyzer for the ignite store app."""

import enna_hcp_configuration.android.contexts
from enna_hcp_configuration.android.xpaths import ignite_store, aem
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathDetectorExtension, ElementByXPathBlacklistWhitelistDetectorExtension
from enna_hcp_configuration.common.base import Element

INIT = Element("init", ElementByXPathDetectorExtension([ignite_store.INIT_TITLE]))
BLOCKED_DRIVING = Element("blocked_driving", ElementByXPathDetectorExtension([ignite_store.BLOCKING_DISCLAIMER_TITLE]))
BLOCKED_DRIVING_AUTOMATIC_UPDATES = Element("SHOP_BLOCKING_DISCLAIMER_AUTOMATIC_UPDATES", ElementByXPathDetectorExtension([ignite_store.BLOCKING_DISCLAIMER_AUTOMATIC_UPDATES_TITLE]))
LOADING_SCREEN = Element("loading_screen", ElementByXPathDetectorExtension([ignite_store.SKELETON_TITLE]))
CAR_FUNCTIONALITY = Element("car_functionality", ElementByXPathDetectorExtension([ignite_store.CAR_FUNCTIONALITY_SELECTED_TITLE]))
APPS = Element("apps", ElementByXPathDetectorExtension([ignite_store.APPS_SELECTED_TITLE]))
MY_APPLICATIONS = Element("my_applications", ElementByXPathDetectorExtension([ignite_store.MY_APPLICATIONS_SELECTED_TITLE]))
APP_DESCRIPTION_FOD = Element("app_description_fod", ElementByXPathDetectorExtension([ignite_store.PURCHASE_BUTTON_FOD_SCREEN_TITLE]))
APP_DESCRIPTION = Element("app_description", ElementByXPathDetectorExtension([ignite_store.DETAIL_PAGE_ABOUT_THIS_APP_TITLE]))
SETTINGS = Element("settings", ElementByXPathDetectorExtension([ignite_store.SETTINGS_TITLE]))
SEARCH = Element("search", ElementByXPathDetectorExtension([ignite_store.SEARCH_TITLE]))
PRIVACY_MODE = Element("privacy_mode_screen", ElementByXPathDetectorExtension([ignite_store.PRIVACY_MODE_TITLE]))
NOT_IN_THIS_CAR = Element("not_in_this_car", ElementByXPathDetectorExtension([ignite_store.NOT_IN_THIS_CAR_TITLE]))

SETTINGS_COUNTRY_SELECTION_DISCLAIMER_WHITELIST = [ignite_store.COUNTRY_SELECTION_DISCLAIMER_HEADLINE_TITLE, ignite_store.DISCLAIMER_CHANGE_SETTINGS_TITLE]
SETTINGS_COUNTRY_SELECTION_DISCLAIMER = Element("SETTINGS_COUNTRY_SELECTION_DISCLAIMER", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=SETTINGS_COUNTRY_SELECTION_DISCLAIMER_WHITELIST,
		must_not_exist=[ignite_store.CONTINUE_BUTTON]))

SETTINGS_COUNTRY_SELECTION_DISCLAIMER_TWO_OPTIONS_DETECTORS = [ignite_store.COUNTRY_SELECTION_DISCLAIMER_HEADLINE_TITLE, ignite_store.DISCLAIMER_CHANGE_SETTINGS_TITLE, ignite_store.CONTINUE_BUTTON]
SETTINGS_COUNTRY_SELECTION_DISCLAIMER_TWO_OPTIONS = Element("SETTINGS_COUNTRY_SELECTION_DISCLAIMER_TWO_OPTIONS", ElementByXPathDetectorExtension(SETTINGS_COUNTRY_SELECTION_DISCLAIMER_TWO_OPTIONS_DETECTORS))

DEEP_CHECKOUT_LEGAL_LIST = Element("DEEP_CHECKOUT_LEGAL_LIST", ElementByXPathDetectorExtension([ignite_store.DEEP_CHECKOUT_LEGAL_LIST_HEADLINE]))
POPUP_DIALOG = Element("POPUP_dialog_question", ElementByXPathDetectorExtension([ignite_store.POPUP_QUESTION]))
POPUP_AUTOMATIC_UPDATE = Element("POPUP_AUTOMATIC_UPDATE", ElementByXPathDetectorExtension([ignite_store.POPUP_AUTOMATIC_UPDATES]))
POPUP_SETTINGS_AUTOMATIC_UPDATE_INFO_THIRDPARTY = Element("POPUP_SETTINGS_AUTOMATIC_UPDATE_INFO_THIRDPARTY", ElementByXPathDetectorExtension([ignite_store.AUTOMATIC_UPDATES_POP_UP_THIRD_PARTY]))
POPUP_SETTINGS_AUTOMATIC_UPDATE_INFO_GROUPAPP = Element("POPUP_SETTINGS_AUTOMATIC_UPDATE_INFO_GROUPAPP", ElementByXPathDetectorExtension([ignite_store.AUTOMATIC_UPDATES_POP_UP_GROUP_APPS]))
POPUP_INITIAL_AUTOMATIC_UPDATES = Element("POPUP_INITIAL_AUTOMATIC_UPDATES", ElementByXPathDetectorExtension([ignite_store.POPUP_WELCOME_HEADLINE, ignite_store.OK_BUTTON]))
USER_MISSING = Element("user_missing", ElementByXPathDetectorExtension([ignite_store.DIALOG_USER_MISSING]))
POPUP_COMMUNICATION_ERROR = Element("POPUP_communication_error", ElementByXPathDetectorExtension([ignite_store.DIALOG_COMMUNICATION_ERROR]))
POPUP_GENERIC_ERROR = Element("POPUP_GENERIC_ERROR", ElementByXPathDetectorExtension([ignite_store.GENERIC_ERROR]))
NOTE = Element("note", ElementByXPathDetectorExtension([ignite_store.NOTE_TITLE]))
SUPPLIER_COUNTRY = Element("suppplier_country", ElementByXPathDetectorExtension([ignite_store.SUPPLIER_COUNTRY_HEADLINE]))
LICENSE_PACKAGES = Element("license_packages", ElementByXPathDetectorExtension([ignite_store.LICENSE_PACKAGES_HEADLINE]))
VARIANT_SELECTION = Element("variant_selection", ElementByXPathDetectorExtension([ignite_store.VARIANT_SELECTION_TITLE]))
CHECKOUT_SCREEN = Element("checkout_screen", ElementByXPathDetectorExtension([ignite_store.QR_CODE, ignite_store.PURCHASE_INFORMATION_HEADLINE]))
ABOUT_THIS_APP = Element("about_this_app", ElementByXPathDetectorExtension([ignite_store.DETAIL_PAGE_ABOUT_THIS_APP_HEADLINE]))
READ_MORE = Element("read_more", ElementByXPathDetectorExtension([ignite_store.DETAIL_PAGE_READ_MORE_HEADLINE]))
WHATS_NEW = Element("whats_new", ElementByXPathDetectorExtension([ignite_store.DETAIL_PAGE_WHATS_NEW_HEADLINE]))
IMAGE_LARGE = Element("image_large", ElementByXPathDetectorExtension([ignite_store.LICENSE_IMAGE_LARGE_HEADLINE]))
OPEN_SOURCE = Element("open_source", ElementByXPathDetectorExtension([ignite_store.OPEN_SOURCE_HEADLINE]))
CHECKOUT_OPTION_DIALOG = Element("CHECKOUT_OPTION_DIALOG", ElementByXPathDetectorExtension([ignite_store.CHECKOUT_DIALOG_HEADLINE]))
CHECK_ORDER = Element("CHECK_ORDER", ElementByXPathDetectorExtension([ignite_store.SHOPPING_CART_HEADLINE]))
BILLING_INFORMATION = Element("BILLING_INFORMATION", ElementByXPathDetectorExtension([ignite_store.BILLING_INFORMATION_HEADLINE]))
COMPLETE_PROCESS_NOT_CHECKED = Element("COMPLETE_PROCESS_NOT_CHECKED", ElementByXPathDetectorExtension([ignite_store.PURCHASE_INFORMATION_HEADLINE, ignite_store.CHECKBOX_ACCEPT_TERMS_NOTCHECKED]))
COMPLETE_PROCESS_CHECKED = Element("COMPLETE_PROCESS_CHECKED", ElementByXPathDetectorExtension([ignite_store.PURCHASE_INFORMATION_HEADLINE, ignite_store.CHECKBOX_ACCEPT_TERMS_CHECKED]))
ORDER_CREATION = Element("ORDER_CREATION", ElementByXPathDetectorExtension([ignite_store.ORDERCREATION]))
ORDER_SENT = Element("ORDER_SENT", ElementByXPathDetectorExtension([ignite_store.PURCHASECONFIRMATION_HEADLINE]))
TERMS_OF_USE_QR = Element("TERMS_OF_USE_QR", ElementByXPathDetectorExtension([ignite_store.TERMS_OF_USE_HEADLINE, ignite_store.QR_CODE]))
TERMS_OF_USE_WEB = Element("TERMS_OF_USE_WEB", ElementByXPathDetectorExtension([ignite_store.TERMS_OF_USE_HEADLINE, ignite_store.WEB_VIEW]))
PRIVACY_POLICY_QR = Element("PRIVACY_POLICY_QR", ElementByXPathDetectorExtension([ignite_store.PRIVACY_POLICY_HEADLINE, ignite_store.QR_CODE]))
PRIVACY_POLICY_WEB = Element("PRIVACY_POLICY_WEB", ElementByXPathDetectorExtension([ignite_store.PRIVACY_POLICY_HEADLINE, ignite_store.WEB_VIEW]))
THIRD_PARTY_LEGAL_INFO = Element("THIRD_PARTY_LEGAL_INFO", ElementByXPathDetectorExtension([ignite_store.THIRD_PARTY_LEGAL_INFO_CONTENT]))
INCLUDED_APPS = Element("INCLUDED_APPS", ElementByXPathDetectorExtension([ignite_store.INCLUDED_APPS_HEADLINE]))
USAGE_INSTRUCTIONS = Element("USAGE_INSTRUCTIONS", ElementByXPathDetectorExtension([ignite_store.USAGE_INSTRUCTIONS_HEADLINE]))
PRICE_INFORMATION_LEGAL = Element("SHOP_FUNCTIONS_PRICE_INFO_TEXT_VIEW", ElementByXPathDetectorExtension([ignite_store.PRICE_INFORMATION]))
ABOUT_THIS_FUNCTION = Element("SHOP_FUNCTIONS_DETAIL_ABOUT_THE_FUNCTION", ElementByXPathDetectorExtension([ignite_store.DETAIL_PAGE_ABOUT_THIS_FUNCTION_HEADLINE]))
TAB1_IMPRINT = Element("SHOP_FUNCTIONS_LEGAL_TEXT_VIEW_IMPRINT", ElementByXPathDetectorExtension([ignite_store.IMPRINT]))
TAB1_PRIVACY_POLICY = Element("SHOP_FUNCTIONS_LEGAL_TEXT_VIEW_PRIVACY_POLICY", ElementByXPathDetectorExtension([ignite_store.DATA_PRIVACY]))
POPUP_INSTALLATION = Element("POPUP_SHOP_INSTALLATION_PROGRESS_DETAIL_PAGE", ElementByXPathDetectorExtension([ignite_store.INSTALLATION_POPUP_CHECKBOX, ignite_store.INSTALLATION_POPUP_TEXT]))

AEM_IGNITE_STORE_ENGINEERING_MENUE = Element("aem_ignite_store_engineering_menu", ElementByXPathDetectorExtension([aem.IGNITE_STORE_ENGINEERING_MENU_BACK_BUTTON]))

CONTEXT = ContextAnalyzer("ignite_store", AppPackageDetectorExtension(["com.harman.ignite.appstore.audi"]))
CONTEXT.add_elements_from_module(globals())

# Add wait screens for ignite store
enna_hcp_configuration.android.contexts.WAIT_SCREENS[INIT.name] = {"wait_time": 20}
enna_hcp_configuration.android.contexts.WAIT_SCREENS[LOADING_SCREEN.name] = {"wait_time": 15}
enna_hcp_configuration.android.contexts.WAIT_SCREENS[ORDER_CREATION.name] = {"wait_time": 50}
