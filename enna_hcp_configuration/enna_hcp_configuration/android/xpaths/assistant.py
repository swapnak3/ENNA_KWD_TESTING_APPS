# -*- coding: utf-8 -*-
"""Module contains xpath of digital assistant app."""
import enna_hcp_configuration.android.xpaths
from . import XpathString

# pylint: disable=line-too-long, fixme
if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.sem import Assistant as assistant
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.sem import Assistant as assistant
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.sem import Assistant as assistant
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.sem import Assistant as assistant
else:
	from enna_hcp_configuration.texts.CLU46.center.sem import Assistant as assistant


LIST_CONTAINER = XpathString("//*[@resource-id='technology.cariad.assistant:id/recyclerViewList'][@class='androidx.recyclerview.widget.RecyclerView']")
ASSISTANT_PACKAGE = XpathString("//*[@package='technology.cariad.assistant']")
ASSISTANT_RESOURCES = XpathString("//*[contains(@resource-id, 'technology.cariad.assistant')]")

# context markers
CONTEXT_IDENTIFIER = XpathString("//*[contains(@content-desc, 'basicLayout_activitySettings')]")
GENERAL_SELECTED_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{assistant.assist_settings_assistant_tile_activation}/../../*[@selected='true']")
PROACTIVITY_SELECTED_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{assistant.assist_settings_assistant_tile_proactivity}/../../*[@selected='true']")
SMART_ROUTINES_SELECTED_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{assistant.assist_settings_assistant_tile_routines}/../../*[@selected='true']")
HELP_SELECTED_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{assistant.assist_settings_assistant_tile_help}/../../*[@selected='true']")
HELP_HINTS_TITLE = XpathString(f"//*[@resource-id='technology.cariad.assistant:id/logoAndTitleLineContainer']/.//*{assistant.assist_settings_help_wizard_item_assistant}")
# HELP_SPEECHEXCLUSIVE_TITLE = XpathString("//*[contains(@content-desc, 'technology.cariad.assistant:string/assist_settings_help_item_speechexclusive_temperature') or contains(@content-desc, 'technology.cariad.assistant:string/assist_settings_help_item_speechexclusive_battery_load_status')]")  # pylint: disable=line-too-long # noqa
HELP_SPEECHEXCLUSIVE_TITLE = XpathString(f"//*{assistant.assist_settings_help_item_speechexclusive}")
HELP_SPEECHEXCLUSIVE_TEMPERATURE_TITLE = XpathString(f"//*{assistant.assist_settings_help_item_speechexclusive_temperature}")
HELP_SPEECHEXCLUSIVE_BATTERIE_TITLE = XpathString(f"//*{assistant.assist_settings_help_item_speechexclusive_battery_load_status}")
HELP_NAVIGATION_TITLE = XpathString("//*[contains(@content-desc, 'technology.cariad.assistant:string/assist_settings_help_navigation_item_munich') or contains(@content-desc,'technology.cariad.assistant:string/assist_settings_help_navigation_item_home') or contains(@content-desc,'technology.cariad.assistant:string/assist_settings_help_navigation_item_italian')]")  # pylint: disable=line-too-long # noqa
HELP_NAVIGATION_HOME_TITLE = XpathString(f"//*{assistant.assist_settings_help_navigation_item_home}")
HELP_CAR_TITLE = XpathString(f"//*{assistant.assist_settings_help_car_item_menu}")
HELP_PHONE_TITLE = XpathString("//*[contains(@content-desc,'technology.cariad.assistant:string/assist_settings_help_phone_item_connect')]")
# HELP_PHONE_TITLE = XpathString(f"//*{assistant.assist_settings_help_phone_item_connect}")
HELP_MEDIA_TITLE = XpathString(f"//*{assistant.assist_settings_help_media_item_title}")
HELP_CLIMATE_TITLE = XpathString("//*[contains(@content-desc,'technology.cariad.assistant:string/assist_settings_help_climate_item_lower_temperature')]")
HELP_FAQ_TITLE = XpathString("//*[@resource-id='technology.cariad.assistant:id/recyclerViewList'][contains(@content-desc,'frameLayout_fragmentFaq-list')]")
HELP_CONVERSATIONALS_TITLE = XpathString("//*[@resource-id='technology.cariad.assistant:id/recyclerViewList'][contains(@content-desc,'frameLayout_fragmentConversationals-list')]")
HELP_PLUG_AND_PLAY_TITLE = XpathString("//*[@resource-id='technology.cariad.assistant:id/recyclerViewList'][contains(@content-desc,'frameLayout_fragmentPlugAndPlay-list')]")
PHONE_RECOMMENDATIONS_TITLE = XpathString("//*[@content-desc='com.vwgroup.assistant:string/assist_settings_proactivity_item_phone_name']")

# buttons
BACK_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][contains(@content-desc, 'Back')]")
DELETE_ROUTINE = XpathString("//*[@content-desc='com.vwgroup.assistant:string/assist_settings_proactivity_item_recommendations']")
GENERAL_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{assistant.assist_settings_assistant_tile_activation}")
PROACTIVITY_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{assistant.assist_settings_assistant_tile_proactivity}")
SMART_ROUTINES_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{assistant.assist_settings_assistant_tile_routines}")
HELP_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{assistant.assist_settings_assistant_tile_help}")
HELP_HINTS_BUTTON = XpathString(f"//*{assistant.assist_settings_help_item_hints}")
HELP_SPEECHEXCLUSIVE_BUTTON =  XpathString(f"//*{assistant.assist_settings_help_item_speechexclusive}")
HELP_NAVIGATION_BUTTON =  XpathString(f"//*{assistant.assist_settings_help_item_navigation}")
HELP_CAR_BUTTON =  XpathString(f"//*{assistant.assist_settings_help_item_car}")
HELP_PHONE_BUTTON =  XpathString(f"//*{assistant.assist_settings_help_item_phone}")
HELP_MEDIA_BUTTON =  XpathString(f"//*{assistant.assist_settings_help_item_media}")
HELP_CLIMATE_BUTTON = XpathString(f"//*{assistant.assist_settings_help_item_climate}")
HELP_FAQ_BUTTON = XpathString(f"//*{assistant.assist_settings_help_item_faq_tab_caption}")
HELP_CONVERSATIONALS_BUTTON = XpathString(f"//*{assistant.assist_settings_help_item_conversationals_tab_caption}")
HELP_PLUG_AND_PLAY_BUTTON = XpathString(f"//*{assistant.assist_settings_help_item_plug_and_play_tab_caption}")
PROACTIVE_RECOMMENDATIONS_TITLE = XpathString(f"//*{assistant.assist_settings_assistant_tile_proactivity}")
JUST_TALK_SWITCH_BUTTON = XpathString("//*[contains(@content-desc, 'GeneralFragment/setting_listItemSettings_justTalk-switch')]")
SHORT_PROMPT_SWITCH_BUTTON = XpathString("//*[contains(@content-desc, 'GeneralFragment/setting_listItemSettings_shortPrompt-switch')]")
ACTIVATION_ITEM_SWITCH_BUTTON = XpathString("//*[contains(@content-desc, 'GeneralFragment/setting_listItemSettings_wuw-switch')]")
INFORMATION_FOR_THE_DRIVER_SWITCH_BUTTON = XpathString("//*[contains(@content-desc, 'GeneralFragment/setting_listItemSettings_virtualCockpitInformation-switch')]")
SOUND_SIGNAL_SWITCH_BUTTON = XpathString("//*[contains(@content-desc, 'GeneralFragment/setting_listItemSettings_earcon-switch')]")
INTERRUPT_SPOKEN_OUTPUTS_SWITCH_BUTTON = XpathString("//*[contains(@content-desc, 'GeneralFragment/setting_listItemSettings_voiceBargeIn-switch')]")
HELP_SPECIAL_FEATURES_BUTTON = XpathString("//*[contains(@content-desc, 'assist_settings_help_wizard_item_special_features_desc')]")
PROACTIVE_RECOMMONDATIONS_AND_ROUTINES_SWITCH = XpathString("//*[contains(@content-desc, 'ProactivityFragment/setting_listItem_recommendation-switch')]")
PROACTIVE_SWITCH = XpathString("//*[contains(@content-desc, 'ProactivityFragment/setting_listItem_recommendation-switch')]")
ACOUSTIC_MODE_SPEECH_AND_SOUNDS = XpathString("//*[contains(@content-desc, 'ProactivityFragment/setting_toggleButton_acousticModeSpeechAudio')]")
ACOUSTIC_MODE_SOUNDS_ONLY = XpathString("//*[contains(@content-desc, '###ProactivityFragment/setting_toggleButton_acousticModeOnlyAudio')]")
ACOUSTIC_MODE_OFF = XpathString("//*[contains(@content-desc, '###ProactivityFragment/setting_toggleButton_acousticModeOff')]")
