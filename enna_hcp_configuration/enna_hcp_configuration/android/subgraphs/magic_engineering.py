# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of core services."""

from enna_hcp_configuration.android import xpaths
from enna_hcp_configuration.android.xpaths import magic_engineering as xpaths_magic_engineering
from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import magic_engineering as contexts_magic_engineering, launcher as contexts_launcher

def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	# Exit the app
	graph.add_transition(contexts_magic_engineering.CONNECTIVITY, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_magic_engineering.ACCOUNT_SERVICE, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_magic_engineering.SERVICE_MANAGEMENT_TTS, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_magic_engineering.SERVICE_MANAGEMENT_VTTL, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_magic_engineering.MQTT, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_magic_engineering.MAGIC_SERVICE, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))

	# Switch between menue in the app
	graph.add_transition(contexts_magic_engineering.CONNECTIVITY, contexts_magic_engineering.ACCOUNT_SERVICE, (HMIActionType.click_element, [xpaths_magic_engineering.ACCOUNT_SERVICE_BUTTON]))
	graph.add_transition(contexts_magic_engineering.CONNECTIVITY, contexts_magic_engineering.SERVICE_MANAGEMENT_TTS, (HMIActionType.click_element, [xpaths_magic_engineering.SERVICE_MANAGEMENT_BUTTON]))
	graph.add_transition(contexts_magic_engineering.CONNECTIVITY, contexts_magic_engineering.SERVICE_MANAGEMENT_VTTL, (HMIActionType.click_element, [xpaths_magic_engineering.SERVICE_MANAGEMENT_BUTTON]))
	graph.add_transition(contexts_magic_engineering.CONNECTIVITY, contexts_magic_engineering.MQTT, (HMIActionType.click_element, [xpaths_magic_engineering.MQTT_BUTTON]))
	graph.add_transition(contexts_magic_engineering.CONNECTIVITY, contexts_magic_engineering.MAGIC_SERVICE, (HMIActionType.click_element, [xpaths_magic_engineering.MAGIC_SERVICE_BUTTON]))
	graph.add_transition(contexts_magic_engineering.ACCOUNT_SERVICE, contexts_magic_engineering.CONNECTIVITY, (HMIActionType.click_element, [xpaths_magic_engineering.CONNECTIVITY_BUTTON]))
	graph.add_transition(contexts_magic_engineering.ACCOUNT_SERVICE, contexts_magic_engineering.SERVICE_MANAGEMENT_TTS, (HMIActionType.click_element, [xpaths_magic_engineering.SERVICE_MANAGEMENT_BUTTON]))
	graph.add_transition(contexts_magic_engineering.ACCOUNT_SERVICE, contexts_magic_engineering.SERVICE_MANAGEMENT_VTTL, (HMIActionType.click_element, [xpaths_magic_engineering.SERVICE_MANAGEMENT_BUTTON]))
	graph.add_transition(contexts_magic_engineering.ACCOUNT_SERVICE, contexts_magic_engineering.MQTT, (HMIActionType.click_element, [xpaths_magic_engineering.MQTT_BUTTON]))
	graph.add_transition(contexts_magic_engineering.ACCOUNT_SERVICE, contexts_magic_engineering.MAGIC_SERVICE, (HMIActionType.click_element, [xpaths_magic_engineering.MAGIC_SERVICE_BUTTON]))
	graph.add_transition(contexts_magic_engineering.SERVICE_MANAGEMENT_TTS, contexts_magic_engineering.CONNECTIVITY, (HMIActionType.click_element, [xpaths_magic_engineering.CONNECTIVITY_BUTTON]))
	graph.add_transition(contexts_magic_engineering.SERVICE_MANAGEMENT_VTTL, contexts_magic_engineering.CONNECTIVITY, (HMIActionType.click_element, [xpaths_magic_engineering.CONNECTIVITY_BUTTON]))
	graph.add_transition(contexts_magic_engineering.SERVICE_MANAGEMENT_TTS, contexts_magic_engineering.ACCOUNT_SERVICE, (HMIActionType.click_element, [xpaths_magic_engineering.ACCOUNT_SERVICE_BUTTON]))
	graph.add_transition(contexts_magic_engineering.SERVICE_MANAGEMENT_VTTL, contexts_magic_engineering.ACCOUNT_SERVICE, (HMIActionType.click_element, [xpaths_magic_engineering.ACCOUNT_SERVICE_BUTTON]))
	graph.add_transition(contexts_magic_engineering.SERVICE_MANAGEMENT_TTS, contexts_magic_engineering.MQTT, (HMIActionType.click_element, [xpaths_magic_engineering.MQTT_BUTTON]))
	graph.add_transition(contexts_magic_engineering.SERVICE_MANAGEMENT_VTTL, contexts_magic_engineering.MQTT, (HMIActionType.click_element, [xpaths_magic_engineering.MQTT_BUTTON]))
	graph.add_transition(contexts_magic_engineering.SERVICE_MANAGEMENT_TTS, contexts_magic_engineering.MAGIC_SERVICE, (HMIActionType.click_element, [xpaths_magic_engineering.MAGIC_SERVICE_BUTTON]))
	graph.add_transition(contexts_magic_engineering.SERVICE_MANAGEMENT_VTTL, contexts_magic_engineering.MAGIC_SERVICE, (HMIActionType.click_element, [xpaths_magic_engineering.MAGIC_SERVICE_BUTTON]))
	graph.add_transition(contexts_magic_engineering.SERVICE_MANAGEMENT_TTS, contexts_magic_engineering.SERVICE_MANAGEMENT_VTTL, (HMIActionType.click_element, [xpaths_magic_engineering.SERVICE_MANAGEMENT_VTTL_BUTTON]))
	graph.add_transition(contexts_magic_engineering.SERVICE_MANAGEMENT_VTTL, contexts_magic_engineering.SERVICE_MANAGEMENT_TTS, (HMIActionType.click_element, [xpaths_magic_engineering.SERVICE_MANAGEMENT_TTS_BUTTON]))
	graph.add_transition(contexts_magic_engineering.MQTT, contexts_magic_engineering.CONNECTIVITY, (HMIActionType.click_element, [xpaths_magic_engineering.CONNECTIVITY_BUTTON]))
	graph.add_transition(contexts_magic_engineering.MQTT, contexts_magic_engineering.ACCOUNT_SERVICE, (HMIActionType.click_element, [xpaths_magic_engineering.ACCOUNT_SERVICE_BUTTON]))
	graph.add_transition(contexts_magic_engineering.MQTT, contexts_magic_engineering.SERVICE_MANAGEMENT_TTS, (HMIActionType.click_element, [xpaths_magic_engineering.SERVICE_MANAGEMENT_BUTTON]))
	graph.add_transition(contexts_magic_engineering.MQTT, contexts_magic_engineering.SERVICE_MANAGEMENT_VTTL, (HMIActionType.click_element, [xpaths_magic_engineering.SERVICE_MANAGEMENT_BUTTON]))
	graph.add_transition(contexts_magic_engineering.MQTT, contexts_magic_engineering.MAGIC_SERVICE, (HMIActionType.click_element, [xpaths_magic_engineering.MAGIC_SERVICE_BUTTON]))
	graph.add_transition(contexts_magic_engineering.MAGIC_SERVICE, contexts_magic_engineering.CONNECTIVITY, (HMIActionType.click_element, [xpaths_magic_engineering.CONNECTIVITY_BUTTON]))
	graph.add_transition(contexts_magic_engineering.MAGIC_SERVICE, contexts_magic_engineering.ACCOUNT_SERVICE, (HMIActionType.click_element, [xpaths_magic_engineering.ACCOUNT_SERVICE_BUTTON]))
	graph.add_transition(contexts_magic_engineering.MAGIC_SERVICE, contexts_magic_engineering.SERVICE_MANAGEMENT_TTS, (HMIActionType.click_element, [xpaths_magic_engineering.SERVICE_MANAGEMENT_BUTTON]))
	graph.add_transition(contexts_magic_engineering.MAGIC_SERVICE, contexts_magic_engineering.SERVICE_MANAGEMENT_VTTL, (HMIActionType.click_element, [xpaths_magic_engineering.SERVICE_MANAGEMENT_BUTTON]))
	graph.add_transition(contexts_magic_engineering.MAGIC_SERVICE, contexts_magic_engineering.MQTT, (HMIActionType.click_element, [xpaths_magic_engineering.MQTT_BUTTON]))
