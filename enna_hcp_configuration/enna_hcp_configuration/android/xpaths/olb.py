# -*- coding: utf-8 -*-
"""Module contains xpath of olb app."""
from . import XpathString

# pylint: disable=line-too-long

# names unchanged
POPUP_PERMISSION_OLB_LOCATION_ALLOW_W_USING_BUTTON = XpathString("//*[@resource-id='com.android.permissioncontroller:id/car_ui_list_item_title'][@text='Bei Nutzung der App' or @text='While using the app']")
POPUP_PERMISSION_HINT_OLB_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.olb.audi:id/titleTextViewRef'][contains(@text, 'Online-Fahrtenbuch: Hinweis')]")
POPUP_PERMISSION_HINT_OLB_TO_SETTINGS_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.olb.audi:id/operationPanelItemTextView'][contains(@text, 'Zu den Einstellungen')]")

# was POPUP_OLB_*
POPUP_PERMISSION_LOCATION_TITLE = XpathString("//*[@resource-id='com.android.permissioncontroller:id/car_ui_alert_title'][contains(@text, 'Online-Fahrtenbuch') and contains(@text, 'erlauben, den Gerätestandort abzurufen?')] or //*[@resource-id='com.android.permissioncontroller:id/car_ui_alert_title'][contains(@text, 'Allow Online logbook') and contains(@text, 'to access this device') and contains(@text, 'location')]")
POPUP_PERMISSION_HINT_TO_SETTINGS_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.olb.audi:id/titleTextViewRef'][contains(@text, 'Online-Fahrtenbuch: Hinweis')] and //*[contains(@text, 'Zu den Einstellungen')]")
POPUP_PERMISSION_HINT_TO_SETTINGS_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.olb.audi:id/operationPanelItemTextView'][contains(@text, 'Zu den Einstellungen')]")

