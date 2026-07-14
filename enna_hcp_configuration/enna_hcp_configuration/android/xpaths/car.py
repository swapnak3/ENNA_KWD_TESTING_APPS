# -*- coding: utf-8 -*-
"""Module contains xpath of car app."""
import enna_hcp_configuration.android.xpaths
from . import XpathString

# pylint: disable=reimported
if enna_hcp_configuration.android.xpaths.CLUSTER in enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.de.eso.car import audi
elif enna_hcp_configuration.android.xpaths.CLUSTER in enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.de.eso.car import audi
elif enna_hcp_configuration.android.xpaths.CLUSTER in enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.de.eso.car import audi
elif enna_hcp_configuration.android.xpaths.CLUSTER in enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.de.eso.car import audi
else:
	from enna_hcp_configuration.texts.CLU46.center.de.eso.car import audi


LIST = XpathString("//*[@class='android.widget.HorizontalScrollView']") # i.O. tested
BACK_BUTTON = XpathString("//*[contains(@content-desc, 'backButton')]") # language independant, i.O. tested

AUDI_DRIVE_SELECT_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.drive_select_title}") # i.O. tested
DISPLAYS_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.display}") # i.O. tested
LIGHTS_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.light}") # i.O. tested
SEATS_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.seats}") # i.O. tested
DOORS_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.ase_tab if enna_hcp_configuration.android.xpaths.CLUSTER in enna_hcp_configuration.android.xpaths.CLUSTERS_PPE else "[@text='§undefined§']"}") # i.O. tested
SERVICING_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.service}") # i.O. tested
MORE_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.more}") # i.O. tested

ENERGY_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.etron_charging_energy}")
DEPARTURE_TIMES_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.etron_charging_timers}")
LOCATIONS_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.etron_locations_tile_name}")
TIPPS_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.etron_charging_help}")

AUDI_DRIVE_SELECT_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.drive_select_title}[@selected='true']") # i.O. tested
DISPLAYS_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.display}[@selected='true']") # i.O. tested
LIGHTS_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.light}[@selected='true']") # i.O. tested
SEATS_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.seats}[@selected='true']") # i.O. tested
DOORS_TITLE = XpathString(f"{DOORS_BUTTON.get()}[@selected='true']") # i.O. tested
SERVICING_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.service}[@selected='true']") # i.O. tested

ENERGY_TITLE= XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.etron_charging_energy}[@selected='true']")
DEPARTURE_TIMES_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.etron_charging_timers}[@selected='true']")
LOCATIONS_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.etron_charging_locations}[@selected='true']")
TIPPS_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.etron_charging_help}[@selected='true']")


AUDI_DRIVE_SELECT_INDIVIDUAL_SETTINGS_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/drive_select_title')]")

SERVICING_VEHICLE_STATUS_TITLE = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.title_service_warning}") # i.O. tested
SERVICING_VEHICLE_DATA_TITLE = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.title_service_vehicle_data}") # i.O. tested
SERVICING_VEHICLE_ALLREPORTS_BUTTON = XpathString(f"//*[@resource-id='de.eso.car.audi:id/listItemGrid2']/.//*{audi.warning_memory}") # i.O. tested
SERVICING_VEHICLE_DATA_BUTTON = XpathString(f"//*[@resource-id='de.eso.car.audi:id/listItemGrid2']/.//*{audi.vehicle_data}") # i.O. tested
SERVICING_VEHICLE_STATUS_BACK_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][contains(@content-desc, 'backButton')]") # i.O. tested
SERVICING_VEHICLE_DATA_BACK_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][contains(@content-desc, 'backButton')]") # i.O. tested

MORE_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*[@package='de.eso.car.audi']{audi.more}[@selected='true']") # i.O. tested

DISPLAY_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{audi.display}[@selected='true']")

