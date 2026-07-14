# -*- coding: utf-8 -*-
"""Module contains capturing methods for video."""
import datetime
import logging
import pathlib
import threading
import time
import cv2

import enna.core.config

import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.data_interfaces.android_hmi.exceptions

MODULE_LOGGER = logging.getLogger(__name__)
MODULE_CONFIG = enna.core.config.get(__name__)


class Recorder(threading.Thread):
	"""Recorder for video capturing."""

	def __init__(self, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface | None = None, save_path: pathlib.Path | None = None) -> None:
		"""Constructor Video Recorder.

		:param android_hmi: instance of interface for Android UI Controller
		:param save_path: path to Save Video file
		"""

		super().__init__()
		self._android_hmi = android_hmi
		self._save_path  = save_path
		self._fps: float = 2.0
		self._running: bool = False
		if self._save_path is not None:
			if not self._save_path.exists():
				try:
					save_path.mkdir(parents=True)
				except OSError as error:
					MODULE_LOGGER.error(f"Directory could not created! {error}")
					self._save_path = None
					return
			self._save_path = self._save_path.joinpath(f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_video.mp4")

	def start(self) -> None:
		"""Starting video capture."""
		self._running = True
		super().start()
		MODULE_LOGGER.debug("Video capturing is started.")

	def run(self) -> None:
		"""Capturing Video."""
		if self._android_hmi is None:
			MODULE_LOGGER.error("Not start video! No interface for Android UI Controlling.")
			return
		if self._save_path is None:
			MODULE_LOGGER.error("Not start video! Missing Path to save video. Path not get or Path does not exist on File System.")
			return
		try:
			fourcc = cv2.VideoWriter_fourcc(*'X264')
			capture = cv2.VideoWriter(str(self._save_path), fourcc, self._fps, self._android_hmi.window_size.value)
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			MODULE_LOGGER.error(f"Android HMI Error! {error}")
			return

		try:
			while capture.isOpened() and self._running:
				wait_timestamp = time.time() + 1 / self._fps
				capture.write(self._android_hmi.take_screenshot().as_ndarray)
				diff = int((wait_timestamp - time.time()) * 1000) if int((wait_timestamp - time.time()) * 1000) > 0 else 0
				cv2.waitKey(diff)
		except (cv2.error, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as error:
			MODULE_LOGGER.error(f"Video capturing aborted! {error}")
		capture.release()
		return

	def stop(self):
		"""Stopping video capturing!"""
		self._running = False
		super().join(timeout=3.0)
		MODULE_LOGGER.info(f"Video capturing is finish. Video save under '{self._save_path}'")