# was OLB_*
LOADING_TITLE = XpathString("//*[@class='android.widget.ProgressBar'][@package='com.valtech_mobility.olb.audi']")
SEVEN_DAY_TITLE = XpathString("//*[contains(@resource-id, 'com.valtech_mobility.olb.audi:id/titleTextView')][@package='com.valtech_mobility.olb.audi'][contains(@text, 'Statistics') or contains(@text, 'Statistik')] and //*[contains(@content-desc, 'e3a8_logbook_template')]")
SEVEN_DAY_SETTINGS_TITLE = XpathString("//*[@class='android.widget.LinearLayout'][@package='com.valtech_mobility.olb.audi'][contains(@content-desc, '7days')][@selected='true']")
STATISTIC_TITLE = XpathString("//*[@index='0'][@class='android.widget.LinearLayout'][@package='com.valtech_mobility.olb.audi'][contains(@content-desc, 'Statistik') or contains(@content-desc, 'Statistics')]")
STATISTIC_UNSELECTED_ICON = XpathString("//*[contains(@content-desc, 'e4d5_statistic_all_categories')]")
STATISTIC_UNSELECTED_TITLE = XpathString("//*[@index='0'][@class='android.widget.LinearLayout'][@package='com.valtech_mobility.olb.audi'][contains(@content-desc, 'Statistik') or contains(@content-desc, 'Statistics')] and //*[contains(@content-desc, 'e4d5_statistic_all_categories')]")
STATISTIC_BUSINESS_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.olb.audi:id/container_business_bars']/*[@resource-id='com.valtech_mobility.olb.audi:id/root_business']")
STATISTIC_BUSINESS_ICON = XpathString("//*[contains(@content-desc, 'e800_navigation_business')]")
STATISTIC_BUSINESS_TITLE = XpathString("//*[@index='0'][@class='android.widget.LinearLayout'][@package='com.valtech_mobility.olb.audi'][contains(@content-desc, 'Statistik') or contains(@content-desc, 'Statistics')] and //*[contains(@content-desc, 'e800_navigation_business')]")
STATISTIC_PRIVATE_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.olb.audi:id/container_private_bars']/*[@resource-id='com.valtech_mobility.olb.audi:id/root_private']")
STATISTIC_PRIVATE_ICON = XpathString("//*[contains(@content-desc, 'e0c8_navigation_home')]")
STATISTIC_PRIVATE_TITLE = XpathString("//*[@index='0'][@class='android.widget.LinearLayout'][@package='com.valtech_mobility.olb.audi'][contains(@content-desc, 'Statistik') or contains(@content-desc, 'Statistics')] and //*[contains(@content-desc, 'e0c8_navigation_home')]")
STATISTIC_COMMUTE_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.olb.audi:id/container_commute_bars']/*[@resource-id='com.valtech_mobility.olb.audi:id/root_commute']")
STATISTIC_COMMUTE_ICON = XpathString("//*[contains(@content-desc, 'e3b5_olb_route_to_workplace')]")
STATISTIC_COMMUTE_TITLE = XpathString("//*[@index='0'][@class='android.widget.LinearLayout'][@package='com.valtech_mobility.olb.audi'][contains(@content-desc, 'Statistik') or contains(@content-desc, 'Statistics')] and //*[contains(@content-desc, 'e3b5_olb_route_to_workplace')]")
STATISTIC_UNCATEGORIZED_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.olb.audi:id/container_uncategorized_bars']/*[@resource-id='com.valtech_mobility.olb.audi:id/root_uncategorized']")
STATISTIC_UNCATEGORIZED_ICON = XpathString("//*[contains(@content-desc, 'e4d4_statistic_no_category')]")
STATISTIC_UNCATEGORIZED_TITLE = XpathString("//*[@index='0'][@class='android.widget.LinearLayout'][@package='com.valtech_mobility.olb.audi'][contains(@content-desc, 'Statistik') or contains(@content-desc, 'Statistics')] and //*[contains(@content-desc, 'e4d4_statistic_no_category')]")
SETTINGS_TITLE = XpathString("//*[contains(@resource-id, 'com.valtech_mobility.olb.audi:id/titleTextView')][contains(@text, 'Einstellungen') or contains(@text, 'Settings')]")
AUTOMATIC_PAUSE_DETECTION_TITLE = XpathString("//*[contains(@resource-id, 'com.valtech_mobility.olb.audi:id/titleTextView')][@package='com.valtech_mobility.olb.audi'][contains(@text, 'Information zur automatischen Pausenerkennung')]")
OPEN_SOURCE_SOFTWARE_NOTICE_TITLE = XpathString("//*[@index='0'][contains(@text, 'Open Source Software Notice')][contains(@resource-id, 'com.valtech_mobility.olb.audi:id/titleTextView')] and //*[@resource-id='com.valtech_mobility.olb.audi:id/legal_osd_screen_container_blocking']")  # pylint: disable=line-too-long # noqa
OPEN_SOURCE_SOFTWARE_NOTICE_BUTTON = XpathString("//*[contains(@text, 'Open Source Software Notice')]")
LOADING_ERROR_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.olb.audi:id/error_text_and_buttons']//*[@resource-id='com.valtech_mobility.olb.audi:id/textView1'][contains(@text, 'konnte nicht geladen werden') or contains(@text, 'The logbook could not be loaded')]")  # pylint: disable=line-too-long # noqa
GENERIC_ERROR_TITLE = XpathString("//*[@content-desc='com.valtech_mobility.olb.audi:string/logbook_error_screen__confirm_button__label']")
PRIVACY_ERROR_TITLE = XpathString("//*[contains(@content-desc, 'Privatsphäre-Einstellungen') or contains(@content-desc, 'OperationPanelItem-Datenschutzeinstellungen') or contains(@content-desc, 'OperationPanelItem-Privacy settings')]")
PRIMARYUSER_ERROR_TITLE = XpathString("//*[@package='com.valtech_mobility.olb.audi'][@resource-id='com.valtech_mobility.olb.audi:id/textView1'][contains(@text, 'Hauptnutzer')]")
LICENSE_ERROR_TITLE = XpathString("//*[@content-desc='*OK'][@resource-id='com.valtech_mobility.olb.audi:id/operationPanelItemTextView'][contains(@text, 'Lizenz')]")
SEVEN_DAY_SETTINGS_BUTTON = XpathString("//*[@class='android.widget.LinearLayout'][@package='com.valtech_mobility.olb.audi'][contains(@content-desc, 'Fahrtenliste')]")
SEVEN_DAY_SETTINGS_BACK_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][@package='com.valtech_mobility.olb.audi'][contains(@content-desc, 'Back')]")
STATISTIC_BUTTON = XpathString("//*[@class='android.widget.LinearLayout'][@package='com.valtech_mobility.olb.audi'][contains(@content-desc, 'Statistik')]")
SETTINGS_BUTTON = XpathString("//*[@class='android.widget.FrameLayout'][@package='com.valtech_mobility.olb.audi'][@resource-id='com.valtech_mobility.olb.audi:id/menuActionsBackground']")
SETTINGS_INFO_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][@package='com.valtech_mobility.olb.audi'][@resource-id='com.valtech_mobility.olb.audi:id/listItemButton_0']")
SETTINGS_BACK_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][@package='com.valtech_mobility.olb.audi'][contains(@content-desc, 'Back')]")
PERMISSION_TITLE = XpathString("//*[contains(@text, 'Online-Fahrtenbuch')] and //*[contains(@text, 'Online-Fahrtenbuch')] or //*[contains(@text, 'Online logbook')] or //*[contains(@text, 'Location permission')] and //*[contains(@text, 'Online logbook')] or //*[contains(@text, 'Allow Online logbook to')]")

