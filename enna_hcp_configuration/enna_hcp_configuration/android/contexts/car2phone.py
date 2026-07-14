# -*- coding: utf-8 -*-
"""Analyzer for the car2phone app."""

from enna_hcp_configuration.android.xpaths import car2phone
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathBlacklistWhitelistDetectorExtension#, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import Element

MAIN = Element("main", ElementByXPathBlacklistWhitelistDetectorExtension(must_exist=[car2phone.MAIN_TITLE], must_not_exist=[car2phone.INFO_MESSAGE_TEXT]))

CONTEXT = ContextAnalyzer("car2phone", AppPackageDetectorExtension(["technology.cariad.hcp3.car2phone.audi"]))
CONTEXT.add_elements_from_module(globals())
