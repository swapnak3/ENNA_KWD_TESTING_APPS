# -*- coding: utf-8 -*-
"""Contexts for the fod app (Functions on demand - Overview of functions)."""

from enna_hcp_configuration.android.base import ContextAnalyzer, ElementByXPathDetectorExtension, AppPackageDetectorExtension
from enna_hcp_configuration.android.xpaths import fod as xpaths_fod
from enna_hcp_configuration.common.base import Element


OVERVIEW_OF_FUNCTIONS = Element("overview_of_functions", ElementByXPathDetectorExtension([xpaths_fod.OVERVIEW_OF_FUNCTIONS_TITLE]))

CONTEXT = ContextAnalyzer("r2f", AppPackageDetectorExtension(["de.eso.audi.fod"]))
CONTEXT.add_elements_from_module(globals())
