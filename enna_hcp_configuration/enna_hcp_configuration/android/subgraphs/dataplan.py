# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""

# from enna_hcp_configuration.android import xpaths
from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import dataplan as contexts_dataplan, globalsearch as contexts_globalsearch, phone as contexts_phone


def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_dataplan.MAIN, contexts_phone.CONNECTIONS, (HMIActionType.click_coordinates, [485, 60]))
	graph.add_transition(contexts_dataplan.MAIN, contexts_globalsearch.MAIN, (HMIActionType.click_coordinates, [616, 60]))
