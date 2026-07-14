# -*- coding: utf-8 -*-
"""Example to using phone utility."""

import logging
import os
import pathlib

import enna.core.image_processing.helper
import enna.core.logger
import enna.core.time

import enna_kwd_testing.utilities.phone.factory
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.definitions import RESOURCES_PATH
from enna_kwd_testing.utilities.helper import myaudi_hmi_helper
from enna_kwd_testing.utilities.phone.myaudi.frontend import screens
from enna_kwd_testing.utilities.phone.myaudi.frontend.myaudi_xpath_collection import MyAudiXpathLoader
from enna_kwd_testing.utilities.phone.myaudi.resources.localized_texts import LocalizedTexts

os.environ["ENNA_CONFIG_PATH"] = r"C:\SDKs\Python\enna_kwd_testing\config_dev"

MODULE_LOGGER = logging.getLogger(__name__)

# pylint: disable=too-many-statements,too-many-locals


def main():
	"""Test Procedure which is evaluating several Phone-Functions"""
	# ####################################################################################################
	# Setup and test Phone Connection
	# ####################################################################################################
	enna.core.logger.basic_setup("example_phone")
	factory = enna_kwd_testing.utilities.phone.factory.Factory(create_servers=True)
	factory.build_all()

	phone = factory["first_phone"]
	phone.take_screenshot(pathlib.Path("reports/log/phone_screenshot"))

	# ####################################################################################################
	# Variables
	# ####################################################################################################
	_xpath_collection = MyAudiXpathLoader(phone.get_package_name_long())
	_car_vin = "SUPERQ70000000000"

	# ####################################################################################################
	# Check Localized Texts
	# ####################################################################################################
	cms_data = LocalizedTexts(phone.get_app_version())
	pushnotifications_body_fallback_geofence_v1_deactivation_nok = cms_data.get_text("pushnotifications_body_fallback_geofence_v1_deactivation_nok")
	MODULE_LOGGER.info("pushnotifications_body_fallback_geofence_v1_deactivation_nok: " + pushnotifications_body_fallback_geofence_v1_deactivation_nok)

	# ####################################################################################################
	# Start MyAudi App
	# ####################################################################################################
	active_app = phone.get_active_package_name()
	MODULE_LOGGER.debug("Active App: " + active_app)

	if active_app != phone.get_package_name_long():
		phone.start_app_by_package_name(phone.get_package_name_long())

	# ####################################################################################################
	# Test Notification Menu
	# ####################################################################################################
	phone.get_device().open_notification()
	phone.get_device().open_quick_settings()
	phone.click_back_button()
	phone.click_back_button()

	# ####################################################################################################
	# Check if Dashboard is active and switch if not active
	# ####################################################################################################
	phone.select_screen(screens.SCREEN_LIST["REMOTE_PARKING_ASSIST"].get(VIN=_car_vin))
	phone.select_screen(screens.SCREEN_LIST["DASHBOARD"].get(VIN=_car_vin))
	# Not implemented yet: check_screen_is_visible

	# ####################################################################################################
	# Check if element is visible
	# ####################################################################################################
	xpath_dashboard_car_image = _xpath_collection.get_xpath("dashboard", "car_image")
	car_image_visible = phone.element_is_visible(xpath_dashboard_car_image)
	if not car_image_visible:
		error_msg = "Car Image not found on screen"
		MODULE_LOGGER.error(error_msg)

	# ####################################################################################################
	# Scroll up, down and sidewards
	# ####################################################################################################
	MODULE_LOGGER.info("*** Testing - Scroll up, down and sidewards ***")
	myaudi_hmi_helper.scroll_to_vehicle_messages_card_on_dashboard(phone, _xpath_collection)
	myaudi_hmi_helper.scroll_to_vehicle_information_card_on_dashboard(phone, _xpath_collection)

	# ####################################################################################################
	# Scroll to Element in List
	# ####################################################################################################
	MODULE_LOGGER.info("*** Testing - Scroll to Bottom and Back ***")

	xpath_dashboard_scroll_container = _xpath_collection.get_xpath("dashboard", "scroll_container")
	xpath_dashboard_btn_all_functions = _xpath_collection.get_xpath("dashboard", "btn_all_functions")
	phone.scroll_to_element_in_list(xpath_dashboard_scroll_container, xpath_dashboard_btn_all_functions)

	# ####################################################################################################
	# Screenshot Element
	# ####################################################################################################
	phone.take_screenshot_of_element(xpath_dashboard_btn_all_functions, pathlib.Path("reports/log/element_screenshot_all_functions_tile"))

	# ####################################################################################################
	# Navigate to All-Functions
	# ####################################################################################################
	MODULE_LOGGER.info("*** Testing - Navigate into All-Functions-Screen ***")

	phone.click_element(xpath_dashboard_btn_all_functions)

	# ####################################################################################################
	# Image Comparison
	# ####################################################################################################
	MODULE_LOGGER.info("*** Testing - Image Comparison ***")

	xpath_all_functions_scroll_container = _xpath_collection.get_xpath("all_functions", "scroll_container")
	xpath_all_functions_btn_geofence_alert = _xpath_collection.get_xpath("all_functions", "btn_geofence_alert")

	phone.scroll_to_element_in_list(xpath_all_functions_scroll_container, xpath_all_functions_btn_geofence_alert)

	template_image_path = RESOURCES_PATH / "template_data/all_functions_geofence_alert_active_icon"
	template_image_path = f"{template_image_path}.png"

	check1 = phone.image_is_visible_on_element(xpath_all_functions_btn_geofence_alert, template_image_path)
	MODULE_LOGGER.info("Image Template Check 1 (Element): " + str(check1))

	check2 = phone.image_is_visible_on_screen(template_image_path)
	MODULE_LOGGER.info("Image Template Check 1 (Screen): " + str(check2))

	# ####################################################################################################
	# Navigate to Geofence -> Add new Alert
	# ####################################################################################################
	MODULE_LOGGER.info("*** Testing - Navigate to Geofence -> Add new Alert ***")

	phone.click_element_in_list(xpath_all_functions_scroll_container, xpath_all_functions_btn_geofence_alert)

	xpath_geofence_alert_btn_add_alert = _xpath_collection.get_xpath("geofence_alert", "btn_add_alert")
	phone.click_element(xpath_geofence_alert_btn_add_alert)

	# ####################################################################################################
	# Click on Element
	# ####################################################################################################
	MODULE_LOGGER.info("*** Testing - Click on Element ***")

	xpath_geofence_add_alert_btn_edit_profile_name = _xpath_collection.get_xpath("geofence_add_alert", "btn_edit_profile_name")
	phone.click_element(xpath_geofence_add_alert_btn_edit_profile_name)

	# ####################################################################################################
	# Get Text of Element
	# ####################################################################################################
	MODULE_LOGGER.info("*** Testing - Get Text of Element ***")

	xpath_geofence_add_alert_input_profile_name = _xpath_collection.get_xpath("geofence_add_alert", "input_profile_name")
	element_text = phone.get_element_text(xpath_geofence_add_alert_input_profile_name)
	MODULE_LOGGER.debug("Element-Text: " + element_text)

	# ####################################################################################################
	# Set new Text on Element
	# ####################################################################################################
	MODULE_LOGGER.info("*** Testing - Set new Text on Element ***")

	phone.set_element_text(xpath_geofence_add_alert_input_profile_name, "test456", True)
	element_text_replaced = phone.get_element_text(xpath_geofence_add_alert_input_profile_name)
	MODULE_LOGGER.debug("Element-Text Replaced: " + element_text_replaced)

	# ####################################################################################################
	# Append Text on Element
	# ####################################################################################################
	MODULE_LOGGER.info("*** Testing - Append Text on Element ***")

	phone.set_element_text(xpath_geofence_add_alert_input_profile_name, "789", False)
	element_text_append = phone.get_element_text(xpath_geofence_add_alert_input_profile_name)
	MODULE_LOGGER.debug("Element-Text Append: " + element_text_append)

	# ####################################################################################################
	# Set Toggle Button State
	# ####################################################################################################
	MODULE_LOGGER.info("*** Testing - Set Toggle Button State ***")

	xpath_geofence_add_alert_btn_toggle_state = _xpath_collection.get_xpath("geofence_add_alert", "btn_toggle_state")
	phone.set_toggle_button_state(xpath_geofence_add_alert_btn_toggle_state, True)  # Do Nothing - Variant 1
	phone.set_toggle_button_state(xpath_geofence_add_alert_btn_toggle_state, False)  # Change State - Variant 1
	phone.set_toggle_button_state(xpath_geofence_add_alert_btn_toggle_state, False)  # Do Nothing - Variant 2
	phone.set_toggle_button_state(xpath_geofence_add_alert_btn_toggle_state, True)  # Change State - Variant 2

	# ####################################################################################################
	# OS-Functions
	# ####################################################################################################
	MODULE_LOGGER.info("*** Testing - OS-Functions ***")

	phone.put_app_in_background()
	phone.open_recent_apps()
	phone.click_back_button()
	phone.stop_app_by_package_name(phone.get_package_name_long())

	# ####################################################################################################
	# Finish Operations
	# ####################################################################################################
	MODULE_LOGGER.info("*** Testing - Finish Operations ***")
	phone.disconnect()


if __name__ == "__main__":
	main()
