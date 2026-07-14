# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""

from enna_hcp_configuration.android.contexts import in_car_office as contexts_in_car_office, launcher as contexts_launcher, privacy as contexts_privacy
from enna_hcp_configuration.android import xpaths
from enna_hcp_configuration.android.xpaths import in_car_office as xpaths_in_car_office
from enna_hcp_configuration.android.base import HMIActionType


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""

	# Back to App-List
	graph.add_transition(contexts_in_car_office.WELCOME, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	graph.add_transition(contexts_in_car_office.EMAIL_OVERVIEW, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_in_car_office.EMAIL_OVERVIEW_FILTER, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_in_car_office.EMAIL_OVERVIEW_SLIDE_OUT, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	graph.add_transition(contexts_in_car_office.READ_MAIL, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_in_car_office.READ_MAIL_ANSWER, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	graph.add_transition(contexts_in_car_office.CALENDAR, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_in_car_office.CALENDAR_EVENT_SELECTED, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_in_car_office.CALENDAR_NO_EVENTS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_in_car_office.CALENDAR_ALL_DAY_EVENTS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_in_car_office.CALENDAR_EVENT_CONTACTS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	graph.add_transition(contexts_in_car_office.SETTINGS_GENERAL, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_CALENDAR, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_in_car_office.UNLINK_ACCOUNT_DIALOG, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_OSD, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	graph.add_transition(contexts_in_car_office.BLOCKING_DISCLAIMER, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	graph.add_transition(contexts_in_car_office.PRIVACY_SETTINGS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	# welcome
	graph.add_transition(contexts_in_car_office.WELCOME, contexts_in_car_office.EMAIL_OVERVIEW, (HMIActionType.click_element, [xpaths_in_car_office.WELCOME_CONNECT_ACCOUNT_BUTTON]))

	# email overview
	graph.add_transition(contexts_in_car_office.EMAIL_OVERVIEW, contexts_in_car_office.CALENDAR, (HMIActionType.click_element, [xpaths_in_car_office.TAB_CALENDAR_BUTTON]))
	graph.add_transition(contexts_in_car_office.EMAIL_OVERVIEW, contexts_in_car_office.SETTINGS_GENERAL, (HMIActionType.click_element, [xpaths_in_car_office.SETTINGS_BUTTON]))
	graph.add_transition(contexts_in_car_office.EMAIL_OVERVIEW, contexts_in_car_office.EMAIL_OVERVIEW_FILTER, (HMIActionType.click_element, [xpaths_in_car_office.EMAIL_FILTER_BUTTON]))

	graph.add_transition(contexts_in_car_office.EMAIL_OVERVIEW_SLIDE_OUT, contexts_in_car_office.EMAIL_OVERVIEW, (HMIActionType.click_element, [xpaths_in_car_office.CLOSE_BUTTON]))

	# read email
	graph.add_transition(contexts_in_car_office.READ_MAIL, contexts_in_car_office.EMAIL_OVERVIEW, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))
	graph.add_transition(contexts_in_car_office.READ_MAIL, contexts_in_car_office.READ_MAIL_ANSWER, (HMIActionType.click_element, [xpaths_in_car_office.ANSWER_EMAIL_BUTTON]))

	graph.add_transition(contexts_in_car_office.READ_MAIL_ANSWER, contexts_in_car_office.READ_MAIL, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))

	# calendar
	graph.add_transition(contexts_in_car_office.CALENDAR, contexts_in_car_office.EMAIL_OVERVIEW, (HMIActionType.click_element, [xpaths_in_car_office.TAB_EMAIL_BUTTON]))
	graph.add_transition(contexts_in_car_office.CALENDAR_EVENT_SELECTED, contexts_in_car_office.EMAIL_OVERVIEW, (HMIActionType.click_element, [xpaths_in_car_office.TAB_EMAIL_BUTTON]))
	graph.add_transition(contexts_in_car_office.CALENDAR_NO_EVENTS, contexts_in_car_office.EMAIL_OVERVIEW, (HMIActionType.click_element, [xpaths_in_car_office.TAB_EMAIL_BUTTON]))
	graph.add_transition(contexts_in_car_office.CALENDAR_ALL_DAY_EVENTS, contexts_in_car_office.EMAIL_OVERVIEW, (HMIActionType.click_element, [xpaths_in_car_office.TAB_EMAIL_BUTTON]))
	graph.add_transition(contexts_in_car_office.CALENDAR_EVENT_CONTACTS, contexts_in_car_office.EMAIL_OVERVIEW, (HMIActionType.click_element, [xpaths_in_car_office.TAB_EMAIL_BUTTON]))

	graph.add_transition(contexts_in_car_office.CALENDAR, contexts_in_car_office.SETTINGS_GENERAL, (HMIActionType.click_element, [xpaths_in_car_office.SETTINGS_BUTTON]))

	# settings
	graph.add_transition(contexts_in_car_office.SETTINGS_GENERAL, contexts_in_car_office.SETTINGS_CALENDAR, (HMIActionType.click_element, [xpaths_in_car_office.SETTINGS_TAB_CALENDAR_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_GENERAL, contexts_in_car_office.EMAIL_OVERVIEW, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_GENERAL, contexts_in_car_office.READ_MAIL, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))

	graph.add_transition(contexts_in_car_office.SETTINGS_GENERAL, contexts_in_car_office.CALENDAR, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_GENERAL, contexts_in_car_office.CALENDAR_EVENT_SELECTED, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_GENERAL, contexts_in_car_office.CALENDAR_NO_EVENTS, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_GENERAL, contexts_in_car_office.CALENDAR_ALL_DAY_EVENTS, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_GENERAL, contexts_in_car_office.CALENDAR_EVENT_CONTACTS, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))

	graph.add_transition(contexts_in_car_office.SETTINGS_GENERAL, contexts_in_car_office.SETTINGS_EDIT_ACCOUNT, (HMIActionType.click_element_in_list, [xpaths_in_car_office.SETTINGS_EDIT_ACCOUNT_BUTTON, xpaths_in_car_office.SETTINGS_LIST]))

	graph.add_transition(contexts_in_car_office.SETTINGS_CALENDAR, contexts_in_car_office.SETTINGS_GENERAL, (HMIActionType.click_element, [xpaths_in_car_office.SETTINGS_TAB_GENERAL_BUTTON]))

	graph.add_transition(contexts_in_car_office.SETTINGS_CALENDAR, contexts_in_car_office.EMAIL_OVERVIEW, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_CALENDAR, contexts_in_car_office.READ_MAIL, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_CALENDAR, contexts_in_car_office.CALENDAR, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_CALENDAR, contexts_in_car_office.CALENDAR_EVENT_SELECTED, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_CALENDAR, contexts_in_car_office.CALENDAR_NO_EVENTS, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_CALENDAR, contexts_in_car_office.CALENDAR_ALL_DAY_EVENTS, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_CALENDAR, contexts_in_car_office.CALENDAR_EVENT_CONTACTS, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))

	graph.add_transition(contexts_in_car_office.SETTINGS_EDIT_ACCOUNT, contexts_in_car_office.SETTINGS_GENERAL, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))
	graph.add_transition(contexts_in_car_office.SETTINGS_EDIT_ACCOUNT, contexts_in_car_office.UNLINK_ACCOUNT_DIALOG, (HMIActionType.click_element, [xpaths_in_car_office.SETTINGS_DISCONNECT_ACCOUNT_BUTTON]))

	graph.add_transition(contexts_in_car_office.SETTINGS_OSD, contexts_in_car_office.SETTINGS_GENERAL, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))

	graph.add_transition(contexts_in_car_office.UNLINK_ACCOUNT_DIALOG, contexts_in_car_office.SETTINGS_EDIT_ACCOUNT, (HMIActionType.click_element, [xpaths_in_car_office.POPUP_NO_BUTTON]))

	graph.add_transition(contexts_in_car_office.BLOCKING_DISCLAIMER, contexts_in_car_office.SETTINGS_GENERAL, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))

	graph.add_transition(contexts_in_car_office.PRIVACY_SETTINGS, contexts_in_car_office.EMAIL_OVERVIEW, (HMIActionType.click_element, [xpaths_in_car_office.PRIVACY_OK_BUTTON]))
	graph.add_transition(contexts_in_car_office.PRIVACY_SETTINGS, contexts_privacy.PRIVACY_SETTINGS, (HMIActionType.click_element, [xpaths_in_car_office.PRIVACY_PRIVACY_SETTINGS_BUTTON]))

	graph.add_transition(contexts_in_car_office.WELCOME_SIGNING_CONNECTING, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_in_car_office.WELCOME_SIGNING_CONNECTING, contexts_in_car_office.LINKING_TO_EMAIL_ACOUNT, (HMIActionType.click_element, [xpaths_in_car_office.WELCOME_ACCOUNT_USE_BUTTON]))
	graph.add_transition(contexts_in_car_office.LINKING_TO_EMAIL_ACOUNT, contexts_in_car_office.WELCOME_SIGNING_CONNECTING, (HMIActionType.click_element, [xpaths_in_car_office.BACK_BUTTON]))
