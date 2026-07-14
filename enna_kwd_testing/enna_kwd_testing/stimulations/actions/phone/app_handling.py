# -*- coding: utf-8 -*-
"""Created on 27.05.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.

Contains KWD-Keyword 'START_APP_ON_PHONE'
Contains KWD-Keyword 'STOP_APP_ON_PHONE'
Contains KWD-Keyword 'PUT_PHONE_APP_IN_BACKGROUND_ON_PHONE'
Contains KWD-Keyword 'GO_BACK_ON_PHONE'
"""
import logging

import enna.core.component_system.decorators
import uiautomator2

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
from enna_kwd_testing.utilities.phone import interface

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class StartAppOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Start app by its package-name if it's not already open"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["APP_PACKAGE_NAME"]

	def _action(self) -> bool:
		"""Execute action.

		Start app by its package-name if it's not already open

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		package_name = self.values["APP_PACKAGE_NAME"].lower()

		active_app = self.__phone.get_active_package_name()
		self._reporting.add_report_message_info("Active App: " + active_app)

		if active_app == package_name:
			self._reporting.add_report_message_pass("App already open")
			return True
		else:
			try:
				app_started = self.__phone.start_app_by_package_name(package_name)
			except uiautomator2.exceptions.BaseError as ex:
				self._reporting.add_report_message_ta_error(f"Starting app failed - '{ex}'")
				return False

			if app_started:
				self._reporting.add_report_message_pass("App successfully started")
				return True
			else:
				self._reporting.add_report_message_ta_error("Starting app failed")
				return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class StopAppOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Stop app by its package-name and clear cache if necessary"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["APP_PACKAGE_NAME"]

	def _action(self) -> bool:
		"""Execute action.

		Stop app by its package-name and clear cache if necessary

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		package_name = self.values["APP_PACKAGE_NAME"].lower()

		try:
			clear_cache = self.values["CLEAR_CACHE"].lower() == 'true'
		except KeyError:
			clear_cache = False

		self.__phone.stop_app_by_package_name(package_name, clear_cache)

		status_message = f"App - {package_name} - closed and cache cleared" if clear_cache else f"App - {package_name} - closed"

		self._reporting.add_report_message_pass(status_message)
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class PutAppInBackgroundOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Put the active app in the background by clicking the Android-Home-Button"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = [""]

	def _action(self) -> bool:
		"""Execute action.

		Put the active app in the background by clicking the Android-Home-Button

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		self.__phone.put_app_in_background()

		self._reporting.add_report_message_pass("Put app in background / goto Home-Screen finished")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class GoBackOnPhone(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Click Back-Button of Android-OS"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = [""]

	def _action(self) -> bool:
		"""Execute action.

		Click Back-Button of Android-OS

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		self.__phone.click_back_button()

		self._reporting.add_report_message_pass("Click Back-Button finished")
		return True
