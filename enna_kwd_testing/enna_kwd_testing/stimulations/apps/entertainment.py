# -*- coding: utf-8 -*-
"""Module contains stimulation for touching and checking methods of entertainment app."""
import enna.core.exceptions
import enna.core.component_system.decorators
import enna.core.reporting.interface

import enna_st12.instance_names
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.data_interfaces.android_hmi.helper
import enna_st12.utilities.menu_navigation.interface

from enna_hcp_configuration.android.contexts import launcher

import enna_kwd_testing.utilities.xpath_collection.helper
import enna_kwd_testing.utilities.xpath_collection.exceptions
import enna_kwd_testing.stimulations.apps._internal
import enna_kwd_testing.stimulations.base.keyword_stim_baseclass



# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetMediaSource(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Stimulation for change a media source in entertainment"""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Constructor of stimulation of change media source.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, menu_navigation=menu_navigation, android_hmi=android_hmi)
		self.allowed_parameter_keys.append("SOURCE")

	def _precondition(self) -> bool:
		"""Navigate to source selection menu.

		:return: True if success, else False
		"""
		return self._go_to_screen(destination=launcher.CHANGE_SOURCE)

	def _action(self) -> bool:
		"""Select a new media source.

		:return: True if success, else false
		"""
		source: str = self.values.get("SOURCE", "Media Source is not set.")
		if source.title() == "Radio":
			source = source.title()
		try:
			xpath_source = f"//*[contains(@text, '{source}')]"
			self._android_hmi.wait_for_element_visible(xpath=xpath_source, max_time=3.0)
			self._android_hmi.click_element(xpath=xpath_source)
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error(f"Media Source '{source}' is not available!")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_ta_error(f"Could not click on '{source}'! {error}")
			return False
		try:
			self._android_hmi.wait_for_event("screen_id", condition=lambda msg: self._android_hmi.screen_id.value != launcher.CHANGE_SOURCE.name, max_time=5.0)
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error(f"Change to source '{source}' is not successful!")
			return False

		self._reporting.add_report_message_pass(f"Source '{source}' is selected!")
		return True
