# -*- coding: utf-8 -*-
"""Module contains xpath of themes app (AudiAsAMatchmaker, com.valtech_mobility.aaam.audi package)."""

import enna_hcp_configuration.android.xpaths
from . import XpathString

if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.VTM import AudiasaMatchmaker as audiasamatchmaker
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.VTM import AudiasaMatchmaker as audiasamatchmaker
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.VTM import AudiasaMatchmaker as audiasamatchmaker
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.VTM import AudiasaMatchmaker as audiasamatchmaker
else:
	from enna_hcp_configuration.texts.CLU46.center.VTM import AudiasaMatchmaker as audiasamatchmaker

# pylint: disable=line-too-long, fixme
SETTINGS_OSD_AAAM = XpathString("//*[@content-desc='###com.android.settings.category.ia.about_legal/com.valtech_mobility.aaam.presentation.osd.OsdActivity']", context="settings.system_open_source_software_notice") # ger_ok
SETTINGS_OSD_AAAM_TEXT = XpathString("//*[@resource-id='com.valtech_mobility.aaam.audi:id/longTextDisclaimerScreen']/.//*[@class='android.widget.FrameLayout']")
THEMES_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audiasamatchmaker.aaam_selecttheme_themes__theme_tab__title}[@selected='true']")
CATALOG_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audiasamatchmaker.aaam_product_catalog__page__title}[@selected='true']")
CATALOG_INFO_TITLE = XpathString(f"//*{audiasamatchmaker.aaam_product_catalog_info__label_info_text}")
CATALOG_INFO_TOCATALOG_BUTTON = XpathString(f"//*{audiasamatchmaker.aaam_product_catalog_info__label_button}")

SETTINGS_TITLE = XpathString(f"//*[@resource-id='com.valtech_mobility.aaam.audi:id/titleTextViewRef'][@class='android.widget.TextView']{audiasamatchmaker.aaam_settings_main__title_line__title}")
SETTINGS_RECYCLERVIEW = XpathString("//*[@resource-id='com.valtech_mobility.aaam.audi:id/settings_recycler_view_list']")
SETTINGS_ABOUTUS_BUTTON = XpathString(f"//*[@resource-id='com.valtech_mobility.aaam.audi:id/listItemGrid2MainContent_textStart']{audiasamatchmaker.aaam_settings_main__legal_imprint__label}")
SETTINGS_IMPRINT_TITLE = XpathString(f"//*[@resource-id='com.valtech_mobility.legal.audi:id/titleTextViewRef'][@class='android.widget.TextView']{audiasamatchmaker.aaam_settings_main__legal_imprint__label}")
SETTINGS_DATA_PROTECTION_NOTES_BUTTON = XpathString(f"//*[@resource-id='com.valtech_mobility.aaam.audi:id/listItemGrid2MainContent_textStart']{audiasamatchmaker.aaam_settings_main__legal_data_protection__label}")
SETTINGS_DATA_PROTECTION_NOTES_TITLE = XpathString(f"//*[@resource-id='com.valtech_mobility.legal.audi:id/titleTextViewRef'][@class='android.widget.TextView']{audiasamatchmaker.aaam_settings_main__legal_data_protection__label}")
SETTINGS_OSSN_BUTTON = XpathString(f"//*[@resource-id='com.valtech_mobility.aaam.audi:id/listItemGrid2MainContent_textStart']{audiasamatchmaker.aaam_settings_main__legal_osd__label}")
SETTINGS_OSSN_TITLE = XpathString(f"//*[@resource-id='com.valtech_mobility.aaam.audi:id/titleTextViewRef'][@class='android.widget.TextView']{audiasamatchmaker.disclaimer_screen__aaam_skeleton_title__title}")
SETTINGS_OSSN_TITLE_BLOCKING_DISCLAIMER = XpathString(f"//*[@resource-id='com.valtech_mobility.aaam.audi:id/fullscreenDisclaimerText'][@class='android.widget.TextView']{audiasamatchmaker.aaam_info_themes__blocking_text__text_locking}")

CATALOG_POPUP_DATA_PRIVACY_TITLE = XpathString(f"//*[@class='android.widget.TextView']{audiasamatchmaker.aaam_selecttheme_themes_privacy__content__text}")
CATALOG_POPUP_DATA_PRIVACY_BUTTON = XpathString(f"//*[@class='android.widget.TextView']{audiasamatchmaker.aaam_selecttheme_themes_privacy__to_privacy__label}")
CATALOG_POPUP_CANCEL_BUTTON = XpathString(f"//*[@class='android.widget.TextView' or @class='android.widget.Button']{audiasamatchmaker.aaaam_selecttheme_themes_privacy__cancel__label}")
CATALOG_POPUP_FUNCTION_UNAVAILABLE_TITLE = XpathString(f"//*[@class='android.widget.TextView']{audiasamatchmaker.aaam_product_catalog_error__error_message__text}")
CATALOG_POPUP_FUNCTION_UNAVAILABLE_CANCEL_BUTTON = XpathString(f"//*[@class='android.widget.TextView']{audiasamatchmaker.aaam_app_not_available__cancel__label}")

CATALOG_HIGHLIGHTS_MORE_BUTTON = XpathString(f"//*[@class='android.widget.TextView']{audiasamatchmaker.aaam_product_catalog_promotions_channel_overview__page__title}")
CATALOG_HIGHLIGHTS_MORE_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audiasamatchmaker.aaam_product_catalog_promotions_channel_overview__page__title}[@selected='true']")

