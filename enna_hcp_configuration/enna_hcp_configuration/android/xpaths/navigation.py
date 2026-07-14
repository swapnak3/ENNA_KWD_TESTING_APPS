# -*- coding: utf-8 -*-
"""Module contains xpath of navigation app."""
import enna_hcp_configuration.android.xpaths
from . import XpathString

if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.technology.cariad.navi.oi import audi as navi
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.technology.cariad.navi.oi import audi as navi
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.technology.cariad.navi.oi import audi as navi
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.technology.cariad.navi import audi as navi
else:
	from enna_hcp_configuration.texts.CLU46.center.technology.cariad.navi import audi as navi

# pylint: disable=line-too-long
SIDEBAR_BUTTON = XpathString(f"//*[contains(@resource-id, 'com.android.systemui:id/navigation_bar_favorite_button1')]{str(navi.texttool_globals_application_label___app_name).replace('@text', '@content-desc')}", context="launcher.home")
MAIN_TITLE = XpathString("//*[contains(@resource-id, 'id/mapMainButtonsContainer') or contains(@resource-id, 'id/scaleConstraint') or contains(@resource-id, 'id/searchTitleLine')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.main") # language independent
ALTERNATIVE_ROUTES_CLOSE_BUTTON_TITLE = XpathString("//*[contains(@content-desc, 'alternativeRoutesCloseButton')]") #_todo not found
#DEST_INPUT_TITLE = XpathString("//*[contains(@content-desc, 'string/search_hint')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
DEST_INPUT_TITLE = XpathString("//*[contains(@resource-id, 'id/searchTitleLine')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.search_details") # language independent
#ESO_MOCK_TITLE = XpathString("//*[contains(@resource-id, 'id/DemoPositionGem')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
ESO_MOCK_TITLE = XpathString("//*[contains(@text,'Default Locations :')][contains(@resource-id, 'id/textView')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
DESTINATION_DETAILS_SCREEN_TITLE = XpathString("//*[contains(@resource-id, 'id/destinationDetailsFragment')]")
DETAILS_SCREEN_CLOSE_BUTTON = XpathString("//*[contains(@content-desc, 'detailsTitleLineCloseButton')]")

#GEM_TITLE = XpathString("//*[contains(@resource-id, 'id/gemOverlay')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.gem") # language independent
GEM_TITLE = XpathString("//*[contains(@content-desc,'HMI')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi'][@selected='true']", context="navigation.gem") # language independent
# GEM_BUTTON = XpathString("//*[contains(@content-desc, 'string/gem')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']") # not found, seems to be unused
#GEM_CLOSE_BUTTON = XpathString("//*[contains(@resource-id, 'id/gemOverlayCloseButton')]") # button no longer had a resource-id
GEM_CLOSE_BUTTON = XpathString("//*[contains(@resource-id, 'id/actionButtons')]/*[@class='android.widget.ImageButton' and @index=0]") # button no longer had a resource-id but the parent group has only one button
#GEM_POS_INFO_BUTTON = XpathString("//*[contains(@content-desc, 'Show position information via AIDL') or contains(@text, 'Show position information via AIDL')]")
GEM_LIST_HORIZONTAL = XpathString("//*[contains(@resource-id, 'id/gemHmiRecyclerListBase')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.gem")
GEM_NAVADAPTER_LIST = XpathString("//*[contains(@resource-id,'id/expandableMenu')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.navadapter")
#GEM_LIST = XpathString("//*[contains(@resource-id, 'id/gemHmiRecyclerListBase')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_SET_USER_CONSENT_GIVEN = XpathString("//*[@text='given'][@package='technology.cariad.navi.audi']")
# GEM_SET_USER_CONSENT_DISABLE_OVERRIDE = XpathString("//*[@text='disable override'][@package='technology.cariad.navi.audi']")
# GEM_SET_USER_CONSENT_REJECTED = XpathString("//*[@text='rejected'][@package='technology.cariad.navi.audi']")

GEM_NAVADAPTER_BUTTON = XpathString("//*[contains(@content-desc,'Navigation adapter')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.gem")
GEM_NAVADAPTER_TITLE = XpathString("//*[contains(@content-desc,'Navigation adapter')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi'][@selected='true']", context="navigation.navadapter")
GEM_NAVADAPTER_MOCK_BUTTON = XpathString("//*[@text='MOCK'][contains(@resource-id,'id/groupText')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.navadapter")
GEM_NAVADAPTER_MOCK_TITLE = XpathString("//*[@text='mocked'][contains(@resource-id,'id/textView')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.navadapter")
GEM_NAVADAPTER_DEMO_MOCK_BUTTON = XpathString("//*[@text='DEMO_POSITION'][contains(@resource-id,'id/groupText')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.navadapter")
# GEM_MOCKGEM_BUTTON = XpathString("//*[contains(@resource-id, 'id/ServiceMockGem')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_MOCK_ALL_SWITCH = XpathString("//*[contains(@resource-id, 'id/switchMockAll')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_MAP_DEBUG_OVERLAY_SWITCH = XpathString("//*[node/node[contains(@text, 'Show Map Debug Overlay')]]/node[@resource-id='technology.cariad.navi.audi:id/checkBox']")
# GEM_MOCK_CHARGING_MANAGEMENT_CORE = XpathString("//*[contains(@resource-id, 'technology.cariad.navi.audi:id/switchMockChargingManagementCore')]")
# GEM_MOCK_ROUTE_BASED_CONSUMPTION = XpathString("//*[contains(@resource-id, 'technology.cariad.navi.audi:id/switchMockRouteBasedConsumption')]")
# GEM_VEHICLEDATA_STATUS_BUTTON = XpathString("//*[contains(@resource-id, 'id/VehicleDataStatusGem')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_VEHICLEDATA_ERROR = XpathString("//*[contains(@resource-id, 'id/txtVehicleDataStateErrorMessage')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_DEMOPOSITION_BUTTON = XpathString("//*[contains(@resource-id, 'id/DemoPositionGem')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_DEMOPOSITION_ENABLE = XpathString("//*[contains(@resource-id, 'id/switchEnable')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_SET_DEFAULT_POSITION = XpathString("//*[contains(@resource-id, 'id/btnSetDefaultPosition')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_SEND_LAST_ACTIVE_TOUR = XpathString("//*[@text='Send last active tour as synced route']")
# GEM_PLAY_ROUTE = XpathString("//*[contains(@resource-id, 'id/btnPlayNaviRoute')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_GRID_CONTAINER = XpathString("//*[@package='technology.cariad.navi.audi'][@class='android.widget.GridLayout']")
# GEM_CORE_SERVICES = XpathString("//*[contains(@content-desc, 'Core (online) services') or contains(@text, 'Core (online) services')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_ONLINE_SEARCH = XpathString("//*[contains(@content-desc, 'onlinesearch_v1 availability') or contains(@text, 'onlinesearch_v1 availability')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_GOOGLE_SEARCH = XpathString("//*[contains(@content-desc, 'googlesearch_v1 availability') or contains(@text, 'googlesearch_v1 availability')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_SATELLITE_MAPS = XpathString("//*[contains(@content-desc, 'satellitemaps_v4 availability') or contains(@text, 'satellitemaps_v4 availability')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_SERVICE_ENABLE = XpathString("//*[contains(@content-desc, 'ENABLE') or contains(@text, 'ENABLE')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_SERVICE_NOT_AVAILABLE = XpathString("//*[contains(@content-desc, 'NOT_AVAILABLE') or contains(@text, 'NOT_AVAILABLE')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_SERVICE_DISABLE = XpathString("//*[contains(@content-desc, 'DISABLE') or contains(@text, 'DISABLE')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_MAP_MATCHER = XpathString("//*[contains(@content-desc, 'Map matcher')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_MAP_MATCHER_TIMESTAMP = XpathString("//*[contains(@resource-id, 'id/timestamp')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi' or @package='technology.cariad.mapmatcher']")
# GEM_MAP_MATCHER_ENABLE_GNSS = XpathString("//*[contains(@resource-id, 'id/enable_gnss')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_MAP_MATCHER_DISABLE_GNSS = XpathString("//*[contains(@resource-id, 'id/disable_gnss')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# GEM_MAP_MATCHER_LATITUDE = XpathString("(//*[contains(@resource-id, 'id/latitude')])[1]")
# GEM_MAP_MATCHER_LONGITUDE = XpathString("(//*[contains(@resource-id, 'id/longitude')])[1]")
# GEM_MAP_MATCHER_MODE = XpathString("//*[contains(@resource-id, 'id/onroad')]")

INIT_TITLE = XpathString("//*[contains(@content-desc, 'string/app_init_message')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")

SETTING_TITLE = XpathString("//*[contains(@content-desc, 'string/settings')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
SETTING_LIST = XpathString("//*[contains(@content-desc, 'settingsOverlayList')]")
SETTING_BUTTON = XpathString("//*[contains(@resource-id, 'id/settingsButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_ANNOUNCEMENTS_COMPACT = XpathString("//*[contains(@content-desc, 'settingVoiceGuidanceModesCompact')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_ANNOUNCEMENTS_COMPLETE = XpathString("//*[contains(@content-desc, 'settingVoiceGuidanceModesFull')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_ANNOUNCEMENTS_TRAFFIC = XpathString("//*[contains(@content-desc, 'settingVoiceGuidanceModesTraffic')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
SETTING_ANNOUNCEMENTS_DURING_CALL_SWITCH = XpathString("//*[contains(@content-desc, 'settingAnnouncementsDuringCall-switch')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_MAP_COLOR_AUTO = XpathString("//*[contains(@content-desc, 'settingMapColorsAuto')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_MAP_COLOR_DAY = XpathString("//*[contains(@content-desc, 'settingMapColorsDay')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_MAP_COLOR_NIGHT = XpathString("//*[contains(@content-desc, 'settingMapColorsNight')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
SETTING_CHARGING_BUTTON = XpathString("//*[contains(@content-desc, 'string/navi_settings__charging_settings_list_item')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
SETTING_CHARGING_TITLE = XpathString("//*[contains(@content-desc, 'string/navi_settings__charging_settings_title_line')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
SETTING_CHARGING_BACK_BUTTON = XpathString("//*[contains(@content-desc, 'settingsOverlayTitle-backButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_CHARGING_LIST = XpathString("//*[contains(@content-desc, 'settingsOverlayList')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_CHARGING_EV_TRIP_PLANNER_SWITCH = XpathString("//*[contains(@content-desc, 'settingEvTripPlanner-switch')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_CHARGING_PREFER_BRAND_SWITCH = XpathString("//*[contains(@content-desc, 'settingPreferBrandChargingStations-switch')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_CHARGING_DESTINATION_SOC_SEEKBAR = XpathString("//*[contains(@content-desc, 'settingDestinationSoc-seekBar')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_CHARGING_DESTINATION_SOC_VALUE = XpathString("//*[contains(@content-desc, 'settingDestinationSoc')]//*[@resource-id='technology.cariad.navi.audi:id/currentValuePermanentTextView'][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")  # pylint: disable=line-too-long # noqa
# SETTING_CHARGING_STOP_SOC_SEEKBAR = XpathString("//*[contains(@content-desc, 'settingChargingStopSoc-seekBar')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_MAP_CONTENT = XpathString("//*[contains(@content-desc, 'string/map_contents_setting_label')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_MAP_CONTENT_POI = XpathString("//*[contains(@content-desc, 'settingMapPoiIcons-checkbox')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_MAP_CONTENT_3D_CITY = XpathString("//*[contains(@content-desc, 'settingMapCityModel-checkbox')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_MAP_CONTENT_FAVORITES = XpathString("//*[contains(@content-desc, 'settingFavorites-checkbox')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_MAP_CONTENT_TRAFFIC_FLOW = XpathString("//*[contains(@content-desc, 'settingMapTrafficFlow-checkbox')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_MAP_CONTENT_ALTERNATIVES_ROUTES = XpathString("//*[contains(@content-desc, 'settingAlternativeRoutes-checkbox')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_MAP_CONTENT_RANGE = XpathString("//*[contains(@content-desc, 'settingMapRange-checkbox')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_TOUR_PLAN_ENTRY_POINT = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/tour_plan_settings_entry_point')]")
# SETTING_TRAFFIC_MINI_MAPS_SWITCH = XpathString("//*[contains(@content-desc, 'settingTrafficMiniMapPopups-switch')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_GOOLE_SAT_MAP = XpathString("//*[contains(@content-desc, 'map_satellite_map_list_setting_label')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
SETTING_GOOLE_SAT_MAP_SWITCH = XpathString("//*[contains(@content-desc, 'settingSatelliteMap-switch')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_AUTOMATIC_REROUTING_SWITCH = XpathString("//*[contains(@content-desc, 'settingAutomaticRerouting-switch')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
SETTING_SHOW_MANEUVER_SWITCH = XpathString("//*[contains(@content-desc, 'settingShowManeuver-switch')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_ROUTE_GUIDANCE_CRITERIA = XpathString("//*[contains(@content-desc, 'settingGuidanceRouteCriteria')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_ROUTE_GUIDANCE_CRITERIA_MOTORWAYS = XpathString("//*[contains(@content-desc, 'settingGuidanceRouteCriteriaMotorways-checkbox')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_ROUTE_GUIDANCE_CRITERIA_TOLL = XpathString("//*[contains(@content-desc, 'settingGuidanceRouteCriteriaTollRoads-checkbox')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_ROUTE_GUIDANCE_CRITERIA_FERRY = XpathString("//*[contains(@content-desc, 'settingGuidanceRouteCriteriaFerries-checkbox')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_ROUTE_GUIDANCE_CRITERIA_VIGNETTE = XpathString("//*[contains(@content-desc, 'settingGuidanceRouteCriteriaVignetteRoads-checkbox')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_ANNOUNCEMENT_VOLUME_SEEKBAR = XpathString("//*[contains(@content-desc, 'settingAnnouncementVolume-seekBar')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
SETTING_CLOSE_BUTTON = XpathString("//*[contains(@content-desc, 'settingsOverlayTitle-closeButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
SETTING_COUNTRY_INFORMATION_BUTTON = XpathString("//*[contains(@content-desc, 'string/country_info_entry_point')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
SETTING_COUNTRY_INFORMATION_TITLE = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/country_info')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
SETTING_COUNTRY_INFORMATION_BACK_BUTTON = XpathString("//*[contains(@content-desc, 'settingsOverlayTitle-backButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_COUNTRY_INFORMATION_NOT_AVAILABLE = XpathString("//*[contains(@content-desc, 'string/road_class_missing_info')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SETTING_COUNTRY_INFORMATION_COUNTRY_NAME = XpathString("//*[contains(@content-desc, 'settingCountryName')]//*[contains(@resource-id, 'technology.cariad.navi.audi:id/listItemGrid2MainContent_textStart')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")  # pylint: disable=line-too-long # noqa
AUTOMATIC_DATABASE_UPDATE_SWITCH = XpathString("//*[contains(@content-desc, 'settingInfoAutomaticDatabaseUpdate-switch')]")
SETTING_NAVI_INFORMATION_BUTTON = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/navi_settings__navi_info_list_item')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
SETTING_NAVI_INFORMATION_TITLE = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/navi_settings')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
SETTING_NAVI_INFORMATION_BACK_BUTTON = XpathString("//*[contains(@content-desc, 'settingsOverlayTitle-backButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# COMPASS_BUTTON = XpathString("//*[contains(@resource-id, 'id/compassButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
SEARCH_BUTTON = XpathString("//*[contains(@content-desc, 'searchButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi'][@class='android.widget.ImageView']", context="navigation.main")
# SEARCH_TEXT = XpathString("//*[contains(@resource-id, 'id/searchTextView')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# SEARCH_EDIT_TEXT = XpathString("//*[contains(@resource-id, 'id/editText')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.search") # language independent
# SEARCH_LIST = XpathString("//*[contains(@resource-id, 'id/recyclerViewList')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.search") # language independent
SEARCH_CLOSE = XpathString("//*[contains(@content-desc, 'searchTitleLineCloseButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.search") # language independent
SEARCH_CATEGORIES_TITLE = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/destination_input_screen__poiCategories__title_line')]", context="navigation.search_categories") # language independent
SEARCH_CATEGORIES_BUTTON = XpathString("//*[contains(@content-desc, 'searchFilterBarAllPoiCategoriesButton')]", context="navigation.search") # language independent
SEARCH_CATEGORIES_CLOSE_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][@package='technology.cariad.navi.audi'][contains(@content-desc, 'searchTitleLineCloseButton')]", context="navigation.search_categories") # language independent
# SEARCH_OFFLINE_INDICATION = XpathString("//*[contains(@content-desc, 'offline_indicator')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']") # not found, seems to be unused
# SEARCH_RESULT_MAP_PIN = XpathString("//*[contains(@content-desc, 'map_pin_')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']") # not found, seems to be unused
# SEARCH_RESULT_MAP_PIN_1 = XpathString("//*[contains(@content-desc, 'map_pin_1')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']") # not found, seems to be unused
# SEARCH_RESULT_MAP_PIN_2 = XpathString("//*[contains(@content-desc, 'map_pin_2')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']") # not found, seems to be unused
# SEARCH_RESULT_MAP_PIN_3 = XpathString("//*[contains(@content-desc, 'map_pin_3')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']") # not found, seems to be unused
# SEARCH_RESULT_MAP_PIN_4 = XpathString("//*[contains(@content-desc, 'map_pin_4')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']") # not found, seems to be unused
# SEARCH_RESULT_MAP_PIN_5 = XpathString("//*[contains(@content-desc, 'map_pin_5')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']") # not found, seems to be unused
# SEARCH_RESULT_FIRST_ROW = XpathString("//*[contains(@resource-id, 'id/firstRowFirstText')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.search_details") # language independent, matches every result on screen
# SEARCH_RESULT_SECOND_ROW = XpathString("//*[contains(@resource-id, 'id/secondRowFirstText')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.search_details") # language independent, matches every result on screen
# SEARCH_RESULT_DISTANCE = XpathString("//*[contains(@resource-id, 'technology.cariad.navi.audi:id/lidIconText') or contains(@resource-id, 'technology.cariad.navi.audi:id/leadingIconText')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']") # not found, seems to be unused
# SEARCH_IS_DONE = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/recyclerViewList']/node[ not(node//node[@resource-id='technology.cariad.navi.audi:id/loadingSpinner']) ]", context="navigation.search_details") # matches, but not sure if it is the right match
# SEARCH_HOME_ADDRESS = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:drawable/home_address')]", context="navigation.search") # language independent
# SEARCH_RESULT_ICON = XpathString("//*[contains(@resource-id, 'technology.cariad.navi.audi:id/firstRowIcon')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.search_details") # language independent
# SEARCH_RESULT_NO_RESULT = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/search_no_results_found')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.search_details") # language independent, only when offline
# SEARCH_RESULT_ONLINE_DATA_AVAILABLE = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/search_connectivity_online_label')][@package='technology.cariad.navi.audi']") # not found, seems to be unused
# SEARCH_RESULT_NEARBY = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/search_results_in_vincinity')][@package='technology.cariad.navi.audi']") # not found, seems to be unused
# SEARCH_GOOGLE_BUTTON = XpathString("//*[contains(@content-desc, 'searchTitleLineGoogleButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.search_details") # language independent

# # seems like this buttons no longer exist
# #ZOOMIN_BUTTON = XpathString("//*[contains(@resource-id, 'id/zoomInButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# #ZOOMOUT_BUTTON = XpathString("//*[contains(@resource-id, 'id/zoomOutButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# #ZOOM_MODE_BUTTON = XpathString("//*[contains(@content-desc, 'autoZoomButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# #ZOOM_MODE_OVERVIEW = XpathString("//*[contains(@content-desc, 'zoomModeOverview')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# #ZOOM_MAP_MAIN_SCALE_BUTTON = XpathString("//*[contains(@resource-id, 'id/mapMainScaleButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# #ZOOM_RECENTER = XpathString("//*[contains(@resource-id, 'id/recenterButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# ZOOM_MODE_AUTO = XpathString("//*[contains(@content-desc, 'zoomModeAutomatic')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.main") # language independent
# ZOOM_MODE_MANUAL = XpathString("//*[contains(@content-desc, 'zoomModeManual')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']", context="navigation.main") # language independent
# # zoom scale value / unit do not seem to be separate any more
# #ZOOM_SCALE_VALUE = XpathString("//*[contains(@resource-id, 'id/zoomScaleValue')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# #ZOOM_SCALE_UNIT = XpathString("//*[contains(@resource-id, 'id/zoomScaleUnit')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# ZOOM_SCALE = XpathString("//*[contains(@resource-id, 'id/zoomScale')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# MAP_DEBUG_OVERLAY = XpathString("//*[contains(@text, 'RenderingMode')][@package='technology.cariad.navi.audi'][@resource-id='technology.cariad.navi.audi:id/info_text_view']")
NOT_ACTIVATED_TITLE = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/not_activated_screen_description')]")
SEARCH_OVERLAY_TITLE = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/searchOverlay']")
# POI_ALL_CATEGORIES_BUTTON = XpathString("//*[contains(@resource-id, 'allPoiCategoriesButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# POI_HOTEL = XpathString("//*[contains(@content-desc, 'Hotel') or contains(@text, 'Hotel')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# POI_FIRST_RESULT = XpathString("//*[contains(@resource-id, 'id/firstRow_container')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
POI_STACK_CLOSE_BUTTON = XpathString("//*[contains(@content-desc, 'poiTitleLineCloseButton')]")
POI_STACK_SCREEN_TITLE = XpathString("//*[contains(@resource-id, 'id/poiStackOverlay')]")
POI_OVERVIEW_TITLE = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/destination_input_screen__slide_out__poiCategories__title_line')]")
# ROUTE_MONITOR_CCP = XpathString("//*[contains(@content-desc, 'routemonitor_ccp')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# REPLACE_OR_ADD_STOPOVER_POPUP = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/texttool_globals_dialog_title___dialog_title_replace_route_or_add_as_stopover')]")
# REPLACE_ROUTE_BUTTON = XpathString("//*[contains(@resource-id, 'android:id/button2')]")
# ADD_STOPOVER_BUTTON = XpathString("//*[contains(@resource-id, 'android:id/button1')]")

# ROUTE_LINE = XpathString("//*[contains(@resource-id, 'technology.cariad.navi.audi:id/routeLine')]") # not found, seems to be unused
# ROUTE_INFO_ARRIVAL_SOC = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/arrivalSoc' or @resource-id='technology.cariad.navi.audi:id/arrivalSocLayout']", context="navigation.guidance") # language independent
# ROUTE_INFO_BOX = XpathString("//*[contains(@content-desc, 'routeInfoBox')]", context="navigation.guidance") # language independent
# ROUTE_INFO_TRIPTIME = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/tripTime']", context="navigation.guidance") # language independent
# ROUTE_INFO_TRIPTIME_UNIT = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/tripTimeUnit']", context="navigation.guidance") # language independent
# ROUTE_INFO_ETA = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/eta']", context="navigation.guidance") # language independent
# ROUTE_INFO_DISTANCE = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/distance']", context="navigation.guidance") # language independent
# ROUTE_INFO_DISTANCE_UNIT = XpathString("//*[contains(@content-desc, 'routeInfoDistanceUnit')][@resource-id='technology.cariad.navi.audi:id/distanceUnit']", context="navigation.guidance") # language independent
# ROUTE_INFO_CHARGING_STOP_TIME_VALUE = XpathString("//*[contains(@resource-id, 'id/chargingTimeValue')]") # not found, seems to be unused
# ROUTE_INFO_CHARGING_STOP_TIME_UNIT = XpathString("//*[contains(@resource-id, 'id/chargingTimeUnit')]") # not found, seems to be unused
#ROUTE_INFO_DESTINATION_FLAG = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:drawable/e0b0_navigation_zielflagge')]") # not found, seems to be unused
ROUTE_INFO_DESTINATION_FLAG = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/destinationFlagIcon']", context="navigation.guidance") # language independent
ROUTE_TOUR_PLAN_TITLE = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/tour_plan')]", context="navigation.tourplan") # language independent
#ROUTE_TOUR_PLAN_LIST = XpathString("//*[contains(@resource-id, 'id/recyclerView')]", context="navigation.tourplan") # language independent)
ROUTE_TOUR_PLAN_CLOSE_BUTTON = XpathString("//*[contains(@resource-id, 'technology.cariad.navi.audi:id/actionButtons')]", context="navigation.tourplan") # language independent

# ROUTE_TOUR_PLAN_STOP_TEXT_START = XpathString("//*[contains(@resource-id, 'id/textStart')]") # not found, seems to be unused
# ROUTE_TOUR_PLAN_STOP_DISTANCE = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/tour_plan_image1_text')]", context="navigation.tourplan") # language independent, multiple matches
# #ROUTE_TOUR_PLAN_STOP_ARRIVAL_SOC = XpathString("//*[contains(@resource-id, 'id/subTextStart_text1')]")
# ROUTE_TOUR_PLAN_STOP_ARRIVAL_SOC = XpathString("//*[contains(@resource-id, 'id/listItemTourPlan_subtextStart_text1')]", context="navigation.tourplan") # language independent
# ROUTE_TOUR_PLAN_STOP_SOC_TIME_AT_CHARGING = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/tour_plan_soc_info_with_charging_time_and_capacity')]")
# ROUTE_TOUR_PLAN_STOP_SOC_CHARGING_POWER = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/tour_plan_second_line_Info')]")
# ROUTE_TOUR_PLAN_STOP_ETA = XpathString("//*[contains(@content-desc, 'technology.cariad.navi.audi:string/tour_plan_first_line_Info')]", context="navigation.tourplan") # language independent
# ROUTE_TOUR_PLAN_SCROLLBAR = XpathString("//*[contains(@content-desc, 'tourPlanRecyclerview')]", context="navigation.tourplan") # language independent

# ROUTE_MONITOR_CLOSE_BUTTON = XpathString("//*[contains(@content-desc, 'closeRouteMonitorButton')]")
# ROUTE_MONITOR_OPEN_BUTTON = XpathString("//*[contains(@content-desc, 'openRouteMonitorButton')]")

TRAFFIC_DETAILS_TITLE = XpathString("//*[contains(@content-desc, 'traffic_details_screen__title_line')]")

# ROUTE_NMB_FIRST_MANEUVER_CONTAINER = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/maneuverContainer']")
# ROUTE_NMB_SECOND_MANEUVER_CONTAINER = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/secondaryManeuverContainer']")
# ROUTE_NMB_FIRST_MANEUVER_ICON = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/nextManeuverIcon']")
# ROUTE_NMB_FIRST_MANEUVER_DISTANCE_VALUE = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/nextManeuverDistanceValue']")
# ROUTE_NMB_FIRST_MANEUVER_DISTANCE_UNIT = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/nextManeuverDistanceUnit']")
# ROUTE_NMB_FIRST_MANEUVER_ROAD_INFO = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/streetOrLocation']")
# ROUTE_NMB_SECOND_MANEUVER_ICON = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/secondaryManeuverIcon']")
# ROUTE_NMB_SECOND_MANEUVER_DISTANCE_VALUE = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/secondaryManeuverDistanceValue']")
# ROUTE_NMB_SECOND_MANEUVER_DISTANCE_UNIT = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/secondaryManeuverDistanceUnit']")

ABORT_ROUTE_GUIDANCE_BUTTON_TITLE = XpathString("//*[contains(@content-desc, 'stopButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")
# #HOME = XpathString("//*[@package='com.android.systemui'][contains(@content-desc, 'Navigation')]")
# HOME = XpathString(f"//*[@package='com.android.systemui']{str(navi.texttool_globals_application_label___app_name).replace('@text', '@content-desc')}")
# #SIDEBAR_BUTTON = XpathString(f"//*[contains(@resource-id, 'com.android.systemui:id/navigation_bar_favorite_button1')]{str(navi.texttool_globals_application_label___app_name).replace('@text', '@content-desc')}", context="launcher.home")

FAVORITES_TITLE = XpathString("//*[contains(@content-desc, 'searchFilterBarFavoriteButton') or contains(@resource-id, 'technology.cariad.navi.audi:id/favoritesButton')][@package='de.eso.audi.navi' or @package='technology.cariad.navi.audi']")  # ger_ok

# TOP_POI_BUTTON_1 = XpathString("//*[contains(@resource-id, 'topPoiButtons')]/*[1]")
# TOP_POI_BUTTON_2 = XpathString("//*[contains(@resource-id, 'topPoiButtons')]/*[2]")
# TOP_POI_BUTTON_3 = XpathString("//*[contains(@resource-id, 'topPoiButtons')]/*[3]")
# TOP_POI_BUTTON_4 = XpathString("//*[contains(@resource-id, 'topPoiButtons')]/*[4]")
# TOP_POI_BUTTON_5 = XpathString("//*[contains(@resource-id, 'topPoiButtons')]/*[5]")
# LOADING_SPINNER = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/loadingSpinner']")
# LIST_LOADING_SPINNER = XpathString("//*[contains(@content-desc, 'searchListLoadingSpinner')]")

POPUP_LOCATION_PERMISSION_KEYBOARD_DIALOG_TITLE = XpathString("//*[@package='com.android.permissioncontroller'][contains(@text, 'Keyboard')]")
# POPUP_LOCATION_PERMISSION_KEYBOARD_BUTTON_ALLOW = XpathString("//*[@package='com.android.permissioncontroller'][contains(@text, 'App')]")
POPUP_DATABASE_AUTO_UPDATE_TITLE = XpathString("//*[@resource-id='technology.cariad.navi.audi:id/popupTitle'][contains(@content-desc, 'texttool_globals_dialog_title___popup_online_auto_update_map_database')]")
# POPUP_DATABASE_AUTO_UPDATE_ALLOW = XpathString("//*[@resource-id='android:id/button1'][contains(@text, 'Ja') or contains(@text, 'Yes') or contains(@text, 'Ja') or contains(@text, 'Sì') or contains(@text, 'Ano') or contains(@text, 'Sí')]")
POPUP_COUNTRY_CHANGED_TITLE = XpathString("//*[@resource-id='com.android.systemui:id/notification_body_title'][contains(@text, 'Länderwechsel') or contains(@text, 'Country change')]")
POPUP_KEYBOARD_AUTHORIZATION_DIALOG_TITLE = XpathString("//*[@resource-id='android:id/message'][contains(@text, 'Bitte erteile die benötigte Berechtigung') or contains(@text, 'handwriting input')]") #_todo not in texttool
# #POPUP_KEYBOARD_AUTHORIZATION_CONTINUE_BUTTON = XpathString("//*[contains(@resource-id, 'android:id/button1')][@text='Weiter' or @text='Continue']")
# POPUP_KEYBOARD_AUTHORIZATION_CONTINUE_BUTTON = XpathString(f"//*[contains(@resource-id, 'android:id/button1')]{sw_update.wizard_button_next_text}") # untested, not explicitly found in texttool: import from enna_hcp_configuration.texts.CLUXX.center.de.eso.audi import softwareupdate as sw_update, seems to be unused