DRIVER_ASSISTANCE_FAVORITES_TITLE = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.texttool_custom_fas_subscreen_title___fas_titleline_favorites}[@selected='true']") # i.O. tested
DRIVER_ASSISTANCE_WARNINGS_TITLE = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.texttool_custom_fas_subscreen_title___fas_titleline_warnings}[@selected='true']") # i.O. tested
DRIVER_ASSISTANCE_LANE_TITLE = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.texttool_custom_fas_subscreen_title___fas_titleline_laneassist}[@selected='true']") # i.O. tested
DRIVER_ASSISTANCE_SPEED_TITLE = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.texttool_custom_fas_subscreen_title___fas_titleline_speedassist}[@selected='true']") # i.O. tested
DRIVER_ASSISTANCE_BRAKE_TITLE = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.texttool_custom_fas_subscreen_title___fas_titleline_brakeassist}[@selected='true']") # i.O. tested
DRIVER_ASSISTANCE_EFFICIENCY_TITLE = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.texttool_custom_fas_subscreen_title___fas_titleline_efficiency}[@selected='true']") # i.O. tested
DRIVER_ASSISTANCE_SETTINGS_TITLE = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.fas_global_setting_title}") # i.O. tested

DRIVER_ASSISTANCE_LIST = XpathString("//*[@class='android.widget.HorizontalScrollView']") # i.O. tested, identical to LIST
DRIVER_ASSISTANCE_FAVORITES_BUTTON = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.texttool_custom_fas_subscreen_title___fas_titleline_favorites}") # i.O. tested
DRIVER_ASSISTANCE_WARNINGS_BUTTON = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.texttool_custom_fas_subscreen_title___fas_titleline_warnings}") # i.O. tested
DRIVER_ASSISTANCE_LANE_BUTTON = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.texttool_custom_fas_subscreen_title___fas_titleline_laneassist}") # i.O. tested
DRIVER_ASSISTANCE_SPEED_BUTTON = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.texttool_custom_fas_subscreen_title___fas_titleline_speedassist}") # i.O. tested
DRIVER_ASSISTANCE_BRAKE_BUTTON = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.texttool_custom_fas_subscreen_title___fas_titleline_brakeassist}") # i.O. tested
DRIVER_ASSISTANCE_EFFICIENCY_BUTTON = XpathString(f"//*[@resource-id='de.eso.car.audi:id/logoAndTitleLineContainer']/.//*{audi.texttool_custom_fas_subscreen_title___fas_titleline_efficiency}") # i.O. tested
DRIVER_ASSISTANCE_SETTINGS_BUTTON = XpathString(f"//*[@resource-id='de.eso.car.audi:id/tabLayoutTitleLineContainer']/.//*{str(audi.settings).replace("@text","@content-desc")}") # i.O. tested
# DRIVER_ASSISTANCE_SETTINGS_BACK_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/interactionContainer']/.//*[contains(@content-desc, 'backButton')]") # language independant, i.O. tested

SETTINGS_SYSTEM_LIST_CONTAINER = XpathString("//*[@resource-id='de.eso.car.audi:id/list_fragment_list_view']")
SETTINGS_SYSTEM_DATE_AND_TIME_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.car.audi:string/title_setup_system_date_time')]")
SETTINGS_SYSTEM_DATE_AND_TIME_MANUALLY_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.car.audi:string/title_setup_system_date_time_picker')]")
SETTINGS_SYSTEM_DATE_AND_TIME_MANUALLY_BUTTON = XpathString("//*[contains(@content-desc, 'ManualTimeSettingsDateAndTime.ListItem')]")
SETTINGS_SYSTEM_DATE_AND_TIME_MANUALLY_BACK_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/actionButtons']/./*[@class='android.widget.ImageButton'][@index='0']")
SETTINGS_SYSTEM_DATE_AND_TIME_TIMEZONE_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.car.audi:string/title_setup_system_time_zone')]")
SETTINGS_SYSTEM_DATE_AND_TIME_TIMEZONE_BUTTON = XpathString("//*[contains(@content-desc, 'TimeZoneSettingsDateAndTime.ListItem')]")
SETTINGS_SYSTEM_DATE_AND_TIME_TIMEZONE_BACK_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/actionButtons']/./*[@class='android.widget.ImageButton'][@index='0']")

SETTINGS_SYSTEM_UNITS_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.car.audi:string/title_setup_system_units')]")
SETTINGS_SYSTEM_UNITS_BACK_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/actionButtons']/./*[@class='android.widget.ImageButton'][@index='0']")

