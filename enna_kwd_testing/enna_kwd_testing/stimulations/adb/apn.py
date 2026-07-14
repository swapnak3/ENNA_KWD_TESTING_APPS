# -*- coding: utf-8 -*-
"""Created on 25.11.2024.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Teubner Claus.

Contains stimulations for keyword driven testing in context of APN1 / APN2 state.
"""

import logging

import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface
import enna.utilities.diagnosis.helper
from enna.data_interfaces.adb.exceptions import ADBException

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)


class _SetAPN(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Activation or Deactivation APN Connection. For deactivation change Firewall to block APN Connection.
	Write Firewall to origin for activation
	"""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface) -> None:
		"""Constructor of Setting APN Firewall.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of android debug bridge interface
		"""
		super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.3")
		self.__adb = adb
		self.allowed_parameter_keys = ["STATE"]
		self._max_time: float = 10.0
		self._apn_number: int = 0


	def _activation(self) -> bool:
		"""Activation APN

		:return: Get true if success, else false
		"""
		try:
			self.__adb.execute_shell_command(command="iptables -D INPUT 1", timeout=self._max_time)
			self.__adb.execute_shell_command(command="iptables -D OUTPUT 1", timeout=self._max_time)
			self.__adb.execute_shell_command(command="ip6tables -D INPUT 1", timeout=self._max_time)
			self.__adb.execute_shell_command(command="ip6tables -D OUTPUT 1", timeout=self._max_time)
			# workaround for endless loading screen of
			# self.__adb.execute_shell_command(command="am force-stop com.valtech_mobility.obb.audi", timeout=self._max_time)
		except ADBException as error:
			MODULE_LOGGER.error(f"Exception: {str(error)}")
			self._reporting.add_report_message_ta_error("Could not activation APN Connection! Firewall is not reset.")
			return False
		self._reporting.add_report_message_pass("Firewall is reset. APN Connections allowed.")
		return True

	def _deactivation(self) -> bool:
		"""Deactivation APN Connection with expected number.

		:return: Get true if success, else false
		"""
		try:
			self.__adb.execute_shell_command(command=f"iptables -I INPUT 1 -i l2tp-apn{self._apn_number} -j DROP", timeout=self._max_time)
			self.__adb.execute_shell_command(command=f"iptables -I OUTPUT 1 -o l2tp-apn{self._apn_number} -j DROP", timeout=self._max_time)
			self.__adb.execute_shell_command(command=f"ip6tables -I INPUT 1 -i l2tp-apn{self._apn_number} -j DROP", timeout=self._max_time)
			self.__adb.execute_shell_command(command=f"ip6tables -I OUTPUT 1 -o l2tp-apn{self._apn_number} -j DROP", timeout=self._max_time)
		except ADBException as error:
			MODULE_LOGGER.error(f"Exception: {str(error)}")
			self._reporting.add_report_message_ta_error(f"Could not deactivation of APN{self._apn_number} Connection! Disconnecting was not successful.")
			return False
		self._reporting.add_report_message_pass(f"Connection of APN{self._apn_number} is blocked by firewall.")
		return True

	def _action(self) -> bool:
		"""Execute Firewall changes.

		:return: Get true if success, else false
		"""
		if not self.values["STATE"]:
			return self._deactivation()
		return self._activation()


@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class SetApn1(_SetAPN):
	"""De/Activate APN1 connection with adb shell and firewall iptables commands."""

	def __init__(self, reporting, adb) -> None:
		"""Constructor of De/Activation APN1 with adb shell and firewall iptables commands.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of android debug bridge
		"""
		super().__init__(reporting=reporting, adb=adb)
		self._apn_number = 0


@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
class SetApn2(_SetAPN):
	"""De/Activate APN2 connection with adb shell and firewall iptables commands."""

	def __init__(self, reporting, adb) -> None:
		"""Constructor of De/Activation APN2 with adb shell and firewall iptables commands.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of android debug bridge
		"""
		super().__init__(reporting=reporting, adb=adb)
		self._apn_number = 1
