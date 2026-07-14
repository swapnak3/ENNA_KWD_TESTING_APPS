# -*- coding: utf-8 -*-
"""Module for speech recognizing. Using http://www.google.com/speech-api/v2/recognize to recognize."""

import logging
import threading
import enna.core.config
import enna.core.exceptions
import enna.core.interfaces
import enna.core.interfaces.server
import enna.core.time
import speech_recognition

import enna_kwd_testing.utilities.speech.exceptions
import enna_kwd_testing.utilities.speech.interface
import enna_kwd_testing.utilities.speech.base.engine
import enna_kwd_testing.utilities.speech.base.sound

INSTANCE_CONFIG = enna.core.config.get_instance_config(__name__)

MODULE_LOGGER = logging.getLogger(__name__)

VOICES = {
	"de_DE": "Microsoft Hedda Desktop",
	"en_US": "Microsoft David Desktop"
}


# pylint: disable=too-many-instance-attributes
class Server(enna_kwd_testing.utilities.speech.interface.Interface, enna.core.interfaces.server.Server):
	"""Provides methods for text to speech and speech to text."""

	def __init__(self, instance_name):
		"""Create a instance of speech handling.

		:param str instance_name: Name of instance to initialize server for.
		"""
		enna_kwd_testing.utilities.speech.interface.Interface.__init__(self)
		enna.core.interfaces.server.Server.__init__(self, instance_name=instance_name)
		self._listing = False
		self._loop = None

		self._speech_recognizer = None

		self._instance_name = instance_name
		self._instance_config = INSTANCE_CONFIG[instance_name]
		self._read_configuration()
		self._initialize_speaker()
		self._initialize_microphone()

		# self.start_listening()
		# enna.core.time.sleep(3)
		# self.stop_listening()
		MODULE_LOGGER.debug(f'Instance of Speech-Server is created. Name="{self._instance_name}"')
		self._set_online()

	def _read_configuration(self):
		"""Reed configuration for instance.

		:raises enna.core.exceptions.ConfigurationException: if chosen microphone could not be found on system
		"""
		try:
			self._instance_config = INSTANCE_CONFIG[self._instance_name]
		except KeyError:
			message = f"Missing istance configuration for instance '{self._instance_name}'"
			MODULE_LOGGER.exception(message)
			raise enna.core.exceptions.ConfigurationException(message)
		self._language = self._instance_config.get("language", "de_DE")
		self._output = self._instance_config.get("output", {})
		self._input = self._instance_config.get("input", {})

	def _initialize_microphone(self):
		"""Initialize microphone to using for speech input.

		:raises enna.core.exceptions.ConfigurationException: If chosen microphone could not be found on system
		"""
		self._phrase_time_limit = self._input.get("phrase_time_limit", None)
		self._microphone_sample_rate = self._input.get("sample_rate", None)
		microphone_name = ""
		self._speech_recognizer = speech_recognition.Recognizer()
		try:
			microphones = speech_recognition.Microphone.list_microphone_names()
			microphone_name = self._input["microphone"]
			self._microphone_index = microphones.index(microphone_name)
			MODULE_LOGGER.info(
				f"Initializing microphone '{microphone_name}' success. Microphone index = {self._microphone_index}")
		except ValueError:
			message = f"Could not initialize microphone '{microphone_name}'! Please check your configuration and your hardware."
			MODULE_LOGGER.exception(message)
			raise enna.core.exceptions.ConfigurationException(message)
		except KeyError:
			self._microphone_index = 0
			MODULE_LOGGER.info(
				f"Initializing microphone '{microphones[self._microphone_index]}' success. It will use default microphone because of not set in configuration.")

	def _initialize_speaker(self):
		"""Initialize speaker to using speech output.

		:raise enna_kwd_testing.utilities.speech.exceptions.SpeechOutputError: If an error occurs at initializing the speaker for the speech output
		"""
		speaker_name = self._output.get("speaker", None)
		self.__speaker = enna_kwd_testing.utilities.speech.base.sound.OutputDevice(speaker_name)
		volume = self._output.get("volume", 100)
		rate = self._output.get("rate", 0)
		try:
			voice_name = {VOICES[self._language]}
		except KeyError:
			message = f"Language '{VOICES[self._language]}' not in supported Voice list!"
			MODULE_LOGGER.exception(message)
			raise enna_kwd_testing.utilities.speech.exceptions.SpeechOutputError(message)
		self.__tts_engine = enna_kwd_testing.utilities.speech.base.engine.Engine(voice_name, volume, rate)

	def speak(self, text: str) -> None:
		"""Speak a text. Output via sound card.

		:param str text: Text output to speak
		"""
		self.__speaker.play_sound(self.__tts_engine.text_to_speech(text))
		MODULE_LOGGER.info(f"say: '{text}'")

	def driver_speak(self, text: str) -> None:
		"""Driver speak a text. Output via sound card on left channel.

		:param str text: Text output to speak
		"""
		self.__speaker.play_sound_on_left_channel(self.__tts_engine.text_to_speech(text))
		MODULE_LOGGER.info(f"Driver say: '{text}'")

	def co_driver_speak(self, text: str) -> None:
		"""Co-Driver speak a text. Output via sound card on right channel.

		:param str text: Text output to speak
		"""
		self.__speaker.play_sound_on_right_channel(self.__tts_engine.text_to_speech(text))
		MODULE_LOGGER.info(f"Driver say: '{text}'")

	def start_listening(self) -> None:
		"""Start listing at microphone. Start thread to recognize speech."""
		if self._listing:
			MODULE_LOGGER.error("You have to stop listen! Before you can start listen again.")
			return
		self._listing = True
		self._loop = threading.Thread(target=self._recognizer_loop, daemon=True)
		self._loop.start()

	def stop_listening(self, timeout=10.0) -> str:
		"""Stop listing at microphone.

		:param float timeout: time out to end listing in seconds
		:return: all recognized phrases
		:rtype: str
		"""
		if not self._listing:
			MODULE_LOGGER.error("You have to start listen! Before you can stop listen.")
		self._listing = False
		self._loop.join(timeout)
		phrases = self.all_phrases.value
		self._current_phrase = enna.core.interfaces.Data("")
		self._all_phrases = enna.core.interfaces.Data("")
		self._signal_property("current_phrase", self._current_phrase)
		self._signal_property("all_phrases", self._all_phrases)
		return phrases

	def _recognizer_loop(self) -> None:
		"""Recognize speech while listing is active.

		:raises enna_kwd_testing.utilities.speech.exceptions.RecognitionRequestError: If an error appears while processing speech input online
		:raises enna_kwd_testing.utilities.speech.exceptions.SpeechInputError: If the audio source is not functional
		"""
		while self._listing:
			try:
				with speech_recognition.Microphone(device_index=self._microphone_index, sample_rate=self._microphone_sample_rate) as source:
					audio = self._speech_recognizer.listen(source=source, phrase_time_limit=self._phrase_time_limit)
				threading.Thread(target=self.__google_recognizer_thread, kwargs={"audio": audio, "language": self._language}).start()
			except AssertionError:
				message = f"Audio source index '{source.device_index}' is not functional! Follow device are selectable: {source.list_microphone_names()}"
				MODULE_LOGGER.exception(message)
				raise enna_kwd_testing.utilities.speech.exceptions.SpeechInputError(message)

	def __google_recognizer_thread(self, audio: speech_recognition.AudioData, language: str) -> None:
		"""Send audio data to google. And write response in attributes.
		Write current response text to _current_phrase
		Add current response text to _all_phrases

		:param speech_recognition.AudioData audio: Audio data of send to google
		:param str language: language to translate
		:raises enna_kwd_testing.utilities.speech.exceptions.RecognitionRequestError: If an error appears while processing speech input online
		"""
		# pylint: disable=too-many-try-statements)
		try:
			text = self._speech_recognizer.recognize_google(audio, language=language)
			MODULE_LOGGER.info(f"Recognized phrase = '{text}'")
			if self.current_phrase.value != text:
				self._current_phrase = enna.core.interfaces.Data(text)
				text_all = f"{self.all_phrases.value}\n{text}"
				self._all_phrases = enna.core.interfaces.Data(text_all)
				self._signal_property("current_phrase", self._current_phrase)
				self._signal_property("all_phrases", self._all_phrases)
		except speech_recognition.RequestError:
			msg = "Request Error of recognize speech by google!"
			MODULE_LOGGER.exception(msg)
			raise enna_kwd_testing.utilities.speech.exceptions.RecognitionRequestError(msg)

		except speech_recognition.UnknownValueError:
			MODULE_LOGGER.debug(f"Unknown Value error by listening. | Language = '{self._language}'")
