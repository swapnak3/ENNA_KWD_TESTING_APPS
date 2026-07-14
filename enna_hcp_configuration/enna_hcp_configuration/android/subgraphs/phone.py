# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""
from enna_hcp_configuration.android.xpaths import phone as xpaths_phone
from enna_hcp_configuration.android.xpaths import launcher as xpaths_launcher

from enna_hcp_configuration.android.base import HMIActionType

from enna_hcp_configuration.android.contexts import phone as contexts_phone
from enna_hcp_configuration.android.contexts import settings as contexts_settings
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher
from enna_hcp_configuration.android.contexts import dataplan as contexts_dataplan
from enna_hcp_configuration.android.contexts import car2phone as contexts_car2phone


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_phone.MAIN, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	# graph.add_transition(contexts_phone.MAIN, contexts_phone.SEARCH_DEVICES, (HMIActionType.click_element, [xpaths_phone.MAIN_CONNECT_PHONE_BUTTON])) # not usage because of dependencies from connection state

	# from connections
	graph.add_transition(contexts_phone.CONNECTIONS, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_phone.BUTTON_BACK_BUTTON]))
	graph.add_transition(contexts_phone.CONNECTIONS, contexts_phone.DEVICE_MANAGER, (HMIActionType.click_element_in_list, [xpaths_phone.LIST_ITEM_OPEN_DEVICE_MANAGER, xpaths_phone.LIST_CONTAINER]))
	graph.add_transition(contexts_phone.CONNECTIONS, contexts_phone.BLUETOOTH_SETTINGS, (HMIActionType.click_element_in_list, [xpaths_phone.SUB_MENU_LIST_ITEM_OPEN_BLUETOOTH_SETTINGS, xpaths_phone.LIST_CONTAINER]))
	graph.add_transition(contexts_phone.CONNECTIONS, contexts_phone.VEHICLE_HOTSPOT_SETTINGS, (HMIActionType.click_element_in_list, [xpaths_phone.SUB_MENU_LIST_ITEM_OPEN_HOTSPOT_SETTINGS, xpaths_phone.LIST_CONTAINER]))
	graph.add_transition(contexts_phone.CONNECTIONS, contexts_phone.WIFI_SETTINGS,(HMIActionType.click_element_in_list, [xpaths_phone.SUB_MENU_LIST_ITEM_OPEN_WIFI_SETTINGS, xpaths_phone.LIST_CONTAINER]))
	graph.add_transition(contexts_phone.CONNECTIONS, contexts_phone.WIRELESS_CHARGING_SETTINGS, (HMIActionType.click_element_in_list, [xpaths_phone.LIST_ITEM_OPEN_WIRELESS_CHARGING_SETTINGS, xpaths_phone.LIST_CONTAINER]))
	graph.add_transition(contexts_phone.CONNECTIONS, contexts_dataplan.MAIN, (HMIActionType.click_element_in_list, [xpaths_phone.LIST_ITEM_OPEN_DATAPLAN_MENU, xpaths_phone.LIST_CONTAINER]))
	graph.add_transition(contexts_phone.CONNECTIONS, contexts_car2phone.MAIN, (HMIActionType.click_element_in_list, [xpaths_phone.LIST_ITEM_OPEN_CAR2PHONE, xpaths_phone.LIST_CONTAINER]))
	graph.add_transition(contexts_phone.CONNECTIONS, contexts_phone.OPEN_SOURCE_SOFTWARE_NOTICE, (HMIActionType.click_element_in_list, [xpaths_phone.LIST_ITEM_OPEN_SOURCE_SOFTWARE_NOTICE, xpaths_phone.LIST_CONTAINER]))


	graph.add_transition(contexts_phone.WIFI_SETTINGS, contexts_phone.CONNECTIONS, (HMIActionType.click_element, [xpaths_phone.BUTTON_BACK_BUTTON ]))
	graph.add_transition(contexts_phone.BLUETOOTH_SETTINGS, contexts_phone.CONNECTIONS, (HMIActionType.click_element, [xpaths_phone.BUTTON_BACK_BUTTON]))
	graph.add_transition(contexts_phone.VEHICLE_HOTSPOT_SETTINGS, contexts_phone.CONNECTIONS, (HMIActionType.click_element, [xpaths_phone.BUTTON_BACK_BUTTON]))
	graph.add_transition(contexts_phone.WIRELESS_CHARGING_SETTINGS, contexts_phone.CONNECTIONS, (HMIActionType.click_element, [xpaths_phone.BUTTON_BACK_BUTTON]))
	graph.add_transition(contexts_phone.DEVICE_MANAGER, contexts_phone.CONNECTIONS, (HMIActionType.click_element, [xpaths_phone.BUTTON_BACK_BUTTON]))

	# search device via device manager
	graph.add_transition(contexts_phone.DEVICE_MANAGER, contexts_phone.SEARCH_DEVICES, (HMIActionType.click_element, [xpaths_phone.ICON_ADD_NEW_DEVICE]))
	graph.add_transition(contexts_phone.SEARCH_DEVICES, contexts_phone.DEVICE_MANAGER, (HMIActionType.click_element, [xpaths_phone.BUTTON_BACK_BUTTON]))


	graph.add_transition(contexts_phone.SKELETON, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