CATALOG_HIGHLIGHTS_MORE_WHALE_BUTTON = XpathString("//*[@class='android.widget.TextView'][@text='Whale' or @text='Buckelwal']")  # ToDo fehlt in TextTool
CATALOG_HIGHLIGHTS_MORE_WHALE_TITLE = XpathString("//*[@class='android.widget.HorizontalScrollView']/.//*[@content-desc='Whale' or @content-desc='Buckelwal'][@selected='true']")  # ToDo fehlt in TextTool
CATALOG_HIGHLIGHTS_MORE_WHALE_PREVIEW_BUTTON = XpathString(f"//*[@class='android.widget.TextView']{audiasamatchmaker.aaam_product_catalog_product_preview__button__label}")
CATALOG_HIGHLIGHTS_MORE_WHALE_PREVIEW_TITLE = XpathString("//*[@class='android.widget.HorizontalScrollView']/.//*[@content-desc='Whale' or @content-desc='Buckelwal'][@selected='true']")  # ToDo fehlt im TextTool
CATALOG_HIGHLIGHTS_MORE_WHALE_PREVIEW_TEXT = XpathString(f"//*[@class='android.widget.TextView']{audiasamatchmaker.aaam_product_catalog_product_preview_hint_description__content__text}")

CATALOG_AUDI_TITLE = XpathString("//*[@class='android.widget.HorizontalScrollView']/.//*[contains(@content-desc, 'Audi')][@selected='true']")
CATALOG_AUDI_MORE_BUTTON = XpathString("//*[@class='android.widget.TextView'][@text='Audi Sport']")

CATALOG_AUDI_AUDISPORT_MORE_TITLE = XpathString("//*[@class='android.widget.HorizontalScrollView']/.//*[contains(@content-desc, 'Audi Sport')][@selected='true']")
CATALOG_AUDI_AUDISPORT_MORE_WEBVIEW_TITLE = XpathString("//*[@class='android.webkit.WebView'][contains(@text, 'Audi Sport')]")
CATALOG_SEASONAL_HOLIDAYS_MORE_TITLE = XpathString("//*[@class='android.widget.HorizontalScrollView']/.//*[contains(@content-desc, 'Seasonal & Holidays')][@selected='true']")
CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_PREVIEW_BUTTON = XpathString(f"//*[@class='android.widget.TextView']{audiasamatchmaker.aaam_product_catalog_product_preview__button__label}")

CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_TITLE = XpathString("//*[@class='android.widget.HorizontalScrollView']/.//*[contains(@content-desc, 'Bonsai')][@selected='true']")
CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_PREVIEW_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*[contains(@content-desc, 'Bonsai')][@selected='true']"
                                                                  f"//*[@class='android.widget.TextView']{audiasamatchmaker.aaam_product_catalog_product_preview_hint_timer__content__text}")

CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_BUY_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audiasamatchmaker.aaam_product_catalog_product_order__button__label}[@selected='true']"
                                                              f"//*[@class='android.widget.TextView'][@text='Bonsai']")

CATALOG_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audiasamatchmaker.aaam_product_catalog__page__title}")
THEMES_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audiasamatchmaker.aaam_starter_screen__titleline__title}")
SETTINGS_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.aaam.audi:id/detailContainer']/.//*[@class='android.widget.ImageButton']")
SETTINGS_BACK_BUTTON = XpathString("//*[@content-desc='###Back']")

CATALOG_HIGHLIGHTS_BUTTON = XpathString(f"//*[@class='android.view.View']/.//*{audiasamatchmaker.aaam_product_catalog_promotions_channel_overview__page__title}")

CATALOG_LIST_CONTAINER = XpathString("//*[@scrollable='true']")
CATALOG_HIGHLIGHTS_BACK_BUTTON = XpathString("//*[@content-desc='###Back']")
CATALOG_HIGHLIGHTS_THEMES_4 =  XpathString("//*[@class='android.view.View']/.//*[@index='4']")
CATALOG_AUDI_BUTTON = XpathString("//*[@class='android.view.View']/.//*[@text='Audi']")
CATALOG_AUDI_BACK_BUTTON = XpathString("//*[@content-desc='###Back']")

CATALOG_SEASONAL_HOLIDAYS_BUTTON = XpathString("//*[@class='android.view.View']/.//*[@text='Seasonal & Holidays']")
CATALOG_SEASONAL_HOLIDAYS_MORE_BACK_BUTTON = XpathString("//*[@content-desc='###Back']")
CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_BUTTON = XpathString("//*[@class='android.view.View']/.//*[@text='Bonsai']")
CATALOG_SEASONAL_HOLIDAYS_MORE_BONSAI_BUY_BUTTON = XpathString(f"//*[@class='android.widget.TextView']{audiasamatchmaker.aaam_product_catalog_product_order__button__label}")

CONSENT_TO_ADVERTISING_TITLE = XpathString(f"//*{audiasamatchmaker.aaam_marketing_consent__title_line__title}[contains(@resource-id,'id/titleTextViewRef')]")
CONSENT_TO_ADVERTISING_ACCEPT_BUTTON = XpathString(f"//*{audiasamatchmaker.aaam_marketing_consent__title_line__title}/following::*{audiasamatchmaker.aaam_marketing_consent__accept_button__label}/..")
CONSENT_TO_ADVERTISING_DECLINE_BUTTON = XpathString(f"//*{audiasamatchmaker.aaam_marketing_consent__title_line__title}/following::*{audiasamatchmaker.aaam_marketing_consent__decline_button__label}/..")
