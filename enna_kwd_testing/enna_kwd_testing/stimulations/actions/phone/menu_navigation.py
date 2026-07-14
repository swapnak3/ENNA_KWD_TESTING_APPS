# -*- coding: utf-8 -*-
"""Created on 21.05.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.

Contains KWD-Keyword 'NAVIGATE_TO_SCREEN_ON_PHONE'
"""
import logging

import enna.core.component_system.decorators
import enna.core.exceptions

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
from enna_kwd_testing.utilities.phone import interface
from enna_kwd_testing.utilities.phone.exceptions import NoVehicleDefinedException
from enna_kwd_testing.utilities.phone.myaudi import runtime_storage
from enna_kwd_testing.utilities.phone.myaudi.frontend import screens

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class NavigateToScreenOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to navigate to screen on phone."""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["APP_SCREEN_NAME"]

	def _action(self) -> bool:
		"""Execute action.

		Navigate to screen which is defined in SCREEN_LIST in file: [phone.myaudi.frontend.screens].

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""

		app_screen_name = self.values["APP_SCREEN_NAME"].upper()

		vehicle = runtime_storage.USED_VEHICLE

		if vehicle is None:
			raise NoVehicleDefinedException("Vehicle is not defined - Vehicle must be set via Keyword (PRE_SET_VIN_ON_PHONE) in Precondition")

		try:
			self.__phone.select_screen(screens.SCREEN_LIST[app_screen_name].get(VIN=vehicle.vin))

			self._reporting.add_report_message_pass(f"Successfully navigate to screen {app_screen_name}")
			return True
		except KeyError:
			self._reporting.add_report_message_ta_error(f"Navigate to Screen failed / Screen Name '{app_screen_name}' not available")
			return False