CID_SETTINGS_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/central_display_layout']")
CID_SETTINGS_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/title_displays_central_display')]")
HUD_SETTINGS_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/headup_display_layout']")
HUD_SETTINGS_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/title_displays_hud')]")
FID_SETTINGS_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/displaysDriverDisplayEnterButton']")
FID_SETTINGS_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/title_displays_instrument_cluster')]")
PID_SETTINGS_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/passengerDisplayLayout']")
PID_SETTINGS_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/title_displays_passenger_display')]")
VA_SETTINGS_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/virtual_mirror_layout']")
VA_SETTINGS_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/virtual_mirror_title')]")

LIGHTS_INTERIOR_BUTTON = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/interior_light')]")
LIGHTS_INTERIOR_TITLE = XpathString("//*[@content-desc='###de.eso.car.audi:string/title_light_intlight']")
LIGHTS_INTERIOR_SETTINGS_TITLE = XpathString("//*[@content-desc='###de.eso.car.audi:string/title_light_intlight_advanced']")
LIGHTS_INTERIOR_SETTINGS_POPUP_LINK_COLORS_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/texttool_globals_dialog_title___title_light_link_color_info')]")
LIGHTS_EXTERIOR_BUTTON = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/exterior_light')]")
LIGHTS_EXTERIOR_TITLE = XpathString("//*[@content-desc='###de.eso.car.audi:string/title_light_exterior']")
LIGHTS_EXTERIOR_SETTINGS_TITLE = XpathString("//*[@content-desc='###de.eso.car.audi:string/title_light_exterior_settings']")
LIGHTS_COMING_LEAVING_HOME_BUTTON = XpathString("//*[contains(@content-desc,'CarLightOverview.button.comingLeavingHomeButton')]")
LIGHTS_COMING_LEAVING_HOME_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/car__tab_bar_fragment_title___advanced_coming_leaving_home')]")
LIGHTS_DIGITAL_SIGNATURES_BUTTON = XpathString("//*[contains(@content-desc,'CarLightOverview.button.signatures')]")
LIGHTS_DIGITAL_SIGNATURES_TITLE = XpathString("//*[contains(@content-desc,'CarLightOverview.button.signatures')]")
LIGHTS_INTERIOR_DISPLAY_COLOR_INFO_BUTTON = XpathString("//*[contains(@content-desc,'LinkUIBackgroundColorInfo')]")

SEATS_MASSAGE_BUTTON = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/seats_massage_button')]")
SEATS_MASSAGE_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/car__tab_bar_fragment_title___seats_massage')]")
SEATS_ADJUSTMENT_BUTTON = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/seats_adjustment_button')]")
SEATS_ADJUSTMENT_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/car__tab_bar_fragment_title___seats_adjustment')]")
SEATS_POSITION_BUTTON = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/seats_position_button')]")
SEATS_POSITION_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/car__tab_bar_fragment_title___seats_position')]")
SEATS_SETTINGS_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/car__settings_submenu_title___seats_setup')]")
SEATS_MASSAGE_DRIVER_PROGRAMM_BUTTON = XpathString("//*[contains(@content-desc,'Massage.ProgramsLeft')]")
SEATS_MASSAGE_CODRIVER_PROGRAMM_BUTTON = XpathString("//*[contains(@content-desc,'Massage.ProgramsRight')]")
SEATS_MASSAGE_BALANCE_BUTTON = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/massage_program_balance')]")
SEATS_MASSAGE_RELAX_BUTTON = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/massage_program_relax')]")
SEATS_MASSAGE_STRETCH_BUTTON = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/massage_program_stretch')]")
SEATS_START_MASSAGE_DRIVER_BUTTON = XpathString("//*[contains(@content-desc,'Massage.SwitchLeft')]")
SEATS_START_MASSAGE_CO_DRIVER_BUTTON = XpathString("//*[contains(@content-desc,'Massage.SwitchRight')]")
SEATS_INTENSITY_DRIVER_BUTTON = XpathString("//*[contains(@content-desc,'Massage.IntensityLeft')]")
SEATS_INTENSITY_CO_DRIVER_BUTTON = XpathString("//*[contains(@content-desc,'Massage.IntensityRight')]")

