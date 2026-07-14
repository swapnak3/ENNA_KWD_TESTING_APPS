# -*- coding: utf-8 -*-
"""Created on 05.09.2023/Update on 06.02.24.

@project: enna_kwd_testing
@author: DYX34ZN: Jakob Kein
@author: SPLATZP: Platzer Pascal

Contains stimulations for keyword driven testing in context of android_hmi screen functions.
"""

import logging

import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna_st12.data_interfaces.android_hmi.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
from enna_kwd_testing.utilities.helper.android_hmi_helper import get_app_and_screen_name_from_screen, wait_till_screen_id_is_visible

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckScreenVisibility(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check if current screen name matches the given screen name."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__android_hmi = android_hmi
		self._reporting = reporting

	def _action(self) -> bool:
		"""Execute action.

		Check if the screen name of the currently displayed screen matches the given screen name.

		1. Get screen id and check if it is equal to the given screen id defined in instance attribute "values" and key "screen_name".

		:return: True if actual screen_id is equal to expected screen_id, False otherwise.
		:rtype: bool
		"""
		str_expected_screen_name = str(self.values["SCREEN_NAME"]).lower()

		str_screen_id = str(wait_till_screen_id_is_visible(str_expected_screen_name, self._reporting, self.__android_hmi))

		if str_screen_id != str_expected_screen_name:
			self._reporting.add_report_message_system_error(f"Current screen_id: '{str_screen_id}' is not equal to expected screen_id: '{str_expected_screen_name}'.")
			return False

		MODULE_LOGGER.info(f"Current screen_id: '{str_screen_id}' is equal to expected screen_id: '{str_expected_screen_name}'.")

		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckScreenNoVisibility(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check if current screen name matches the given screen name."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__android_hmi = android_hmi
		self._reporting = reporting

	def _action(self) -> bool:
		"""Execute action.

		Check if the screen name of the currently displayed screen matches the given screen name.

		1. Get screen id and check if it is equal to the given screen id defined in instance attribute "values" and key "screen_name".

		:return: True if actual screen_id is equal to expected screen_id, False otherwise.
		:rtype: bool
		"""
		str_expected_screen_name = str(self.values["SCREEN_NAME"]).lower()
		app, screen = get_app_and_screen_name_from_screen(self._reporting, self.__android_hmi)
		str_screen_id = f"{app}.{screen}"

		if str_screen_id == str_expected_screen_name:
			self._reporting.add_report_message_system_error(f"Current screen_id: '{str_expected_screen_name}' is still shown'.")
			return False

		MODULE_LOGGER.info(f"Current screen_id: '{str_screen_id}' is not equal to expected screen_id: '{str_expected_screen_name}'.")

		return True