# was SETTINGS_OLB_*
SETTINGS_PERMISSION_RECYCLERVIEW = XpathString("//*[@resource-id='com.android.permissioncontroller:id/recycler_view'][@content-desc='com.android.car.ui.utils.ROTARY_CONTAINER']")

# was SETTINGS_POPUP_OLB_*
SETTINGS_POPUP_PERMISSION_ALWAYS_TITLE = XpathString("//*[contains(@text, 'Online-Fahrtenbuch')] and //*[contains(@text, 'Immer zulassen')]/../../..//*[@resource-id='com.android.permissioncontroller:id/radio_button'][@checked='true'] or //*[contains(@text, 'Online logbook')]//*[contains(@text, 'Allow all the time')]/../../..//*[@resource-id='com.android.permissioncontroller:id/radio_button'][@checked='true']")
SETTINGS_POPUP_PERMISSION_ALWAYS_BUTTON = XpathString("//*[@resource-id='android:id/title'][contains(@text, 'Immer zulassen') or contains(@text, 'Allow all the time')]")
SETTINGS_POPUP_PERMISSION_BACK_BUTTON = XpathString("//*[@class='android.widget.FrameLayout'][@package='com.android.permissioncontroller'][contains(@content-desc, 'Zurück') or contains(@content-desc, 'Back')]")
SETTINGS_POPUP_PERMISSION_USINGAPP_TITLE = XpathString("//*[contains(@text, 'Online-Fahrtenbuch')] and //*[contains(@text, 'Zugriff nur während der Nutzung der App zulassen')]/../../..//*[@resource-id='com.android.permissioncontroller:id/radio_button'][@checked='true'] or //*[contains(@text, 'Online logbook')] and //*[contains(@text, 'Allow only while using the app')]/../../..//*[@resource-id='com.android.permissioncontroller:id/radio_button'][@checked='true']")
SETTINGS_POPUP_PERMISSION_USINGAPP_BUTTON = XpathString("//*[@resource-id='android:id/title'][contains(@text, 'Zugriff nur während der Nutzung der App zulassen') or contains(@text, 'Allow only while using the app')]")
SETTINGS_POPUP_PERMISSION_NEVER_TITLE = XpathString("//*[contains(@text, 'Online-Fahrtenbuch')] and //*[contains(@text, 'Nicht zulassen')]/../../..//*[@resource-id='com.android.permissioncontroller:id/radio_button'][@checked='true'] or //*[contains(@text, 'Online logbook')]//*[contains(@text, \"Don't allow\")]/../../..//*[@resource-id='com.android.permissioncontroller:id/radio_button'][@checked='true']")
SETTINGS_POPUP_PERMISSION_NEVER_BUTTON = XpathString("//*[@resource-id='android:id/title'][contains(@text, 'Nicht zulassen') or contains(@text, \"Don't allow\")]")
