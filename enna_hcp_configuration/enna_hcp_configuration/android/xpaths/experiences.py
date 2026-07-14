# -*- coding: utf-8 -*-
"""Module contains xpath of experiences app."""
import enna_hcp_configuration

from enna_hcp_configuration.android.xpaths import XpathString

if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.CARI import InteriorExperience as experience
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.CARI import InteriorExperience as experience
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.CARI import InteriorExperience as experience
else:
	from enna_hcp_configuration.texts.CLU46.center.CARI import InteriorExperience as experience

# pylint: disable=line-too-long

__app_package_name = "technology.cariad.interiorexperience.icc.mqb.audi.experiences" if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55 else "technology.cariad.interiorexperience.audi.experiences" # pylint: disable=invalid-name

MORE_BUTTON = XpathString("//*[@content-desc='###More']", context="experiences.mood") # ger_ok
SETTINGS_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/titleTextViewRef']{experience.int_ex_settings_title_tab_main_settings}", context="experiences.settings") # ger_ok
SETTINGS_RECYCLER_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/recyclerViewList']/.//*{experience.int_ex_settings_list_vertical_provider_info}", context="experiences.settings") # ger_ok
SETTINGS_BACK_BUTTON = XpathString("//*[@content-desc='###BackButton']", context="experiences.settings") # ger_ok
MOOD_MODESETTINGS_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/titleTextViewRef']{experience.int_ex_settings_title_view_scenario_settings}", context="experiences.mood_relaxing_modesettings_settings") # ger_ok
MOOD_RELAXING_MODESETTINGS_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][@content-desc='###Menu']", context="experiences.mood_relaxing") # ger_ok
MOOD_RELAXING_MODESETTINGS_SETTINGS_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{str(experience.int_ex_settings_title_tab_main_settings).replace("contains","starts-with")}", context="experiences.mood_relaxing_modesettings_settings") # ger_ok
MOOD_RELAXING_MODESETTINGS_SETTINGS_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{str(experience.int_ex_settings_title_tab_main_settings).replace("contains","starts-with")}[@selected='true']", context="experiences.mood_relaxing_modesettings_settings") # ger_ok
MOOD_RELAXING_MODESETTINGS_ADDITIONALSETTINGS_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{experience.int_ex_settings_title_tab_advanced_settings}", context="experiences.mood_relaxing_modesettings_settings") # ger_ok
MOOD_RELAXING_MODESETTINGS_ADDITIONALSETTINGS_NOTSELECTED_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{experience.int_ex_settings_title_tab_advanced_settings}[@selected='false']", context="experiences.mood_relaxing_modesettings_settings") # ger_ok
MOOD_RELAXING_MODESETTINGS_ADDITIONALSETTINGS_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{experience.int_ex_settings_title_tab_advanced_settings}[@selected='true']", context="experiences.mood_relaxing_modesettings_settings") # ger_ok
MOOD_RELAXING_MODESETTINGS_SETTINGS_BACK_BUTTON = XpathString("//*[@content-desc='###BackButton']", context="experiences.mood_relaxing_modesettings_settings") # ger_ok
MOOD_MODESETTINGS_SETTINGS_MUSIC_LIST = XpathString("//*[@class='android.view.ViewGroup']/.//*[@content-desc='first']")
MOOD_MODESETTINGS_SETTINGS_DURATION_LIST = XpathString("//*[@class='android.view.ViewGroup']/.//*[@content-desc='second']")
MOOD_MODESETTINGS_SETTINGS_DURATION_LIST_NR_5 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='5']")
MOOD_MODESETTINGS_SETTINGS_DURATION_LIST_NR_10 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='10']")
MOOD_MODESETTINGS_SETTINGS_DURATION_LIST_NR_15 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='15']")
MOOD_MODESETTINGS_SETTINGS_DURATION_LIST_NR_20 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='20']")
MOOD_MODESETTINGS_SETTINGS_DURATION_LIST_NR_30 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='30']")
MOOD_MODESETTINGS_SETTINGS_LIGHT_LIST = XpathString("//*[@class='android.view.ViewGroup']/.//*[@content-desc='third']")
MOOD_MODESETTINGS_SETTINGS_LIGHT_LIST_NR_1 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='1']")
MOOD_MODESETTINGS_SETTINGS_LIGHT_LIST_NR_2 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='2']")
MOOD_MODESETTINGS_SETTINGS_LIGHT_LIST_NR_3 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='3']")
MOOD_MODESETTINGS_SETTINGS_LIGHT_LIST_NR_4 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='4']")
MOOD_MODESETTINGS_SETTINGS_LIGHT_LIST_NR_5 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='5']")

