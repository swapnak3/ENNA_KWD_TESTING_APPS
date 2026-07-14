# -*- coding: utf-8 -*-
"""Module contains to Service list States from esotrace logger."""
import logging

import enna.core.config
import enna.core.exceptions
import enna.core.interfaces
import enna.core.interfaces.server
import enna.core.component_system.decorators

import enna.data_interfaces.esotrace.interface

import enna_kwd_testing.utilities.service_list_states.interface


MODULE_LOGGER = logging.getLogger(__name__)



@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.esotrace", instance_name="ivi")
class Server(enna_kwd_testing.utilities.service_list_states.interface.Interface, enna.core.interfaces.server.Server):
	"""Server of reading service interface states from esotrace."""

	def __init__(self, esotrace: enna.data_interfaces.esotrace.interface.Interface, instance_name: str = "server") -> None:
		"""Instance server of reading service list.

		:param esotrace: instance of interface to streaming traces
		:param instance_name: name of that instance
		"""
		enna_kwd_testing.utilities.service_list_states.interface.Interface.__init__(self)
		enna.core.interfaces.server.Server.__init__(self, instance_name=instance_name)
		self._trace = esotrace
		self._trace.register("APN1_STATE", self.__update_apn1)
		self._trace.register("APN2_STATE", self.__update_apn2)
		self._trace.register("IGNITESTORE_V1", self.__update_disable_reason_ignite_store)
		self._trace.register("ICO_V1", self.__update_disable_reason_ico)
		self._trace.register("OBB_V1", self.__update_disable_reason_obb)
		self._trace.register("OLB_V1", self.__update_disable_reason_olb)
		self._trace.connect()
		self._set_online()

	def __update_apn1(self, msg: enna.core.interfaces.Data[enna.data_interfaces.esotrace.EsotraceMessage]) -> None:
		"""Update of state from apn1.

		:param msg: message from trace
		"""
		state: str = msg.value.meta_data.extracted_parameters.get("state", "UNKNOWN")
		if state == "CONNECTED":
			self._apn1 = enna.core.interfaces.Data(True)
		else:
			self._apn1 = enna.core.interfaces.Data(False)
		self._signal_property("apn1", self.apn1)
		MODULE_LOGGER.debug(f"Updated from message: '{msg.value.message_data}'")

	def __update_apn2(self, msg: enna.core.interfaces.Data[enna.data_interfaces.esotrace.EsotraceMessage]) -> None:
		"""Update of state from apn2.

		:param msg: message from trace
		"""
		state: str = msg.value.meta_data.extracted_parameters.get("state", "UNKNOWN")
		if state == "CONNECTED":
			self._apn2 = enna.core.interfaces.Data(True)
		else:
			self._apn2 = enna.core.interfaces.Data(False)
		self._signal_property("apn2", self.apn2)
		MODULE_LOGGER.debug(f"Updated from message: '{msg.value.message_data}'")

	@staticmethod
	def __get_disable_reason(msg: enna.core.interfaces.Data[enna.data_interfaces.esotrace.EsotraceMessage]) -> str:
		"""Get disable reason from trace message.

		:param msg: message from trace
		:return: disable reason
		"""
		MODULE_LOGGER.debug(f"Update disable reason: '{msg.value.message_data}'")
		if msg.value.meta_data.extracted_parameters.get("license", "") != "":
			MODULE_LOGGER.debug("Detect a license disable reason!")
			return "license error"
		if msg.value.meta_data.extracted_parameters.get("backend", "") != "":
			MODULE_LOGGER.debug("Detect a backend disable reason!")
			return "backend error"
		if msg.value.meta_data.extracted_parameters.get("configuration", "") != "":
			MODULE_LOGGER.debug("Detect a configuration disable reason!")
			return "configuration error"
		if msg.value.meta_data.extracted_parameters.get("connectivity", "") != "":
			MODULE_LOGGER.debug("Detect a connectivity disable reason!")
			return "connectivity error"
		MODULE_LOGGER.debug("No disable reason for this service.")
		return ""

	def __update_disable_reason_ignite_store(self, msg: enna.core.interfaces.Data[enna.data_interfaces.esotrace.EsotraceMessage]) -> None:
		"""Update of disabled/enabled state from service 'ignite_store'.

		:param msg: message from trace
		"""
		disable_reason: str = self.__get_disable_reason(msg)
		if disable_reason == "":
			self._ignitestore_v1 = enna.core.interfaces.Data(True)
		else:
			self._ignitestore_v1 = enna.core.interfaces.Data(False)
		self._signal_property("ignitestore_v1", self.ignitestore_v1)

	def __update_disable_reason_ico(self, msg: enna.core.interfaces.Data[enna.data_interfaces.esotrace.EsotraceMessage]) -> None:
		"""Update of disabled/enabled state from service 'ico_v1'.

		:param msg: message from trace
		"""
		disable_reason: str = self.__get_disable_reason(msg)
		if disable_reason == "":
			self._ico_v1 = enna.core.interfaces.Data(True)
		else:
			self._ico_v1 = enna.core.interfaces.Data(False)
		self._signal_property("ico_v1", self.ico_v1)

	def __update_disable_reason_obb(self, msg: enna.core.interfaces.Data[enna.data_interfaces.esotrace.EsotraceMessage]) -> None:
		"""Update of disabled/enabled state from service 'obb_v1'.

		:param msg: message from trace
		"""
		disable_reason: str = self.__get_disable_reason(msg)
		if disable_reason == "":
			self._obb_v1 = enna.core.interfaces.Data(True)
		else:
			self._obb_v1 = enna.core.interfaces.Data(False)
		self._signal_property("obb_v1", self.obb_v1)

	def __update_disable_reason_olb(self, msg: enna.core.interfaces.Data[enna.data_interfaces.esotrace.EsotraceMessage]) -> None:
		"""Update of disabled/enabled state from service 'olb_v1'.

		:param msg: message from trace
		"""
		disable_reason: str = self.__get_disable_reason(msg)
		if disable_reason == "":
			self._olb_v1 = enna.core.interfaces.Data(True)
		else:
			self._olb_v1 = enna.core.interfaces.Data(False)
		self._signal_property("olb_v1", self.olb_v1)
