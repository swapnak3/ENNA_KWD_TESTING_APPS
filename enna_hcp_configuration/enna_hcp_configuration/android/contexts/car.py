# -*- coding: utf-8 -*-
"""Contexts for the car app."""

from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathBlacklistWhitelistDetectorExtension, ElementByXPathDetectorExtension
from enna_hcp_configuration.android.xpaths import car as xpaths_car
from enna_hcp_configuration.common.base import Element

AUDI_DRIVE_SELECT = Element("audi_drive_select", ElementByXPathDetectorExtension(xpaths_car.AUDI_DRIVE_SELECT_TITLE))
DISPLAY = Element("display", ElementByXPathDetectorExtension(xpaths_car.DISPLAY_TITLE))
LIGHTS = Element("lights", ElementByXPathDetectorExtension(xpaths_car.LIGHTS_TITLE))
SEATS = Element("seats", ElementByXPathDetectorExtension(xpaths_car.SEATS_TITLE))
DOORS = Element("doors", ElementByXPathDetectorExtension(xpaths_car.DOORS_TITLE))
SERVICING = Element("servicing", ElementByXPathDetectorExtension(xpaths_car.SERVICING_TITLE))
SERVICING_VEHICLE_STATUS = Element("servicing_vehicle_status", ElementByXPathDetectorExtension(xpaths_car.SERVICING_VEHICLE_STATUS_TITLE)) #no longer found
SERVICING_VEHICLE_DATA = Element("servicing_vehicle_data", ElementByXPathDetectorExtension(xpaths_car.SERVICING_VEHICLE_DATA_TITLE)) #no longer found
SERVICING_INTERVAL = Element("servicing_interval", ElementByXPathDetectorExtension(xpaths_car.SERVICE_INTERVAL_TITLE))
SERVICING_OIL = Element("servicing_oil", ElementByXPathDetectorExtension(xpaths_car.OIL_SERVICE_TITLE))
SERVICING_WARNING_MEMORY = Element("servicing_warning_memory", ElementByXPathDetectorExtension(xpaths_car.WARNING_MEMORY_TITLE))
MORE = Element("more", ElementByXPathDetectorExtension(xpaths_car.MORE_TITLE))

ENERGY = Element("energy", ElementByXPathDetectorExtension(xpaths_car.ENERGY_TITLE))
DEPARTURE_TIMES = Element("departure_times", ElementByXPathDetectorExtension(xpaths_car.DEPARTURE_TIMES_TITLE))
LOCATIONS = Element("locations", ElementByXPathDetectorExtension(xpaths_car.LOCATIONS_TITLE))
TIPPS = Element("tipps", ElementByXPathDetectorExtension(xpaths_car.TIPPS_TITLE))

ENERGY_TIPPS_PERFORMANCE_BATTERY_LEVEL = Element("energy_tipps_performance_battery_level", ElementByXPathDetectorExtension(xpaths_car.ENERGY_TIPPS_PERFORMANCE_BATTERY_LEVEL_TITLE))
ENERGY_TIPPS_BATTERY_PHEV = Element("energy_tipps_battery_phev", ElementByXPathDetectorExtension(xpaths_car.ENERGY_TIPPS_BATTERY_PHEV_TITLE))
ENERGY_TIPPS_ELECTRIC_DRIVING_PHEV = Element("energy_tipps_electric_driving_phev", ElementByXPathDetectorExtension(xpaths_car.ENERGY_TIPPS_ELECTRIC_DRIVING_PHEV_TITLE))

GOODBYE_SCREEN = Element("goodbye_screen", ElementByXPathDetectorExtension(xpaths_car.GOODBYE_TITLE))

SERVICING_RDK_SAVE = Element("servicing_rdk_save", ElementByXPathDetectorExtension([xpaths_car.SERVICING_RDK_SAVE_TITLE, xpaths_car.SERVICING_TIRE_PRESSURE_SAVE_BUTTON]))
SERVICING_RDK_SAVE_CONFIRM = Element("servicing_rdk_save_confirm", ElementByXPathDetectorExtension([xpaths_car.SERVICING_RDK_SAVE_TITLE, xpaths_car.SERVICING_TIRE_PRESSURE_CONFIRM_BUTTON]))
SERVICING_RDK_SAVE_CONFIRM_LOADING = Element("servicing_rdk_save_confirm_loading", ElementByXPathBlacklistWhitelistDetectorExtension(
	must_exist=[xpaths_car.SERVICING_RDK_SAVE_TITLE],
	must_not_exist=[xpaths_car.SERVICING_TIRE_PRESSURE_SAVE_BUTTON, xpaths_car.SERVICING_TIRE_PRESSURE_CONFIRM_BUTTON]
))

