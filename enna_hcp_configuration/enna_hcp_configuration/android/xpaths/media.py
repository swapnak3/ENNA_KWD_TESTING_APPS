# -*- coding: utf-8 -*-
"""Module contains xpath of media app."""
import enna_hcp_configuration.android.xpaths
from enna_hcp_configuration.texts.CLU46.center.com.harman import mediacoreservice # only available in texttool of CL46
from enna_hcp_configuration.texts.CLU46.center.CARI import UBIInCarApp # only available in texttool of CL46
from . import XpathString

#only found in cl46, needed for both

if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.de.eso import video
	from enna_hcp_configuration.texts.CLU55.center.de.esolutions.alexa import audi
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.de.eso import video
	from enna_hcp_configuration.texts.CLU53.center.de.esolutions.alexa import audi
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.de.eso import video
	from enna_hcp_configuration.texts.CLU51.center.de.esolutions.alexa import audi
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.de.eso import video
	from enna_hcp_configuration.texts.CLU48.center.de.esolutions.alexa import audi
else:
	from enna_hcp_configuration.texts.CLU46.center.de.eso import video
	from enna_hcp_configuration.texts.CLU46.center.de.esolutions.alexa import audi


# All Xpaths were equal for cl46/53
ALBUMS_TITLE = XpathString(f"//*{mediacoreservice.hcp3_ext_albums}[@resource-id='com.android.car.media:id/car_ui_toolbar_title']") # chose translation that "fits"
ALL_TITLE = XpathString("//*[contains(@text,'all')][@resource-id='com.android.car.media:id/car_ui_toolbar_title']") #_todo not found in texttool
APPS_SCREEN_CONTENT_TITLE = XpathString("//*[@resource-id='de.eso.launcheraudi:id/mediaAppGrid']") # chose translation that "fits"
ARTISTS_TITLE = XpathString(f"//*{mediacoreservice.hcp3_ext_artists}[@resource-id='com.android.car.media:id/car_ui_toolbar_title']")
BACK_BUTTON = XpathString("//*[@resource-id='com.android.car.media:id/car_ui_toolbar_nav_icon_container']")
# ERROR_MESSAGE = XpathString("//*[@resoure-id='com.android.car.media:id/error_message']")
ERROR_TITLE = XpathString("//*[@content-desc='errorText']")
# FILE_LIST_ALBUMS_GROUP = XpathString("//*[@text='Albums' or @text='Alben']") #_todo
# FILE_LIST_ARTISTS_GROUP = XpathString("//*[@text='Artists' or @text='Interpreten']") #_todo
# FILE_LIST_FOLDERS_GROUP = XpathString("//*[@text='Folders' or @text='Ordner']") #_todo
# FILE_LIST_GENRES_GROUP = XpathString("//*[@text='Genres']") #_todo
# FILE_LIST_ITEM_GO_BACK = XpathString("//*[@content-desc='Back']")
# FILE_LIST_ITEM_NAME = XpathString("//*[@resource-id='com.android.car.media:id/title']")
# FILE_LIST_ITEM_RIGHT_ARROW = XpathString("//*[@resource-id='com.android.car.media:id/right_arrow']")
# FILE_LIST_ITEM_THUMBNAIL = XpathString("//*[@resource-id='com.android.car.media:id/thumbnail']")
# FILE_LIST_ITEM_TITLE = XpathString("//*[@resource-id='com.android.car.media:id/car_ui_toolbar_title']")
# FILE_LIST_NO_ITEMS = XpathString("//*[@text='No media available for browsing here' or @text='Medien sind für diese Liste nicht verfügbar']") #_todo
# FILE_LIST_TAB_ICON = XpathString("//*[@resource-id='com.android.car.media:id/car_ui_toolbar_menu_item_icon']")
# FILE_LIST_TAB_LOGO = XpathString("//*[@resource-id='com.android.car.media:id/car_ui_toolbar_title_logo']")
# FILE_LIST_TAB_TEXT = XpathString("//*[@resource-id='com.android.car.media:id/car_ui_toolbar_tab_item_text']")
FOLDERS_ALL_BUTTON = XpathString("//*[@index='0'][@resource-id='com.android.car.media:id/container']")
FOLDERS_LIST = XpathString("//*[@resource-id='com.android.car.media:id/car_ui_internal_recycler_view']")
FOLDERS_TITLE = XpathString(f"//*{mediacoreservice.hcp3_ext_folders}[@resource-id='com.android.car.media:id/car_ui_toolbar_title']") # chose translation that "fits"
FORMATS_TITLE = XpathString("//*[contains(@text, 'formats')][@resource-id='com.android.car.media:id/car_ui_toolbar_title']") #_todo not found in texttool
GENERIC_LIST = XpathString("//*[@resource-id='com.android.car.media:id/car_ui_internal_recycler_view'][@scrollable='true']")
# GENERIC_LIST_ENTRY = XpathString("//*[@resource-id='com.android.car.media:id/container']")
# GENERIC_LIST_ENTRY_FIRST_VISIBLE = XpathString("//*[@index='0'][@resource-id='com.android.car.media:id/item_container']")
# GENERIC_LIST_ENTRY_LAST_VISIBLE = XpathString("//*[@index='3'][@resource-id='com.android.car.media:id/item_container']")
# GENERIC_LIST_ENTRY_TITLE = XpathString("//*[@resource-id='com.android.car.media:id/title']")
# GENERIC_LIST_ENTRY_TITLED = XpathString("//*[contains(@text, '{}')]") #_todo
# GENERIC_PLAYLIST_ENTRY = XpathString("//*[@resource-id='com.android.car.media:id/container']")
# GENERIC_PLAYLIST_ENTRY_FIRST_VISIBLE = XpathString("//*[@index='0'][@resource-id='com.android.car.media:id/item_container']")
# GENERIC_PLAYLIST_ENTRY_LAST_VISIBLE = XpathString("//*[@index='4'][@resource-id='com.android.car.media:id/item_container']")
# GENERIC_PLAYLIST_ENTRY_TITLE = XpathString("//*[@resource-id='com.android.car.media:id/queue_list_item_title']")
# GENERIC_PLAYLIST_ENTRY_TITLED = XpathString("//*[contains(@text, '{}')]") #_todo
GENERIC_PLAYLIST_TITLE = XpathString("//*[@resource-id='com.android.car.media:id/queue_list'][@scrollable='true']")
GENRES_TITLE = XpathString(f"//*{mediacoreservice.hcp3_ext_genres}[@resource-id='com.android.car.media:id/car_ui_toolbar_title']") # chose translation that "fits"
# LIST_CONTAINER = XpathString("//*[@content-desc='com.android.car.ui.utils.ROTARY_CONTAINER'][@scrollable='true']")
# LOADING_SCREEN = XpathString("//*[@resource-id='com.android.car.media:id/error_message'][@text='Loading content…']") #_todo
# MAIN_ACTIVE_SOURCE_LOGO = XpathString("//*[@resource-id='com.android.car.media:id/car_ui_toolbar_title_logo_container']")
MAIN_ALBUMS_BUTTON = XpathString(f"//*{mediacoreservice.hcp3_ext_albums}[@resource-id='com.android.car.media:id/title']") # chose translation that "fits"
MAIN_ARTISTS_BUTTON = XpathString(f"//*{mediacoreservice.hcp3_ext_artists}[@resource-id='com.android.car.media:id/title']") # chose translation that "fits"
MAIN_FOLDERS_BUTTON = XpathString(f"//*{mediacoreservice.hcp3_ext_folders}[@resource-id='com.android.car.media:id/title']") # chose translation that "fits"
MAIN_GENRES_BUTTON = XpathString(f"//*{mediacoreservice.hcp3_ext_genres}[@resource-id='com.android.car.media:id/title']") # chose translation that "fits"
MAIN_PLAYLISTS_BUTTON = XpathString(f"//*{mediacoreservice.hcp3_ext_playlists}[@resource-id='com.android.car.media:id/title']") # chose translation that "fits"
MAIN_RECENTS_BUTTON = XpathString(f"//*{mediacoreservice.hcp3_ext_recents}[@resource-id='com.android.car.media:id/title']") # chose translation that "fits"
# MAIN_TITLE = XpathString("//*[contains(@text, 'TA_MEDIA') or contains(@text, 'W40')][@resource-id='com.android.car.media:id/car_ui_toolbar_title']") # "Name" of USB-Stick, no translation
MAIN_TITLE = XpathString("//*[contains(@text, 'TA_MEDIA') or contains(@text, 'W40') or contains(@text, 'USB ') or contains(@text, 'INTENSO')][@resource-id='com.android.car.media:id/car_ui_toolbar_title']") # "Name" of USB-Stick, no translation
MAIN_TRACKS_BUTTON = XpathString("//*[contains(@text, 'Tracks') or contains(@text, 'Titel')][@resource-id='com.android.car.media:id/title']") #_todo
MAIN_VIDEOS_BUTTON = XpathString(f"//*{mediacoreservice.hcp3_ext_videos}[@resource-id='com.android.car.media:id/title']") # chose translation that "fits"
# MUTE_ICON = XpathString("//*[contains(@content-desc, 'Mute')]")
# NP_ALBUM_TITLE = XpathString("//*[@resource-id='com.android.car.media:id/album_title']")
# NP_ARTIST = XpathString("//*[@resource-id='com.android.car.media:id/artist']")
# NP_CURRENT_PLAYTIME = XpathString("//*[@resource-id='com.android.car.media:id/current_time']")
# NP_MAX_PLAYTIME = XpathString("//*[@resource-id='com.android.car.media:id/max_time']")
# NP_METADATA_CONTAINER = XpathString("//*[@resource-id='com.android.car.media:id/metadata_container']")
NP_MINIMIZE_BUTTON = XpathString("//*[@content-desc='Back' or @content-desc='Zurück']") #_todo not found in texttool
# NP_OVERFLOW = XpathString("//*[@resource-id='com.android.car.media:id/overflow']")
# NP_PLAY_PAUSE = XpathString("//*[@resource-id='com.android.car.media:id/play_pause_stop']")
NP_PLAYLIST_BUTTON = XpathString("//*[@resource-id='com.android.car.media:id/car_ui_toolbar_menu_item_icon_container']")
NP_PLAYLIST_BUTTON_SELECTED = XpathString("//*[@class='android.widget.FrameLayout'][@package='com.android.car.media'][@clickable='true']")
# NP_REPEAT_MODE_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][@resource-id='']")
NP_SEEK_BAR_TITLE = XpathString("//*[@resource-id='com.android.car.media:id/playback_seek_bar']")
# NP_SKIP_BACKWARD = XpathString("//*[@resource-id='com.android.car.media:id/skip_prev']")
# NP_SKIP_FORWARD = XpathString("//*[@resource-id='com.android.car.media:id/skip_next']")
# NP_SONG_TITLE = XpathString("//*[@resource-id='com.android.car.media:id/title']")
# NP_SS_TITLE = XpathString("//*[contains(@text, 'Now playing')][@resource-id='de.eso.video:id/titleTextView']") #_todo
NP_TITLE = XpathString(f"//*[@resource-id='com.android.car.media:id/car_ui_toolbar_title']{video.video_now_playing_screen_title}") # Original contained "Now Playing" instead of "Now playing"
# NP_TOTAL_PLAYTIME = XpathString("//*[@resource-id='com.android.car.media:id/max_time']")
# NP_VIDEO_NS_FULLSCREEN_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][@resource-id='']")
# NP_VIDEO_NS_OVERFLOW = XpathString("//*[@resource-id='com.android.car.media:id/overflow']")
# NP_VIDEO_NS_PLAY_PAUSE = XpathString("//*[@resource-id='com.android.car.media:id/play_pause_stop']")
# NP_VIDEO_NS_SEEK_BAR = XpathString("//*[@resource-id='com.android.car.media:id/seek_bar']")
# NP_VIDEO_NS_SKIP_BACKWARD = XpathString("//*[@resource-id='com.android.car.media:id/skip_prev']")
# NP_VIDEO_NS_SKIP_FORWARD = XpathString("//*[@resource-id='com.android.car.media:id/skip_next']")
# NP_VIDEO_NS_TITLE = XpathString(f"//*[@resource-id='com.android.car.media:id/car_ui_toolbar_title']{video.video_now_playing_screen_title}")
# NP_VIDEO_SS_BACK_BUTTON = XpathString("//*[@index='0'][@class='android.widget.ImageButton']")
# NP_VIDEO_SS_ELAPSED_PLAYTIME = XpathString("//*[@resource-id='de.eso.video:id/elapsedTime']")
NP_VIDEO_SS_FS_TITLE = XpathString("//*[@resource-id='de.eso.video:id/video_surface']")
NP_VIDEO_SS_FULLSCREEN_BUTTON = XpathString("//*[@resource-id='de.eso.video:id/first_custom_action_button']")
NP_VIDEO_SS_INTERACTION_FOREGROUND_TITLE = XpathString("//*[@resource-id='de.eso.video:id/nps_foreground']")
# NP_VIDEO_SS_OVERFLOW = XpathString("//*[@resource-id='de.eso.video:id/more_button']")
# NP_VIDEO_SS_PLAY_PAUSE = XpathString("//*[@resource-id='de.eso.video:id/play_pause_button']")
NP_VIDEO_SS_PLAYLIST_BUTTON = XpathString("//*[@index='1'][@class='android.widget.ImageButton']")
# NP_VIDEO_SS_REMAINING_PLAYTIME = XpathString("//*[@resource-id='de.eso.video:id/remainingTime']")
# NP_VIDEO_SS_SEEK_BAR = XpathString("//*[@resource-id='de.eso.video:id/seekBar']")
# NP_VIDEO_SS_SKIP_BACKWARD = XpathString("//*[@resource-id='de.eso.video:id/skip_back_button']")
# NP_VIDEO_SS_SKIP_FORWARD = XpathString("//*[@resource-id='de.eso.video:id/skip_forward_button']")
NPS_MINIMIZED = XpathString("//*[@resource-id='com.android.car.media:id/minimized_playback_controls']")
PERMISSION_REQUEST_TEXT_TITLE = XpathString(f"//*{mediacoreservice.hcp3_ext_hmi_permission_read_external_storage_info}")
# PLAYER_CURRENT_PLAYTIME = XpathString("//*[@resource-id='com.android.car.media:id/current_time']")
PLAYLISTS_TITLE = XpathString(f"//*{mediacoreservice.hcp3_ext_playlists}[@resource-id='com.android.car.media:id/car_ui_toolbar_title']")
POPUP_MISSING_PERMISSION_DIALOG = XpathString(f"//*[@resource-id='android:id/message']{audi.texttool_globals_dialog_title___calling__missing_android_phone_permission_title}") #_todo? was 'Missing permission'
POPUP_MISSING_PERMISSION_DIALOG_BUTTON_GRANT = XpathString(f"//*[@resource-id='android:id/button1']{UBIInCarApp.permissionsScreen_accept}") #_todo? was [contains(@text, 'Grant permission') or contains(@text, 'Zugriff erlauben')]
POPUP_STORAGE_PERMISSION_DIALOG = XpathString("//*[@resource-id='com.android.permissioncontroller:id/car_ui_alert_title'][contains(@text, 'Allow Media Application') or contains(@text, 'Media Application erlauben')]") #_todo not found in texttool
# POPUP_STORAGE_PERMISSION_DIALOG_BUTTON_ALLOW = XpathString("//*[@text='Allow' or @text='Zulassen']") #_todo
# POPUP_STORAGE_PERMISSION_DIALOG_BUTTON_CONTAINER = XpathString("//*[@resource-id='com.android.permissioncontroller:id/list']")
RECENTS_TITLE = XpathString(f"//*{mediacoreservice.hcp3_ext_recents}[@resource-id='com.android.car.media:id/car_ui_toolbar_title']")
SEARCH_BUTTON = XpathString("//*[@index='0'][@resource-id=''][@clickable='true']")
#SEARCH_ENTRY_FIELD_TITLE = XpathString("//*[@resource-id='com.android.car.media:id/hcp3_car_ui_toolbar_search_view_input_background']")
SEARCH_ENTRY_FIELD_TITLE = XpathString("//*[@resource-id='technology.cariad.overlays.media.cid.audi:id/hcp3_car_ui_toolbar_search_view_input_background']")
SEARCH_X = XpathString("//*[@resource-id='com.android.car.media:id/car_ui_toolbar_nav_icon_container']")
SETTINGS_BUTTON = XpathString("//*[@index='1'][@resource-id=''][@clickable='true']")
SETTINGS_TOP_BAR_TITLE = XpathString("//*[@resource-id='com.harman.mediacoreservice:id/tb_setting_bar']")
# SOURCE_SELECTION_BACK_BUTTON = XpathString("//*[contains(@text, 'Back')]") #_todo
# SOURCE_SELECTION_MEDIA_BUTTON = XpathString("//*[@text='TA_MEDIA' or contains(@text, 'W40')]") #_todo
# SOURCE_SELECTION_RADIO_BUTTON = XpathString("//*[contains(@text, 'Radio')]") #_todo
# SOURCE_SELECTION_TITLE = XpathString("//*[@content-desc='MediaSourceSelection']")
# SPEED_DISCLAIMER = XpathString("//*[@resource-id='de.eso.video:id/speed_disclaimer_text']")
SWITCHAPPS_BUTTON = XpathString("//*[@index='2'][@resource-id=''][@clickable='true']")
#TRACKS_TITLE = XpathString("//*[contains(@text, 'Tracks') or contains(@text, 'Titel')][@resource-id='com.android.car.media:id/car_ui_toolbar_title']") #_todo
TRACKS_TITLE = XpathString(f"//*{mediacoreservice.hcp3_ext_songs}[@resource-id='com.android.car.media:id/car_ui_toolbar_title']") #_todo
VIDEOS_TITLE = XpathString(f"//*{mediacoreservice.hcp3_ext_videos}[@resource-id='com.android.car.media:id/car_ui_toolbar_title']")
