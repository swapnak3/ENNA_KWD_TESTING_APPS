# -*- coding: utf-8 -*-
"""Contains Passive Tests for campaign."""
import queue
import datetime
import threading
import logging
import pathlib

import enna.core.config
import enna.core.component_system.decorators
import enna.core.interfaces.testing
import enna.core.reporting.interface
import enna.data_interfaces.esotrace.interface
import enna.data_interfaces.esotrace


MODULE_CONFIG = enna.core.config.get(__name__)
MODULE_LOGGER = logging.getLogger(__name__)

FAKE_CASE_LOGGING = enna.core.interfaces.testing.TestCaseSpecification(id="Traces", name="Logging Traces", action="capture esutraces")

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.esotrace", instance_name="ivi")
class TraceLogger(enna.core.interfaces.testing.PassiveTest):
	"""Contains esotrace logging for campaign."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, esotrace: enna.data_interfaces.esotrace.interface.Interface) -> None:
		"""Instantiate passive test for capture traces

		:param reporting: instance of reporting
		:param esotrace: instance of interface to capture esotrace
		"""
		super().__init__(reporting=reporting, test_case_specifications=FAKE_CASE_LOGGING)
		self._trace = esotrace
		self._queue = queue.Queue()
		self._recording = False
		self._file = None
		MODULE_LOGGER.info("Passive test instanced.")

	def start(self) -> None:
		"""Start Logging"""
		save_path = pathlib.Path(MODULE_CONFIG.get("save_path", "."))
		save_path.mkdir(parents=True, exist_ok=True)
		self._recording = True
		self._trace.register(enna.data_interfaces.esotrace.ANY_ESOTRACE_MESSAGE, self.__get_callback)
		timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
		self._file = save_path.joinpath(f"{timestamp}_ivi_traces.log")
		threading.Thread(target=self.__write_log_message, name="ivi_trace_logger", daemon=True).start()
		MODULE_LOGGER.info("Logger is started.")

	def stop(self) -> None:
		"""Stop Logging"""
		self._recording = False

	def __get_callback(self, msg: enna.core.interfaces.Data[enna.data_interfaces.esotrace.EsotraceMessage]) -> None:
		"""Get message from esotrace.

		:param msg: esotrace message
		"""
		data = msg.value
		self._queue.put_nowait(data)

	def __write_log_message(self):
		"""Write Log message to a File."""
		while  self._recording or not self._queue.empty():
			if not self._queue.empty():
				with open(str(self._file), "a", encoding="utf-8", errors="ignore") as file:
					data: enna.data_interfaces.esotrace.EsotraceMessage = self._queue.get_nowait()
					line = f"{data.logger_timestamp} || {data.log_level.value} || {data.channel_name} || {data.source} || {data.message_data}\n"
					file.write(line)
