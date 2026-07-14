# -*- coding: utf-8 -*-
"""Module contains transitions for a sub graph of the android HMI."""

from enna_hcp_configuration.android import xpaths
from enna_hcp_configuration.android.xpaths import experiences as xpaths_experiences
from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import experiences as contexts_experiences
from enna_hcp_configuration.android.contexts import launcher as contexts_launcher


# pylint: disable=line-too-long
def initialize(graph):
	"""Initialize the sub graph in this module by adding transitions to the main graph.

	:param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
	"""
	graph.add_transition(contexts_experiences.MOOD, contexts_experiences.ENTERTAINMENT, (HMIActionType.click_element, [xpaths_experiences.ENTERTAINMENT_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD, contexts_experiences.POWERNAP, (HMIActionType.click_element, [xpaths_experiences.POWERNAP_BUTTON]))

	graph.add_transition(contexts_experiences.MOOD, contexts_experiences.MOOD_RELAXING_POPUP, (HMIActionType.click_element, [xpaths_experiences.MOOD_RELAXING_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD_RELAXING_POPUP, contexts_experiences.MOOD_RELAXING, (HMIActionType.click_element, [xpaths_experiences.MOOD_RELAXING_OK_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD_RELAXING, contexts_experiences.MOOD, (HMIActionType.click_element, [xpaths_experiences.MOOD_RELAXING_CLOSE_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD_RELAXING, contexts_experiences.MOOD_RELAXING_MODESETTINGS_SETTINGS, (HMIActionType.click_element, [xpaths_experiences.MOOD_RELAXING_MODESETTINGS_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD_RELAXING_MODESETTINGS_SETTINGS, contexts_experiences.MOOD_RELAXING, (HMIActionType.click_element, [xpaths_experiences.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD_RELAXING_MODESETTINGS_SETTINGS, contexts_experiences.MOOD_RELAXING_MODESETTINGS_ADDITIONALSETTINGS, (HMIActionType.click_element, [xpaths_experiences.MOOD_RELAXING_MODESETTINGS_ADDITIONALSETTINGS_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD_RELAXING_MODESETTINGS_ADDITIONALSETTINGS, contexts_experiences.MOOD_RELAXING_MODESETTINGS_SETTINGS, (HMIActionType.click_element, [xpaths_experiences.MOOD_RELAXING_MODESETTINGS_SETTINGS_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD_RELAXING_MODESETTINGS_ADDITIONALSETTINGS, contexts_experiences.MOOD_RELAXING, (HMIActionType.click_element, [xpaths_experiences.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD_RELAXING, contexts_experiences.MOOD_RELAXING_FULLSCREEN, (HMIActionType.click_coordinates, [960, 360]))
	graph.add_transition(contexts_experiences.MOOD_RELAXING_FULLSCREEN, contexts_experiences.MOOD_RELAXING, (HMIActionType.click_element, [xpaths_experiences.MOOD_RELAXING_FULLSCREEN_TITLE]))

	graph.add_transition(contexts_experiences.MOOD, contexts_experiences.MOOD_HARMONISING_POPUP, (HMIActionType.click_element, [xpaths_experiences.MOOD_HARMONISING_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD_HARMONISING_POPUP, contexts_experiences.MOOD_HARMONISING, (HMIActionType.click_element, [xpaths_experiences.MOOD_HARMONISING_OK_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD_HARMONISING, contexts_experiences.MOOD, (HMIActionType.click_element, [xpaths_experiences.MOOD_HARMONISING_CLOSE_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD_HARMONISING, contexts_experiences.MOOD_HARMONISING_FULLSCREEN, (HMIActionType.click_coordinates, [960, 360]))
	graph.add_transition(contexts_experiences.MOOD_HARMONISING_FULLSCREEN, contexts_experiences.MOOD_HARMONISING, (HMIActionType.click_element, [xpaths_experiences.MOOD_HARMONISING_FULLSCREEN_TITLE]))

	graph.add_transition(contexts_experiences.MOOD, contexts_experiences.MOOD_ANIMATING_POPUP, (HMIActionType.click_element, [xpaths_experiences.MOOD_ANIMATING_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD_ANIMATING_POPUP, contexts_experiences.MOOD_ANIMATING, (HMIActionType.click_element, [xpaths_experiences.MOOD_ANIMATING_OK_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD_ANIMATING, contexts_experiences.MOOD, (HMIActionType.click_element, [xpaths_experiences.MOOD_ANIMATING_CLOSE_BUTTON]))
	graph.add_transition(contexts_experiences.MOOD_ANIMATING, contexts_experiences.MOOD_ANIMATING_FULLSCREEN, (HMIActionType.click_coordinates, [960, 360]))
	graph.add_transition(contexts_experiences.MOOD_ANIMATING_FULLSCREEN, contexts_experiences.MOOD_ANIMATING, (HMIActionType.click_element, [xpaths_experiences.MOOD_ANIMATING_FULLSCREEN_TITLE]))

	graph.add_transition(contexts_experiences.ENTERTAINMENT, contexts_experiences.MOOD, (HMIActionType.click_element, [xpaths_experiences.MOOD_BUTTON]))
	graph.add_transition(contexts_experiences.ENTERTAINMENT, contexts_experiences.POWERNAP, (HMIActionType.click_element, [xpaths_experiences.POWERNAP_BUTTON]))
	graph.add_transition(contexts_experiences.ENTERTAINMENT, contexts_experiences.ENTERTAINMENT_MUSIC_POPUP, (HMIActionType.click_element, [xpaths_experiences.ENTERTAINMENT_MUSIC_BUTTON]))
	graph.add_transition(contexts_experiences.ENTERTAINMENT_MUSIC_POPUP, contexts_experiences.ENTERTAINMENT_MUSIC, (HMIActionType.click_element, [xpaths_experiences.ENTERTAINMENT_MUSIC_OK_BUTTON]))
	graph.add_transition(contexts_experiences.ENTERTAINMENT_MUSIC, contexts_experiences.ENTERTAINMENT, (HMIActionType.click_element, [xpaths_experiences.ENTERTAINMENT_MUSIC_CLOSE_BUTTON]))
	graph.add_transition(contexts_experiences.ENTERTAINMENT_MUSIC, contexts_experiences.ENTERTAINMENT_MUSIC_MODESETTINGS_SETTINGS, (HMIActionType.click_element, [xpaths_experiences.ENTERTAINMENT_MUSIC_MODESETTINGS_BUTTON]))
	graph.add_transition(contexts_experiences.ENTERTAINMENT_MUSIC_MODESETTINGS_SETTINGS, contexts_experiences.ENTERTAINMENT_MUSIC, (HMIActionType.click_element, [xpaths_experiences.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_experiences.ENTERTAINMENT_MUSIC, contexts_experiences.ENTERTAINMENT_MUSIC_FULLSCREEN, (HMIActionType.click_coordinates, [960, 360]))
	graph.add_transition(contexts_experiences.ENTERTAINMENT_MUSIC_FULLSCREEN, contexts_experiences.ENTERTAINMENT_MUSIC, (HMIActionType.click_element, [xpaths_experiences.ENTERTAINMENT_MUSIC_FULLSCREEN_TITLE]))
	graph.add_transition(contexts_experiences.ENTERTAINMENT, contexts_experiences.ENTERTAINMENT_VIDEO_INFO_POPUP, (HMIActionType.click_element, [xpaths_experiences.ENTERTAINMENT_VIDEO_BUTTON]))
	graph.add_transition(contexts_experiences.ENTERTAINMENT_VIDEO_INFO_POPUP, contexts_experiences.ENTERTAINMENT_VIDEO, (HMIActionType.click_element, [xpaths_experiences.ENTERTAINMENT_VIDEO_OK_BUTTON]))
	graph.add_transition(contexts_experiences.ENTERTAINMENT_VIDEO_INFO_POPUP, contexts_experiences.ENTERTAINMENT, (HMIActionType.click_element, [xpaths_experiences.ENTERTAINMENT_VIDEO_CANCEL_BUTTON]))
	graph.add_transition(contexts_experiences.ENTERTAINMENT_VIDEO, contexts_experiences.ENTERTAINMENT, (HMIActionType.click_element, [xpaths_experiences.ENTERTAINMENT_VIDEO_CLOSE_BUTTON]))

	graph.add_transition(contexts_experiences.POWERNAP, contexts_experiences.MOOD, (HMIActionType.click_element, [xpaths_experiences.MOOD_BUTTON]))
	graph.add_transition(contexts_experiences.POWERNAP, contexts_experiences.ENTERTAINMENT, (HMIActionType.click_element, [xpaths_experiences.ENTERTAINMENT_BUTTON]))

	graph.add_transition(contexts_experiences.MOOD, contexts_experiences.SETTINGS, (HMIActionType.click_element, [xpaths_experiences.MORE_BUTTON]))
	graph.add_transition(contexts_experiences.ENTERTAINMENT, contexts_experiences.SETTINGS, (HMIActionType.click_element, [xpaths_experiences.MORE_BUTTON]))
	graph.add_transition(contexts_experiences.POWERNAP, contexts_experiences.SETTINGS, (HMIActionType.click_element, [xpaths_experiences.MORE_BUTTON]))
	graph.add_transition(contexts_experiences.SETTINGS, contexts_experiences.MOOD, (HMIActionType.click_element, [xpaths_experiences.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_experiences.SETTINGS, contexts_experiences.ENTERTAINMENT, (HMIActionType.click_element, [xpaths_experiences.SETTINGS_BACK_BUTTON]))
	graph.add_transition(contexts_experiences.SETTINGS, contexts_experiences.POWERNAP, (HMIActionType.click_element, [xpaths_experiences.SETTINGS_BACK_BUTTON]))

	graph.add_transition(contexts_experiences.MOOD, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_experiences.ENTERTAINMENT, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
	graph.add_transition(contexts_experiences.POWERNAP, contexts_launcher.APP_LIST, (HMIActionType.click_element, [xpaths.APP_LIST_BUTTON]))
