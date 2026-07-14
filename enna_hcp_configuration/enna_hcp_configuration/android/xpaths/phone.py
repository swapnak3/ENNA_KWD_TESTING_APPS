# -*- coding: utf-8 -*-
"""Module contains xpath of launcher app."""
import enna_hcp_configuration.android.xpaths
from . import XpathString

if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.de.eso import phone
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.de.eso import phone
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.de.eso import phone
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.de.eso import phone
else:
	from enna_hcp_configuration.texts.CLU46.center.de.eso import phone

# pylint: disable=line-too-long
LIST_CONTAINER = XpathString("//*[@resource-id='de.eso.phone:id/recyclerViewList']")
MAIN_LIST = XpathString("//*[@class='androidx.recyclerview.widget.RecyclerView']")

MAIN_TITLE = XpathString(f"//*[@resource-id='de.eso.phone:id/titleTextView']{phone.top_bar_title__phone__title}")
CONNECTION_MANAGER_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.phone:string/connection_mgr__main_menu__title')]")
BLUETOOTH_SETTINGS_TITLE = XpathString("//*[contains(@content-desc,'###de.eso.phone:string/connection_mgr__bluetooth__title')]")
DEVICE_MANAGER_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.phone:string/connection_mgr__device_manager__list_item__title')]")
WIFI_SETTINGS_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.phone:string/connection_mgr__wifi__setting__title')]")
CAR2PHONE_SKELETON_TITLE = XpathString("//*[@resource-id='technology.cariad.hcp3.car2phone.audi:id/skeleton_screen_layout']")
SEARCH_DEVICES_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.phone:string/connection_mgr__bluetooth__pairing__title')]")
OPEN_SOURCE_SOFTWARE_NOTICE_TITLE = XpathString(f"//*[@resource-id='de.eso.phone:id/titleTextView']{phone.connection_mgr__open_source_disclaimer__title}")
VEHICLE_HOTSPOT_SETTINGS_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.phone:string/connection_mgr__hotspot__setting__title')]")
WIRELESS_CHARGING_SETTINGS_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.phone:string/wlc__settings__title')]")


LIST_ITEM_OPEN_DEVICE_MANAGER = XpathString("//*[contains(@content-desc, 'de.eso.phone:string/connection_mgr__main_menu__device_manager__text')]")
LIST_ITEM_OPEN_HOTSPOT_SETTINGS = XpathString("//*[contains(@content-desc, '###VehicleHotspotSetting')]")
LIST_ITEM_OPEN_WIFI_SETTINGS = XpathString("//*[contains(@content-desc, '###WiFiSetting')]")
LIST_ITEM_OPEN_BLUETOOTH_SETTINGS = XpathString("//*[contains(@content-desc, '###BluetoothSetting')]")
LIST_ITEM_OPEN_SOURCE_SOFTWARE_NOTICE = XpathString("//*[contains(@content-desc, 'de.eso.phone:string/connection_mgr__main_menu__open_source_disclaimer__text')]")
LIST_ITEM_OPEN_CAR2PHONE = XpathString("//*[contains(@content-desc, 'de.eso.phone:string/connection_mgr__main_menu__car_2_phone__text')]")
LIST_ITEM_OPEN_DATAPLAN_MENU = XpathString("//*[contains(@content-desc, 'DataPackage')]")
LIST_ITEM_OPEN_WIRELESS_CHARGING_SETTINGS = XpathString("//*[contains(@content-desc, 'de.eso.phone:string/connection_mgr__main_menu__wireless_charging__text')]")

SUB_MENU_ICON = XpathString("//*[@resource-id='de.eso.phone:id/listItemButton_0']")
SUB_MENU_LIST_ITEM_OPEN_BLUETOOTH_SETTINGS = XpathString(f"{LIST_ITEM_OPEN_BLUETOOTH_SETTINGS.get()}/.{SUB_MENU_ICON.get()}")
SUB_MENU_LIST_ITEM_OPEN_WIFI_SETTINGS = XpathString(f"{LIST_ITEM_OPEN_WIFI_SETTINGS.get()}/.{SUB_MENU_ICON.get()}")
SUB_MENU_LIST_ITEM_OPEN_HOTSPOT_SETTINGS = XpathString(f"{LIST_ITEM_OPEN_HOTSPOT_SETTINGS.get()}/.{SUB_MENU_ICON.get()}")

TEXT_NO_DEVICE_CONNECTED_SCREEN = XpathString("//*[@resource-id='de.eso.phone:id/device_list_empty_list_text']")
TEXT_SEARCH_DEVICES_NO_DEVICE_FOUND = XpathString("//*[contains(@content-desc, 'de.eso.phone:string/connection_mgr__bluetooth__pairing__no_device_found__text')]")

ICON_ADD_NEW_DEVICE = XpathString("//*[contains(@content-desc, 'de.eso.phone:drawable/device_list_new_device_icon')]")

BUTTON_PLEASE_CONNECT_PHONE = XpathString("//*[contains(@content-desc, 'de.eso.phone:string/phone_not_attached__connect_phone__button_text')]")
BUTTON_BACK_BUTTON = XpathString("//*[contains(@content-desc, 'backButton')]")

POPUP_CONNECTION_BLUETOOTH_TITLE = XpathString("//*[contains(@content-desc, 'de.eso.phone:string/connection_mgr__pregranted_permissions__popup_title__text')]")

POPUP_HOTSPOT_DEACTIVATION_IGNORE_TITLE = XpathString("//*[@resource-id='android:id/button1'][contains(@text, 'Ignor')]")
POPUP_ACCEPT_PHONE_PERMISSIONS_TITLE = XpathString("//*[@resource-id='de.eso.phone:id/popupPositiveButton']")
POPUP_ACTIVATE_BLUETOOTH_TITLE = XpathString("//*[contains(@content-desc, 'technology.cariad.hcp3.car2phone.audi:string/textAndButton_info_bluetooth_deactivated')]")
POPUP_ACCEPT_BLUETOOTH_ACTIVATION_BUTTON = XpathString("//*[@resource-id='android:id/button1']")

WIFI_SWITCH_BUTTON = XpathString("//*[contains(@content-desc, '###de.eso.phone:string/connection_mgr__wifi__setting__on_off__list_item__text')]/../../*[@resource-id='de.eso.phone:id/switchControl']")
BLUETOOTH_SWITCH_BUTTON = XpathString("//*[@resource-id='de.eso.phone:id/listItemGrid2'][.//*[contains(@content-desc, 'de.eso.phone:string/connection_mgr__bluetooth__setting__on_off__text')]]//*[@resource-id='de.eso.phone:id/switchControl']")

SETTINGS_CONNECTION_BLUETOOTH_TITLE = XpathString(f"//*[@content-desc='de.eso.phone:id/car_ui_toolbar_title']{phone.connection_mgr__bluetooth__setting__on_off__text} or //*[contains(@content-desc, 'de.eso.phone:string/connection_mgr__bluetooth__title')]")

TEXT_UNBLOCKING_BY_PASSENGER = XpathString("//*[contains(@content-desc, '###de.eso.phone:string/texttool_globals_toast___connection_mgr__function_off_while_driving__text_utp')]")
BUTTON_CONFIRM_I_AM_PASSENGER = XpathString("//*[contains(@content-desc, '###de.eso.phone:string/hmisdk__i_am_the_passenger_button_text')]")
