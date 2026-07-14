# -*- coding: utf-8 -*-
"""Created on 08.08.2024.

@project: enna_kwd_testing.
@author: WZ40Y0R: Simon Schmidt.

Contains KWD-Keyword 'SPEED_ALERT_ACTIVATE_PROFILE'
Contains KWD-Keyword 'SPEED_ALERT_DEACTIVATE_PROFILE'
Contains KWD-Keyword 'SPEED_ALERT_TRIGGER_VIOLATION'
Contains KWD-Keyword 'GEOFENCE_ALERT_ACTIVATE_PROFILE'
Contains KWD-Keyword 'GEOFENCE_ALERT_DEACTIVATE_PROFILE'
Contains KWD-Keyword 'GEOFENCE_ALERT_TRIGGER_VIOLATION'
Contains KWD-Keyword 'VALET_ALERT_ACTIVATE_PROFILE'
Contains KWD-Keyword 'VALET_ALERT_DEACTIVATE_PROFILE'
Contains KWD-Keyword 'VALET_ALERT_ACTIVATE_PROFILE_RESPOND_WITH_ERROR'
Contains KWD-Keyword 'VALET_ALERT_DEACTIVATE_PROFILE_RESPOND_WITH_ERROR'
Contains KWD-Keyword 'VALET_ALERT_TRIGGER_SPEED_VIOLATION'
Contains KWD-Keyword 'VALET_ALERT_TRIGGER_GEOFENCE_VIOLATION'
"""

import datetime
import logging

import enna.core.component_system.decorators
import enna.data_interfaces.adb.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
from enna_kwd_testing.utilities.phone import interface
from enna_kwd_testing.utilities.phone.myaudi import runtime_storage

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class SpeedAlertActivateProfile(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to activate a new speed alert profile"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Activate Speed alert Profile

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			vehicle.speedalert_service.jobs.response_to_profile_activation_job()

			self._reporting.add_report_message_pass(f"Activate Speed Alert Profile (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Activate Speed Alert Profile (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class SpeedAlertDeactivateProfile(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to deactivate an existing speed alert profile"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Deactivate Speed alert Profile

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			vehicle.speedalert_service.jobs.response_to_profile_deactivation_job()

			self._reporting.add_report_message_pass(f"Deactivate Speed Alert Profile (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Deactivate Speed Alert Profile (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class SpeedAlertTriggerViolation(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to start violation for a speed alert profile"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Start Violation

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			alert_state = self.values["STATE"].upper()

			vehicle.speedalert_service.violations.trigger_violation(alert_state)

			self._reporting.add_report_message_pass(f"Start violation for a speed alert profile (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Start violation for a speed alert profile (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class GeofenceAlertActivateProfile(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to activate a new geofence alert profile"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Activate Geofence alert Profile

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			vehicle.geofencealert_service.jobs.response_to_profile_activation_job()

			self._reporting.add_report_message_pass(f"Activate Geofence Alert Profile (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Activate Geofence Alert Profile (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class GeofenceAlertDeactivateProfile(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to deactivate an existing geofence alert profile"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Deactivate Geofence alert Profile

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			vehicle.geofencealert_service.jobs.response_to_profile_deactivation_job()

			self._reporting.add_report_message_pass(f"Deactivate Geofence Alert Profile profile (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Deactivate Geofence Alert Profile profile (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class GeofenceAlertTriggerViolation(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to start violation for a geofence alert profile"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["EVENT_TYPE"]

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Start Violation

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			event_type = self.values["EVENT_TYPE"].upper()

			vehicle.geofencealert_service.violations.trigger_violation(event_type)

			self._reporting.add_report_message_pass(f"Start violation for a geofence alert profile (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Start violation for a geofence alert profile (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ValetAlertActivateProfile(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to activate the valet alert"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Activate Valet Alert

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			vehicle.valetalert_service.jobs.response_to_profile_activation_job()

			self._reporting.add_report_message_pass(f"Activate Valet Alert (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Activate Valet Alert (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ValetAlertDeactivateProfile(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to deactivate the valet alert"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Deactivate Valet Alert

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			vehicle.valetalert_service.jobs.response_to_profile_deactivation_job()

			self._reporting.add_report_message_pass(f"Deactivate Valet Alert (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Deactivate Valet Alert (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ValetAlertActivateProfileRespondWithError(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality respond to the valet alert profile activation with an error"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["ERROR"]

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Respond with error

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			error = self.values["ERROR"].upper()

			vehicle.valetalert_service.jobs.response_to_profile_activation_job_with_error(error)

			self._reporting.add_report_message_pass(f"Respond to the valet alert profile activation with an error (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Respond to the valet alert profile activation with an error (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ValetAlertDeactivateProfileRespondWithError(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality respond to the valet alert profile deactivation with an error"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["ERROR"]

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Respond with error

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			error = self.values["ERROR"].upper()

			vehicle.valetalert_service.jobs.response_to_profile_deactivation_job_with_error(error)

			self._reporting.add_report_message_pass(f"Respond to the valet alert profile deactivation with an error (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Respond to the valet alert profile deactivation with an error (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ValetAlertTriggerSpeedViolation(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to start speed violation for the valet alert profile"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["STATE"]

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Start Speed Violation

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			alert_state = self.values["STATE"].upper()

			vehicle.valetalert_service.violations.trigger_speed_violation(alert_state)

			self._reporting.add_report_message_pass(f"Start Speed violation for the Valet Alert (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Start Speed violation for the Valet Alert (Action) failed with reason: {exc}")
			return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_kwd_testing.utilities.phone")
class ValetAlertTriggerGeofenceViolation(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to start geofence violation for the valet alert profile"""

	def __init__(self, reporting, phone: enna_kwd_testing.utilities.phone.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param  enna_kwd_testing.utilities.phone.Interface phone: phone interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.3")
		self.__phone = phone
		self.allowed_parameter_keys = ["EVENT_TYPE"]

	def _action(self) -> bool:
		"""Execute action.

		1. Get Vehicle from Factory
		2. Start Geofence Violation

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		try:
			vehicle = runtime_storage.USED_VEHICLE

			event_type = self.values["EVENT_TYPE"].upper()

			vehicle.valetalert_service.violations.trigger_geofence_violation(event_type)

			self._reporting.add_report_message_pass(f"Start Geofence violation for the Valet Alert (Action) successful")
			return True
		except Exception as exc:
			self._reporting.add_report_message_ta_error(f"Start Geofence violation for the Valet Alert (Action) failed with reason: {exc}")
			return False
