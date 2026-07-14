# -*- coding: utf-8 -*-
"""Analyzer for the launcher app."""

from enna_hcp_configuration.android.base import ContextAnalyzer, ElementByXPathDetectorExtension, AppPackageDetectorExtension
from enna_hcp_configuration.android.xpaths import launcher as xpath_launcher
from enna_hcp_configuration.common.base import Element

HOME = Element("home", ElementByXPathDetectorExtension([xpath_launcher.HOME_BUTTON_SELECTED, xpath_launcher.HOME_SCREEN_DASHBOARD]))
APP_LIST = Element("app_list", ElementByXPathDetectorExtension([xpath_launcher.APP_LIST_CONTAINER]))
CHANGE_SOURCE = Element("change_source", ElementByXPathDetectorExtension(xpath_launcher.MEDIA_SOURCES))

CONTEXT = ContextAnalyzer("launcher", AppPackageDetectorExtension(["de.eso.launcheraudi"]))
CONTEXT.add_elements_from_module(globals())
