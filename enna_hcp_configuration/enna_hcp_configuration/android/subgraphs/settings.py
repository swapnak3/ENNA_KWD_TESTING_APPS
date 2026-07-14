# -*- coding: utf-8 -*-
"""Module contains transitions from settings to any menu"""

from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import assistant as contexts_assistant
from enna_hcp_configuration.android.contexts import car as contexts_car
from enna_hcp_configuration.android.contexts import fod as contexts_fod
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher
from enna_hcp_configuration.android.contexts import phone as contexts_phone
from enna_hcp_configuration.android.contexts import r2f as contexts_r2f
from enna_hcp_configuration.android.contexts import settings as contexts_settings
from enna_hcp_configuration.android.contexts import softwareupdate as contexts_softwareupdate
from enna_hcp_configuration.android.contexts import sound as contexts_sound
from enna_hcp_configuration.android.contexts import privacy as contexts_privacy
from enna_hcp_configuration.android.xpaths import launcher as xpaths_launcher
from enna_hcp_configuration.android.xpaths import settings as xpaths_settings

# pylint: disable=line-too-long
def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_settings.MAIN, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	# from main settings
	graph.add_transition(contexts_settings.MAIN, contexts_settings.SYSTEM, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SYSTEM, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.MAIN, contexts_phone.CONNECTIONS, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_CONNECTIONS, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.MAIN, contexts_sound.PRESETS_CONCERTS, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SOUND, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.MAIN, contexts_car.DISPLAY, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_DISPLAY, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.MAIN, contexts_car.AUDI_DRIVE_SELECT, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_VEHICLE_SETTINGS, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.MAIN, contexts_assistant.GENERAL, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_AUDI_ASSISTANT, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.MAIN, contexts_settings.NOTIFICATIONS, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_NOTIFICATIONS, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.MAIN, contexts_settings.PRIVACY, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_PRIVACY, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.MAIN, contexts_settings.LINKED_APP_ACCOUNTS, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_LINKED_APP_ACCOUNTS, xpaths_settings.LIST_CONTAINER]))
	# graph.add_transition(contexts_settings.MAIN, contexts_usermanagement.CONFIRM_CURRENT_PIN_PROTECTION, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SECURITY, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.MAIN, contexts_fod.OVERVIEW_OF_FUNCTIONS, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_FUNCTIONS_ON_DEMAND, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.MAIN, contexts_settings.APPS, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_APPS, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.MAIN, contexts_settings.STORAGE, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_STORAGE, xpaths_settings.LIST_CONTAINER]))
	# graph.add_transition(contexts_settings.MAIN, contexts_audi_assistant.APP_FOR_DIGITAL_ASSISTANT, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_APP_FOR_DIGITAL_ASSISTANT, xpaths_settings.LIST_CONTAINER]))

	graph.add_transition(contexts_settings.SYSTEM, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.NOTIFICATIONS, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.PRIVACY, contexts_privacy.PRIVACY_SETTINGS, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_OEM_PRIVACY_SETTINGS, xpaths_settings.PRIVACY_LIST_CONTAINER]))
	graph.add_transition(contexts_settings.PRIVACY, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.LINKED_APP_ACCOUNTS, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.APPS, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.APPS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_settings.STORAGE, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))

	graph.add_transition(contexts_settings.APPS, contexts_settings.APPS_APP_INFO, (HMIActionType.click_element, [xpaths_settings.APPS_APP_INFO_ENTRY]))
	graph.add_transition(contexts_settings.APPS_APP_INFO, contexts_settings.APPS, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.APPS_APP_INFO, contexts_settings.APPS_APP_INFO_VIEWALL, (HMIActionType.click_element, [xpaths_settings.APPS_APP_HIDE_SYSTEM_APPS_TOGGLE]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL, contexts_settings.APPS_APP_INFO, (HMIActionType.click_element, [xpaths_settings.APPS_APP_HIDE_SYSTEM_APPS_TOGGLE]))

	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL, contexts_settings.APPS_APP_INFO_VIEWALL_AUDI_ASSISTANT, (HMIActionType.click_element_in_list, [xpaths_settings.APPS_APP_INFO_VIEWALL_AUDI_ASSISTANT_LIST_ITEM, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL, contexts_settings.APPS_APP_INFO_VIEWALL_CAR, (HMIActionType.click_element_in_list, [xpaths_settings.APPS_APP_INFO_VIEWALL_CAR_LIST_ITEM, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL, contexts_settings.APPS_APP_INFO_VIEWALL_CAR2PHONE, (HMIActionType.click_element_in_list, [xpaths_settings.APPS_APP_INFO_VIEWALL_CAR2PHONE_LIST_ITEM, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL, contexts_settings.APPS_APP_INFO_VIEWALL_EXPERIENCES, (HMIActionType.click_element_in_list, [xpaths_settings.APPS_APP_INFO_VIEWALL_EXPERIENCES_LIST_ITEM, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL, contexts_settings.APPS_APP_INFO_VIEWALL_LEGAL, (HMIActionType.click_element_in_list, [xpaths_settings.APPS_APP_INFO_VIEWALL_LEGAL_LIST_ITEM, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL, contexts_settings.APPS_APP_INFO_VIEWALL_NAVIGATION, (HMIActionType.click_element_in_list, [xpaths_settings.APPS_APP_INFO_VIEWALL_NAVIGATION_LIST_ITEM, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL, contexts_settings.APPS_APP_INFO_VIEWALL_OBB, (HMIActionType.click_element_in_list, [xpaths_settings.APPS_APP_INFO_VIEWALL_OBB_LIST_ITEM, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL, contexts_settings.APPS_APP_INFO_VIEWALL_PRIVACY_SETTINGS, (HMIActionType.click_element_in_list, [xpaths_settings.APPS_APP_INFO_VIEWALL_OEM_PRIVACY_SETTINGS_LIST_ITEM, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL, contexts_settings.APPS_APP_INFO_VIEWALL_TLI, (HMIActionType.click_element_in_list, [xpaths_settings.APPS_APP_INFO_VIEWALL_TLI_LIST_ITEM, xpaths_settings.LIST_CONTAINER]))
	# graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL, contexts_settings.APPS_APP_INFO_VIEWALL_STORAGE, (HMIActionType.click_element_in_list, [xpaths_settings.APPS_APP_INFO_VIEWALL_STORAGE_LIST_ITEM, xpaths_settings.LIST_CONTAINER]))
	# graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL, contexts_settings.APPS_APP_INFO_VIEWALL_STORAGE_MUSIC_AND_AUDIO, (HMIActionType.click_element_in_list, [xpaths_settings.APPS_APP_INFO_VIEWALL_STORAGE_LIST_ITEM, xpaths_settings.LIST_CONTAINER]))
	# graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL, contexts_settings.APPS_APP_INFO_VIEWALL_STORAGE_OTHER_APPS, (HMIActionType.click_element_in_list, [xpaths_settings.APPS_APP_INFO_VIEWALL_STORAGE_LIST_ITEM, xpaths_settings.LIST_CONTAINER]))

	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL_AUDI_ASSISTANT, contexts_settings.APPS_APP_INFO_VIEWALL, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL_CAR, contexts_settings.APPS_APP_INFO_VIEWALL, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL_CAR2PHONE, contexts_settings.APPS_APP_INFO_VIEWALL, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL_EXPERIENCES, contexts_settings.APPS_APP_INFO_VIEWALL, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL_LEGAL, contexts_settings.APPS_APP_INFO_VIEWALL, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL_NAVIGATION, contexts_settings.APPS_APP_INFO_VIEWALL, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL_OBB, contexts_settings.APPS_APP_INFO_VIEWALL, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL_PRIVACY_SETTINGS, contexts_settings.APPS_APP_INFO_VIEWALL, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL_TLI, contexts_settings.APPS_APP_INFO_VIEWALL, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	# graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL_STORAGE, contexts_settings.APPS_APP_INFO_VIEWALL, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	# graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL_STORAGE_MUSIC_AND_AUDIO, contexts_settings.APPS_APP_INFO_VIEWALL, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	# graph.add_transition(contexts_settings.APPS_APP_INFO_VIEWALL_STORAGE_OTHER_APPS, contexts_settings.APPS_APP_INFO_VIEWALL, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))

	graph.add_transition(contexts_settings.SYSTEM, contexts_settings.SYSTEM_LANGUAGESINPUT_INPUT, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SYSTEM_LANGUAGESINPUT, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.SYSTEM, contexts_settings.SYSTEM_LOCATION, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SYSTEM_LOCATION, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.SYSTEM, contexts_car.SETTINGS_SYSTEM_DATE_AND_TIME, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SYSTEM_DATE_AND_TIME, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.SYSTEM, contexts_car.SETTINGS_SYSTEM_UNITS, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SYSTEM_UNITS, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.SYSTEM, contexts_softwareupdate.MAIN, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SYSTEM_SOFTWARE_UPDATE, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.SYSTEM, contexts_r2f.RESTORE_FACTORY_SETTINGS, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SYSTEM_RESTORE_FACTORY_SETTINGS, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.SYSTEM, contexts_settings.SYSTEM_ABOUT, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SYSTEM_ABOUT, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.SYSTEM, contexts_settings.SYSTEM_OPEN_SOURCE_SOFTWARE_NOTICE, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SYSTEM_OPEN_SOURCE_SOFTWARE_NOTICE, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.SYSTEM, contexts_settings.SYSTEM_LEGAL_INFORMATION, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SYSTEM_LEGAL_INFORMATION, xpaths_settings.LIST_CONTAINER]))
	# graph.add_transition(contexts_settings.SYSTEM, contexts_settings.SYSTEM_LOCAL_SYSTEM_UPDATE, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SYSTEM_LOCAL_SYSTEM_UPDATE, xpaths_settings.LIST_CONTAINER]))
	# graph.add_transition(contexts_settings.SYSTEM, contexts_android_embedded_projection.ANDROID_AUTO, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SYSTEM_ANDROID_AUTO, xpaths_settings.LIST_CONTAINER]))

	graph.add_transition(contexts_settings.SYSTEM_LANGUAGESINPUT_INPUT, contexts_settings.SYSTEM, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.SYSTEM_LOCATION, contexts_settings.SYSTEM, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.SYSTEM_ABOUT, contexts_settings.SYSTEM, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.SYSTEM_OPEN_SOURCE_SOFTWARE_NOTICE, contexts_settings.SYSTEM, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.SYSTEM_OPEN_SOURCE_SOFTWARE_NOTICE, contexts_settings.SYSTEM_OPEN_SOURCE_SOFTWARE_NOTICE_TLI, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_OPEN_SOURCE_SW_NOTICE_TLI, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.SYSTEM_OPEN_SOURCE_SOFTWARE_NOTICE_TLI, contexts_settings.SYSTEM_OPEN_SOURCE_SOFTWARE_NOTICE, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	graph.add_transition(contexts_settings.SYSTEM_LEGAL_INFORMATION, contexts_settings.SYSTEM, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	# graph.add_transition(contexts_settings.SYSTEM_LOCAL_SYSTEM_UPDATE, contexts_settings.SYSTEM, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))

	# graph.add_transition(contexts_settings.SYSTEM_LANGUAGESINPUT_INPUT, contexts_settings.SYSTEM_LANGUAGESINPUT_LANGUAGES, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SYSTEM_LANGUAGESINPUT_LANGUAGES, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.SYSTEM_LANGUAGESINPUT_INPUT, contexts_settings.SYSTEM_LANGUAGESINPUT_LANGUAGES, (HMIActionType.click_element, [xpaths_settings.LIST_ITEM_SYSTEM_LANGUAGESINPUT_LANGUAGES]))
	graph.add_transition(contexts_settings.SYSTEM_LANGUAGESINPUT_LANGUAGES, contexts_settings.SYSTEM_LANGUAGESINPUT_INPUT, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
	# graph.add_transition(contexts_settings.SYSTEM_LANGUAGESINPUT_INPUT, contexts_settings.SYSTEM_LANGUAGESINPUT_KEYBOARD, (HMIActionType.click_element_in_list, [xpaths_settings.LIST_ITEM_SYSTEM_LANGUAGESINPUT_KEYBOARD, xpaths_settings.LIST_CONTAINER]))
	graph.add_transition(contexts_settings.SYSTEM_LANGUAGESINPUT_INPUT, contexts_settings.SYSTEM_LANGUAGESINPUT_KEYBOARD, (HMIActionType.click_element, [xpaths_settings.LIST_ITEM_SYSTEM_LANGUAGESINPUT_KEYBOARD]))
	graph.add_transition(contexts_settings.SYSTEM_LANGUAGESINPUT_KEYBOARD, contexts_settings.SYSTEM_LANGUAGESINPUT_INPUT, (HMIActionType.click_element, [xpaths_settings.BACK_BUTTON]))
