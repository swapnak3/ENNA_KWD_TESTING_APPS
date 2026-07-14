# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""

from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import aaam as contexts_aaam
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher
from enna_hcp_configuration.android.contexts import legal as contexts_legal
from enna_hcp_configuration.android.contexts import obb as contexts_obb
from enna_hcp_configuration.android.contexts import olb as contexts_olb
from enna_hcp_configuration.android.contexts import privacy as contexts_privacy
from enna_hcp_configuration.android.xpaths import launcher as xpaths_launcher
from enna_hcp_configuration.android.xpaths import legal as xpaths_legal

def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_legal.OVERVIEW, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_legal.QR_CODE, contexts_legal.OVERVIEW, (HMIActionType.click_element, [xpaths_legal.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_legal.QR_CODE, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_legal.SKELETON, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_legal.PRIVACY_MODE_INFO, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))

	graph.add_transition(contexts_legal.PRIVACY_MODE_INFO, contexts_privacy.PRIVACY_SETTINGS, (HMIActionType.click_element, [xpaths_legal.PRIVACY_MODE_INFO_SETTINGS_BUTTON]))
	graph.add_transition(contexts_legal.PRIVACY_MODE_INFO, contexts_legal.OVERVIEW, (HMIActionType.click_element, [xpaths_legal.PRIVACY_MODE_INFO_OK_BUTTON]))
	# graph.add_transition(contexts_legal.DATA_PRIVACY, contexts_legal.OVERVIEW, (HMIActionType.click_element, [xpaths_legal.TEXT_BACK_BUTTON]))
	graph.add_transition(contexts_legal.ABOUT_US, contexts_legal.OVERVIEW, (HMIActionType.click_element, [xpaths_legal.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_legal.DATA_PROTECTION_NOTES, contexts_legal.OVERVIEW, (HMIActionType.click_element, [xpaths_legal.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_legal.SETTINGS, contexts_legal.OVERVIEW, (HMIActionType.click_element, [xpaths_legal.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_legal.SETTINGS_OPEN_SOURCE_SOFTWARE_NOTICE, contexts_legal.SETTINGS, (HMIActionType.click_element, [xpaths_legal.SETTINGS_BACK_BUTTON]))

	graph.add_transition(contexts_legal.ABOUT_US, contexts_aaam.SETTINGS, (HMIActionType.click_element, [xpaths_legal.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_legal.ABOUT_US, contexts_obb.SETTINGS, (HMIActionType.click_element, [xpaths_legal.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_legal.ABOUT_US, contexts_olb.SETTINGS, (HMIActionType.click_element, [xpaths_legal.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_legal.DATA_PROTECTION_NOTES, contexts_aaam.SETTINGS, (HMIActionType.click_element, [xpaths_legal.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_legal.DATA_PROTECTION_NOTES, contexts_obb.SETTINGS, (HMIActionType.click_element, [xpaths_legal.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_legal.DATA_PROTECTION_NOTES, contexts_olb.SETTINGS, (HMIActionType.click_element, [xpaths_legal.SETTINGS_BACK_BUTTON]))

	graph.add_transition(contexts_legal.OVERVIEW, contexts_legal.ABOUT_US, (HMIActionType.click_element, [xpaths_legal.IMPRINT_BUTTON]))
	graph.add_transition(contexts_legal.OVERVIEW, contexts_legal.DATA_PROTECTION_NOTES, (HMIActionType.click_element, [xpaths_legal.DATA_PROTECTION_NOTES_BUTTON]))
	graph.add_transition(contexts_legal.OVERVIEW, contexts_legal.SETTINGS, (HMIActionType.click_element, [xpaths_legal.SETTINGS_BUTTON]))

	graph.add_transition(contexts_legal.SETTINGS, contexts_legal.SETTINGS_OPEN_SOURCE_SOFTWARE_NOTICE, (HMIActionType.click_element, [xpaths_legal.OPEN_SOURCE_SOFTWARE_NOTICE_BUTTON]))
	graph.add_transition(contexts_legal.SETTINGS_OPEN_SOURCE_SOFTWARE_NOTICE, contexts_legal.SETTINGS, (HMIActionType.click_element, [xpaths_legal.SETTINGS_BACK_BUTTON]))
