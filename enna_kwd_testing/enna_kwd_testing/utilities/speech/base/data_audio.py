# -*- coding: utf-8 -*-
"""Module contain class for audio data."""


class AudioData:
	"""Class of audio data. """

	def __init__(self, channels: int, sample_width: int, frame_rate: int, raw_data: bytes) -> None:
		"""Constructor for an audio data object

		:param int channels: number of audio channels
		:param int sample_width: number of bytes per sample
		:param int frame_rate: frequency of sampling
		:param bytes raw_data: bytes of audio stream
		:raises IOError: if audio data input not mono
		:raises OSError: if problem with operating system
		"""
		if channels != 1:
			raise IOError('Stereo input data not supported!')
		self.mono = 1  # number of channels for mono
		self.stereo = 2  # number of channels for stereo
		self.frame_rate = frame_rate
		self.sample_width = sample_width

		self.mono_output = raw_data
		self.left_channel_output = b''
		self.right_channel_output = b''
		for i in range(0, len(raw_data), sample_width):
			self.left_channel_output += raw_data[i:i + sample_width] + b'\x00' * sample_width
			self.right_channel_output += b'\x00' * sample_width + raw_data[i:i + sample_width]
