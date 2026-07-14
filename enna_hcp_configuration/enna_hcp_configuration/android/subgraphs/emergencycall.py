# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""

from enna_hcp_configuration.android.xpaths import launcher as xpaths_launcher
from enna_hcp_configuration.android.xpaths import aem as xpaths_aem
from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import aem as contexts_aem
from enna_hcp_configuration.android.contexts import emergencycall as contexts_emergency_call
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_emergency_call.AEM_ECALL_SETTINGS, contexts_aem.MAIN, (HMIActionType.click_element, [xpaths_aem.ECALL_TEST_MENU_BACK_BUTTON]))
	graph.add_transition(contexts_emergency_call.AEM_ECALL_SETTINGS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
