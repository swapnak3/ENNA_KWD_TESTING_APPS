# -*- coding: utf-8 -*-
"""Module contains capturing methods via esotrace tools."""
import datetime
import logging
import pathlib
import subprocess
import time

import eso_tracetools

import enna.core.config

MODULE_LOGGER = logging.getLogger(__name__)
MODULE_CONFIG = enna.core.config.get(__name__)


class Recorder:
	"""Recorder to IVI and SYS Traces"""
	def __init__(self):
		"""Constructor of Recorder."""

		try:
			save_path = pathlib.Path(MODULE_CONFIG.get("save_path", None))
			save_path.mkdir(parents=True, exist_ok=True)
		except (TypeError, OSError):
			MODULE_LOGGER.error(f"Save path is invalid! Could not start recording esotraces. Save Path: '{save_path}'")
			return
		try:
		# pylint: disable=consider-using-with
			save_path_ivi_traces = save_path.joinpath(f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_IVI.esotrcace")
			command_ivi = f"java -jar {eso_tracetools.JTRACECAPTURE_PATH} {enna.core.config.INFOTAINMENT_SYSTEM.ip} -p 21002 -o {save_path_ivi_traces} -M 50 -k 0"
			self.__ivi_recorder = subprocess.Popen(command_ivi, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			MODULE_LOGGER.info(f"Start recording IVI traces. Save Path: '{save_path_ivi_traces}'")

			save_path_sys_traces = save_path.joinpath(f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_SYS.esotrcace")
			command_sys = f"java -jar {eso_tracetools.JTRACECAPTURE_PATH} {enna.core.config.INFOTAINMENT_SYSTEM.ip} -p 21005 -o {save_path_sys_traces} -M 50 -k 0"
			self.__sys_recorder = subprocess.Popen(command_sys, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			MODULE_LOGGER.info(f"Start recording SYS traces. Save Path: '{save_path_sys_traces}'")

			time.sleep(10.0)   # wait time of establish connection to test bench
		except OSError as error:
			MODULE_LOGGER.info(f"Could not start logging esotraces! {error}")

	def __del__(self) -> None:
		"""Stop logging."""
		time.sleep(180) # delay after run
		if isinstance(self.__ivi_recorder, subprocess.Popen):
			self.__ivi_recorder.kill()
			self.__ivi_recorder = None
			MODULE_LOGGER.info("Recording IVI traces was stopping.")
		if isinstance(self.__sys_recorder, subprocess.Popen):
			self.__sys_recorder.kill()
			self.__sys_recorder = None
			MODULE_LOGGER.info("Recording SYS traces was stopping.")
