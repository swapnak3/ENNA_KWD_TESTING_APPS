# -*- coding: utf-8 -*-
"""Helpers for the HMI graph."""
import copy

import enna_hcp_configuration.android.contexts.launcher


def shorten_path_by_app_list(path):
	"""Reduce a path by using the app_list shortcut.

	Due to how the analyzer and graph are setup, a context change will always go through app list. This means the app_list button can be pressed anyways.

	:param path: the current path
	:type path: (list[enna_hcp_configuration.common.base.Element], list[(enna_hcp_configuration.android.base.HMIActionType, list[str])])
	:return: the shortened path as a new tuple
	:rtype: (list[enna_hcp_configuration.common.base.Element], list[(enna_hcp_configuration.android.base.HMIActionType, list[str])])
	"""
	path = copy.deepcopy(path)

	# If app_list is not in path or it's the start or second vertex anyways, nothing to do
	if enna_hcp_configuration.android.contexts.launcher.APP_LIST not in path[0] or path[0].index(enna_hcp_configuration.android.contexts.launcher.APP_LIST) in {0, 1}:
		return path

	# If app_list is destination, we can just press it
	if enna_hcp_configuration.android.contexts.launcher.APP_LIST == path[0][-1]:
		return [path[0][0], path[0][-1]], [path[1][-1]]

	# Remove every element between start and app_list and also clean up actions
	while path[0][1] != enna_hcp_configuration.android.contexts.launcher.APP_LIST:
		path[0].pop(1)
		path[1].pop(0)
	return path
