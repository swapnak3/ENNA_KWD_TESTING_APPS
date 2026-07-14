# -*- coding: utf-8 -*-
"""Module contains stimulation for basic setup of test run."""
import enna.core.config
import enna.core.component_system.decorators
import enna.core.reporting.interface

import enna_st12.instance_names
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface

import enna_kwd_testing.utilities.vehicle.interface

import enna_kwd_testing.stimulations.apps.privacy
import enna_kwd_testing.stimulations.apps.settings
import enna_kwd_testing.stimulations.actions.android_hmi.time
import enna_kwd_testing.stimulations.vehicle.simulation


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetSystemLanguageEnglish(enna_kwd_testing.stimulations.apps.settings.SetSystemLanguage):
	"""Set System language to english."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Constructor of Stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, android_hmi, menu_navigation)
		self.values = {"LANG": "en_GB"}


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetSystemLanguageGerman(enna_kwd_testing.stimulations.apps.settings.SetSystemLanguage):
	"""Set System language to german."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi:  enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Constructor of Stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, android_hmi, menu_navigation)
		self.values = {"LANG": "de_DE"}

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetSystemLanguageToConfigValue(enna_kwd_testing.stimulations.apps.settings.SetSystemLanguage):
	"""Set System language to german."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi:  enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Constructor of Stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, android_hmi, menu_navigation)
		self.values = {"LANG": enna.core.config.INFOTAINMENT_SYSTEM.system_language.value}


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.vehicle")
class SetComfortReadyOn(enna_kwd_testing.stimulations.vehicle.simulation.SwitchComfortReady):
	"""Set ComfortReady signal to true."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, vehicle: enna_kwd_testing.utilities.vehicle.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: Instance of reporting interface.
		:param vehicle: instance of interface for vehicle simulation
		"""
		super().__init__(reporting=reporting, vehicle=vehicle)
		self.values = {"STATE": True}


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.vehicle")
class SetClamp15On(enna_kwd_testing.stimulations.vehicle.simulation.SwitchClamp15):
	"""Set Clamp 15 signal to true."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, vehicle: enna_kwd_testing.utilities.vehicle.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: Instance of reporting interface.
		:param vehicle: instance of interface for vehicle simulation
		"""
		super().__init__(reporting=reporting, vehicle=vehicle)
		self.values = {"STATE": True}


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.vehicle")
class SetClampSOn(enna_kwd_testing.stimulations.vehicle.simulation.SwitchClampS):
	"""Set Clamp S signal to true."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, vehicle: enna_kwd_testing.utilities.vehicle.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: Instance of reporting interface.
		:param vehicle: instance of interface for vehicle simulation
		"""
		super().__init__(reporting=reporting, vehicle=vehicle)
		self.values = {"STATE": True}


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.vehicle")
class SetDriveModeParking(enna_kwd_testing.stimulations.vehicle.simulation.SetDriveMode):
	"""Set vehicle in parking mode. Set vehicle speed to 0m/s. Set gear selection to parking."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, vehicle: enna_kwd_testing.utilities.vehicle.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: Instance of reporting interface.
		:param vehicle: Instance of car interface
		"""
		super().__init__(reporting=reporting, vehicle=vehicle)
		self.values = {"GEAR": "PARKING", "SPEED_IN_M_PER_S": 0}


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetMobileDataOn(enna_kwd_testing.stimulations.apps.privacy.SetMobileData):
	"""Switch mobile data to ON."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Constructor of Stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, android_hmi, menu_navigation)
		self.values = {"STATE": True}


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetCurrentDate(enna_kwd_testing.stimulations.actions.android_hmi.time.SetSpecificDateInSystem):
	"""Set current date in System."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Constructor of Stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, android_hmi, menu_navigation)
		self.values = {"DATE": "TODAY"}


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetCurrentTime(enna_kwd_testing.stimulations.actions.android_hmi.time.SetCurrentTime):
	"""Set current time in System."""
	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Constructor of Stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, android_hmi, menu_navigation)
		self.values = {"HOUR": "NOW", "MINUTE": "NOW"}


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class ActivateUsageAutomaticSystemTime(enna_kwd_testing.stimulations.apps.settings.SetAutomaticSystemTime):
	"""Activate usage automatic system time. (use GPS time signal.)"""
	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Constructor of Stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, android_hmi, menu_navigation)
		self.values = {"STATE": True}


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",
														instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class ActivateUsageAutomaticTimeZone(enna_kwd_testing.stimulations.apps.settings.SetAutomaticTimeZone):
	"""Activate usage automatic time zone detection. (use GPS position.)"""
	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Constructor of Stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, android_hmi, menu_navigation)
		self.values = {"STATE": True}
