# -*- coding: utf-8 -*-
"""Module contains help function to using text tool.

@author: GLM0UBU: Björn König
"""
import logging
import enum
import importlib

import enna.core.config
from enna_hcp_configuration.texts import TextObject

class AvailableSources(enum.StrEnum):
	"""Constants for available text sources"""
	CENTER = "center"
	PASSENGER = "passenger"
	SPEECH_DIALOG_SYSTEM = "sds"


MODULE_LOGGER = logging.getLogger(__name__)


def get_text_from_configuration(text_id: str, source: str = AvailableSources.CENTER, language: str = enna.core.config.INFOTAINMENT_SYSTEM.system_language.value) -> str:
	"""Found text for requested language of text ID. If no text found return text ID as text.
	Replace text tool line break placeholder wit normal line break.

	:param text_id: property nam of text e.g.'de.eso.phone.top_bar_title__all_settings__title'
	:param source: source of text. Available sources are center display, passenger display or speech dialog system
	:param language: language of text. Available languages are german or english
	:return: find text
	"""
	pre_module_name = "enna_hcp_configuration.texts."

	split_id = text_id.replace(" ", "").split(".")
	module_name = ".".join(split_id[:-1])
	object_name = split_id[-1]

	# If starts Text-ID with 'inputs' or 'android' don't use Audi Text Tool.
	module_name = f"{pre_module_name}{module_name}" if module_name.startswith("inputs") or module_name.startswith("android") else f"{pre_module_name}CLU{enna.core.config.INFOTAINMENT_SYSTEM.cluster}.{source}.{module_name}"
	try:
		text_module = importlib.import_module(module_name)
		text_object: TextObject = getattr(text_module, object_name)
		text = text_object.get(language=language)
	except (ImportError, AttributeError) as error:
		MODULE_LOGGER.debug(f"Text '{text_id}' not from Text Tool. {error}")
		text = str(text_id)

	return text.replace("\\n", "\n")
