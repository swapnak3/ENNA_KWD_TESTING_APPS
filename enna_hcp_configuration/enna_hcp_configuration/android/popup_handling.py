# -*- coding: utf-8 -*-
"""Contains the default action definitions to handle specific popups."""

from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import permissioncontroller as contexts_permissioncontroller
from enna_hcp_configuration.android.xpaths import permissioncontroller as xpaths_permissioncontroller

POPUP_ACTIONS = {
	contexts_permissioncontroller.POPUP_NOTIFICATIONS_PERMISSION_ERLIN_LOCATION.name: (HMIActionType.click_element, [xpaths_permissioncontroller.POPUP_NOTIFICATIONS_DIALOG_ERLIN_LOCATION_BUTTON_ALLOW]),
	contexts_permissioncontroller.POPUP_NOTIFICATIONS_PERMISSION_ERLIN_SOUND.name: (HMIActionType.click_element, [xpaths_permissioncontroller.POPUP_NOTIFICATIONS_DIALOG_ERLIN_SOUND_BUTTON_USE]),
	contexts_permissioncontroller.POPUP_NOTIFICATIONS_PERMISSION_ERLIN_NOTIFICATIONS.name: (HMIActionType.click_element, [xpaths_permissioncontroller.POPUP_NOTIFICATIONS_DIALOG_ERLIN_NOTIFICATIONS_BUTTON_ALLOW]),
}
