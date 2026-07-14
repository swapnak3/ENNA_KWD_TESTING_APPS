# -*- coding: utf-8 -*-
"""Module contains transitions from softwareupdate to any menu"""

from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import softwareupdate as contexts_softwareupdate
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher
from enna_hcp_configuration.android.contexts import settings as contexts_settings
from enna_hcp_configuration.android.xpaths import launcher as xpaths_launcher
from enna_hcp_configuration.android.xpaths import softwareupdate as xpaths_softwareupdate

def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_softwareupdate.MAIN, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_softwareupdate.MAIN, contexts_settings.SYSTEM, (HMIActionType.click_element, [xpaths_softwareupdate.BACK_BUTTON]))
