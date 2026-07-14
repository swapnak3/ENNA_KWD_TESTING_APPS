# -*- coding: utf-8 -*-
"""Analyzer for the dataplan App."""

from enna_hcp_configuration.android.xpaths import dataplan
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import Element

MAIN = Element("main", ElementByXPathDetectorExtension([dataplan.MAIN_TITLE]))

CONTEXT = ContextAnalyzer("dataplan", AppPackageDetectorExtension(["de.eso.audi.dataplan"]))
CONTEXT.add_elements_from_module(globals())
