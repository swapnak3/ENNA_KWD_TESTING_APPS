# -*- coding: utf-8 -*-
"""Module contains stimulation for reading configuration of ECUs."""
import abc
import logging
import os

import enna.core.config
import enna.core.component_system.decorators
import enna.core.interfaces.testing
import enna.utilities.diagnosis.helper
import enna_kwd_testing.definitions

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.utilities.diagnosis")
class ReadingMainUnit(enna.core.interfaces.testing.Stimulation, metaclass=abc.ABCMeta):
	"""Class reading configuration of main unit."""

	def __init__(self, reporting, diagnosis):
		"""Constructor of stimulation for reading main unit configuration.

		:param enna.core.reporting.interface.Interface reporting: instance of report handler
		:param enna.utilities.diagnosis.interface.Interface diagnosis: instance of diagnosis interface
		"""
		super().__init__(reporting)
		self.__diagnosis = diagnosis
		self.__ecu_address = 0x5F
		self.__icc_sw_address = 0x8125
		self.__diagnosis.wait_for_online(max_time=60)
		enna_kwd_testing.definitions.REPORT_PATH = self._reporting.report_path.value
		MODULE_LOGGER.info(f"Path to Reporting Files: {enna_kwd_testing.definitions.REPORT_PATH}")

	def _action(self) -> bool:
		"""Read main unit configuration.

		:return: state of execution
		:rtype: bool
		"""
		self._reporting.attach_meta_data_to_report({"order": enna_kwd_testing.definitions.META_DATA.get("testorder", "unknown")})
		self._reporting.attach_meta_data_to_report({"department": enna_kwd_testing.definitions.META_DATA.get("project", "unknown")})
		self._reporting.attach_meta_data_to_report({"environment": os.environ.get("TestCubeName", "unknown")})
		self._reporting.attach_meta_data_to_report({"environment_identifier": os.environ.get("COMPUTERNAME", "unknown")})
		self._reporting.attach_meta_data_to_report({"cluster": str(enna.core.config.INFOTAINMENT_SYSTEM.cluster)})
		# pylint: disable=no-member
		self._reporting.attach_meta_data_to_report({"vehicle": str(enna.core.config.ENVIRONMENT.vehicle_project)})
		response = None
		try:
			# response = enna.utilities.diagnosis.helper.send_raw_service(self.__diagnosis, ecu=0x19, service_id=0x10, payload=[0x08])
			response = enna.utilities.diagnosis.helper.send_raw_service(self.__diagnosis, ecu=0x19, service_id=0x2e, payload=[0x03, 0x1D, 0x00])
			MODULE_LOGGER.info(f"Deactivate temporarily diagnose filter.: {response}")
		except enna.utilities.diagnosis.exceptions.DiagnosisException:
			MODULE_LOGGER.error(f"Error while deactivation diagnose filter! {response}")
		try:
			response = enna.utilities.diagnosis.helper.read_identification(self.__diagnosis, self.__ecu_address)
			enna_kwd_testing.definitions.META_DATA["hw"] = response[0].hw_version
			self._reporting.attach_meta_data_to_report({"hardware_version": response[0].hw_version})

			if enna.core.config.INFOTAINMENT_SYSTEM.cluster in {51, 53, 55}:
				response =  enna.utilities.diagnosis.helper.read_identification(self.__diagnosis, self.__icc_sw_address)

			enna_kwd_testing.definitions.META_DATA["sw"] = response[0].sw_version
			self._reporting.attach_meta_data_to_report({"software_version": response[0].sw_version})

			MODULE_LOGGER.info(f"Reading from main unit: hardware version = {enna_kwd_testing.definitions.META_DATA['hw']}; software version = {enna_kwd_testing.definitions.META_DATA['sw']}")

			response = enna.utilities.diagnosis.helper.read_coding(self.__diagnosis, self.__ecu_address)
			enna_kwd_testing.definitions.ADDITIONAL_INFORMATION += f"\n{response[0].text_coding}"
			self._reporting.attach_meta_data_to_report({"additional_information": enna_kwd_testing.definitions.ADDITIONAL_INFORMATION})
			MODULE_LOGGER.info(f"Coding of main unit: {response[0].text_coding}")
		except enna.utilities.diagnosis.exceptions.DiagnosisException:
			MODULE_LOGGER.error("Could not read main unit! Diagnostic address = 005F")
			return False
		except KeyError:
			MODULE_LOGGER.error("Not found parameter in response from diagnostic interface!")
			return False
		return True
