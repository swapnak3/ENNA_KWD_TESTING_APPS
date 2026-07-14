# -*- coding: utf-8 -*-
"""Created on 08.06.2022.

@project: enna_tc_connect_apps_hcp3.
@author: DYX34ZN: Jakob Kein.
"""

import copy

import enna_st12.campaigns


def get_models_alignment():
	"""Get models alignment.

	:return: Alignment
	:rtype: dict
	"""
	alignment = copy.deepcopy(enna_st12.campaigns.ALIGNMENT)
	alignment["Utilities"]["models"].append("enna_kwd_testing.utilities.data_logcat")
	alignment["Utilities"]["models"].append("enna_kwd_testing.utilities.speech")
	alignment["Utilities"]["models"].append("enna_kwd_testing.utilities.speller")
	alignment["PassiveTest"] = {"models": ["enna_kwd_testing.passive.tests.TraceLogger"], "test_process": True}

	return alignment


DEFAULT_ALIGNMENT = get_models_alignment()
