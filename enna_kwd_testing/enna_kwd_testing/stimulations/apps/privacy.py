# -*- coding: utf-8 -*-
"""Module contains stimulation for touching and checking methods of privacy setup."""
import enna.core.component_system.decorators
import enna.core.reporting.interface

import enna_st12.instance_names
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface

import enna_hcp_configuration.android.contexts.privacy
import enna_hcp_configuration.android.xpaths.privacy

import enna_kwd_testing.stimulations.apps._internal


# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetMobileData(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation mobile data connection (privacy)."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.privacy.PRIVACY_SETTINGS
		self._list_container = enna_hcp_configuration.android.xpaths.privacy.MAIN_LIST
		self._button = enna_hcp_configuration.android.xpaths.privacy.SETTING_MOBILE_DATA

# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckMobileData(enna_kwd_testing.stimulations.apps._internal.CheckSwitchButtonInScreen):
	"""check mobile data connection (privacy)."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.privacy.PRIVACY_SETTINGS
		self._list_container = enna_hcp_configuration.android.xpaths.privacy.MAIN_LIST
		self._button = enna_hcp_configuration.android.xpaths.privacy.SETTING_MOBILE_DATA


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetLocationForVehicleRelatedOnlineServices(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation using location data for online connection."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.privacy.PRIVACY_SETTINGS
		self._list_container = enna_hcp_configuration.android.xpaths.privacy.MAIN_LIST
		self._button = enna_hcp_configuration.android.xpaths.privacy.SETTING_LOCATION_DATA