# xpath_collection
DRIVE_SELECT_BAR = XpathString("//*[@resource-id='de.eso.car.audi:id/dsProfilesToggle']")
DRIVE_SELECT_BALANCED = XpathString("//*[@content-desc='###DriveSelect.ProfileSelection.Balanced']")
DRIVE_SELECT_DYNAMIC = XpathString("//*[@content-desc='###DriveSelect.ProfileSelection.Dynamic']")
DRIVE_SELECT_DYNAMIC_PLUS = XpathString("//*[contains(@content-desc,'DriveSelect.dynamicPlusEfficiencyScreen')]")
DRIVE_SELECT_ECO_PLUS = XpathString("//*[contains(@content-desc,'DriveSelect.ecoPlusEfficiencyScreen')]")
DRIVE_SELECT_OFFROAD_PLUS = XpathString("//*[contains(@content-desc,'DriveSelect.offroadPlusEfficiencyScreen')]")
DRIVE_SELECT_COMFORT = XpathString("//*[@content-desc='###DriveSelect.ProfileSelection.Comfort']")
DRIVE_SELECT_ECO = XpathString("//*[@content-desc='###DriveSelect.ProfileSelection.Eco']")
DRIVE_SELECT_INDIVIDUAL = XpathString("//*[@content-desc='###DriveSelect.ProfileSelection.Individual']")
DRIVE_SELECT_ADAPTIVE_MODE = XpathString("//*[@content-desc='###DriveSelect.ProfileSelection.AdaptiveMode']")
DRIVE_SELECT_ADAPTIVE_MODE_ACTIVE = XpathString("//*[@content-desc='###DriveSelect.ProfileSelection.AdaptiveMode'][@checked='true']")
DRIVE_SELECT_OFFROAD = XpathString("//*[contains(@content-desc,'###DriveSelect.ProfileSelection.Offroad')]")

LIFT_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/lift_up']")
LIFT_DOWN_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/lift_down']")

INDIVIDUAL_SETTINGS_BALANCE_BUTTON = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/memberValue2')]")
INDIVIDUAL_SETTINGS_COMFORT_BUTTON = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/memberValue1')]")
INDIVIDUAL_SETTINGS_DYNAMIC_BUTTON = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/memberValue3')]")
INDIVIDUAL_SETTINGS_ECO_BUTTON = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/memberValue5')]")
INDIVIDUAL_SETTINGS_OFFROAD_BUTTON = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/memberValue9')]")
SELECTION_GROUP_STEERING_ASSIST = XpathString("//*[contains(@content-desc,'member_power_steering_assist')]/../../*")
SELECTION_GROUP_DRIVE_TRAIN = XpathString("//*[contains(@content-desc,'member_driveTrain')]/../../*")
SELECTION_GROUP_ALL_WHEEL_STEERING = XpathString("//*[contains(@content-desc,'member_all_wheel_steering')]/../../*")
SELECTION_GROUP_DAMPER_CONTROL = XpathString("//*[contains(@content-desc,'member_damper_control')]/../../*")
SELECTION_GROUP_LEVEL_CONTROL = XpathString("//*[contains(@content-desc,'member_level_control')]/../../*")
SELECTION_GROUP_CHASSIS = XpathString("//*[contains(@content-desc,'member_chassis')]/../../*")
SELECTION_GROUP_SOUND_COMPONENTS = XpathString("//*[contains(@content-desc,'member_sound_components')]/../../*")
SELECTION_GROUP_REAR_AXLE_DIFFERENTIAL = XpathString("//*[contains(@content-desc,'member_rear_axle_differential')]/../../*")
SELECTION_GROUP_DRIVER_ASSISTANCE = XpathString("//*[contains(@content-desc,'member_driver_assistance')]/../../*")
SELECTION_GROUP_DISPLAY_SETUP = XpathString("//*[contains(@content-desc,'member_display_setup')]/../../*")


DOORS_SETTINGS_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/car__tab_bar_fragment_title___smart_entry')]")

INFO_BUTTON_HIGHWAY = XpathString(f"//*{audi.virtual_mirror_highway_view}/../..//*[@resource-id='de.eso.car.audi:id/listItemButton_0']")
INFO_BUTTON_TURN_VIEW = XpathString(f"//*{audi.virtual_mirror_turn_view}/../..//*[@resource-id='de.eso.car.audi:id/listItemButton_0']")
INFO_BUTTON_PARK_VIEW = XpathString(f"//*{audi.virtual_mirror_park_view}/../..//*[@resource-id='de.eso.car.audi:id/listItemButton_0']")

