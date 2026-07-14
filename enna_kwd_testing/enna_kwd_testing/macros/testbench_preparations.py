# -*- coding: utf-8 -*-
"""Module contains stimulations to apply and remove rsi-workaround"""
import os
import logging

import enna.core.config
import enna.core.component_system.decorators
import enna_kwd_testing.stimulations.base.macro_stim_baseclass
MODULE_LOGGER = logging.getLogger(__name__)

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.base.setup.SetComfortReadyOn")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.base.setup.SetClamp15On")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.base.setup.SetClampSOn")
class Startup(enna_kwd_testing.stimulations.base.macro_stim_baseclass.MacroStimulation):
	"""Class to activate startup testbench"""
	def _action(self, run_sequence: bool = True) -> bool:
		"""Overwrite action for additional info line with testcubename

		:param bool run_sequence: shall the commands waiting in self.sequence be exectued or ignored?
		:return: Merged result of stimulation. True if everything worked as expected, False otherwise
		:rtype: bool
		"""
		self._reporting.add_report_message_info(f"running on TestCube {os.environ.get("TestCubeName")}")
		return super()._action(run_sequence=run_sequence)

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireStimulation(Startup)
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.base.setup.SetDriveModeParking")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.base.setup.SetSystemLanguageToConfigValue")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.base.setup.SetMobileDataOn")
class PrepareHMICampaign(enna_kwd_testing.stimulations.base.macro_stim_baseclass.MacroStimulation):
	"""Class to prepare testbench for hmi campaign"""

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireStimulation(Startup)
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.base.setup.SetDriveModeParking")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.base.setup.SetSystemLanguageEnglish")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.base.setup.SetMobileDataOn")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.base.setup.SetCurrentDate")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.base.setup.SetCurrentTime")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.base.setup.ActivateUsageAutomaticSystemTime")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.base.setup.ActivateUsageAutomaticTimeZone")
class PrepareConnectCampaign(enna_kwd_testing.stimulations.base.macro_stim_baseclass.MacroStimulation):
	"""Class to prepare testbench for connect campaign"""
	def __init__(self, reporting, **kwargs):
		r"""Initialize keyword object.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param dict \**kwargs: for handling stimulations passed via decorator
		"""
		super().__init__(reporting, **kwargs)
		if enna.core.config.INFOTAINMENT_SYSTEM.cluster == 43:
			self.sequence.remove("enna_kwd_testing.stimulations.base.setup.ActivateUsageAutomaticSystemTime")
			self.sequence.remove("enna_kwd_testing.stimulations.base.setup.ActivateUsageAutomaticTimeZone")
		else:
			self.sequence.remove("enna_kwd_testing.stimulations.base.setup.SetCurrentDate")
			self.sequence.remove("enna_kwd_testing.stimulations.base.setup.SetCurrentTime")
