# -*- coding: utf-8 -*-
"""Analyzer for the olb App."""

import enna_hcp_configuration.android.contexts
from enna_hcp_configuration.android.xpaths import olb
from enna_hcp_configuration.android.base import AppPackageDetectorExtension, ContextAnalyzer, ElementByXPathDetectorExtension
from enna_hcp_configuration.common.base import Element

LOADING = Element("loading", ElementByXPathDetectorExtension([olb.LOADING_TITLE]))

SEVEN_DAYS_EDIT = Element("seven_days_edit", ElementByXPathDetectorExtension([olb.SEVEN_DAY_TITLE]))
SEVEN_DAYS_EDIT_SETTINGS = Element("seven_days_edit_settings", ElementByXPathDetectorExtension([olb.SEVEN_DAY_SETTINGS_TITLE]))

STATISTIC = Element("statistic", ElementByXPathDetectorExtension([olb.STATISTIC_UNSELECTED_TITLE]))
STATISTIC_BUSINESS = Element("statistic_business", ElementByXPathDetectorExtension([olb.STATISTIC_BUSINESS_TITLE]))
STATISTIC_PRIVATE = Element("statistic_private", ElementByXPathDetectorExtension([olb.STATISTIC_PRIVATE_TITLE]))
STATISTIC_COMMUTE = Element("statistic_commute", ElementByXPathDetectorExtension([olb.STATISTIC_COMMUTE_TITLE]))
STATISTIC_UNCATEGORIZED = Element("statistic_uncategorized", ElementByXPathDetectorExtension([olb.STATISTIC_UNCATEGORIZED_TITLE]))

SETTINGS = Element("settings", ElementByXPathDetectorExtension([olb.SETTINGS_TITLE]))
SETTINGS_OPEN_SOURCE_SOFTWARE_NOTICE = Element("settings_open_source_software_notice", ElementByXPathDetectorExtension([olb.OPEN_SOURCE_SOFTWARE_NOTICE_TITLE]))

AUTOMATIC_PAUSE_DETECTION = Element("automatic_pause_detection", ElementByXPathDetectorExtension([olb.AUTOMATIC_PAUSE_DETECTION_TITLE]))
GENERIC_ERROR = Element("generic_error", ElementByXPathDetectorExtension([olb.GENERIC_ERROR_TITLE]))
PRIVACY_ERROR = Element("privacy_error", ElementByXPathDetectorExtension([olb.PRIVACY_ERROR_TITLE]))
PRIMARYUSER_ERROR = Element("primaryuser_error", ElementByXPathDetectorExtension([olb.PRIMARYUSER_ERROR_TITLE]))
LICENSE_ERROR = Element("license_error", ElementByXPathDetectorExtension([olb.LICENSE_ERROR_TITLE]))
LOADING_ERROR = Element("loading_error", ElementByXPathDetectorExtension([olb.LOADING_ERROR_TITLE]))


CONTEXT = ContextAnalyzer("olb", AppPackageDetectorExtension(["com.valtech_mobility.olb.audi"]))
CONTEXT.add_elements_from_module(globals())

# Add wait screens for olb
enna_hcp_configuration.android.contexts.WAIT_SCREENS[LOADING.name] = {"wait_time": 30}