MOOD_RELAXING_DECORATOR_ANIMATION_1 = XpathString("//*[@content-desc='se_0088_wellbeing_calming_1_content']", context="experiences.mood_relaxing") # ger_ok
MOOD_RELAXING_DECORATOR_ANIMATION_1_FULLSCREEN = XpathString("//*[@content-desc='###se_0088_wellbeing_calming_1_content'][@bounds='[0,0][2220,816]']", context="experiences.mood_relaxing")
MOOD_RELAXING_DECORATOR_ANIMATION_2 = XpathString("//*[@content-desc='se_0088_wellbeing_calming_2_content']", context="experiences.mood_relaxing") # ger_ok
MOOD_RELAXING_DECORATOR_ANIMATION_3 = XpathString("//*[@content-desc='se_0088_wellbeing_calming_3_content']", context="experiences.mood_relaxing") # ger_ok

MOOD_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{experience.int_ex_main_tab_layout_wellbeing}", context="experiences.mood") # ger_ok
MOOD_RELAXING_BUTTON = XpathString("//*[@class='androidx.recyclerview.widget.RecyclerView']/.//*[@content-desc='###CALM']", context="experiences.mood")
MOOD_RELAXING_POPUP_CHECK_BOX = XpathString(f"//*[@content-desc='###{__app_package_name}:string/int_ex_full_content_popup_checkbox']", context="experiences.mood_relaxing_popup") # ger_ok
MOOD_RELAXING_OK_BUTTON = XpathString(f"//*{experience.int_ex_ok}", context="experiences.mood_relaxing_popup") # ger_ok
MOOD_RELAXING_EMBEDDED_ARROWLEFT= XpathString("//*[@content-desc='###imageViewArrowLeft']", context="experiences.mood_relaxing") # ger_ok
MOOD_RELAXING_EMBEDDED_ARROWRIGHT= XpathString("//*[@content-desc='###imageViewArrowRight']", context="experiences.mood_relaxing") # ger_ok
MOOD_RELAXING_EMBEDDED_TIME_BAR= XpathString("//*[@content-desc='###timeBarMedia-seekbar']", context="experiences.mood_relaxing") # ger_ok
MOOD_EMBEDDED_TIME_BAR= XpathString("//*[@content-desc='###timeBarMedia-seekbar']") # ger_ok
MOOD_EMBEDDED_PLAYING_TIME= XpathString("//*[@content-desc='###timeBar-elapsedTime']") # ger_ok
MOOD_EMBEDDED_REMAINING_TIME= XpathString("//*[@content-desc='###timeBar-remainingTime']") # ger_ok

