# -*- coding: utf-8 -*-
"""Module contains stimulation for controlling RSI simulation"""
import logging

import enna.core.component_system.decorators
import enna.core.exceptions
import enna.core.interfaces
import enna.data_interfaces.rsi.exceptions
import enna.data_interfaces.rsi.interface

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
from enna_kwd_testing.utilities.rsi.helper import save_rsi_resource_element

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.rsi")
class SetRsiValue(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to set the a service value via rsi data interface."""

	def __init__(self, reporting, rsi: enna.data_interfaces.rsi.interface.Interface):
		"""Initialize keyword stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.rsi.interface.Interface rsi: Instance of rsi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.allowed_parameter_keys = ["SERVICE", "VALUE"]
		self.__rsi = rsi

	def _action(self) -> bool:
		"""Execute action.

		Set a Service value via rsi data interface.

		:return: True if value was set correctly, False otherwise
		:rtype: bool
		"""

		# casting rsi value
		try:
			rsi_service = str(self.values["SERVICE"]).replace(".", "/")
			if self.values["VALUE"] == "None":
				value_to_set = None
			else:
				try:
					value_to_set = int(self.values["VALUE"])
				except ValueError:
					try:
						value_to_set = float(self.values["VALUE"])
					except ValueError:
						value_to_set = self.values["VALUE"]
		except KeyError:
			self._reporting.add_report_message_ta_error("Missing mandatory parameter! SERVICE and VALUE are necessary.")
			return False


		post_service = "/".join(rsi_service.split("/")[:-1])
		payload = {rsi_service.split("/")[-1]: value_to_set} # pylint: disable=use-maxsplit-arg
		MODULE_LOGGER.debug(f"Send post request uri='{post_service}'; payload='{payload}")

		try:
			self.__rsi.post(rsi_uri=post_service, properties=payload)
			current_value = self.__rsi.get(rsi_uri=rsi_service)
		except (enna.core.exceptions.EventNotFoundException, enna.data_interfaces.rsi.exceptions.RSIException) as exception:
			self._reporting.add_report_message_ta_error(f"Error by writing '{value_to_set}' on RSI service '{rsi_service}'! {exception}")
			return False

		if current_value != value_to_set:
			self._reporting.add_report_message_system_error(f"Value {value_to_set} is not set on {rsi_service}! Current value is {current_value}.")
			return False

		self._reporting.add_report_message_pass(f"Service '{rsi_service}' is set to {current_value}.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.rsi")
class DeleteRsiService(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to delete a service value via rsi data interface."""

	def __init__(self, reporting, rsi: enna.data_interfaces.rsi.interface.Interface):
		"""Initialize keyword stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.rsi.interface.Interface rsi: Instance of rsi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__rsi = rsi
		self.allowed_parameter_keys = ["SERVICE", "DELETE_ALL"]

	def _action(self) -> bool:
		"""Execute action.

		Delete a Service value via rsi data interface.

		:return: True if value was set correctly, False otherwise
		:rtype: bool
		"""

		rsi_service = self.values["SERVICE"]
		delete_all = self.values.get("DELETE_ALL", True)

		if delete_all:
			try:
				resources = self.__rsi.get(rsi_service)
				if len(resources) != 0:
					for resource in resources:
						self.__rsi.delete(f"{rsi_service}/{resource['id']}")
						self._reporting.add_report_message_info(f"{resource['id']} deleted")
					self._reporting.add_report_message_pass(f"All '{rsi_service}' deleted")
				else:
					self._reporting.add_report_message_info(f"No elements on '{rsi_service}' which could to be deleted.")
			except (enna.core.exceptions.EventNotFoundException, enna.data_interfaces.rsi.exceptions.RSIException) as exception:
				self._reporting.add_report_message_ta_error(f"Error by deleting service '{rsi_service}'! {exception}")
				return False
		else:
			try:
				rsi_resource = self.__rsi.get(rsi_service)
				save_rsi_resource_element(rsi_resource)
				self.__rsi.delete(rsi_uri=rsi_service)
			except (enna.core.exceptions.EventNotFoundException, enna.data_interfaces.rsi.exceptions.RSIException) as exception:
				self._reporting.add_report_message_ta_error(f"Error by deleting service '{rsi_service}'! {exception}")
				return False

		MODULE_LOGGER.info(f"The Service '{rsi_service}' is deleted.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.rsi")
class CheckRsiValue(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to check a RSI Service."""

	def __init__(self, reporting, rsi: enna.data_interfaces.rsi.interface.Interface):
		"""Initialize keyword stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.rsi.interface.Interface rsi: Instance of rsi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.allowed_parameter_keys = ["SERVICE", "VALUE"]
		self.__rsi = rsi

	def _action(self) -> bool:
		"""Check on value on RSI Service

		:return: True if value was set correctly, False otherwise
		"""

		# casting rsi value
		try:
			rsi_service = str(self.values["SERVICE"]).replace(".", "/")
			try:
				expected_value = int(self.values["VALUE"])
			except ValueError:
				try:
					expected_value = float(self.values["VALUE"])
				except ValueError:
					expected_value = self.values["VALUE"]
		except KeyError:
			self._reporting.add_report_message_ta_error("Missing mandatory parameter! SERVICE and VALUE are necessary.")
			return False
		try:
			current_value = self.__rsi.get(rsi_uri=rsi_service)
		except (enna.core.exceptions.EventNotFoundException, enna.data_interfaces.rsi.exceptions.RSIException) as exception:
			self._reporting.add_report_message_ta_error(f"Error by reading service '{rsi_service}'! {exception}")
			return False

		if isinstance(current_value, dict):
			current_value = current_value.get("name", "unknown-value-by-name")

		if current_value != expected_value:
			self._reporting.add_report_message_system_error(f"Value '{expected_value}' is not equal current value '{current_value}' on service {rsi_service}!")
			return False

		self._reporting.add_report_message_pass(f"Value '{expected_value}' is equal current value '{current_value}' on service {rsi_service}.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.rsi")
class DeleteRsiFieldOnService(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Stimulation of deleting a Filed on RSI service."""

	def __init__(self, reporting, rsi: enna.data_interfaces.rsi.interface.Interface) -> None:
		"""Initialize keyword stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.rsi.interface.Interface rsi: Instance of rsi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.5")
		self.allowed_parameter_keys = ["URL"]
		self.__rsi = rsi

	def _action(self) -> bool:
		"""Delete a field on RSI service
		:return: True if value was set correctly, False otherwise
		"""
		try:
			rsi_property = str(self.values["URL"]).replace(".", "/")
		except KeyError:
			self._reporting.add_report_message_ta_error("Missing mandatory parameter! URL necessary.")
			return False

		service_url = "/".join(rsi_property.split("/")[:-1])
		field = rsi_property.split("/")[-1] # pylint: disable=use-maxsplit-arg

		try:
			self.__rsi.delete(rsi_uri=service_url, fields=[field])
		except (enna.core.exceptions.EventNotFoundException, enna.data_interfaces.rsi.exceptions.RSIException) as error:
			self._reporting.add_report_message_ta_error(f"Could not delete property '{field}' on service '{service_url}'! {error}")
			return False
		self._reporting.add_report_message_pass(f"Property '{field}' on service '{service_url}' is deleted.")
		return True
