# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""

from enna_hcp_configuration.android import xpaths
from enna_hcp_configuration.android.xpaths import olb as xpaths_olb, legal as xpaths_legal
from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher, legal as contexts_legal, olb as contexts_olb


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_olb.LOADING, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	graph.add_transition(contexts_olb.SEVEN_DAYS_EDIT, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	graph.add_transition(contexts_olb.SETTINGS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_olb.SETTINGS_OPEN_SOURCE_SOFTWARE_NOTICE, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	graph.add_transition(contexts_olb.AUTOMATIC_PAUSE_DETECTION, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_olb.GENERIC_ERROR, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_olb.PRIVACY_ERROR, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_olb.PRIMARYUSER_ERROR, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_olb.LICENSE_ERROR, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_olb.LOADING_ERROR, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	graph.add_transition(contexts_olb.SEVEN_DAYS_EDIT, contexts_olb.STATISTIC, (HMIActionType.click_element, [xpaths_olb.STATISTIC_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC, contexts_olb.SEVEN_DAYS_EDIT, (HMIActionType.click_element, [xpaths_olb.SEVEN_DAY_SETTINGS_BUTTON]))

	graph.add_transition(contexts_olb.SEVEN_DAYS_EDIT, contexts_olb.SETTINGS, (HMIActionType.click_element, [xpaths_olb.SEVEN_DAY_SETTINGS_BUTTON]))
	graph.add_transition(contexts_olb.SETTINGS, contexts_olb.SEVEN_DAYS_EDIT, (HMIActionType.click_element, [xpaths_olb.SEVEN_DAY_SETTINGS_BACK_BUTTON]))

	graph.add_transition(contexts_olb.STATISTIC, contexts_olb.STATISTIC_BUSINESS, (HMIActionType.click_element, [xpaths_olb.STATISTIC_BUSINESS_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC, contexts_olb.STATISTIC_PRIVATE, (HMIActionType.click_element, [xpaths_olb.STATISTIC_PRIVATE_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC, contexts_olb.STATISTIC_COMMUTE, (HMIActionType.click_element, [xpaths_olb.STATISTIC_COMMUTE_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC, contexts_olb.STATISTIC_UNCATEGORIZED, (HMIActionType.click_element, [xpaths_olb.STATISTIC_UNCATEGORIZED_BUTTON]))

	graph.add_transition(contexts_olb.STATISTIC_BUSINESS, contexts_olb.STATISTIC, (HMIActionType.click_element, [xpaths_olb.STATISTIC_BUSINESS_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_BUSINESS, contexts_olb.STATISTIC_PRIVATE, (HMIActionType.click_element, [xpaths_olb.STATISTIC_PRIVATE_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_BUSINESS, contexts_olb.STATISTIC_COMMUTE, (HMIActionType.click_element, [xpaths_olb.STATISTIC_COMMUTE_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_BUSINESS, contexts_olb.STATISTIC_UNCATEGORIZED, (HMIActionType.click_element, [xpaths_olb.STATISTIC_COMMUTE_BUTTON]))

	graph.add_transition(contexts_olb.STATISTIC_PRIVATE, contexts_olb.STATISTIC, (HMIActionType.click_element, [xpaths_olb.STATISTIC_PRIVATE_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_PRIVATE, contexts_olb.STATISTIC_BUSINESS, (HMIActionType.click_element, [xpaths_olb.STATISTIC_BUSINESS_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_PRIVATE, contexts_olb.STATISTIC_COMMUTE, (HMIActionType.click_element, [xpaths_olb.STATISTIC_COMMUTE_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_PRIVATE, contexts_olb.STATISTIC_UNCATEGORIZED, (HMIActionType.click_element, [xpaths_olb.STATISTIC_COMMUTE_BUTTON]))

	graph.add_transition(contexts_olb.STATISTIC_COMMUTE, contexts_olb.STATISTIC, (HMIActionType.click_element, [xpaths_olb.STATISTIC_COMMUTE_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_COMMUTE, contexts_olb.STATISTIC_BUSINESS, (HMIActionType.click_element, [xpaths_olb.STATISTIC_BUSINESS_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_COMMUTE, contexts_olb.STATISTIC_PRIVATE, (HMIActionType.click_element, [xpaths_olb.STATISTIC_PRIVATE_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_COMMUTE, contexts_olb.STATISTIC_UNCATEGORIZED, (HMIActionType.click_element, [xpaths_olb.STATISTIC_COMMUTE_BUTTON]))

	graph.add_transition(contexts_olb.STATISTIC_UNCATEGORIZED, contexts_olb.STATISTIC, (HMIActionType.click_element, [xpaths_olb.STATISTIC_UNCATEGORIZED_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_UNCATEGORIZED, contexts_olb.STATISTIC_BUSINESS, (HMIActionType.click_element, [xpaths_olb.STATISTIC_BUSINESS_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_UNCATEGORIZED, contexts_olb.STATISTIC_PRIVATE, (HMIActionType.click_element, [xpaths_olb.STATISTIC_PRIVATE_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_UNCATEGORIZED, contexts_olb.STATISTIC_COMMUTE, (HMIActionType.click_element, [xpaths_olb.STATISTIC_COMMUTE_BUTTON]))

	graph.add_transition(contexts_olb.STATISTIC, contexts_olb.SETTINGS, (HMIActionType.click_element, [xpaths_olb.SETTINGS_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_BUSINESS, contexts_olb.SETTINGS, (HMIActionType.click_element, [xpaths_olb.SETTINGS_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_PRIVATE, contexts_olb.SETTINGS, (HMIActionType.click_element, [xpaths_olb.SETTINGS_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_COMMUTE, contexts_olb.SETTINGS, (HMIActionType.click_element, [xpaths_olb.SETTINGS_BUTTON]))
	graph.add_transition(contexts_olb.STATISTIC_UNCATEGORIZED, contexts_olb.SETTINGS, (HMIActionType.click_element, [xpaths_olb.SETTINGS_BUTTON]))

	graph.add_transition(contexts_olb.SETTINGS, contexts_legal.ABOUT_US, (HMIActionType.click_element, [xpaths_legal.IMPRINT_BUTTON]))
	graph.add_transition(contexts_olb.SETTINGS, contexts_legal.DATA_PROTECTION_NOTES, (HMIActionType.click_element, [xpaths_legal.DATAPRIVACY_BUTTON]))

	graph.add_transition(contexts_olb.SETTINGS, contexts_olb.SETTINGS_OPEN_SOURCE_SOFTWARE_NOTICE, (HMIActionType.click_element, [xpaths_olb.OPEN_SOURCE_SOFTWARE_NOTICE_BUTTON]))
	graph.add_transition(contexts_olb.SETTINGS_OPEN_SOURCE_SOFTWARE_NOTICE, contexts_olb.SETTINGS, (HMIActionType.click_element, [xpaths_olb.SETTINGS_BACK_BUTTON]))

	graph.add_transition(contexts_olb.SETTINGS, contexts_olb.STATISTIC, (HMIActionType.click_element, [xpaths_olb.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_olb.SETTINGS, contexts_olb.STATISTIC_BUSINESS, (HMIActionType.click_element, [xpaths_olb.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_olb.SETTINGS, contexts_olb.STATISTIC_PRIVATE, (HMIActionType.click_element, [xpaths_olb.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_olb.SETTINGS, contexts_olb.STATISTIC_COMMUTE, (HMIActionType.click_element, [xpaths_olb.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_olb.SETTINGS, contexts_olb.STATISTIC_UNCATEGORIZED, (HMIActionType.click_element, [xpaths_olb.SETTINGS_BACK_BUTTON]))

	graph.add_transition(contexts_olb.SETTINGS, contexts_olb.AUTOMATIC_PAUSE_DETECTION, (HMIActionType.click_element, [xpaths_olb.SETTINGS_INFO_BUTTON]))
	graph.add_transition(contexts_olb.AUTOMATIC_PAUSE_DETECTION, contexts_olb.SETTINGS, (HMIActionType.click_element, [xpaths_olb.SETTINGS_BACK_BUTTON]))
