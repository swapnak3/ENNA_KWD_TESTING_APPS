# -*- coding: utf-8 -*-
"""Analyzer for the Android Engineering Menu."""

from enna_hcp_configuration.android.xpaths import aem
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import Element

AEM_ECALL_SETTINGS = Element("aem_ecall_settings", ElementByXPathDetectorExtension([aem.ECALL_TEST_MENU_TITLE]))

CONTEXT = ContextAnalyzer("aem_emergencycall", AppPackageDetectorExtension(["de.eso.emergencycall"]))

CONTEXT.add_elements_from_module(globals())
