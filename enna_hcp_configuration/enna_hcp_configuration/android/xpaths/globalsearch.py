# -*- coding: utf-8 -*-
"""Module contains xpath of globalsearch app."""
from . import XpathString

BACK_BUTTON = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'Back')]")
LIST_CONTAINER = XpathString("//*[@package='de.eso.globalsearch'][@class='androidx.recyclerview.widget.RecyclerView']")
SEARCH_FIELD_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.globalsearch:string/input_field__hint')]")
SETTINGS_BUTTON = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'SettingsButton')]")

MAIN_LIST_ITEM_RADIO_HEADER = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'SearchCategory_Radio_Headline')]")

SETTINGS_HEADLINE_ABOUT = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'de.eso.globalsearch:string/internal_settings__about_headline')]")
SETTINGS_HEADLINE_HISTORY = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'de.eso.globalsearch:string/internal_settings__history_headline_with_predictions')]")
SETTINGS_LIST_ITEM_APP_PREDICTION = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'DisplayAppPredictionsItem')]")
SETTINGS_LIST_ITEM_APP_PREDICTION_INFO_ICON = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'DisplayAppPredictionsInfo')]")
SETTINGS_LIST_ITEM_APP_PREDICTION_LIST_ICON = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'DisplayAppPredictionsItem')]//*[contains(@content-desc, 'de.eso.globalsearch:drawable/common_previoussearches_icon')]")
SETTINGS_LIST_ITEM_APP_PREDICTION_TEXT = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'DisplayAppPredictionsItem')]//*[contains(@content-desc, 'de.eso.globalsearch:string/internal_settings__display_app_predictions')]")
SETTINGS_LIST_ITEM_APP_PREDICTION_TOGGLE_BUTTON = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'DisplayAppPredictionsItem-switch')]")
SETTINGS_LIST_ITEM_DELETE_HISTORY = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'DeleteHistoryItem')]")
SETTINGS_LIST_ITEM_DELETE_HISTORY_ICON = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'DeleteHistoryItem')]//*[contains(@content-desc, 'de.eso.globalsearch:drawable/common_delete_icon')]")
SETTINGS_LIST_ITEM_DELETE_HISTORY_TEXT = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'DeleteHistoryItem')]//*[contains(@content-desc, 'de.eso.globalsearch:string/internal_settings__delete_history')]")
SETTINGS_LIST_ITEM_DISPLAY_HISTORY = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'DisplayHistoryItem')]")
SETTINGS_LIST_ITEM_DISPLAY_HISTORY_INFO_ICON = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'DisplayHistoryInfo')]")
SETTINGS_LIST_ITEM_DISPLAY_HISTORY_LIST_ICON = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'DisplayHistoryItem')]//*[contains(@content-desc, 'de.eso.globalsearch:drawable/common_previoussearches_icon')]")
SETTINGS_LIST_ITEM_DISPLAY_HISTORY_TEXT = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'DisplayHistoryItem')]//*[contains(@content-desc, 'de.eso.globalsearch:string/internal_settings__display_history')]")
SETTINGS_LIST_ITEM_DISPLAY_HISTORY_TOGGLE_BUTTON = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'DisplayHistoryItem-switch')]")
SETTINGS_LIST_ITEM_OPEN_SOURCE_DISCLAIMER = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'OpenSourceDisclaimerItem')]")
SETTINGS_LIST_ITEM_OPEN_SOURCE_DISCLAIMER_TEXT = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'OpenSourceDisclaimerItem')]//*[contains(@content-desc, 'de.eso.globalsearch:string/osd_disclaimer__element')]")
SETTINGS_LIST_ITEM_PRIVACY = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'PrivacyItem')]")
SETTINGS_LIST_ITEM_PRIVACY_TEXT = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'PrivacyItem')]//*[contains(@content-desc, 'de.eso.globalsearch:string/privacy__element')]")
SETTINGS_TITLE = XpathString("//*[@package='de.eso.globalsearch'][contains(@content-desc, 'de.eso.globalsearch:string/settings__title')]")
