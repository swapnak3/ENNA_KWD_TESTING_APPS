# -*- coding: utf-8 -*-
"""Module contains xpath of user_management app."""

import enna_hcp_configuration.android.xpaths
from . import XpathString


if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.de.eso import usermanagement
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.de.eso import usermanagement
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.de.eso import usermanagement
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.de.eso import usermanagement
else:
	from enna_hcp_configuration.texts.CLU46.center.de.eso import usermanagement


POPUP_USER_CHANGE_CONFIRM_CANCEL_BUTTON = XpathString("//*[contains(@resource-id, 'android:id/button2')]")

MY_AUDI_LOGIN_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.usermanagement:string/add_user_title_online_user_login')]")
CONTINUE_WITHOUT_MY_AUDI_LOGIN_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.usermanagement:string/add_user_title_offline_user_info')]")

MAIN_ALL_USERS_SELECTED_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{usermanagement.app_tabbar_title_all_users}[@selected='true']")
MAIN_YOUR_PROFILE_SELECTED_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{usermanagement.app_tabbar_tab_profile_settings}[@selected='true']")
MAIN_PRIMARY_USER_SELECTED_TITLE = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{usermanagement.app_tabbar_tab_primary_user}[@selected='true']")
MAIN_USER_SETTINGS_TITLE = XpathString("//*[@content-desc='###de.eso.usermanagement:string/settings_title']")
ADD_LOCAL_USER_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.usermanagement:string/add_user_title_name_offline_user')]")
MAIN_KEY_USER_SELECTED_TITLE = XpathString("//*[contains(@content-desc, 'R.string.app_tabbar_title_primary_user')][@selected='true']")
MAIN_USER_DELETE_USER_TITLE = XpathString("//*[contains(@content-desc, 'texttool_globals_dialog_message___primary_user_reset_warning_dialog_with_logbook')]")

MAIN_KEY_USER_BUTTON = XpathString("//*[contains(@content-desc, 'R.string.app_tabbar_title_primary_user')]")
MAIN_YOUR_PROFILE_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{usermanagement.app_tabbar_tab_profile_settings}")
MAIN_PRIMARY_USER_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{usermanagement.app_tabbar_tab_primary_user}")
MAIN_ALL_USERS_ADD_NEW_USER_BUTTON = XpathString("//*[contains(@content-desc, 'de.eso.usermanagement:drawable/add_element_icon')]")
MAIN_USER_SETTINGS_BACK_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][contains(@content-desc, 'Back')]")
MAIN_USER_SETTINGS_BUTTON = XpathString("//*[@content-desc='topbarSettingsAction']")
MAIN_ALL_USERS_BUTTON = XpathString(f"//*[@class='android.widget.HorizontalScrollView']/.//*{usermanagement.app_tabbar_title_all_users}")
MAIN_USER_DELETE_USER_BUTTON = XpathString("//*[contains(@content-desc, 'R.string.primary_user_action_remove_pu')]")

USER_BUTTON = XpathString("//*[@resource-id='com.android.systemui:id/status_bar_user_button']")
SELECT_USER_BUTTON = XpathString("//*[@resource-id='de.eso.usermanagement:id/listItemContactTileItemText']")
SELECT_GUEST_USER_BUTTON = XpathString(f"{SELECT_USER_BUTTON.get()}{usermanagement.user_profile_role_default}")
CHANGE_USER_BUTTON = XpathString("//*[contains(@content-desc,'switch_user') and contains(@content-desc,'warning')]/../../../../../..//*[@class='android.widget.Button'][@index=1]")
CANCEL_CHANGE_USER_BUTTON = XpathString("//*[contains(@content-desc,'switch_user') and contains(@content-desc,'warning')]/../../../../../..//*[@class='android.widget.Button'][@index=0]")
POPUP_CLOSE_BUTTON = XpathString("//*[contains(@resource-id,'popupCloseButton')]")
