# -*- coding: utf-8 -*-
"""Module contains stimulation to demonstrate possible uses of macroStimulation-Class"""
import logging

import enna.core.config
import enna_kwd_testing.stimulations.base.macro_stim_baseclass
import enna_kwd_testing.stimulations.apps.general

MODULE_LOGGER = logging.getLogger(__name__)

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.general.NavigateToScreen")
class FlickerScreen(enna_kwd_testing.stimulations.base.macro_stim_baseclass.MacroStimulation):
	"""Class to demonstrate sequence manipulation including independent values"""
	def _action(self, run_sequence:bool = True) -> bool:
		"""start the required stimulations for enabling/disabling the rsi-Workaround with respect to cluster of Infotainment-System
		
		:param bool run_sequence: shall the commands waiting in self.sequence be exectued or ignored?
		:return: Merged result of stimulation. True if everything worked as expected, False otherwise
		:rtype: bool
		"""
		self.sequence=[
			("enna_kwd_testing.stimulations.apps.general.NavigateToScreen", {"SCREEN_NAME": "launcher.home"}),
			("enna_kwd_testing.stimulations.apps.general.NavigateToScreen", {"SCREEN_NAME": "launcher.app_list"}),
			("enna_kwd_testing.stimulations.apps.general.NavigateToScreen", {"SCREEN_NAME": "launcher.home"}),
			("enna_kwd_testing.stimulations.apps.general.NavigateToScreen", {"SCREEN_NAME": "launcher.app_list"}),
			("enna_kwd_testing.stimulations.apps.general.NavigateToScreen", {"SCREEN_NAME": "launcher.home"}),
			("enna_kwd_testing.stimulations.apps.general.NavigateToScreen", {"SCREEN_NAME": "launcher.app_list"})
		]
		return super()._action()


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.general.NavigateToScreen")
class ConditionalExectuion(enna_kwd_testing.stimulations.base.macro_stim_baseclass.MacroStimulation):
	"""Class to demonstrate sequence manipulation including independent values"""

	def _action(self, run_sequence: bool = True) -> bool:
		"""start the required stimulations for enabling/disabling the rsi-Workaround with respect to cluster of Infotainment-System

		:param bool run_sequence: shall the commands waiting in self.sequence be exectued or ignored?
		:return: Merged result of stimulation. True if everything worked as expected, False otherwise
		:rtype: bool
		"""
		# the following makes no sense, it is just for demonstration purposes
		self.run_if(
			check_sequence=("enna_kwd_testing.stimulations.apps.general.NavigateToScreen", {"SCREEN_NAME": "launcher.home"}),
			run_if_true=("enna_kwd_testing.stimulations.apps.general.NavigateToScreen", {"SCREEN_NAME": "launcher.app_list"}),
			run_if_false=("enna_kwd_testing.stimulations.apps.general.NavigateToScreen", {"SCREEN_NAME": "launcher.home"})
		)
		return super()._action(run_sequence=False)  # run_sequence=False ignores the default sequence built by the constructor
