# -*- coding: utf-8 -*-
"""Module contains stimulations to apply and remove rsi-workaround"""
import logging

import enna.core.config
import enna.core.component_system.decorators
import enna_kwd_testing.stimulations.base.macro_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.remount.EnablingRemount")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.change_configs.ModifyCommAccess")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.change_configs.ModifyFramework")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.change_configs.ModifyGateway")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.change_configs.ModifyNetwork")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.change_configs.ModifyRudiRegistry")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.remount.Restart")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.firewall.DeactivationFirewall")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.register.RegistryRSI")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.register.SetTimeOnRSI")
class WorkaroundActivate(enna_kwd_testing.stimulations.base.macro_stim_baseclass.MacroStimulation):
	"""Class to activate rsi-Workaround"""
	def __init__(self, reporting, **kwargs):
		r"""Initialize keyword object.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param dict \**kwargs: for handling stimulations passed via decorator
		"""
		super().__init__(reporting, **kwargs)
		if enna.core.config.INFOTAINMENT_SYSTEM.cluster in {43, 46}:
			self.sequence.remove("enna_kwd_testing.workarounds.rsi.change_configs.ModifyNetwork")
		else:
			self.sequence.remove("enna_kwd_testing.workarounds.rsi.change_configs.ModifyGateway")

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.change_configs.OriginalCommAccess")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.change_configs.OriginalFramework")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.change_configs.OriginalGateway")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.change_configs.OriginalNetwork")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.change_configs.OriginalRudiRegistry")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.workarounds.rsi.remount.DisablingRemount")
class WorkaroundDeactivate(enna_kwd_testing.stimulations.base.macro_stim_baseclass.MacroStimulation):
	"""Class to deactivate rsi-Workaround"""