INFO_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/infoButton']")
DRIVE_SELECT_INDIVIDUAL_SETTINGS_BUTTON = XpathString("//*[contains(@content-desc,'DriveSelect.Settings')][contains(@resource-id,'floatingButton')]")

DRIVE_SELECT_SETTINGS_BUTTON = XpathString("//*[contains(@content-desc,'DriveSelect.Settings')][contains(@resource-id,'settingsButton')]")
DRIVE_SELECT_SETTINGS_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/drive_select_title')]")
DRIVE_SELECT_CURVE_CONTROL_INFO_BUTTON = XpathString("//*[contains(@content-desc,'CurveViewSwitchInfo')]")
DRIVE_SELECT_PITCH_CONTROL_INFO_BUTTON = XpathString("//*[contains(@content-desc,'PitchControlSwitchInfo')]")
DRIVE_SELECT_SETTINGS_POPUP_PITCH_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/ds_comfort_pitch_title')]")
DRIVE_SELECT_SETTINGS_POPUP_CURVE_TITLE = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/ds_comfort_curve_title')]")

SERVICE_INTERVAL_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/service_interval')]")
SERVICE_INTERVAL_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_service_sia')]")

VEHICLE_DATA_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/vehicle_data')]")
VEHICLE_DATA_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/vehicle_data')]")

OIL_SERVICE_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/oil_service')]/..")
OIL_SERVICE_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_service_oil_level')]")
OIL_BAR_GRAPH = XpathString ("//*[@resource-id='de.eso.car.audi:id/oil_bar_graph']")

WARNING_MEMORY_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/warning_memory')]")
WARNING_MEMORY_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_service_warning')]")

SERVICING_RDK_SAVE_BUTTON = XpathString ("//*[contains(@content-desc,'CarService.button.rdkEnterButton')]")
SERVICING_RDK_SAVE_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_service_tire_pressure')]")
SERVICING_TIRE_PRESSURE_SAVE_BUTTON = XpathString ("//*[contains(@content-desc,'CarServiceRKA.button.tirePressureButton')]")
SERVICING_TIRE_PRESSURE_CANCEL_BUTTON = XpathString ("//*[contains(@content-desc,'CarServiceRKA.button.tirePressureNoButton')]")
SERVICING_TIRE_PRESSURE_CONFIRM_BUTTON = XpathString ("//*[contains(@content-desc,'CarServiceRKA.button.tirePressureYesButton')]")

MORE_ZV_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/centrallocking')]/../..")
MORE_ZV_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_more_zv')]")
MORE_TILT_ANGLE_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/more_tiltangle')]/../..")
MORE_TILT_ANGLE_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/car__settings_submenu_title___tiltangle')]")
MORE_AUTO_RECU_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/etron_auto_recuparation')]/../..")
MORE_VIN_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/vin_keys')]/../..")
MORE_VIN_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_keys_vin')]")
MORE_JOKERKEY_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/jokerkey_settings')]/../..")
MORE_JOKERKEY_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_jokerkey')]")
MORE_UGDO_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/ugdo')]/../..")
MORE_UGDO_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_ugdo')]")
MORE_BRAKE_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/brake')]/../..")
MORE_BRAKE_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_brakes')]")
MORE_WIPER_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/wiper')]/../..")
MORE_WIPER_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_wiper')]")
MORE_DRIVING_SCHOOL_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/car_driving_school')]/../..")
MORE_DRIVING_SCHOOL_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_driving_school')]")
MORE_DATA_MANAGEMENT_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/data_managment')]/../..")
MORE_DATA_MANAGEMENT_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_data_managment')]")
MORE_TRAILER_MODE_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/trailer_mode')]/../..")
MORE_JACK_MODE_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/car_jack_mode')]/../..")
MORE_OSD_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/osd')]/../..")
MORE_OSD_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_osd')]")
MORE_EASY_ENTRY_DRIVER_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/easy_entry_drive')]/../..")
MORE_CPD_ONE_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/child_presence_detection_1_0_title')]/../..")
MORE_CPD_TWO_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/child_presence_detection_2_0_title')]/../..")
MORE_CPD_TWO_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_child_presence_detection')]")

MORE_DPN_DISCLAIMER_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/data_managment_data_protection_note')]/../..")
MORE_DPN_DISCLAIMER_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_data_protection_note')]")
MORE_DAF_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/data_managment_export_piloted_data')]/../..")

