# -*- coding: utf-8 -*-
"""Analyzer for the Experiences app."""

from enna_hcp_configuration.android.xpaths import experiences
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathBlacklistWhitelistDetectorExtension, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import Element


MOOD = Element("mood", ElementByXPathDetectorExtension([experiences.MOOD_TITLE]))
ENTERTAINMENT = Element("entertainment", ElementByXPathDetectorExtension([experiences.ENTERTAINMENT_TITLE]))
POWERNAP = Element("powernap", ElementByXPathDetectorExtension([experiences.POWERNAP_TITLE]))
SETTINGS = Element("settings", ElementByXPathDetectorExtension([experiences.SETTINGS_TITLE, experiences.SETTINGS_RECYCLER_TITLE]))

MOOD_ANIMATING = Element("mood_animating", ElementByXPathDetectorExtension([experiences.MOOD_ANIMATING_TITLE]))
MOOD_ANIMATING_POPUP = Element("mood_animating_popup", ElementByXPathDetectorExtension([experiences.MOOD_ANIMATING_POPUP_TITLE]))
MOOD_ANIMATING_FULLSCREEN = Element("mood_animating_fullscreen", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[experiences.MOOD_ANIMATING_FULLSCREEN_TITLE], must_not_exist=[experiences.MOOD_ANIMATING_TITLE]))
MOOD_HARMONISING = Element("mood_harmonising", ElementByXPathDetectorExtension([experiences.MOOD_HARMONISING_TITLE]))
MOOD_HARMONISING_POPUP = Element("mood_harmonising_popup", ElementByXPathDetectorExtension([experiences.MOOD_HARMONISING_POPUP_TITLE]))
MOOD_HARMONISING_FULLSCREEN = Element("mood_harmonising_fullscreen", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[experiences.MOOD_HARMONISING_FULLSCREEN_TITLE], must_not_exist=[experiences.MOOD_HARMONISING_TITLE]))
MOOD_RELAXING = Element("mood_relaxing", ElementByXPathDetectorExtension([experiences.MOOD_RELAXING_TITLE]))
MOOD_RELAXING_POPUP = Element("mood_relaxing_popup", ElementByXPathDetectorExtension([experiences.MOOD_RELAXING_POPUP_TITLE]))
MOOD_RELAXING_FULLSCREEN = Element("mood_relaxing_fullscreen", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[experiences.MOOD_RELAXING_FULLSCREEN_TITLE], must_not_exist=[experiences.MOOD_RELAXING_TITLE]))

MOOD_RELAXING_MODESETTINGS_SETTINGS = Element("mood_relaxing_modesettings_settings", ElementByXPathDetectorExtension([experiences.MOOD_MODESETTINGS_TITLE, experiences.MOOD_RELAXING_MODESETTINGS_SETTINGS_TITLE, experiences.MOOD_RELAXING_MODESETTINGS_ADDITIONALSETTINGS_NOTSELECTED_TITLE]))  # pylint: disable=line-too-long # noqa
MOOD_RELAXING_MODESETTINGS_ADDITIONALSETTINGS = Element("mood_relaxing_modesettings_additionalsettings", ElementByXPathDetectorExtension([experiences.MOOD_MODESETTINGS_TITLE, experiences.MOOD_RELAXING_MODESETTINGS_ADDITIONALSETTINGS_TITLE]))  # pylint: disable=line-too-long # noqa

ENTERTAINMENT_MUSIC_POPUP = Element("entertainment_music_popup", ElementByXPathDetectorExtension([experiences.ENTERTAINMENT_MUSIC_POPUP_TITLE]))
ENTERTAINMENT_MUSIC = Element("entertainment_music", ElementByXPathDetectorExtension([experiences.ENTERTAINMENT_MUSIC_TITLE]))
ENTERTAINMENT_MUSIC_MODESETTINGS_SETTINGS = Element("entertainment_music_modesettings_settings", ElementByXPathBlacklistWhitelistDetectorExtension(
		must_exist=[experiences.ENTERTAINMENT_MUSIC_MODESETTINGS_TITLE, experiences.ENTERTAINMENT_MUSIC_MODESETTINGS_SETTINGS_TITLE],
		must_not_exist=[experiences.MOOD_RELAXING_MODESETTINGS_ADDITIONALSETTINGS_NOTSELECTED_TITLE]))
ENTERTAINMENT_MUSIC_FULLSCREEN = Element("entertainment_music_fullscreen", ElementByXPathDetectorExtension([experiences.ENTERTAINMENT_MUSIC_FULLSCREEN_TITLE]))
ENTERTAINMENT_VIDEO_INFO_POPUP = Element("entertainment_video_info_popup", ElementByXPathDetectorExtension([experiences.ENTERTAINMENT_VIDEO_INFO_POPUP_TITLE]))
ENTERTAINMENT_VIDEO = Element("entertainment_video", ElementByXPathDetectorExtension([experiences.ENTERTAINMENT_VIDEO_TITLE]))

POPUP_MESSAGE = Element("POPUP_message", ElementByXPathDetectorExtension([experiences.POPUP_TITLE]))

CONTEXT = ContextAnalyzer("experiences", AppPackageDetectorExtension(["technology.cariad.interiorexperience", "technology.cariad.interiorexperience.audi.experiences", "technology.cariad.interiorexperience.icc.mqb.audi.experiences"]))
CONTEXT.add_elements_from_module(globals())