MOOD_HARMONISING_BUTTON = XpathString("//*[@class='androidx.recyclerview.widget.RecyclerView']/.//*[@content-desc='###FLOW']", context="experiences.mood") # ger_ok
MOOD_HARMONISING_POPUP_CHECK_BOX = XpathString(f"//*[@content-desc='###{__app_package_name}:string/int_ex_full_content_popup_checkbox']", context="experiences.mood_harmonising_popup") # ger_ok
MOOD_HARMONISING_OK_BUTTON = XpathString(f"//*{experience.int_ex_ok}", context="experiences.mood_harmonising_popup") # ger_ok
MOOD_HARMONISING_EMBEDDED_ARROWLEFT= XpathString("//*[@content-desc='###imageViewArrowLeft']", context="experiences.mood_harmonising") # ger_ok
MOOD_HARMONISING_EMBEDDED_ARROWRIGHT= XpathString("//*[@content-desc='###imageViewArrowRight']", context="experiences.mood_harmonising") # ger_ok
MOOD_HARMONISING_EMBEDDED_TIME_BAR= XpathString("//*[@content-desc='###timeBarMedia-seekbar']", context="experiences.mood_harmonising") # ger_ok
MOOD_HARMONISING_DECORATOR_ANIMATION_1 = XpathString("//*[@content-desc='se_0088_wellbeing_harmonising_1_content']", context="experiences.mood_harmonising") # ger_ok
MOOD_HARMONISING_DECORATOR_ANIMATION_1_FULLSCREEN = XpathString("//*[@content-desc='###se_0088_wellbeing_harmonising_1_content'][@bounds='[0,0][2220,816]']", context="experiences.mood_harmonising")
MOOD_HARMONISING_DECORATOR_ANIMATION_2 = XpathString("//*[@content-desc='se_0088_wellbeing_harmonising_2_content']", context="experiences.mood_harmonising") # ger_ok
MOOD_HARMONISING_DECORATOR_ANIMATION_3 = XpathString("//*[@content-desc='se_0088_wellbeing_harmonising_3_content']", context="experiences.mood_harmonising") # ger_ok

MOOD_ANIMATING_BUTTON = XpathString("//*[@class='androidx.recyclerview.widget.RecyclerView']/.//*[@content-desc='###ENERGY']", context="experiences.mood") # ger_ok
MOOD_ANIMATING_POPUP_CHECK_BOX = XpathString(f"//*[@content-desc='###{__app_package_name}:string/int_ex_full_content_popup_checkbox']", context="experiences.mood_animating_popup") # ger_ok
MOOD_ANIMATING_OK_BUTTON = XpathString(f"//*{experience.int_ex_ok}", context="experiences.mood_animating_popup") # ger_ok
MOOD_ANIMATING_EMBEDDED_ARROWLEFT= XpathString("//*[@content-desc='###imageViewArrowLeft']", context="experiences.mood_animating") # ger_ok
MOOD_ANIMATING_EMBEDDED_ARROWRIGHT= XpathString("//*[@content-desc='###imageViewArrowRight']", context="experiences.mood_animating") # ger_ok
MOOD_ANIMATING_EMBEDDED_TIME_BAR= XpathString("//*[@content-desc='###timeBarMedia-seekbar']", context="experiences.mood_animating") # ger_ok
MOOD_ANIMATING_DECORATOR_ANIMATION_1 = XpathString("//*[@content-desc='se_0088_wellbeing_activating_1_content']", context="experiences.mood_animating") # ger_ok
MOOD_ANIMATING_DECORATOR_ANIMATION_1_FULLSCREEN = XpathString("//*[@content-desc='###se_0088_wellbeing_activating_1_content'][@bounds='[0,0][2220,816]']", context="experiences.mood_animating")
MOOD_ANIMATING_DECORATOR_ANIMATION_2 = XpathString("//*[@content-desc='se_0088_wellbeing_activating_2_content']", context="experiences.mood_animating") # ger_ok
MOOD_ANIMATING_DECORATOR_ANIMATION_3 = XpathString("//*[@content-desc='se_0088_wellbeing_activating_3_content']", context="experiences.mood_animating") # ger_ok

MOOD_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{experience.int_ex_main_tab_layout_wellbeing}[@selected='true']", context="experiences.mood") # ger_ok

MOOD_RELAXING_POPUP_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/popupTitle']{experience.int_ex_wellbeing_tile_view_calm}", context="experiences.mood_relaxing_popup") # ger_ok
MOOD_RELAXING_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/tabLayoutTitleLineContainer']/.//*[({str(experience.int_ex_main_tab_layout_wellbeing)[1:-1]}) and contains(@text,' - ') and ({str(experience.int_ex_wellbeing_tile_view_calm)[1:-1]})]", context="mood.relaxing") # ok
MOOD_RELAXING_FULLSCREEN_TITLE = XpathString("//*[@content-desc='###se_0088_wellbeing_calming_1_content'][@bounds='[0,0][2220,816]']", context="experiences.mood_relaxing_fullscreen") # ok
MOOD_RELAXING_FULLSCREEN_CLICK = XpathString("//*[@content-desc='se_0088_wellbeing_calming_1_content']") # ok

