# -*- coding: utf-8 -*-
"""Created on 28.05.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
Contains helper functions for the my audi app
"""
import logging

from enna_kwd_testing.utilities.phone.myaudi.frontend.myaudi_xpath_collection import MyAudiXpathLoader
from enna_kwd_testing.utilities.phone.server_android import Server

MODULE_LOGGER = logging.getLogger(__name__)


def scroll_to_vehicle_messages_card_on_dashboard(phone: Server, xpath_collection: MyAudiXpathLoader):
	"""Scroll to the Messages-Card on the Vehicle-Dashboard

	:param Server phone: Device which should be used for navigation
	:param MyAudiXpathLoader xpath_collection: Xpath-Collection
	"""
	xpath_dashboard_scroll_container = xpath_collection.get_xpath("dashboard", "scroll_container")
	xpath_dashboard_vsr_swipe_container = xpath_collection.get_xpath("dashboard", "vsr_swipe_container")
	phone.scroll_to_element_in_list(xpath_dashboard_scroll_container, xpath_dashboard_vsr_swipe_container)

	phone.scroll_horizontal_right(xpath_dashboard_vsr_swipe_container)


def scroll_to_vehicle_information_card_on_dashboard(phone: Server, xpath_collection: MyAudiXpathLoader):
	"""Scroll to the Information-Card on the Vehicle-Dashboard

	:param Server phone: Device which should be used for navigation
	:param MyAudiXpathLoader xpath_collection: Xpath-Collection
	"""
	xpath_dashboard_scroll_container = xpath_collection.get_xpath("dashboard", "scroll_container")
	xpath_dashboard_vsr_swipe_container = xpath_collection.get_xpath("dashboard", "vsr_swipe_container")

	phone.scroll_to_element_in_list(xpath_dashboard_scroll_container, xpath_dashboard_vsr_swipe_container)

	phone.scroll_horizontal_left(xpath_dashboard_vsr_swipe_container)
