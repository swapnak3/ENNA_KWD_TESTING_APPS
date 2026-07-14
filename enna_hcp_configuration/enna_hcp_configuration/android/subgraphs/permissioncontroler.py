# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""

from enna_hcp_configuration.android.xpaths import permissioncontroller as xpaths_permissioncontroller
from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import permissioncontroller as contexts_permissioncontroller, settings as contexts_settings


def initialize(graph):  # pylint: disable=too-many-statements # noqa
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_permissioncontroller.APP_PERMISSION, contexts_settings.APPS, (HMIActionType.click_element, [xpaths_permissioncontroller.BACK_BUTTON]))
	graph.add_transition(contexts_permissioncontroller.APP_PERMISSION, contexts_permissioncontroller.APP_PERMISSION_DATA_AND_MEDIA, (HMIActionType.click_element, [xpaths_permissioncontroller.FILES_AND_MEDIA_BUTTON]))
	graph.add_transition(contexts_permissioncontroller.APP_PERMISSION_DATA_AND_MEDIA, contexts_permissioncontroller.APP_PERMISSION, (HMIActionType.click_element, [xpaths_permissioncontroller.BACK_BUTTON]))
	graph.add_transition(contexts_permissioncontroller.APP_PERMISSION_DATA_AND_MEDIA, contexts_permissioncontroller.APP_PERMISSION_MEDIACORESERVICE,
			(HMIActionType.click_element_in_list, [xpaths_permissioncontroller.MEDIACORESERVICE_BUTTON, xpaths_permissioncontroller.LIST_CONTAINER]))
	graph.add_transition(contexts_permissioncontroller.APP_PERMISSION_MEDIACORESERVICE, contexts_permissioncontroller.APP_PERMISSION_DATA_AND_MEDIA, (HMIActionType.click_element, [xpaths_permissioncontroller.BACK_BUTTON]))
	graph.add_transition(contexts_permissioncontroller.PRIVACY_APP_PERMISSIONS, contexts_settings.PRIVACY, (HMIActionType.click_element, [xpaths_permissioncontroller.BACK_BUTTON]))
