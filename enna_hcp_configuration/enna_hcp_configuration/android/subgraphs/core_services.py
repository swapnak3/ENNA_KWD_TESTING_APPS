# -*- coding: utf-8 -*-
"""Module contains transitions from core_services to any menu"""

from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import core_services as contexts_core_services
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher
from enna_hcp_configuration.android.xpaths import core_services as xpaths_core_services
from enna_hcp_configuration.android.xpaths import launcher as xpaths_launcher

def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	# Exit the app
	graph.add_transition(contexts_core_services.HOME, contexts_core_services.HOME_EXPAND, (HMIActionType.click_element, [xpaths_core_services.BURGER_DEVELOPMENT_BUTTON]))
	graph.add_transition(contexts_core_services.HOME_EXPAND, contexts_core_services.HOME, (HMIActionType.click_element, [xpaths_core_services.BURGER_DEVELOPMENT_BUTTON]))
	graph.add_transition(contexts_core_services.HOME, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_core_services.HEALTH_CHECK, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_core_services.BACKEND_SETTINGS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_core_services.CONFIGURATION, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_core_services.PSO_LOGIN, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_core_services.SERVICE_LIST_DISABLE_REASONS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_core_services.MQTT, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_core_services.TOKENS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))
	graph.add_transition(contexts_core_services.THIRD_PARTY_TRUSTSTORE, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths_launcher.APP_LIST_BUTTON]))

	# Home to all other Screens
	graph.add_transition(contexts_core_services.HOME, contexts_core_services.HEALTH_CHECK, (HMIActionType.click_element, [xpaths_core_services.BURGER_HEALTH_CHECK_BUTTON]))
	graph.add_transition(contexts_core_services.HOME, contexts_core_services.BACKEND_SETTINGS, (HMIActionType.click_element, [xpaths_core_services.BURGER_BACKEND_SETTINGS_BUTTON]))
	graph.add_transition(contexts_core_services.HOME, contexts_core_services.CONFIGURATION, (HMIActionType.click_element, [xpaths_core_services.BURGER_CONFIGURATION_BUTTON]))
	graph.add_transition(contexts_core_services.HOME, contexts_core_services.PSO_LOGIN, (HMIActionType.click_element, [xpaths_core_services.BURGER_PSO_LOGIN_BUTTON]))
	graph.add_transition(contexts_core_services.HOME, contexts_core_services.SERVICE_LIST_DISABLE_REASONS, (HMIActionType.click_element, [xpaths_core_services.BURGER_SERVICE_LIST_DSIABLE_REASON_BUTTON]))
	graph.add_transition(contexts_core_services.HOME, contexts_core_services.MQTT, (HMIActionType.click_element, [xpaths_core_services.BURGER_MQTT_BUTTON]))
	graph.add_transition(contexts_core_services.HOME, contexts_core_services.TOKENS, (HMIActionType.click_element, [xpaths_core_services.BURGER_TOKENS_BUTTON]))
	graph.add_transition(contexts_core_services.HOME, contexts_core_services.THIRD_PARTY_TRUSTSTORE, (HMIActionType.click_element, [xpaths_core_services.BURGER_THIRD_PARTY_TRUSTSTORE_BUTTON]))

	# All Screens back to Home
	graph.add_transition(contexts_core_services.HEALTH_CHECK, contexts_core_services.HOME, (HMIActionType.click_element, [xpaths_core_services.BURGER_HOME_BUTTON]))
	graph.add_transition(contexts_core_services.BACKEND_SETTINGS, contexts_core_services.HOME, (HMIActionType.click_element, [xpaths_core_services.BURGER_HOME_BUTTON]))
	graph.add_transition(contexts_core_services.CONFIGURATION, contexts_core_services.HOME, (HMIActionType.click_element, [xpaths_core_services.BURGER_HOME_BUTTON]))
	graph.add_transition(contexts_core_services.PSO_LOGIN, contexts_core_services.HOME, (HMIActionType.click_element, [xpaths_core_services.BURGER_HOME_BUTTON]))
	graph.add_transition(contexts_core_services.SERVICE_LIST_DISABLE_REASONS, contexts_core_services.HOME, (HMIActionType.click_element, [xpaths_core_services.BURGER_HOME_BUTTON]))
	graph.add_transition(contexts_core_services.MQTT, contexts_core_services.HOME, (HMIActionType.click_element, [xpaths_core_services.BURGER_HOME_BUTTON]))
	graph.add_transition(contexts_core_services.TOKENS, contexts_core_services.HOME, (HMIActionType.click_element, [xpaths_core_services.BURGER_HOME_BUTTON]))
	graph.add_transition(contexts_core_services.THIRD_PARTY_TRUSTSTORE, contexts_core_services.HOME, (HMIActionType.click_element, [xpaths_core_services.BURGER_HOME_BUTTON]))