MOOD_HARMONISING_POPUP_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/popupTitle']{experience.int_ex_wellbeing_tile_view_flow}", context="experiences.mood_harmonising_popup") # ger_ok
MOOD_HARMONISING_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/tabLayoutTitleLineContainer']/.//*[({str(experience.int_ex_main_tab_layout_wellbeing)[1:-1]}) and contains(@text,' - ') and ({str(experience.int_ex_wellbeing_tile_view_flow)[1:-1]})]", context="mood.relaxing") # ok
MOOD_HARMONISING_FULLSCREEN_TITLE = XpathString("//*[@content-desc='###se_0088_wellbeing_harmonising_1_content'][@bounds='[0,0][2220,816]']", context="experiences.mood_harmonising_fullscreen") # ok

MOOD_ANIMATING_POPUP_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/popupTitle']{experience.int_ex_wellbeing_tile_view_energy}", context="experiences.mood_animating_popup") # ger_ok
MOOD_ANIMATING_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/tabLayoutTitleLineContainer']/.//*[({str(experience.int_ex_main_tab_layout_wellbeing)[1:-1]}) and contains(@text,' - ') and ({str(experience.int_ex_wellbeing_tile_view_energy)[1:-1]})]", context="mood.relaxing") # ok
MOOD_ANIMATING_FULLSCREEN_TITLE = XpathString("//*[@content-desc='###se_0088_wellbeing_activating_1_content'][@bounds='[0,0][2220,816]']", context="experiences.mood_animating_fullscreen") # ok

MOOD_RELAXING_CLOSE_BUTTON = XpathString("//*[@content-desc='###CloseButton']", context="experiences.mood_relaxing") # ger_ok
MOOD_HARMONISING_CLOSE_BUTTON = XpathString("//*[@content-desc='###CloseButton']", context="experiences.mood_harmonising") # ger_ok
MOOD_ANIMATING_CLOSE_BUTTON = XpathString("//*[@content-desc='###CloseButton']", context="experiences.mood_animating") # ger_ok

ENTERTAINMENT_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{experience.int_ex_main_tab_layout_entertain}[@selected='true']", context="experiences.entertainment") # ger_ok
ENTERTAINMENT_MUSIC_POPUP_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/popupTitle']{experience.int_ex_entertain_tile_view_music}") # ger_ok
ENTERTAINMENT_MUSIC_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/titleTextViewRef'][({str(experience.int_ex_main_tab_layout_entertain)[1:-1]}) and contains(@text,' - ') and ({str(experience.int_ex_entertain_tile_view_music)[1:-1]})]", context="experiences.entertainment_music") # ok
ENTERTAINMENT_MUSIC_FULLSCREEN_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/overlayVideoView']", context="experiences.entertainment_music_fullscreen") # ok
ENTERTAINMENT_MUSIC_FULLSCREEN_CLICK = XpathString("//*[@selectable='true']", context="experiences.entertainment_music_fullscreen") # ok

