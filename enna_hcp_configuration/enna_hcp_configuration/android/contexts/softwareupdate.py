# -*- coding: utf-8 -*-
"""Contexts for the softwareupdate app."""

from enna_hcp_configuration.android.base import ContextAnalyzer, ElementByXPathDetectorExtension, AppPackageDetectorExtension
from enna_hcp_configuration.android.xpaths import softwareupdate as xpaths_softwareupdate
from enna_hcp_configuration.common.base import Element


MAIN = Element("main", ElementByXPathDetectorExtension([xpaths_softwareupdate.MAIN_TITLE]))

CONTEXT = ContextAnalyzer("softwareupdate", AppPackageDetectorExtension(["de.eso.audi.softwareupdate"]))
CONTEXT.add_elements_from_module(globals())
