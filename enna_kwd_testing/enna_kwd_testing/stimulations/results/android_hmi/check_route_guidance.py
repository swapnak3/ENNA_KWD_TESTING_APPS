# -*- coding: utf-8 -*-
"""Created on 09.10.2023.

@project: enna_kwd_testing.
@author: S6FXUOM, Nikolaus Maier.

Contains stimulations for KWD-TA in context of android_hmi sds settings functions.
"""

import logging

import enna.core.component_system.decorators
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import navigation as navigation_contexts

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckRouteGuidanceState(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check route guidance state in navigation."""

	def __init__(self, reporting, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self.__menu_navigation = menu_navigation
		self._parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Execute action.

		Check route guidance state with HMI.

		1. Check route guidance state with HMI

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		rg_state_new = str(self.values["STATE"])
		if rg_state_new == "ACTIVATED":
			if not wrapper_android_hmi.go_to_screen(navigation_contexts.GUIDANCE, self._reporting, self.__menu_navigation, retries=1):
				MODULE_LOGGER.error("Could not go to screen: 'Navigation App -> navigation.guidance. Route Guidance not active or graph issue.")
				return False
			rg_state_new = True
		elif rg_state_new == "DEACTIVATED":
			if wrapper_android_hmi.go_to_screen(navigation_contexts.GUIDANCE, self._reporting, self.__menu_navigation, retries=1):
				MODULE_LOGGER.error("Could go to screen: 'Navigation App -> navigation.guidance. Route Guidance active or graph issue.")
				return False
			rg_state_new = True
		else:
			MODULE_LOGGER.error(
				f"Wrong parameter for STATE:'{rg_state_new}', should be 'ACTIVATED' or 'DEACTIVATED")
			return False

		return rg_state_new
