# -*- coding: utf-8 -*-
"""Contexts for the r2f app (Restore to factory settings)."""

from enna_hcp_configuration.android.base import ContextAnalyzer, ElementByXPathDetectorExtension, AppPackageDetectorExtension
from enna_hcp_configuration.android.xpaths import r2f as xpaths_r2f
from enna_hcp_configuration.common.base import Element


RESTORE_FACTORY_SETTINGS = Element("restore_factory_settings", ElementByXPathDetectorExtension([xpaths_r2f.RESTORE_FACTORY_SETTINGS_TITLE]))

CONTEXT = ContextAnalyzer("r2f", AppPackageDetectorExtension(["de.eso.r2f", "de.eso.r2f.audi"]))
CONTEXT.add_elements_from_module(globals())
