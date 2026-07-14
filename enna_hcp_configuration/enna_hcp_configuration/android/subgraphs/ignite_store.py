# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""

from enna_hcp_configuration.android import xpaths
from enna_hcp_configuration.android.xpaths import ignite_store as xpaths_ignite_store, aem as xpaths_aem
from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import aem as contexts_aem, ignite_store as contexts_ignite_store, launcher as contexts_launcher


# pylint:disable=too-many-statements, line-too-long
def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	# Enter the store from the app list
	graph.add_transition(contexts_ignite_store.POPUP_INITIAL_AUTOMATIC_UPDATES, contexts_ignite_store.SETTINGS_COUNTRY_SELECTION_DISCLAIMER_TWO_OPTIONS, (HMIActionType.click_element, [xpaths_ignite_store.OK_BUTTON]))
	graph.add_transition(contexts_ignite_store.SETTINGS_COUNTRY_SELECTION_DISCLAIMER_TWO_OPTIONS, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.CONTINUE_BUTTON]))
	graph.add_transition(contexts_ignite_store.SETTINGS_COUNTRY_SELECTION_DISCLAIMER_TWO_OPTIONS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_ignite_store.DISCLAIMER_CLOSE_BUTTON]))

	# Exit ignite store from different screens
	graph.add_transition(contexts_ignite_store.CAR_FUNCTIONALITY, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_ignite_store.APPS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_ignite_store.MY_APPLICATIONS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_ignite_store.PRIVACY_MODE, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_ignite_store.AEM_IGNITE_STORE_ENGINEERING_MENUE, contexts_aem.MAIN, (HMIActionType.click_element, [xpaths_aem.IGNITE_STORE_ENGINEERING_MENU_BACK_BUTTON]))

	# From first tab to other screens
	graph.add_transition(contexts_ignite_store.CAR_FUNCTIONALITY, contexts_ignite_store.APPS, (HMIActionType.click_element, [xpaths_ignite_store.APPS]))
	graph.add_transition(contexts_ignite_store.CAR_FUNCTIONALITY, contexts_ignite_store.MY_APPLICATIONS, (HMIActionType.click_element, [xpaths_ignite_store.MY_APPLICATIONS]))

	# From second tab to other screens
	graph.add_transition(contexts_ignite_store.APPS, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.CAR_FUNCTIONALITY]))
	graph.add_transition(contexts_ignite_store.APPS, contexts_ignite_store.MY_APPLICATIONS, (HMIActionType.click_element, [xpaths_ignite_store.MY_APPLICATIONS]))

	# From third tab to other screens
	graph.add_transition(contexts_ignite_store.MY_APPLICATIONS, contexts_ignite_store.APPS, (HMIActionType.click_element, [xpaths_ignite_store.APPS]))
	graph.add_transition(contexts_ignite_store.MY_APPLICATIONS, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.CAR_FUNCTIONALITY]))
	graph.add_transition(contexts_ignite_store.MY_APPLICATIONS, contexts_ignite_store.LICENSE_PACKAGES, (HMIActionType.click_element_in_list, [xpaths_ignite_store.LICENSE_PACKAGES_ENTRY, xpaths_ignite_store.CONTAINER_APP_LIST]))

	# Outgoing from detail page
	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION_FOD, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION, contexts_ignite_store.APPS, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION, contexts_ignite_store.MY_APPLICATIONS, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION, contexts_ignite_store.ABOUT_THIS_APP, (HMIActionType.click_element, [xpaths_ignite_store.DETAIL_PAGE_ABOUT_THIS_APP_TITLE]))
	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION, contexts_ignite_store.READ_MORE, (HMIActionType.click_element, [xpaths_ignite_store.DETAIL_PAGE_READ_MORE]))
	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION, contexts_ignite_store.WHATS_NEW, (HMIActionType.click_element_in_list, [xpaths_ignite_store.DETAIL_PAGE_WHATS_NEW, xpaths_ignite_store.CONTAINER_APP_LIST]))
	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION, contexts_ignite_store.IMAGE_LARGE, (HMIActionType.click_element, [xpaths_ignite_store.LICENSE_IMAGE_SMALL]))
	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION_FOD, contexts_ignite_store.IMAGE_LARGE, (HMIActionType.click_element, [xpaths_ignite_store.LICENSE_IMAGE_SMALL]))
	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION_FOD, contexts_ignite_store.READ_MORE, (HMIActionType.click_element, [xpaths_ignite_store.DETAIL_PAGE_READ_MORE]))

	# Ingoing to detail page - third party
	graph.add_transition(contexts_ignite_store.ABOUT_THIS_APP, contexts_ignite_store.APP_DESCRIPTION, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.READ_MORE, contexts_ignite_store.APP_DESCRIPTION, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.WHATS_NEW, contexts_ignite_store.APP_DESCRIPTION, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.APPS, contexts_ignite_store.APP_DESCRIPTION, (HMIActionType.click_element_in_list, [xpaths_ignite_store.CLICKABLE_LIST_ITEM, xpaths_ignite_store.CONTAINER_APP_LIST]))
	graph.add_transition(contexts_ignite_store.IMAGE_LARGE, contexts_ignite_store.APP_DESCRIPTION, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))

	# Ingoing to detail page - FOD
	graph.add_transition(contexts_ignite_store.CAR_FUNCTIONALITY, contexts_ignite_store.APP_DESCRIPTION_FOD, (HMIActionType.click_element_in_list, [xpaths_ignite_store.PRICE_INFO_PRODUCT_LIST, xpaths_ignite_store.CONTAINER_APP_LIST]))
	graph.add_transition(contexts_ignite_store.IMAGE_LARGE, contexts_ignite_store.APP_DESCRIPTION_FOD, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.ABOUT_THIS_FUNCTION, contexts_ignite_store.APP_DESCRIPTION_FOD, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))

	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION_FOD, contexts_ignite_store.ABOUT_THIS_FUNCTION, (HMIActionType.click_element, [xpaths_ignite_store.ABOUT_THIS_FUNCTION]))

	# From FOD detail page to Variant selection
	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION_FOD, contexts_ignite_store.VARIANT_SELECTION, (HMIActionType.click_element, [xpaths_ignite_store.PURCHASE_BUTTON_FOD_SCREEN_TITLE]))

	# Ingoing to Settings
	graph.add_transition(contexts_ignite_store.CAR_FUNCTIONALITY, contexts_ignite_store.SETTINGS, (HMIActionType.click_element, [xpaths_ignite_store.SETTINGS_BUTTON]))
	graph.add_transition(contexts_ignite_store.APPS, contexts_ignite_store.SETTINGS, (HMIActionType.click_element, [xpaths_ignite_store.SETTINGS_BUTTON]))
	graph.add_transition(contexts_ignite_store.MY_APPLICATIONS, contexts_ignite_store.SETTINGS, (HMIActionType.click_element, [xpaths_ignite_store.SETTINGS_BUTTON]))
	graph.add_transition(contexts_ignite_store.SEARCH, contexts_ignite_store.SETTINGS, (HMIActionType.click_element, [xpaths_ignite_store.SETTINGS_BUTTON]))
	graph.add_transition(contexts_ignite_store.NOT_IN_THIS_CAR, contexts_ignite_store.SETTINGS, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.SUPPLIER_COUNTRY, contexts_ignite_store.SETTINGS_COUNTRY_SELECTION_DISCLAIMER_TWO_OPTIONS, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.SETTINGS_COUNTRY_SELECTION_DISCLAIMER_TWO_OPTIONS, contexts_ignite_store.SETTINGS, (HMIActionType.click_element, [xpaths_ignite_store.CONTINUE_BUTTON]))
	graph.add_transition(contexts_ignite_store.OPEN_SOURCE, contexts_ignite_store.SETTINGS, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))

	# Outgoing from Settings
	graph.add_transition(contexts_ignite_store.SETTINGS, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.SETTINGS, contexts_ignite_store.APPS, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.SETTINGS, contexts_ignite_store.MY_APPLICATIONS, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.SETTINGS, contexts_ignite_store.SEARCH, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.SETTINGS, contexts_ignite_store.NOT_IN_THIS_CAR, (HMIActionType.click_element_in_list, [xpaths_ignite_store.NOT_IN_THIS_CAR_ENTRY, xpaths_ignite_store.CONTAINER_APP_LIST]))
	graph.add_transition(contexts_ignite_store.SETTINGS, contexts_ignite_store.SETTINGS_COUNTRY_SELECTION_DISCLAIMER, (HMIActionType.click_element_in_list, [xpaths_ignite_store.SUPPLIER_COUNTRY_ENTRY, xpaths_ignite_store.CONTAINER_APP_LIST]))
	graph.add_transition(contexts_ignite_store.SETTINGS, contexts_ignite_store.OPEN_SOURCE, (HMIActionType.click_element_in_list, [xpaths_ignite_store.OPEN_SOURCE_LICENCES_ENTRY, xpaths_ignite_store.CONTAINER_APP_LIST]))

	# Outgoing from disclaimer in settings
	graph.add_transition(contexts_ignite_store.SETTINGS_COUNTRY_SELECTION_DISCLAIMER, contexts_ignite_store.SUPPLIER_COUNTRY, (HMIActionType.click_element, [xpaths_ignite_store.DISCLAIMER_CHANGE_SETTINGS_TITLE]))
	graph.add_transition(contexts_ignite_store.SETTINGS_COUNTRY_SELECTION_DISCLAIMER, contexts_ignite_store.SETTINGS, (HMIActionType.click_element, [xpaths_ignite_store.CONTINUE_BUTTON]))

	# Ingoing to Search
	graph.add_transition(contexts_ignite_store.CAR_FUNCTIONALITY, contexts_ignite_store.SEARCH, (HMIActionType.click_element, [xpaths_ignite_store.SEARCH_BUTTON]))
	graph.add_transition(contexts_ignite_store.APPS, contexts_ignite_store.SEARCH, (HMIActionType.click_element, [xpaths_ignite_store.SEARCH_BUTTON]))
	graph.add_transition(contexts_ignite_store.MY_APPLICATIONS, contexts_ignite_store.SEARCH, (HMIActionType.click_element, [xpaths_ignite_store.SEARCH_BUTTON]))
	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION, contexts_ignite_store.SEARCH, (HMIActionType.click_element, [xpaths_ignite_store.SEARCH_BUTTON]))
	graph.add_transition(contexts_ignite_store.SETTINGS, contexts_ignite_store.SEARCH, (HMIActionType.click_element, [xpaths_ignite_store.SEARCH_BUTTON]))

	# Outgoing from Search
	graph.add_transition(contexts_ignite_store.SEARCH, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.SEARCH, contexts_ignite_store.APPS, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.SEARCH, contexts_ignite_store.MY_APPLICATIONS, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.SEARCH, contexts_ignite_store.APP_DESCRIPTION, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.SEARCH, contexts_ignite_store.SETTINGS, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))

	# Back from license screen
	graph.add_transition(contexts_ignite_store.LICENSE_PACKAGES, contexts_ignite_store.MY_APPLICATIONS, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))

	# Outgoing from variant selection
	graph.add_transition(contexts_ignite_store.CHECKOUT_OPTION_DIALOG, contexts_ignite_store.CHECKOUT_SCREEN, (HMIActionType.click_element, [xpaths_ignite_store.DIALOG_OPTION_MYAUDIAPP]))
	graph.add_transition(contexts_ignite_store.VARIANT_SELECTION, contexts_ignite_store.APP_DESCRIPTION_FOD, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))

	# Outgoing from Checkout screen
	graph.add_transition(contexts_ignite_store.CHECKOUT_SCREEN, contexts_ignite_store.VARIANT_SELECTION, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))

	# Outgoing from Detail page FOD
	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION_FOD, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION_FOD, contexts_ignite_store.USAGE_INSTRUCTIONS, (HMIActionType.click_element, [xpaths_ignite_store.USAGE_INSTRUCTIONS_DETAIL_PAGE]))
	graph.add_transition(contexts_ignite_store.USAGE_INSTRUCTIONS, contexts_ignite_store.APP_DESCRIPTION_FOD, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))

	# Checkout Flow. All paths in and out of the checkout steps.
	graph.add_transition(contexts_ignite_store.VARIANT_SELECTION, contexts_ignite_store.CHECKOUT_OPTION_DIALOG, (HMIActionType.click_element, [xpaths_ignite_store.PURCHASE_BUTTON_VARIANT_SCREEN]))
	graph.add_transition(contexts_ignite_store.CHECKOUT_OPTION_DIALOG, contexts_ignite_store.VARIANT_SELECTION, (HMIActionType.click_element, [xpaths_ignite_store.DIALOG_OPTION_CANCEL]))

	graph.add_transition(contexts_ignite_store.CHECKOUT_OPTION_DIALOG, contexts_ignite_store.CHECK_ORDER, (HMIActionType.click_element, [xpaths_ignite_store.DIALOG_OPTION_INTHECAR]))
	graph.add_transition(contexts_ignite_store.CHECK_ORDER, contexts_ignite_store.VARIANT_SELECTION, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))

	graph.add_transition(contexts_ignite_store.CHECK_ORDER, contexts_ignite_store.BILLING_INFORMATION, (HMIActionType.click_element, [xpaths_ignite_store.CONTINUE_BUTTON]))
	graph.add_transition(contexts_ignite_store.BILLING_INFORMATION, contexts_ignite_store.CHECK_ORDER, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))

	# Last step where user needs to check the checkbox.
	graph.add_transition(contexts_ignite_store.BILLING_INFORMATION, contexts_ignite_store.COMPLETE_PROCESS_NOT_CHECKED, (HMIActionType.click_element, [xpaths_ignite_store.CONTINUE_BUTTON]))
	graph.add_transition(contexts_ignite_store.COMPLETE_PROCESS_CHECKED, contexts_ignite_store.BILLING_INFORMATION, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.COMPLETE_PROCESS_NOT_CHECKED, contexts_ignite_store.BILLING_INFORMATION, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.COMPLETE_PROCESS_NOT_CHECKED, contexts_ignite_store.COMPLETE_PROCESS_CHECKED, (HMIActionType.click_element, [xpaths_ignite_store.CHECKBOX_ACCEPT_TERMS_NOTCHECKED]))
	graph.add_transition(contexts_ignite_store.COMPLETE_PROCESS_CHECKED, contexts_ignite_store.COMPLETE_PROCESS_NOT_CHECKED, (HMIActionType.click_element, [xpaths_ignite_store.CHECKBOX_ACCEPT_TERMS_CHECKED]))

	# Back from deep checkout legal
	graph.add_transition(contexts_ignite_store.DEEP_CHECKOUT_LEGAL_LIST, contexts_ignite_store.COMPLETE_PROCESS_CHECKED, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.DEEP_CHECKOUT_LEGAL_LIST, contexts_ignite_store.COMPLETE_PROCESS_NOT_CHECKED, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))

	# Step to order creation
	graph.add_transition(contexts_ignite_store.COMPLETE_PROCESS_CHECKED, contexts_ignite_store.ORDER_SENT, (HMIActionType.click_element, [xpaths_ignite_store.COMPLETE_PURCHASE_BUTTON]))

	# Path to initial screen after last step
	graph.add_transition(contexts_ignite_store.ORDER_SENT, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.OK_BUTTON]))

	# Return to Tab1 with cancel button from all checkout steps
	graph.add_transition(contexts_ignite_store.CHECK_ORDER, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.CANCEL_BUTTON]))
	graph.add_transition(contexts_ignite_store.BILLING_INFORMATION, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.CANCEL_BUTTON]))
	graph.add_transition(contexts_ignite_store.COMPLETE_PROCESS_NOT_CHECKED, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.CANCEL_BUTTON]))
	graph.add_transition(contexts_ignite_store.COMPLETE_PROCESS_CHECKED, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.CANCEL_BUTTON]))
	graph.add_transition(contexts_ignite_store.ORDER_SENT, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.CANCEL_BUTTON]))

	graph.add_transition(contexts_ignite_store.APP_DESCRIPTION, contexts_ignite_store.THIRD_PARTY_LEGAL_INFO, (HMIActionType.click_element, [xpaths_ignite_store.THIRD_PARTY_LEGAL_ENTRY]))
	graph.add_transition(contexts_ignite_store.THIRD_PARTY_LEGAL_INFO, contexts_ignite_store.APP_DESCRIPTION, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))

	# Return to Tab1 with back button from legal pages with entry point in Tab1
	graph.add_transition(contexts_ignite_store.PRICE_INFORMATION_LEGAL, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.TAB1_IMPRINT, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))
	graph.add_transition(contexts_ignite_store.TAB1_PRIVACY_POLICY, contexts_ignite_store.CAR_FUNCTIONALITY, (HMIActionType.click_element, [xpaths_ignite_store.BACK_BUTTON]))

	# Navigate to legal entries in tab1
	graph.add_transition(contexts_ignite_store.CAR_FUNCTIONALITY, contexts_ignite_store.TAB1_IMPRINT, (HMIActionType.click_element_in_list, [xpaths_ignite_store.IMPRINT_TAB1, xpaths_ignite_store.CONTAINER_APP_LIST]))
	graph.add_transition(contexts_ignite_store.CAR_FUNCTIONALITY, contexts_ignite_store.TAB1_PRIVACY_POLICY, (HMIActionType.click_element_in_list, [xpaths_ignite_store.PRIVACY_POLICY_TAB1, xpaths_ignite_store.CONTAINER_APP_LIST]))
	graph.add_transition(contexts_ignite_store.CAR_FUNCTIONALITY, contexts_ignite_store.PRICE_INFORMATION_LEGAL, (HMIActionType.click_element_in_list, [xpaths_ignite_store.SHOP_FUNCTIONS_PRICE_INFORMATION_LIST_ELEMENT, xpaths_ignite_store.CONTAINER_APP_LIST]))
