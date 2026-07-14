# -*- coding: utf-8 -*-
"""Module contains stimulation for touching and checking methods of audi navigation app."""

import enna.core.reporting.interface
import enna.core.component_system.decorators

import enna_st12.instance_names
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
import enna_st12.utilities.menu_navigation.exceptions

import enna_hcp_configuration.android.xpaths.navigation
import enna_hcp_configuration.android.contexts.navigation

import enna_kwd_testing.stimulations.apps._internal
import enna_kwd_testing.utilities.xpath_collection.helper

# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetSatelliteMapState(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation of satellite map in navigation settings."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.navigation.SETTINGS
		self._list_container = enna_hcp_configuration.android.xpaths.navigation.SETTING_LIST
		self._button = enna_hcp_configuration.android.xpaths.navigation.SETTING_GOOLE_SAT_MAP_SWITCH


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetVoiceGuidanceDuringCalls(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation of voice guidance during calls in navigation settings."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.navigation.SETTINGS
		self._list_container = enna_hcp_configuration.android.xpaths.navigation.SETTING_LIST
		self._button = enna_hcp_configuration.android.xpaths.navigation.SETTING_ANNOUNCEMENTS_DURING_CALL_SWITCH


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetManoeuvreDisplayInNavigation(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation of manoeuvre display in navigation settings."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.navigation.SETTINGS
		self._list_container = enna_hcp_configuration.android.xpaths.navigation.SETTING_LIST
		self._button = enna_hcp_configuration.android.xpaths.navigation.SETTING_SHOW_MANEUVER_SWITCH


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetAutomaticUpdatesNavdb(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation of automatic updates navigation settings."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.navigation.SETTINGS_NAVIINFORMATION
		self._list_container = enna_hcp_configuration.android.xpaths.navigation.SETTING_LIST
		self._button = enna_hcp_configuration.android.xpaths.navigation.AUTOMATIC_DATABASE_UPDATE_SWITCH


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckSatelliteMapState(enna_kwd_testing.stimulations.apps._internal.CheckSwitchButtonInScreen):
	"""Check state from the satellite map in navigation settings."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.navigation.SETTINGS
		self._list_container = enna_hcp_configuration.android.xpaths.navigation.SETTING_LIST
		self._button = enna_hcp_configuration.android.xpaths.navigation.SETTING_GOOLE_SAT_MAP_SWITCH


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckVoiceGuidanceDuringCalls(enna_kwd_testing.stimulations.apps._internal.CheckSwitchButtonInScreen):
	"""Check state from the voice guidance during calls in navigation settings."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.navigation.SETTINGS
		self._list_container = enna_hcp_configuration.android.xpaths.navigation.SETTING_LIST
		self._button = enna_hcp_configuration.android.xpaths.navigation.SETTING_ANNOUNCEMENTS_DURING_CALL_SWITCH


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckManoeuvreDisplayInNavigation(enna_kwd_testing.stimulations.apps._internal.CheckSwitchButtonInScreen):
	"""Check state of manoeuvre display in navigation settings."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.navigation.SETTINGS
		self._list_container = enna_hcp_configuration.android.xpaths.navigation.SETTING_LIST
		self._button = enna_hcp_configuration.android.xpaths.navigation.SETTING_SHOW_MANEUVER_SWITCH


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckAutomaticUpdatesNavdb(enna_kwd_testing.stimulations.apps._internal.CheckSwitchButtonInScreen):
	"""Check state of automatic updates in navigation settings."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.navigation.SETTINGS_NAVIINFORMATION
		self._list_container = enna_hcp_configuration.android.xpaths.navigation.SETTING_LIST
		self._button = enna_hcp_configuration.android.xpaths.navigation.AUTOMATIC_DATABASE_UPDATE_SWITCH
