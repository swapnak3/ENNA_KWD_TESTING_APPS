# -*- coding: utf-8 -*-
"""Module contains handling for sound device"""

import logging
import pyaudio
from enna_kwd_testing.utilities.speech.base.data_audio import AudioData

MODULE_LOGGER = logging.getLogger(__name__)


class OutputDevice:
	"""Sound output device handler"""

	def __init__(self, device: str) -> None:
		"""Constructor for sound device handler.

		:param str device: name of sound device
		"""
		self.audio_manager = pyaudio.PyAudio()
		self.__set_device(device)

	def __set_device(self, name: str) -> None:
		"""Set using sound device.

		:param str name: name of sound device
		"""
		supported_devices = []
		for i in range(0, self.audio_manager.get_device_count()):
			if self.audio_manager.get_device_info_by_index(i)['name'] == name:
				self.__current_device_index = i
				MODULE_LOGGER.info(f"Using '{name}' sound device.")
				return
			supported_devices.append(self.audio_manager.get_device_info_by_index(i)['name'])
		self.__current_device_index = 0
		MODULE_LOGGER.error(f"Using default sound device '{self.audio_manager.get_device_info_by_index(0)['name']}'! Follow sound devices are supported {supported_devices}.")
		return

	def play_sound(self, audio: AudioData):
		"""Play sound. Play mono sound on device output.

		:param AudioData audio: audio data to play
		"""
		output = self.audio_manager.open(format=self.audio_manager.get_format_from_width(audio.sample_width),
										 channels=audio.mono, rate=audio.frame_rate, output=True,
										 output_device_index=self.__current_device_index)
		output.write(audio.mono_output)
		# print(audio.mono_output)
		output.close()

	def play_sound_on_left_channel(self, audio: AudioData):
		"""Play sound. Play sound on left channel from device output.

		:param AudioData audio: audio data to play
		"""
		output = self.audio_manager.open(format=self.audio_manager.get_format_from_width(audio.sample_width),
										 channels=audio.stereo, rate=audio.frame_rate, output=True,
										 output_device_index=self.__current_device_index)
		output.write(audio.left_channel_output)
		output.close()

	def play_sound_on_right_channel(self, audio: AudioData):
		"""Play sound. Play sound on right channel from device output.

		:param AudioData audio: audio data to play
		"""
		output = self.audio_manager.open(format=self.audio_manager.get_format_from_width(audio.sample_width),
										 channels=audio.stereo, rate=audio.frame_rate, output=True,
										 output_device_index=self.__current_device_index)
		output.write(audio.right_channel_output)
		output.close()