MORE_ROLLING_ABILITY_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/rolling_ability')]/../..")
MORE_ROLLING_ABILITY_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_more_rolling_ability')]")
MORE_EPB_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/epb_list_title')]/../..")
MORE_EPB_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/title_epb')]")


SWITCH_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/switchControl']")
CONFIRM_BUTTON = XpathString("//*[@resource-id='android:id/button2']")
CANCEL_BUTTON = XpathString("//*[@resource-id='android:id/button1']")

MORE_CPD_TWO_ENTRY_BUTTON = XpathString ("//*[contains(@content-desc,'ChildPresenceDetection_2.0-Submenu')]")
MORE_CPD_TWO_SWITCH_BUTTON = XpathString (f"{MORE_CPD_TWO_BUTTON}{SWITCH_BUTTON}")

SUBMENU_ENTRY_BUTTON = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:drawable/e020_e520_submenu_rtl_conform')]")


ENERGY_TIPPS_PERFORMANCE_BUTTON = XpathString ("//*[contains(@content-desc,'HelpTile-PERFORMANCE')]")
ENERGY_TIPPS_BATTERY_PHEV_BUTTON = XpathString ("//*[contains(@content-desc,'HelpTile-BATTERY_PHEV')]")
ENERGY_TIPPS_ELECTRIC_DRIVING_PHEV_BUTTON = XpathString ("//*[contains(@content-desc,'HelpTile-ELECTRIC_DRIVING_PHEV')]")
ENERGY_TIPPS_PERFORMANCE_BATTERY_LEVEL_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/texttool_globals_dialog_title___help_performance_subtitle_1')]")
ENERGY_TIPPS_BATTERY_PHEV_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/texttool_globals_dialog_title___help_battery_phev_subtitle_1')]")
ENERGY_TIPPS_ELECTRIC_DRIVING_PHEV_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/texttool_globals_dialog_title___help_electric_driving_subtitle_1')]")

GOODBYE_TITLE = XpathString ("//*[contains(@content-desc,'de.eso.car.audi:string/goodbye_title')]")
GOODBYE_CPD_BUTTON = XpathString ("//*[contains(@resource-id,'child_presense_detection_2_button')]")
GOODBYE_HINT_BOX = XpathString ("//*[contains(@resource-id,'pd_hint_layoput')]")

SHOW_MORE = XpathString("//*[contains(@content-desc, 'de.eso.globalsearch:string/result_headline_button_text__show_more')]")
CLOSE_GROUP = XpathString("//*[contains(@content-desc, 'de.eso.globalsearch:string/result_headline_button_text__close_group')]")
LISTITEM_TEXTSTART = XpathString("//*[contains(@resource-id, 'de.eso.globalsearch:id/listItemGrid2MainContent_textStart')]")
BUTTON_SHOW_LESS = XpathString("//*[contains(@content-desc, 'de.eso.globalsearch:string/result_headline_button_text__show_less')]")

WARNING_STORE_TEXT = XpathString("//*[contains(@content-desc, 'de.eso.car.audi:string/warning_store_')]")
SEARCH_BUTTON = XpathString("//*[@class='android.widget.ImageButton']/ancestor::*[contains(@resource-id, 'de.eso.car.audi:id/actionButtons')]")
SETTINGS_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/menuActionsBackground']")
STEPPER_LEFT_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/stepper_button_left']")
STEPPER_RIGHT_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/stepper_button_right']")
POPUP_CLOSE_BUTTON = XpathString("//*[@resource-id='de.eso.car.audi:id/popupCloseButton']")
MAIN_LIST = XpathString("//*[@resource-id='de.eso.car.audi:id/list_fragment_list_view']")
DATE_TIME_MANUALLY = XpathString("//*[contains(@content-desc, 'ManualTimeSettingsDateAndTime')]")
DATE_TIME_SUBTEXT = XpathString("//*[@resource-id='de.eso.car.audi:id/listItemGrid2MainContent_subtextStart']")
SWITCH_SET_AUTOMATIC = XpathString("//*[@content-desc='###AutomaticTime-switch']")
SWITCH_SET_AUTOMATIC_TIME_ZONE = XpathString("//*[@content-desc='###AutomaticTimeZone-switch']")

