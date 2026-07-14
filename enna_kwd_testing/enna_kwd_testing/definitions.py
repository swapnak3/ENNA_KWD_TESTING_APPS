# -*- coding: utf-8 -*-
"""Created on 23.11.2023.

@project: enna_kwd_testing.
@author: S6FXUOM, Nikolaus Maier.

Contains pathes.
"""
import pathlib

ROOT_PATH = pathlib.Path(__file__).resolve().parent.parent
REPORT_PATH = "."
RESOURCES_PATH = ROOT_PATH / "enna_kwd_testing/resources/"
TEMP_PATH = ROOT_PATH / "enna_kwd_testing/temp/"

RESULT_COLLECTION = []
TESTRUN = 0
META_DATA = {}
ADDITIONAL_INFORMATION = "KWD"
