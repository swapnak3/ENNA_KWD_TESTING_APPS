# -*- coding: utf-8 -*-
"""Module contains implementation for text to speech engine"""

import sys
import logging
from enna_kwd_testing.utilities.speech.base.data_audio import AudioData

if sys.platform == "win32":
	from win32com.client import Dispatch
elif sys.platform == "linux":
	pass

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=possibly-used-before-assignment
class EngineSAPI5:
	"""Text to speech engine for Windows. Use SAPI5."""

	def __init__(self, voice: str, volume: int, rate: int) -> None:
		"""Constructor for SAPI5 text to speech engine.

		:param str voice: name of voice
		:param int volume: volume of audio data. Data range 0 ... 100
		:param int rate: speed of speak. Data range -5 ... +5
		"""
		self.__audio_format = 34  # SAFT44kHz16BitMono = 34
		self.__tts = Dispatch("SAPI.SpVoice")
		self.__set_voice(voice)
		self.__tts.Volume = volume
		self.__tts.Rate = rate
		MODULE_LOGGER.info("SpVoice Interface (SAPI) is initialized! ")
		# set meta data for audio data
		self.__channels = 1  # audio data for mono output
		self.__sample_width = 2  # sample width is 16 bit
		self.__frame_rate = 44100  # sampling frequency

	def _text_to_audio_data(self, text: str) -> bytes:
		"""Convert text to audio data.

		:param str text: text which convert to speech
		:return: audio data for speaking text
		:rtype: bytes
		"""

		stream = Dispatch("SAPI.SpMemoryStream")
		stream.Format.Type = self.__audio_format
		self.__tts.AudioOutputStream = stream
		self.__tts.Speak(text)  # SpeechVoiceSpeakFlags.SVSFPurgeBeforeSpeak = 2
		data = stream.GetData()
		del stream
		return bytes(data)

	def __set_voice(self, name) -> None:
		"""Set current voice for speech engine.

		:param str name: name of voice
		"""
		supported_voices = []
		for voice in self.__tts.GetVoices():
			if voice.GetAttribute("Name") == name:
				self.__tts.Voice = voice
				MODULE_LOGGER.info(f"Set voice to '{name}'. Language code is '{voice.GetAttribute('language')}'.")
				return
			supported_voices.append(voice.GetAttribute("Name"))
		MODULE_LOGGER.error(f"Use Defualt voice '{self.__tts.Voice.GetAttribute('name')}'. Language code is "
							f"'{self.__tts.Voice.GetAttribute('language')}'! Follow voices are supported: {supported_voices}")
		return

	@property
	def channels(self) -> int:
		"""Get audio channels from SAPI5 engine

		return: channels from SAPI5 audio data
		:rtype: int
		"""
		return self.__channels

	@property
	def sample_width(self) -> int:
		"""Get sample width from SAPI5 engine

		return: sample width from SAPI5 audio data
		:rtype: int
		"""
		return self.__sample_width

	@property
	def frame_rate(self) -> int:
		"""Get frame rate from SAPI5 engine.

		return: frame rate
		:rtype: int
		"""
		return self.__frame_rate


class Engine(EngineSAPI5):
	"""Engine for text to speech.

	:raises OSError: if operating System is not windows
	"""

	def __init__(self, voice: str, volume: int, rate: int) -> None:
		"""Constructor for text to speech engine.

		:param str voice: name of voice
		:param int volume: volume of audio data
		:param int rate: speed of speak.
		:raises OSError: if operating system not windows
		"""
		if sys.platform == "win32":
			EngineSAPI5.__init__(self, voice, volume, rate)
		else:
			raise OSError(f"System Platform '{sys.platform}' is not supported!")

	def text_to_speech(self, text: str) -> AudioData:
		"""Convert text to audio data.

		:param str text: text to speech
		:return: audio data from text
		:rtype: AudioData
		"""
		return AudioData(channels=self.channels, sample_width=self.sample_width, frame_rate=self.frame_rate,
						 raw_data=self._text_to_audio_data(text))
