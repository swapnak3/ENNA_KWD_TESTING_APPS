# -*- coding: utf-8 -*-
"""Module contains xpath of experiences app."""
from enna_hcp_configuration.android.xpaths import XpathString


# pylint: disable=line-too-long
RECYCLERVIEW = XpathString("//*[@resource-id='technology.cariad.magic.engineering:id/design_navigation_view'][@class='androidx.recyclerview.widget.RecyclerView']", context="magic_engineering.connectivity")
CHECKED = XpathString("//*[@checked='true'][@class='android.widget.CheckedTextView']", context="magic_engineering.connectivity")
CONNECTIVITY_BUTTON = XpathString("//*[@resource-id='technology.cariad.magic.engineering:id/navigation_connectivity']", context="magic_engineering.connectivity")
ACCOUNT_SERVICE_BUTTON = XpathString("//*[@resource-id='technology.cariad.magic.engineering:id/navigation_account']", context="magic_engineering.connectivity")
SERVICE_MANAGEMENT_BUTTON = XpathString("//*[@resource-id='technology.cariad.magic.engineering:id/tabsFragment']", context="magic_engineering.connectivity")
SERVICE_MANAGEMENT_TTS_BUTTON = XpathString("//*[@content-desc='Transaction Type State']", context="magic_engineering.service_management_tts")
SERVICE_MANAGEMENT_VTTL_BUTTON = XpathString("//*[@content-desc='VTTL']", context="magic_engineering.service_management_tts")
MQTT_BUTTON = XpathString("//*[@resource-id='technology.cariad.magic.engineering:id/navigation_pubsub_subscription']", context="magic_engineering.connectivity")
MAGIC_SERVICE_BUTTON = XpathString("//*[@resource-id='technology.cariad.magic.engineering:id/navigation_magic']", context="magic_engineering.connectivity")
CONNECTIVITY_TITLE = XpathString("//*[@resource-id='technology.cariad.magic.engineering:id/navigation_connectivity']/./*[@checked='true']", context="magic_engineering.connectivity")
ACCOUNT_SERVICE_TITLE = XpathString("//*[@resource-id='technology.cariad.magic.engineering:id/navigation_account']/./*[@checked='true']", context="magic_engineering.account_service")
SERVICE_MANAGEMENT_TTS_TITLE = XpathString("//*[@resource-id='technology.cariad.magic.engineering:id/tabsFragment']/./*[@checked='true'] and //*[@content-desc='Transaction Type State'][@selected='true']", context="magic_engineering.service_management_tts")
SERVICE_MANAGEMENT_VTTL_TITLE = XpathString("//*[@resource-id='technology.cariad.magic.engineering:id/tabsFragment']/./*[@checked='true'] and //*[@content-desc='VTTL'][@selected='true']", context="magic_engineering.service_management_vttl")
MQTT_TITLE = XpathString("//*[@resource-id='technology.cariad.magic.engineering:id/navigation_pubsub_subscription']/./*[@checked='true']", context="magic_engineering.mqtt")
MAGIC_SERVICE_TITLE = XpathString("//*[@resource-id='technology.cariad.magic.engineering:id/navigation_magic']/./*[@checked='true']", context="magic_engineering.magic_service")
