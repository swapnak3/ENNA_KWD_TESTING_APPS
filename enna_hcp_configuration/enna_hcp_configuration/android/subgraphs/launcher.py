# -*- coding: utf-8 -*-
"""Module contains transitions from launcher to any menu"""
from enna_hcp_configuration.android.base import HMIActionType

from enna_hcp_configuration.android.contexts import aaam as contexts_aaam
from enna_hcp_configuration.android.contexts import car as contexts_car
from enna_hcp_configuration.android.contexts import core_services as contexts_core_services
from enna_hcp_configuration.android.contexts import experiences as contexts_experiences
from enna_hcp_configuration.android.contexts import globalsearch as contexts_globalsearch
from enna_hcp_configuration.android.contexts import in_car_office as contexts_in_car_office
from enna_hcp_configuration.android.contexts import ignite_store as contexts_ignite_store
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher
from enna_hcp_configuration.android.contexts import legal as contexts_legal
from enna_hcp_configuration.android.contexts import magic_engineering as contexts_magic_engineering
from enna_hcp_configuration.android.contexts import media as contexts_media
from enna_hcp_configuration.android.contexts import navigation as contexts_navigation
from enna_hcp_configuration.android.contexts import obb as contexts_obb
from enna_hcp_configuration.android.contexts import phone as contexts_phone
from enna_hcp_configuration.android.contexts import radio as contexts_radio
from enna_hcp_configuration.android.contexts import settings as contexts_settings

from enna_hcp_configuration.android.xpaths import launcher as xpaths_launcher


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	# from app list
	graph.add_transition(contexts_launcher.APP_LIST, contexts_aaam.THEMES, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_THEMES, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_car.AUDI_DRIVE_SELECT, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_CAR, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_car.DRIVER_ASSISTANCE_FAVORITES, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_DRIVER_ASSIST, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_car.ENERGY, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_CHARGING, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_core_services.HOME,  (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_CORE_SERVICE, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_experiences.MOOD, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_EXPERIENCES, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_globalsearch.MAIN, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_GLOBAL_SEARCH, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_in_car_office.EMAIL_OVERVIEW, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_IN_CAR_OFFICE, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_STORE, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_launcher.HOME, (HMIActionType.click_element, [xpaths_launcher.HOME_BUTTON]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_legal.OVERVIEW, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_LEGAL, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_magic_engineering.MAGIC_SERVICE, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_MAGIC_ENGINEERING, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_media.MAIN, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_USB_DRIVE, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_navigation.MAIN, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_NAVIGATION, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_obb.MAIN, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_ONLINE_MANUALS, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_phone.MAIN, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_PHONE, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_radio.MAIN_DAB_FM,  (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_RADIO, xpaths_launcher.LIST_CONTAINER]))
	graph.add_transition(contexts_launcher.APP_LIST, contexts_settings.MAIN, (HMIActionType.click_element_in_list, [xpaths_launcher.APP_TILE_SETTINGS, xpaths_launcher.LIST_CONTAINER]))

	# from media source selection
	graph.add_transition(contexts_launcher.CHANGE_SOURCE, contexts_media.MAIN, (HMIActionType.click_element, [xpaths_launcher.MEDIA_SOURCE_TILE_USB_DEVICE]))
	graph.add_transition(contexts_launcher.CHANGE_SOURCE, contexts_radio.MAIN_DAB_FM, (HMIActionType.click_element, [xpaths_launcher.MEDIA_SOURCE_TILE_RADIO]))
	graph.add_transition(contexts_launcher.HOME, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
