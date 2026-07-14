# -*- coding: utf-8 -*-
"""Module contains transitions from sound to any menu"""

from enna_hcp_configuration.android.base import HMIActionType
from enna_hcp_configuration.android.contexts import settings as contexts_settings
from enna_hcp_configuration.android.contexts import sound as contexts_sound
from enna_hcp_configuration.android.xpaths import sound as xpaths_sound

# pylint:disable=bad-indentation
def initialize(graph):
    """Initialize the sub graph in this module by adding transitions to the main graph.

    :param enna_hcp_configuration.bases.Graph graph: the main graph which should be extended
    """
    graph.add_transition(contexts_sound.PRESETS_CONCERTS, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_sound.BACK_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_CONCERTS, contexts_sound.BALANCE_FADER, (HMIActionType.click_element, [xpaths_sound.BALANCE_FADER_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_CONCERTS, contexts_sound.VOLUME, (HMIActionType.click_element, [xpaths_sound.VOLUME_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_CONCERTS, contexts_sound.FOD, (HMIActionType.click_element, [xpaths_sound.FOD_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_NEUTRAL, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_sound.BACK_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_NEUTRAL, contexts_sound.BALANCE_FADER, (HMIActionType.click_element, [xpaths_sound.BALANCE_FADER_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_NEUTRAL, contexts_sound.VOLUME, (HMIActionType.click_element, [xpaths_sound.VOLUME_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_NEUTRAL, contexts_sound.FOD, (HMIActionType.click_element, [xpaths_sound.FOD_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_LOUNGE, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_sound.BACK_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_LOUNGE, contexts_sound.BALANCE_FADER, (HMIActionType.click_element, [xpaths_sound.BALANCE_FADER_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_LOUNGE, contexts_sound.VOLUME, (HMIActionType.click_element, [xpaths_sound.VOLUME_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_LOUNGE, contexts_sound.FOD, (HMIActionType.click_element, [xpaths_sound.FOD_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_POTCAST, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_sound.BACK_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_POTCAST, contexts_sound.BALANCE_FADER, (HMIActionType.click_element, [xpaths_sound.BALANCE_FADER_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_POTCAST, contexts_sound.VOLUME, (HMIActionType.click_element, [xpaths_sound.VOLUME_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_POTCAST, contexts_sound.FOD, (HMIActionType.click_element, [xpaths_sound.FOD_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_sound.BACK_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL, contexts_sound.BALANCE_FADER, (HMIActionType.click_element, [xpaths_sound.BALANCE_FADER_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL, contexts_sound.VOLUME, (HMIActionType.click_element, [xpaths_sound.VOLUME_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL, contexts_sound.FOD, (HMIActionType.click_element, [xpaths_sound.FOD_BUTTON]))

    graph.add_transition(contexts_sound.BALANCE_FADER, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_sound.BACK_BUTTON]))
    graph.add_transition(contexts_sound.BALANCE_FADER, contexts_sound.PRESETS_CONCERTS, (HMIActionType.click_element, [xpaths_sound.PRESETS_BUTTON]))
    graph.add_transition(contexts_sound.BALANCE_FADER, contexts_sound.VOLUME, (HMIActionType.click_element, [xpaths_sound.VOLUME_BUTTON]))
    graph.add_transition(contexts_sound.BALANCE_FADER, contexts_sound.FOD, (HMIActionType.click_element, [xpaths_sound.FOD_BUTTON]))

    graph.add_transition(contexts_sound.VOLUME, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_sound.BACK_BUTTON]))
    graph.add_transition(contexts_sound.VOLUME, contexts_sound.PRESETS_CONCERTS, (HMIActionType.click_element, [xpaths_sound.PRESETS_BUTTON]))
    graph.add_transition(contexts_sound.VOLUME, contexts_sound.BALANCE_FADER, (HMIActionType.click_element, [xpaths_sound.BALANCE_FADER_BUTTON]))
    graph.add_transition(contexts_sound.VOLUME, contexts_sound.FOD, (HMIActionType.click_element, [xpaths_sound.FOD_BUTTON]))
    graph.add_transition(contexts_sound.VOLUME, contexts_sound.VOLUME_OPEN_SOURCE_DISCLAIMER, (HMIActionType.click_element_in_list, [xpaths_sound.VOLUME_OSD_BUTTON, xpaths_sound.VOLUME_RECYCLERVIEW_LIST]))
    graph.add_transition(contexts_sound.VOLUME_OPEN_SOURCE_DISCLAIMER, contexts_sound.VOLUME, (HMIActionType.click_element, [xpaths_sound.BACK_BUTTON]))

    graph.add_transition(contexts_sound.FOD, contexts_settings.MAIN, (HMIActionType.click_element, [xpaths_sound.BACK_BUTTON]))
    graph.add_transition(contexts_sound.FOD, contexts_sound.PRESETS_CONCERTS, (HMIActionType.click_element, [xpaths_sound.PRESETS_BUTTON]))
    graph.add_transition(contexts_sound.FOD, contexts_sound.BALANCE_FADER, (HMIActionType.click_element, [xpaths_sound.BALANCE_FADER_BUTTON]))
    graph.add_transition(contexts_sound.FOD, contexts_sound.VOLUME, (HMIActionType.click_element, [xpaths_sound.VOLUME_BUTTON]))

    graph.add_transition(contexts_sound.PRESETS_CONCERTS, contexts_sound.PRESETS_NEUTRAL, (HMIActionType.click_element, [xpaths_sound.PRESET_NEUTRAL_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_CONCERTS, contexts_sound.PRESETS_LOUNGE, (HMIActionType.click_element, [xpaths_sound.PRESET_LOUNGE_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_CONCERTS, contexts_sound.PRESETS_POTCAST, (HMIActionType.click_element, [xpaths_sound.PRESET_POTCAST_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_CONCERTS, contexts_sound.PRESETS_INDIVIDUAL, (HMIActionType.click_element, [xpaths_sound.PRESET_INDIVIDUAL_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_NEUTRAL, contexts_sound.PRESETS_CONCERTS, (HMIActionType.click_element, [xpaths_sound.PRESET_CONCERTS_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_NEUTRAL, contexts_sound.PRESETS_LOUNGE, (HMIActionType.click_element, [xpaths_sound.PRESET_LOUNGE_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_NEUTRAL, contexts_sound.PRESETS_POTCAST, (HMIActionType.click_element, [xpaths_sound.PRESET_POTCAST_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_NEUTRAL, contexts_sound.PRESETS_INDIVIDUAL, (HMIActionType.click_element, [xpaths_sound.PRESET_INDIVIDUAL_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_LOUNGE, contexts_sound.PRESETS_CONCERTS, (HMIActionType.click_element, [xpaths_sound.PRESET_CONCERTS_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_LOUNGE, contexts_sound.PRESETS_NEUTRAL, (HMIActionType.click_element, [xpaths_sound.PRESET_NEUTRAL_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_LOUNGE, contexts_sound.PRESETS_POTCAST, (HMIActionType.click_element, [xpaths_sound.PRESET_POTCAST_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_LOUNGE, contexts_sound.PRESETS_INDIVIDUAL, (HMIActionType.click_element, [xpaths_sound.PRESET_INDIVIDUAL_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_POTCAST, contexts_sound.PRESETS_CONCERTS, (HMIActionType.click_element, [xpaths_sound.PRESET_CONCERTS_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_POTCAST, contexts_sound.PRESETS_NEUTRAL, (HMIActionType.click_element, [xpaths_sound.PRESET_NEUTRAL_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_POTCAST, contexts_sound.PRESETS_LOUNGE, (HMIActionType.click_element, [xpaths_sound.PRESET_LOUNGE_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_POTCAST, contexts_sound.PRESETS_INDIVIDUAL, (HMIActionType.click_element, [xpaths_sound.PRESET_INDIVIDUAL_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL, contexts_sound.PRESETS_CONCERTS, (HMIActionType.click_element, [xpaths_sound.PRESET_CONCERTS_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL, contexts_sound.PRESETS_NEUTRAL, (HMIActionType.click_element, [xpaths_sound.PRESET_NEUTRAL_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL, contexts_sound.PRESETS_LOUNGE, (HMIActionType.click_element, [xpaths_sound.PRESET_LOUNGE_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL, contexts_sound.PRESETS_POTCAST, (HMIActionType.click_element, [xpaths_sound.PRESET_POTCAST_BUTTON]))

    # graph to PRESETS_INDIVIDUAL_EQUALIZER_NO_PREMIUM only to test without RSI
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL, contexts_sound.PRESETS_INDIVIDUAL_EQUALIZER_NO_PREMIUM, (HMIActionType.click_element, [xpaths_sound.PRESET_INDIVIDUAL_EDIT_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL_EQUALIZER_NO_PREMIUM, contexts_sound.PRESETS_INDIVIDUAL, (HMIActionType.click_element, [xpaths_sound.BACK_BUTTON]))

    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL, contexts_sound.PRESETS_INDIVIDUAL_EQUALIZER, (HMIActionType.click_element, [xpaths_sound.PRESET_INDIVIDUAL_EDIT_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL_EQUALIZER, contexts_sound.PRESETS_INDIVIDUAL_SURROUND, (HMIActionType.click_element, [xpaths_sound.PRESET_INDIVIDUAL_SURROUND_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL_EQUALIZER, contexts_sound.PRESETS_INDIVIDUAL_SEATS, (HMIActionType.click_element, [xpaths_sound.PRESET_INDIVIDUAL_SEATS_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL_EQUALIZER, contexts_sound.PRESETS_INDIVIDUAL, (HMIActionType.click_element, [xpaths_sound.BACK_BUTTON]))

    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL_SURROUND, contexts_sound.PRESETS_INDIVIDUAL_EQUALIZER, (HMIActionType.click_element, [xpaths_sound.PRESET_INDIVIDUAL_EQUALIZER_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL_SURROUND, contexts_sound.PRESETS_INDIVIDUAL_SEATS, (HMIActionType.click_element, [xpaths_sound.PRESET_INDIVIDUAL_SEATS_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL_SURROUND, contexts_sound.PRESETS_INDIVIDUAL, (HMIActionType.click_element, [xpaths_sound.BACK_BUTTON]))

    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL_SEATS, contexts_sound.PRESETS_INDIVIDUAL_EQUALIZER, (HMIActionType.click_element, [xpaths_sound.PRESET_INDIVIDUAL_EQUALIZER_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL_SEATS, contexts_sound.PRESETS_INDIVIDUAL_SURROUND, (HMIActionType.click_element, [xpaths_sound.PRESET_INDIVIDUAL_SURROUND_BUTTON]))
    graph.add_transition(contexts_sound.PRESETS_INDIVIDUAL_SEATS, contexts_sound.PRESETS_INDIVIDUAL, (HMIActionType.click_element, [xpaths_sound.BACK_BUTTON]))