ENTERTAINMENT_MUSIC_GRACENOTE_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][@content-desc='###Gracenote']", context="experiences.entertainment_music") # ger_ok
ENTERTAINMENT_MUSIC_MODESETTINGS_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][@content-desc='###Menu']", context="experiences.entertainment_music") # ger_ok
ENTERTAINMENT_MUSIC_MODESETTINGS_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/titleTextViewRef']{experience.int_ex_settings_title_view_scenario_settings}", context="experiences.entertainment_music_modesettings_settings") # ger_ok
ENTERTAINMENT_MUSIC_MODESETTINGS_SETTINGS_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{experience.int_ex_settings_title_tab_main_settings}[@selected='true']", context="experiences.entertainment_music_modesettings_settings") # ger_ok
ENTERTAINMENT_MUSIC_MODESETTINGS_SETTINGS_MUSIC_LIST = XpathString("//*[@class='android.view.ViewGroup']/.//*[@content-desc='fourth']", context="experiences.entertainment_music_modesettings_settings")
ENTERTAINMENT_MUSIC_MODESETTINGS_SETTINGS_LIGHT_LIST = XpathString("//*[@class='android.view.ViewGroup']/.//*[@content-desc='sixth']", context="experiences.entertainment_music_modesettings_settings")
ENTERTAINMENT_MUSIC_MODESETTINGS_SETTINGS_LIGHT_LIST_NR_1 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='1']")
ENTERTAINMENT_MUSIC_MODESETTINGS_SETTINGS_LIGHT_LIST_NR_2 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='2']")
ENTERTAINMENT_MUSIC_MODESETTINGS_SETTINGS_LIGHT_LIST_NR_3 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='3']")
ENTERTAINMENT_MUSIC_MODESETTINGS_SETTINGS_LIGHT_LIST_NR_4 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='4']")
ENTERTAINMENT_MUSIC_MODESETTINGS_SETTINGS_LIGHT_LIST_NR_5 = XpathString("//*[@class='android.widget.LinearLayout']/.//*[@content-desc='5']")

ENTERTAINMENT_MUSIC_IMAGE_VIEW_COVER =  XpathString("//*[@content-desc='###imageViewCover']", context="experiences.entertainment_music") # ger_ok
ENTERTAINMENT_MUSIC_LYRICSTEXT_TITLE = XpathString("//*[contains(@text, 'lyrics') or contains(@text, 'Liedtexte') or contains(@text, 'Texte')]") #_todo not found in Texttool, untested
ENTERTAINMENT_MUSIC_LYRICSTEXT_FIRST_LINE = XpathString("//*[@content-desc='###metadataFirstLineInformationEmbedded']", context="experiences.entertainment_music") # ger_ok
ENTERTAINMENT_MUSIC_LYRICSTEXT_SECOND_LINE = XpathString("//*[@content-desc='###metadataSecondLineInformationEmbedded']", context="experiences.entertainment_music") # ger_ok
ENTERTAINMENT_MUSIC_LYRICSTEXT_THIRD_LINE =  XpathString("//*[@content-desc='###metadataThirdLineInformationEmbedded']", context="experiences.entertainment_music") # ger_ok
ENTERTAINMENT_MUSIC_SKIP_BW_BUTTON = XpathString(f"//*[@class='android.widget.ImageView'][@content-desc='###{__app_package_name}:drawable/ic_e82d_media_skip_backward']", context="experiences.entertainment_music") # ger_ok
ENTERTAINMENT_MUSIC_PLAY_BUTTON = XpathString(f"//*[@class='android.widget.ImageView'][@content-desc='###{__app_package_name}:drawable/ic_e0f5_play']", context="experiences.entertainment_music") # ger_ok
ENTERTAINMENT_MUSIC_PAUSE_BUTTON = XpathString(f"//*[@class='android.widget.ImageView'][@content-desc='###{__app_package_name}:drawable/ic_e82f_pause']", context="experiences.entertainment_music") # ger_ok
ENTERTAINMENT_MUSIC_SKIP_FW_BUTTON = XpathString(f"//*[@class='android.widget.ImageView'][@content-desc='###{__app_package_name}:drawable/ic_e82c_media_skip_forward']", context="experiences.entertainment_music") # ger_ok
ENTERTAINMENT_MUSIC_MEDIA_SOURCE_ICON = XpathString("//*[@class='android.widget.ImageView'][@content-desc='###media_source_icon']", context="experiences.entertainment_music") # ger_ok
ENTERTAINMENT_MUSIC_FULLSCREEN_MODE = XpathString("//*[@content-desc='vp2_scenario_view'][@bounds='[0,0][2220,816]']", context="experiences.entertainment_music")

