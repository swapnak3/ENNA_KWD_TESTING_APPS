# -*- coding: utf-8 -*-
"""Analyzer for the globalsearch app."""

from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathDetectorExtension
from enna_hcp_configuration.android.xpaths import globalsearch as xpaths_globalsearch
from enna_hcp_configuration.common.base import Element

MAIN = Element("main", ElementByXPathDetectorExtension([xpaths_globalsearch.SEARCH_FIELD_TITLE]))
SETTINGS = Element("settings", ElementByXPathDetectorExtension([xpaths_globalsearch.SETTINGS_TITLE]))

CONTEXT = ContextAnalyzer("globalsearch", AppPackageDetectorExtension(["de.eso.globalsearch"]))
CONTEXT.add_elements_from_module(globals())
