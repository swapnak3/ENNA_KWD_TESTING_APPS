# -*- coding: utf-8 -*-
"""Contexts for the user_management app."""

from enna_hcp_configuration.android.base import ContextAnalyzer, ElementByXPathDetectorExtension, AppPackageDetectorExtension
from enna_hcp_configuration.android.xpaths import user_management as xpaths_user_management
from enna_hcp_configuration.common.base import Element


# user management popups:
# POPUP_CONFIRM_USER_CHANGE = Element("POPUP_confirm_user_change", ElementByXPathDetectorExtension([xpaths_user_management.POPUP_USER_MANAGEMENT_CONFIRM_USER_CHANGE_TITLE]))
# POPUP_CONFIRM_USER_DELETION = Element("POPUP_confirm_user_deletion", ElementByXPathDetectorExtension([xpaths_user_management.POPUP_USER_MANAGEMENT_CONFIRM_USER_DELETION_TITLE]))

MY_AUDI_LOGIN = Element("my_audi_login", ElementByXPathDetectorExtension([xpaths_user_management.MY_AUDI_LOGIN_TITLE]))
CONTINUE_WITHOUT_MY_AUDI_LOGIN = Element("continue_without_login", ElementByXPathDetectorExtension([xpaths_user_management.CONTINUE_WITHOUT_MY_AUDI_LOGIN_TITLE]))

# user management screens witch can be moved to:
ALL_USERS = Element("all_users", ElementByXPathDetectorExtension([xpaths_user_management.MAIN_ALL_USERS_SELECTED_TITLE]))
YOUR_PROFILE = Element("your_profile", ElementByXPathDetectorExtension([xpaths_user_management.MAIN_YOUR_PROFILE_SELECTED_TITLE]))
PRIMARY_USER = Element("primary_user", ElementByXPathDetectorExtension([xpaths_user_management.MAIN_PRIMARY_USER_SELECTED_TITLE]))
USER_SETTINGS = Element("user_settings", ElementByXPathDetectorExtension([xpaths_user_management.MAIN_USER_SETTINGS_TITLE]))

ADD_LOCAL_USER = Element("add_local_user", ElementByXPathDetectorExtension([xpaths_user_management.ADD_LOCAL_USER_TITLE]))

KEY_USER = Element("key_user", ElementByXPathDetectorExtension([xpaths_user_management.MAIN_KEY_USER_SELECTED_TITLE]))
DELETE_USER = Element("delete_user", ElementByXPathDetectorExtension([xpaths_user_management.MAIN_USER_DELETE_USER_TITLE]))

CONTEXT = ContextAnalyzer("user_management", AppPackageDetectorExtension(["de.eso.usermanagement"]))
CONTEXT.add_elements_from_module(globals())
