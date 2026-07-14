# -*- coding: utf-8 -*-
"""Analyzer for the sound app."""

from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathBlacklistWhitelistDetectorExtension, ElementByXPathDetectorExtension
from enna_hcp_configuration.android.xpaths import sound as xpaths_sound
from enna_hcp_configuration.common.base import Element

PRESETS_CONCERTS = Element("presets_concerts", ElementByXPathDetectorExtension([xpaths_sound.PRESETS_TITLE, xpaths_sound.PRESETS_CONCERTS_TITLE]))
PRESETS_NEUTRAL = Element("presets_neutral", ElementByXPathDetectorExtension([xpaths_sound.PRESETS_TITLE, xpaths_sound.PRESETS_NEUTRAL_TITLE]))
PRESETS_LOUNGE = Element("presets_lounge", ElementByXPathDetectorExtension([xpaths_sound.PRESETS_TITLE, xpaths_sound.PRESETS_LOUNGE_TITLE]))
PRESETS_POTCAST = Element("presets_potcast", ElementByXPathDetectorExtension([xpaths_sound.PRESETS_TITLE, xpaths_sound.PRESETS_POTCAST_TITLE]))
PRESETS_INDIVIDUAL = Element("presets_individual", ElementByXPathDetectorExtension([xpaths_sound.PRESETS_TITLE, xpaths_sound.PRESETS_INDIVIDUAL_TITLE]))
PRESETS_INDIVIDUAL_EQUALIZER_NO_PREMIUM = Element("presets_individual_equalizer_no_premium", ElementByXPathBlacklistWhitelistDetectorExtension(
		must_exist=[xpaths_sound.PRESETS_INDIVIDUAL_EQUALIZER_NO_PREMIUM_TITLE],
		must_not_exist=[xpaths_sound.PRESETS_INDIVIDUAL_EQUALIZER_TITLE, xpaths_sound.PRESETS_INDIVIDUAL_SURROUND_TITLE, xpaths_sound.PRESETS_INDIVIDUAL_SEATS_TITLE]))
PRESETS_INDIVIDUAL_EQUALIZER = Element("presets_individual_equalizer", ElementByXPathDetectorExtension([xpaths_sound.PRESETS_INDIVIDUAL_EQUALIZER_TITLE]))
PRESETS_INDIVIDUAL_SURROUND = Element("presets_individual_surround", ElementByXPathDetectorExtension([xpaths_sound.PRESETS_INDIVIDUAL_SURROUND_TITLE]))
PRESETS_INDIVIDUAL_SEATS = Element("presets_individual_seats", ElementByXPathDetectorExtension([xpaths_sound.PRESETS_INDIVIDUAL_SEATS_TITLE]))
BALANCE_FADER = Element("balance_fader", ElementByXPathDetectorExtension([xpaths_sound.BALANCE_FADER_TITLE]))
VOLUME = Element("volume", ElementByXPathDetectorExtension([xpaths_sound.VOLUME_TITLE]))
VOLUME_OPEN_SOURCE_DISCLAIMER = Element("volume_open_source_disclaimer", ElementByXPathDetectorExtension([xpaths_sound.VOLUME_OPEN_SOURCE_DISCLAIMER_TITLE]))
FOD = Element("fod", ElementByXPathDetectorExtension([xpaths_sound.FOD_TITLE]))

CONTEXT = ContextAnalyzer("sound", AppPackageDetectorExtension(["de.eso.sound.audi"]))
CONTEXT.add_elements_from_module(globals())
