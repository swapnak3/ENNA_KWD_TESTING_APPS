# -*- coding: utf-8 -*-
"""Module contains transitions from fod (Functions on demand - Overview of functions) to any menu"""

from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import fod as contexts_fod
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher
from enna_hcp_configuration.android.contexts import settings as contexts_settings
from enna_hcp_configuration.android.xpaths import fod as xpaths_fod
from enna_hcp_configuration.android.xpaths import launcher as xpaths_launcher


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_fod.OVERVIEW_OF_FUNCTIONS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_fod.OVERVIEW_OF_FUNCTIONS, contexts_settings.SYSTEM, (HMIActionType.click_element, [xpaths_fod.BACK_BUTTON]))
