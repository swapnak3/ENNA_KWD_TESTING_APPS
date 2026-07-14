# -*- coding: utf-8 -*-
"""Module contains stimulations to apply and remove rsi-workaround"""
import logging

import enna.core.config
import enna.core.component_system.decorators
import enna_kwd_testing.stimulations.base.macro_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)


class _CoreservicesMagicSwitch(enna_kwd_testing.stimulations.base.macro_stim_baseclass.MacroStimulation):
	"""select between core service and magic service according to cluster"""
	def __init__(self, reporting, **kwargs):
		r"""Initialize keyword object.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param dict \**kwargs: for handling stimulations passed via decorator
		"""
		super().__init__(reporting, **kwargs)
		self.sequence.pop(1 if enna.core.config.INFOTAINMENT_SYSTEM.cluster in {43, 46} else 0)

	def _action(self, _run_sequence:bool = True) -> bool:
		"""select between core service and magic service according to cluster

		:return: result of the selected stimulation
		:rtype: bool
		"""
		# hand over the given values if the selected class has a values attribute
		stim = self.kwd_instances[self.sequence[0]]
		if hasattr(stim,"values"):
			self.default_values[self.sequence[0]] = self.values
		return super()._action()

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.core_services.CheckApn1", arg_name="cs")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.magic_services.CheckApn1", arg_name="m")
class CheckApn1(_CoreservicesMagicSwitch):
	"""selects between Core Services and Magic Services stimulation"""

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.core_services.CheckApn2", arg_name="cs")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.magic_services.CheckApn2", arg_name="m")
class CheckApn2(_CoreservicesMagicSwitch):
	"""selects between Core Services and Magic Services stimulation"""

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.core_services.SetCoreServicesSave", arg_name="cs")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.magic_services.SetCoreServicesSave", arg_name="m")
class SetCoreServicesSave(_CoreservicesMagicSwitch):
	"""selects between Core Services and Magic Services stimulation"""

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.core_services.CheckServiceIdStateDisableReasons", arg_name="cs")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.magic_services.CheckServiceIdStateDisableReasons", arg_name="m")
class CheckServiceIdStateDisableReasons(_CoreservicesMagicSwitch):
	"""selects between Core Services and Magic Services stimulation"""

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.core_services.SetVinInCoreServices", arg_name="cs")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.magic_services.SetVinInCoreServices", arg_name="m")
class SetVinInCoreServices(_CoreservicesMagicSwitch):
	"""selects between Core Services and Magic Services stimulation"""

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.core_services.CheckVinInCoreServices", arg_name="cs")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.magic_services.CheckVinInCoreServices", arg_name="m")
class CheckVinInCoreServices(_CoreservicesMagicSwitch):
	"""selects between Core Services and Magic Services stimulation"""

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.core_services.CheckServiceIdLicenseState", arg_name="cs")
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.magic_services.CheckServiceIdLicenseState", arg_name="m")
class CheckServiceIdLicenseState(_CoreservicesMagicSwitch):
	"""selects between Core Services and Magic Services stimulation"""