AUDI_DRIVE_SELECT_SETTINGS = Element("audi_drive_select_settings", ElementByXPathDetectorExtension([xpaths_car.DRIVE_SELECT_SETTINGS_TITLE,xpaths_car.DRIVE_SELECT_CURVE_CONTROL_INFO_BUTTON]))
AUDI_DRIVE_SELECT_SETTINGS_POPUP_CURVE = Element("audi_drive_select_settings_popup_curve", ElementByXPathDetectorExtension([xpaths_car.DRIVE_SELECT_SETTINGS_POPUP_CURVE_TITLE]))
AUDI_DRIVE_SELECT_SETTINGS_POPUP_PITCH = Element("audi_drive_select_settings_popup_pitch", ElementByXPathDetectorExtension([xpaths_car.DRIVE_SELECT_SETTINGS_POPUP_PITCH_TITLE]))

DISPLAY_SETTINGS_CID = Element("display_settings_cid", ElementByXPathDetectorExtension(xpaths_car.CID_SETTINGS_TITLE))
DISPLAY_SETTINGS_HUD = Element("display_settings_hud", ElementByXPathDetectorExtension(xpaths_car.HUD_SETTINGS_TITLE))
DISPLAY_SETTINGS_FID = Element("display_settings_fid", ElementByXPathDetectorExtension(xpaths_car.FID_SETTINGS_TITLE))
DISPLAY_SETTINGS_PID = Element("display_settings_pid", ElementByXPathDetectorExtension(xpaths_car.PID_SETTINGS_TITLE))
DISPLAY_SETTINGS_VA = Element("display_settings_va", ElementByXPathDetectorExtension(xpaths_car.VA_SETTINGS_TITLE))

LIGHTS_INTERIOR = Element("lights_interior", ElementByXPathDetectorExtension(xpaths_car.LIGHTS_INTERIOR_TITLE))
LIGHTS_EXTERIOR = Element("lights_exterior", ElementByXPathDetectorExtension(xpaths_car.LIGHTS_EXTERIOR_TITLE))
LIGHTS_INTERIOR_SETTINGS = Element("lights_interior_settings", ElementByXPathDetectorExtension(xpaths_car.LIGHTS_INTERIOR_SETTINGS_TITLE))
LIGHTS_INTERIOR_SETTINGS_POPUP_LINK_COLORS = Element("lights_interior_settings_popup_link_colors", ElementByXPathDetectorExtension(xpaths_car.LIGHTS_INTERIOR_SETTINGS_POPUP_LINK_COLORS_TITLE))
LIGHTS_EXTERIOR_SETTINGS = Element("lights_exterior_settings", ElementByXPathDetectorExtension(xpaths_car.LIGHTS_EXTERIOR_SETTINGS_TITLE))
LIGHTS_COMING_LEAVING_HOME = Element("lights_coming_leaving_home", ElementByXPathDetectorExtension(xpaths_car.LIGHTS_COMING_LEAVING_HOME_TITLE))
LIGHTS_DIGITAL_SIGNATURES = Element("lights_digital_signatures", ElementByXPathDetectorExtension(xpaths_car.LIGHTS_DIGITAL_SIGNATURES_TITLE))

MORE_ZV = Element("more_zv", ElementByXPathDetectorExtension(xpaths_car.MORE_ZV_TITLE))
MORE_TILT_ANGEL = Element("more_tilt_angle", ElementByXPathDetectorExtension(xpaths_car.MORE_TILT_ANGLE_TITLE))
MORE_VIN = Element("more_vin", ElementByXPathDetectorExtension(xpaths_car.MORE_VIN_TITLE))
MORE_JOKERKEY = Element("more_jokerkey", ElementByXPathDetectorExtension(xpaths_car.MORE_JOKERKEY_TITLE))
MORE_UGDO = Element("more_ugdo", ElementByXPathDetectorExtension(xpaths_car.MORE_UGDO_TITLE))
MORE_BRAKE = Element("more_brake", ElementByXPathDetectorExtension(xpaths_car.MORE_BRAKE_TITLE))
MORE_WIPER = Element("more_wiper", ElementByXPathDetectorExtension(xpaths_car.MORE_WIPER_TITLE))
MORE_DRIVING_SCHOOL = Element("more_driving_school", ElementByXPathDetectorExtension(xpaths_car.MORE_DRIVING_SCHOOL_TITLE))
MORE_DATA_MANAGEMENT = Element("more_data_management", ElementByXPathDetectorExtension(xpaths_car.MORE_DATA_MANAGEMENT_TITLE))
MORE_OSD = Element("more_osd", ElementByXPathDetectorExtension(xpaths_car.MORE_OSD_TITLE))
MORE_CPD = Element("more_cpd", ElementByXPathDetectorExtension(xpaths_car.MORE_CPD_TWO_TITLE))