ENTERTAINMENT_VIDEO_INFO_POPUP_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/popupTitle']{experience.int_ex_entertain_tile_view_film}") # not found, untested
ENTERTAINMENT_VIDEO_POPUP_CHECK_BOX = XpathString(f"//*[@content-desc='###{__app_package_name}:string/int_ex_full_content_popup_checkbox']", context="experiences.entertainment_video_info_popup") # ger_ok
ENTERTAINMENT_VIDEO_OK_BUTTON = XpathString(f"//*{experience.int_ex_ok}", context="experiences.entertainment_video_info_popup") # ger_ok
ENTERTAINMENT_VIDEO_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/titleTextViewRef'][({str(experience.int_ex_main_tab_layout_entertain)[1:-1]}) and contains(@text,' - ') and ({str(experience.int_ex_entertain_tile_view_film)[1:-1]})]", context="experiences.entertainment_music") # ok
ENTERTAINMENT_VIDEO_THIRD_PARTY_APP_1 = XpathString("//*[@content-desc='###IconHolder0']", context="experiences.entertainment_video") # ger_ok
ENTERTAINMENT_VIDEO_THIRD_PARTY_APP_1_NAME = XpathString("//*[@content-desc='###TextHolder0']", context="experiences.entertainment_video") # ger_ok
ENTERTAINMENT_VIDEO_THIRD_PARTY_APP_2 = XpathString("//*[@content-desc='###IconHolder1']", context="experiences.entertainment_video") # ger_ok
ENTERTAINMENT_VIDEO_THIRD_PARTY_APP_2_NAME = XpathString("//*[@content-desc='###TextHolder1']", context="experiences.entertainment_video") # ger_ok

ENTERTAINMENT_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{experience.int_ex_main_tab_layout_entertain}", context="experiences.entertainment") # ger_ok
ENTERTAINMENT_MUSIC_BUTTON = XpathString("//*[@class='androidx.recyclerview.widget.RecyclerView']/.//*[@content-desc='###MUSIC']", context="experiences.entertainment") # ger_ok
ENTERTAINMENT_MUSIC_OK_BUTTON = XpathString(f"//*{experience.int_ex_ok}", context="experiences.entertainment_music_popup") # ger_ok
ENTERTAINMENT_MUSIC_CLOSE_BUTTON = XpathString("//*[@content-desc='###CloseButton']", context="experiences.entertainment_music") # ger_ok
ENTERTAINMENT_VIDEO_BUTTON = XpathString("//*[@class='androidx.recyclerview.widget.RecyclerView']/.//*[@content-desc='###MOVIE']", context="experiences.entertainment") # ger_ok
ENTERTAINMENT_VIDEO_CLOSE_BUTTON = XpathString("//*[@content-desc='###CloseButton']", context="experiences.entertainment_video") # ger_ok
ENTERTAINMENT_VIDEO_CANCEL_BUTTON = XpathString(f"//*{experience.int_ex_cancel}") # not found, untested

POWERNAP_TITLE = XpathString(f"//*[@resource-id='{__app_package_name}:id/logoAndTitleLineContainer']/.//*{experience.int_ex_main_tab_layout_powernap}[@selected='true']", context="experiences.powernap")
POWERNAP_BUTTON = XpathString(f"//*[@resource-id='{__app_package_name}:id/logoAndTitleLineContainer']/.//*{experience.int_ex_main_tab_layout_powernap}", context="experiences.powernap")
POPUP_TITLE = XpathString(f"//*[contains(@content-desc, 'popupMessage')]{experience.int_ex_full_content_popup_disclaimer}[contains(@package, '{__app_package_name}')]") # untested
POWERNAP_TILE_LOS_ANGELES = XpathString("//*[@content-desc='###LOS_ANGELES']", context="experiences.powernap") # ger_ok
POWERNAP_TILE_FOREST = XpathString("//*[@content-desc='###FOREST']", context="experiences.powernap") # ger_ok
POWERNAP_TILE_UNIVERSE = XpathString("//*[@content-desc='###UNIVERSE']", context="experiences.powernap") # ger_ok