BUTTON_UP_DAY = XpathString("//*[contains(@resource-id, 'de.eso.car.audi:id/dateLayout_day')]//*[contains(@class, 'android.widget.Button')][@index='2']")
BUTTON_DOWN_DAY = XpathString("//*[contains(@resource-id, 'de.eso.car.audi:id/dateLayout_day')]//*[contains(@class, 'android.widget.Button')][@index='0']")
BUTTON_UP_YEAR = XpathString("//*[contains(@resource-id, 'de.eso.car.audi:id/dateLayout_year')]//*[contains(@class, 'android.widget.Button')][@index='2']")
BUTTON_DOWN_YEAR = XpathString("//*[contains(@resource-id, 'de.eso.car.audi:id/dateLayout_year')]//*[contains(@class, 'android.widget.Button')][@index='0']")
BUTTON_UP_MONTH = XpathString("//*[contains(@resource-id, 'de.eso.car.audi:id/dateLayout_month')]//*[contains(@class, 'android.widget.Button')][@index='2']")
BUTTON_DOWN_MONTH = XpathString("//*[contains(@resource-id, 'de.eso.car.audi:id/dateLayout_month')]//*[contains(@class, 'android.widget.Button')][@index='0']")
LABEL_DAY = XpathString("//*[contains(@content-desc, 'CarSetupGeneralDateTimePicker.textView.label_day')]")
LABEL_MONTH = XpathString("//*[contains(@content-desc, 'CarSetupGeneralDateTimePicker.textView.label_month')]")
LABEL_YEAR = XpathString("//*[contains(@content-desc, 'CarSetupGeneralDateTimePicker.textView.label_year')]")
DATE_DAY =XpathString("//*[contains(@resource-id, 'de.eso.car.audi:id/dateLayout_day')]//*[contains(@resource-id, 'android:id/numberpicker_input')]")
DATE_MONTH = XpathString("//*[contains(@resource-id, 'de.eso.car.audi:id/dateLayout_month')]//*[contains(@resource-id, 'android:id/numberpicker_input')]")
DATE_YEAR = XpathString("//*[contains(@resource-id, 'de.eso.car.audi:id/dateLayout_year')]//*[contains(@resource-id, 'android:id/numberpicker_input')]")
BUTTON_UP_HOURS = XpathString("//*[contains(@resource-id, 'de.eso.car.audi:id/clockLayout_hours')]//*[contains(@class, 'android.widget.Button')][@index='2']")
BUTTON_DOWN_HOURS = XpathString("//*[contains(@resource-id, 'de.eso.car.audi:id/clockLayout_hours')]//*[contains(@class, 'android.widget.Button')][@index='0']")
BUTTON_UP_MINUTES = XpathString("//*[contains(@content-desc, 'CarSetupGeneralDateTimePicker.textView.label_minutes')]/following-sibling::*//*[contains(@class, 'android.widget.Button')][@index='2']")
BUTTON_DOWN_MINUTES = XpathString("//*[contains(@content-desc, 'CarSetupGeneralDateTimePicker.textView.label_minutes')]/following-sibling::*//*[contains(@class, 'android.widget.Button')][@index='0']")
TIME_HOURS = XpathString("//*[contains(@resource-id, 'de.eso.car.audi:id/clockLayout_hours')]//*[contains(@resource-id, 'android:id/numberpicker_input')]")
TIME_MINUTES = XpathString("//*[contains(@content-desc, 'CarSetupGeneralDateTimePicker.textView.label_minutes')]/following-sibling::*//*[contains(@resource-id, 'android:id/numberpicker_input')]")
TIME_FORMAT = XpathString("//*[contains(@resource-id, 'de.eso.car.audi:id/switchControl')][contains(@content-desc, '###TimeFormat-switch')]")
TIME_CONTAINER = XpathString("//*[contains(@resource-id, 'de.eso.car.audi:id/list_fragment_list_view')]")

LIST_ENTRY = XpathString("//*[contains(@resource-id, 'listItem')]")
EDIT_TEXT = XpathString("//*[@class='android.widget.EditText']")

TRAFFIC_LIGHT_SWITCH = XpathString("//*[contains(@content-desc,'de.eso.car.audi:string/texttool_custom_fas_tile___traffic_light_information')]/../*[@class='android.widget.Switch']")