MORE_DPN_DISCLAIMER = Element("more_dpn_disclaimer", ElementByXPathDetectorExtension(xpaths_car.MORE_DPN_DISCLAIMER_TITLE))
MORE_ROLLING_ABILITY = Element("more_rolling_ability", ElementByXPathDetectorExtension(xpaths_car.MORE_ROLLING_ABILITY_TITLE))
MORE_EPB = Element("more_epb", ElementByXPathDetectorExtension(xpaths_car.MORE_EPB_TITLE))

SEATS_MASSAGE = Element("seats_massage", ElementByXPathDetectorExtension(xpaths_car.SEATS_MASSAGE_TITLE))
SEATS_ADJUSTMENT = Element("seats_adjustment", ElementByXPathDetectorExtension(xpaths_car.SEATS_ADJUSTMENT_TITLE))
SEATS_POSITION = Element("seats_position", ElementByXPathDetectorExtension(xpaths_car.SEATS_POSITION_TITLE))
SEATS_SETTINGS = Element("seats_settings", ElementByXPathDetectorExtension(xpaths_car.SEATS_SETTINGS_TITLE))

AUDI_DRIVE_SELECT_INDIVIDUAL_SETTINGS = Element("audi_drive_select_individual_settings", ElementByXPathBlacklistWhitelistDetectorExtension(
	must_exist=[xpaths_car.AUDI_DRIVE_SELECT_INDIVIDUAL_SETTINGS_TITLE],
	must_not_exist=[xpaths_car.DRIVE_SELECT_CURVE_CONTROL_INFO_BUTTON]
))

DRIVER_ASSISTANCE_FAVORITES = Element("driver_assistance_favorites", ElementByXPathDetectorExtension([xpaths_car.DRIVER_ASSISTANCE_FAVORITES_TITLE]))
DRIVER_ASSISTANCE_WARNINGS = Element("driver_assistance_warnings", ElementByXPathDetectorExtension([xpaths_car.DRIVER_ASSISTANCE_WARNINGS_TITLE]))
DRIVER_ASSISTANCE_LANE = Element("driver_assistance_lane", ElementByXPathDetectorExtension([xpaths_car.DRIVER_ASSISTANCE_LANE_TITLE]))
DRIVER_ASSISTANCE_SPEED = Element("driver_assistance_speed", ElementByXPathDetectorExtension([xpaths_car.DRIVER_ASSISTANCE_SPEED_TITLE]))
DRIVER_ASSISTANCE_BRAKE = Element("driver_assistance_brake", ElementByXPathDetectorExtension([xpaths_car.DRIVER_ASSISTANCE_BRAKE_TITLE]))
DRIVER_ASSISTANCE_EFFICIENCY = Element("driver_assistance_efficiency", ElementByXPathDetectorExtension([xpaths_car.DRIVER_ASSISTANCE_EFFICIENCY_TITLE]))
DRIVER_ASSISTANCE_SETTINGS = Element("driver_assistance_settings", ElementByXPathDetectorExtension([xpaths_car.DRIVER_ASSISTANCE_SETTINGS_TITLE]))

DOORS_SETTINGS = Element("doors_settings", ElementByXPathDetectorExtension([xpaths_car.DOORS_SETTINGS_TITLE]))

SETTINGS_SYSTEM_DATE_AND_TIME = Element("settings_system_date_and_time", ElementByXPathBlacklistWhitelistDetectorExtension(
		must_exist=[xpaths_car.SETTINGS_SYSTEM_DATE_AND_TIME_TITLE],
		must_not_exist=[xpaths_car.SETTINGS_SYSTEM_DATE_AND_TIME_MANUALLY_TITLE, xpaths_car.SETTINGS_SYSTEM_DATE_AND_TIME_TIMEZONE_TITLE])
)
SETTINGS_SYSTEM_DATE_AND_TIME_MANUALLY = Element("settings_system_date_and_time_manually", ElementByXPathDetectorExtension([xpaths_car.SETTINGS_SYSTEM_DATE_AND_TIME_MANUALLY_TITLE]))
SETTINGS_SYSTEM_DATE_AND_TIME_TIMEZONE = Element("settings_system_date_and_time_timezone", ElementByXPathDetectorExtension([xpaths_car.SETTINGS_SYSTEM_DATE_AND_TIME_TIMEZONE_TITLE]))

SETTINGS_SYSTEM_UNITS = Element("settings_system_units", ElementByXPathDetectorExtension(xpaths_car.SETTINGS_SYSTEM_UNITS_TITLE))

CONTEXT = ContextAnalyzer("car", AppPackageDetectorExtension(["de.eso.car.audi"]))
CONTEXT.add_elements_from_module(globals())
