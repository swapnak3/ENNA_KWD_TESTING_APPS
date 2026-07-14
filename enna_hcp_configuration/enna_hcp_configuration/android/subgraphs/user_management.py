# -*- coding: utf-8 -*-
"""Module contains transitions from user_management to any menu"""

from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import user_management as contexts_user_management
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher
from enna_hcp_configuration.android.xpaths import user_management as xpaths_user_management
from enna_hcp_configuration.android.xpaths import launcher as xpaths_launcher


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""

	# from anywhere in user_management to launcher home
	graph.add_transition(contexts_user_management.MY_AUDI_LOGIN, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_user_management.CONTINUE_WITHOUT_MY_AUDI_LOGIN, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_user_management.ADD_LOCAL_USER, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_user_management.ALL_USERS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_user_management.YOUR_PROFILE, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_user_management.PRIMARY_USER, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_user_management.KEY_USER, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))

	# From ALL_USERS to ...
	graph.add_transition(contexts_user_management.ALL_USERS, contexts_user_management.KEY_USER, (HMIActionType.click_element, [xpaths_user_management.MAIN_KEY_USER_BUTTON]))
	graph.add_transition(contexts_user_management.ALL_USERS, contexts_user_management.YOUR_PROFILE, (HMIActionType.click_element, [xpaths_user_management.MAIN_YOUR_PROFILE_BUTTON]))
	graph.add_transition(contexts_user_management.ALL_USERS, contexts_user_management.PRIMARY_USER, (HMIActionType.click_element, [xpaths_user_management.MAIN_PRIMARY_USER_BUTTON]))
	graph.add_transition(contexts_user_management.ALL_USERS, contexts_user_management.ADD_LOCAL_USER, (HMIActionType.click_element, [xpaths_user_management.MAIN_ALL_USERS_ADD_NEW_USER_BUTTON]))
	graph.add_transition(contexts_user_management.ADD_LOCAL_USER, contexts_user_management.ALL_USERS, (HMIActionType.click_element, [xpaths_user_management.MAIN_USER_SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_user_management.ALL_USERS, contexts_user_management.USER_SETTINGS, (HMIActionType.click_element, [xpaths_user_management.MAIN_USER_SETTINGS_BUTTON]))

	graph.add_transition(contexts_user_management.USER_SETTINGS, contexts_user_management.ALL_USERS, (HMIActionType.click_element, [xpaths_user_management.MAIN_USER_SETTINGS_BACK_BUTTON]))

	# From YOUR_PROFILE to ...
	graph.add_transition(contexts_user_management.YOUR_PROFILE, contexts_user_management.ALL_USERS, (HMIActionType.click_element, [xpaths_user_management.MAIN_ALL_USERS_BUTTON]))
	graph.add_transition(contexts_user_management.YOUR_PROFILE, contexts_user_management.PRIMARY_USER, (HMIActionType.click_element, [xpaths_user_management.MAIN_PRIMARY_USER_BUTTON]))
	graph.add_transition(contexts_user_management.YOUR_PROFILE, contexts_user_management.USER_SETTINGS, (HMIActionType.click_element, [xpaths_user_management.MAIN_USER_SETTINGS_BUTTON]))

	graph.add_transition(contexts_user_management.USER_SETTINGS, contexts_user_management.YOUR_PROFILE, (HMIActionType.click_element, [xpaths_user_management.MAIN_USER_SETTINGS_BACK_BUTTON]))

	# From PRIMARY_USER to ...
	graph.add_transition(contexts_user_management.PRIMARY_USER, contexts_user_management.ALL_USERS, (HMIActionType.click_element, [xpaths_user_management.MAIN_ALL_USERS_BUTTON]))
	graph.add_transition(contexts_user_management.PRIMARY_USER, contexts_user_management.YOUR_PROFILE, (HMIActionType.click_element, [xpaths_user_management.MAIN_ALL_USERS_BUTTON]))
	graph.add_transition(contexts_user_management.PRIMARY_USER, contexts_user_management.USER_SETTINGS, (HMIActionType.click_element, [xpaths_user_management.MAIN_USER_SETTINGS_BUTTON]))
	graph.add_transition(contexts_user_management.PRIMARY_USER, contexts_user_management.DELETE_USER, (HMIActionType.click_element, [xpaths_user_management.MAIN_USER_DELETE_USER_BUTTON]))

	graph.add_transition(contexts_user_management.USER_SETTINGS, contexts_user_management.PRIMARY_USER, (HMIActionType.click_element, [xpaths_user_management.MAIN_USER_SETTINGS_BACK_BUTTON]))

	graph.add_transition(contexts_user_management.PRIMARY_USER, contexts_user_management.DELETE_USER, (HMIActionType.click_element, [xpaths_user_management.MAIN_USER_DELETE_USER_BUTTON]))
	graph.add_transition(contexts_user_management.DELETE_USER, contexts_user_management.PRIMARY_USER, (HMIActionType.click_element, [xpaths_user_management.POPUP_USER_CHANGE_CONFIRM_CANCEL_BUTTON]))


	# From KEY_USER to ...
	graph.add_transition(contexts_user_management.KEY_USER, contexts_user_management.ALL_USERS, (HMIActionType.click_element, [xpaths_user_management.MAIN_ALL_USERS_BUTTON]))
