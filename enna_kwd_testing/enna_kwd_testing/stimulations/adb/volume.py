# -*- coding: utf-8 -*-
"""Contains setting ADB commands to read volume."""
import logging
import time

import enna.core.component_system.decorators
import  enna.core.reporting.interface
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass


MODULE_LOGGER = logging.getLogger(__name__)

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class CheckVolumeStep(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Checking current volume settings on domain"""

	def __init__(self, reporting, adb: enna.data_interfaces.adb.interface.Interface):
		"""Initialize stimulation.

		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		"""
		super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.3")
		self.allowed_parameter_keys.append("DOMAIN")
		self.allowed_parameter_keys.append("VALUE")

		self._adb = adb
		self._volume_type_dict = {"ENTERTAINMENT": "android.car.VOLUME_GROUP/0/0", "NAVIGATION": "android.car.VOLUME_GROUP/0/1",
								  "SPRACHEINGABE": "android.car.VOLUME_GROUP/0/2", " TELEFON": "android.car.VOLUME_GROUP/0/3",
								  "SYSTEM": "android.car.VOLUME_GROUP/0/4"}

	def _action(self) -> bool:
		"""Executing checking volume state.

		:return: True if success, else False
		"""
		expected_volume = int(self.values.get("VALUE", -1))
		volume_group = self.values.get("DOMAIN", "UNKNOWN")
		try:
			current_volume = self._get_volume_state_from_domain(domain=volume_group)
			if expected_volume == current_volume:
				self._reporting.add_report_message_pass(f"Current value '{current_volume}' is equal expected value '{expected_volume}'.")
				return True
		except (KeyError, ValueError, enna.data_interfaces.adb.exceptions.ADBException) as error:
			self._reporting.add_report_message_ta_error(f"Could not read current volume of domain '{volume_group}'! {error}")
			return False
		self._reporting.add_report_message_pass(f"Current value '{current_volume}' is not equal expected value '{expected_volume}'!")
		return False

	def _get_volume_state_from_domain(self, domain: str) -> int:
		"""Get current volume value from domain.

		:param domain: name of volume output
		:return: current volume step
		"""
		return int(self._adb.execute_shell_command(f"settings list system | grep {self._volume_type_dict[domain]}", timeout=5.0, stream=False).replace(f"{self._volume_type_dict[domain]}=", ""))


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class SetVolumeStepTo(CheckVolumeStep):
	"""Class containing stimulation to set volume."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface):
		"""Initialize stimulation.

		:param reporting: Instance of reporting interface.
		:param adb: Instance of adb interface
		"""
		super().__init__(reporting=reporting, adb=adb)


	def _action(self) -> bool:
		"""Adjust volume of audio output.

		:return: True if success, else False
		"""
		expected_volume = int(self.values.get("VALUE", -1))
		volume_group = self.values.get("DOMAIN", "UNKNOWN")
		max_tries = 20
		tries = 0
		try: # pylint: disable=too-many-try-statements
			current_volume = self._get_volume_state_from_domain(domain=volume_group)
			if expected_volume == current_volume:
				self._reporting.add_report_message_pass(f"Volume of {volume_group} is already set to {expected_volume}.")
				return True
			self._reporting.add_report_message_warning("Attention: could only adjust volume of focus audio output. If you select a audio output which mot in focus adjust you the wrong audio output.")
			while current_volume != expected_volume:
				if tries > max_tries:
					self._reporting.add_report_message_system_error(f"Could not set volume of {volume_group} to {expected_volume}! Current volume: {current_volume}")
				if current_volume < expected_volume:
					# volume up
					self._adb.execute_shell_command("input keyevent 24")
				else:
					# volume down
					self._adb.execute_shell_command("input keyevent 25")
				time.sleep(0.1)
				current_volume = self._get_volume_state_from_domain(domain=volume_group)
				tries += 1

		except (KeyError, ValueError, enna.data_interfaces.adb.exceptions.ADBException) as error:
			self._reporting.add_report_message_ta_error(f"Could not set volume of domain '{volume_group}'! {error}")
			return False

		self._reporting.add_report_message_pass(f"Volume of {volume_group} is set to {expected_volume}.")
		return True
