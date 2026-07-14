# -*- coding: utf-8 -*-
"""Module contains stimulation for touching and checking methods of audi assistant app."""

import logging

import enna.core.exceptions
import enna.core.component_system.decorators
import enna.core.reporting.interface

import enna_st12.instance_names
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.utilities.menu_navigation.interface
import enna_st12.utilities.menu_navigation.exceptions

import enna_hcp_configuration.android.xpaths.assistant
import enna_hcp_configuration.android.contexts.assistant

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.stimulations.apps._internal
import enna_kwd_testing.utilities.xpath_collection.helper

MODULE_LOGGER = logging.getLogger(__name__)

# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetAudiAssistantActivationPhrase(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation the using wakeup word for audi assistant."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.assistant.GENERAL
		self._list_container = enna_hcp_configuration.android.xpaths.assistant.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.assistant.ACTIVATION_ITEM_SWITCH_BUTTON


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetAudiAssistantJustTalk(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation the just talk function of audi assistant."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.assistant.GENERAL
		self._list_container = enna_hcp_configuration.android.xpaths.assistant.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.assistant.JUST_TALK_SWITCH_BUTTON


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetAudiAssistantFidContent(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation displaying content of audi assistant in driver information display."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.assistant.GENERAL
		self._list_container = enna_hcp_configuration.android.xpaths.assistant.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.assistant.INFORMATION_FOR_THE_DRIVER_SWITCH_BUTTON


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetAudiAssistantSoundSignal(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation sound signals of audi assistant."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.assistant.GENERAL
		self._list_container = enna_hcp_configuration.android.xpaths.assistant.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.assistant.SOUND_SIGNAL_SWITCH_BUTTON


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetAudiAssistantPromptLength(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation short answers of audi assistant."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.assistant.GENERAL
		self._list_container = enna_hcp_configuration.android.xpaths.assistant.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.assistant.SHORT_PROMPT_SWITCH_BUTTON


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class  SetAudiAssistantVoiceBarge(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation  interrupting voice barge of audi assistant."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.assistant.GENERAL
		self._list_container = enna_hcp_configuration.android.xpaths.assistant.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.assistant.INTERRUPT_SPOKEN_OUTPUTS_SWITCH_BUTTON


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class  SetAudiAssistantProactiveRecommendations(enna_kwd_testing.stimulations.apps._internal.SetSwitchButtonInScreen):
	"""Activation or deactivation proactive suggestions of audi assistant."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.assistant.PROACTIVITY
		self._list_container = enna_hcp_configuration.android.xpaths.assistant.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.assistant.PROACTIVE_RECOMMONDATIONS_AND_ROUTINES_SWITCH


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class  SetAudiAssistantProactiveSoundSignals(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Activation or deactivation sound signals for proactive suggestions of audi assistant."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.3")
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self._buttons_of_sound_signals = {
			"OFF": enna_hcp_configuration.android.xpaths.assistant.ACOUSTIC_MODE_OFF,
			"SOUNDS_ONLY": enna_hcp_configuration.android.xpaths.assistant.ACOUSTIC_MODE_SOUNDS_ONLY,
			"SPEECH_AND_SOUNDS": enna_hcp_configuration.android.xpaths.assistant.ACOUSTIC_MODE_SPEECH_AND_SOUNDS
		}

	def _action(self) -> bool:
		"""Set sound signals for proactive recommendations.

		:return: True if success else false.
		"""

		state = self.values["STATE"].upper()

		try:
			self.__menu_navigation.go_to_screen(enna_hcp_configuration.android.contexts.assistant.PROACTIVITY, max_retries=5)
		except (enna_st12.utilities.menu_navigation.exceptions.MenuNavigationException, AttributeError) as error:
			err_msg = f"Error while navigating to the screen of switch button: {enna_hcp_configuration.android.contexts.assistant.PROACTIVITY.name}. {error}"
			self._reporting.add_report_message_ta_error(err_msg)
			return False
		try:

			xpath = self._buttons_of_sound_signals[state]
			self.__android_hmi.click_element(xpath.get())
			self.__android_hmi.wait_for_element_visible(f"{xpath.get()}[@checked='true']", max_time=1.0)
		except KeyError as error:
			self._reporting.add_report_message_ta_error(f"Xpath not found in collection! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException as error:
			self._reporting.add_report_message_ta_error(f"No connection to MMI! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException as error:
			self._reporting.add_report_message_ta_error(f"Invalid argument! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException as error:
			self._reporting.add_report_message_system_error(f"Toggle button '{state}' not found in screen '{enna_hcp_configuration.android.contexts.assistant.PROACTIVITY.name}'! {error}")
			return False
		except enna.core.exceptions.TimeoutException as error:
			self._reporting.add_report_message_system_error(f"Toggle button '{state}' could not switch on! {error}")
			return False
		self._reporting.add_report_message_pass(f"Toggle button '{state}' is switch to ON")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckAudiAssistantJustToTalk(enna_kwd_testing.stimulations.apps._internal.CheckSwitchButtonInScreen):
	"""Check state from the just talk function of audi assistant."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface,
				 android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface,
				 menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.assistant.GENERAL
		self._list_container = enna_hcp_configuration.android.xpaths.assistant.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.assistant.JUST_TALK_SWITCH_BUTTON


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckAudiAssistantActivationPhrase(enna_kwd_testing.stimulations.apps._internal.CheckSwitchButtonInScreen):
	"""Check state from the activation phrase function of audi assistant."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface,
				 android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface,
				 menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.assistant.GENERAL
		self._list_container = enna_hcp_configuration.android.xpaths.assistant.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.assistant.ACTIVATION_ITEM_SWITCH_BUTTON


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckAudiAssistantFidContent(enna_kwd_testing.stimulations.apps._internal.CheckSwitchButtonInScreen):
	"""Check state from the fid content function of audi assistant."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface,
				 android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface,
				 menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.assistant.GENERAL
		self._list_container = enna_hcp_configuration.android.xpaths.assistant.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.assistant.INFORMATION_FOR_THE_DRIVER_SWITCH_BUTTON


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckAudiAssistantProactiveRecommendations(enna_kwd_testing.stimulations.apps._internal.CheckSwitchButtonInScreen):
	"""Check state from the proactive recommendations function of audi assistant."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface,
				 android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface,
				 menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.assistant.PROACTIVITY
		self._list_container = enna_hcp_configuration.android.xpaths.assistant.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.assistant.PROACTIVE_SWITCH


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckAudiAssistantEarcons(enna_kwd_testing.stimulations.apps._internal.CheckSwitchButtonInScreen):
	"""Check state from the earcons function of audi assistant."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface,
				 android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface,
				 menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.assistant.GENERAL
		self._list_container = enna_hcp_configuration.android.xpaths.assistant.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.assistant.SOUND_SIGNAL_SWITCH_BUTTON


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckAudiAssistantPromptLength(enna_kwd_testing.stimulations.apps._internal.CheckSwitchButtonInScreen):
	"""Check state from the prompt length function of audi assistant."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface,
				 android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface,
				 menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.assistant.GENERAL
		self._list_container = enna_hcp_configuration.android.xpaths.assistant.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.assistant.SHORT_PROMPT_SWITCH_BUTTON


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckAudiAssistantVoiceBarge(enna_kwd_testing.stimulations.apps._internal.CheckSwitchButtonInScreen):
	"""Check state from the voice barge function of audi assistant."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface,
				 android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface,
				 menu_navigation: enna_st12.utilities.menu_navigation.interface):
		"""Initialized Stimulation

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self._screen = enna_hcp_configuration.android.contexts.assistant.GENERAL
		self._list_container = enna_hcp_configuration.android.xpaths.assistant.LIST_CONTAINER
		self._button = enna_hcp_configuration.android.xpaths.assistant.INTERRUPT_SPOKEN_OUTPUTS_SWITCH_BUTTON


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckAudiAssistantSoundSignals(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to Check the state for audi-assistant proactive sound signals"""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting)
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self.allowed_parameter_keys = ["STATE"]
		self._buttons_of_sound_signals = {
			"OFF": enna_hcp_configuration.android.xpaths.assistant.ACOUSTIC_MODE_OFF,
			"SOUNDS_ONLY": enna_hcp_configuration.android.xpaths.assistant.ACOUSTIC_MODE_SOUNDS_ONLY,
			"SPEECH_AND_SOUNDS": enna_hcp_configuration.android.xpaths.assistant.ACOUSTIC_MODE_SPEECH_AND_SOUNDS
		}

	def _action(self) -> bool:
		"""Check selected sound option from Audi Assistant.

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""

		sound_state = self.values["STATE"].upper()
		try:
			self.__menu_navigation.go_to_screen(enna_hcp_configuration.android.contexts.assistant.PROACTIVITY, max_retries=5)
		except (enna_st12.utilities.menu_navigation.exceptions.MenuNavigationException, AttributeError) as error:
			err_msg = f"Error while navigating to the screen of switch button: {enna_hcp_configuration.android.contexts.assistant.PROACTIVITY.name}. {error}"
			self._reporting.add_report_message_ta_error(err_msg)
			return False

		try:
			xpath = self._buttons_of_sound_signals[sound_state]
			self.__android_hmi.wait_for_element_visible(f"{xpath.get()}[@checked='true']", max_time=1.0)
		except KeyError as error:
			self._reporting.add_report_message_ta_error(f"Wrong parameter for STATE: should be 'SPEECH_AND_SOUNDS','SOUNDS_ONLY' or 'OFF'! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException as error:
			self._reporting.add_report_message_ta_error(f"No connection to MMI! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException as error:
			self._reporting.add_report_message_ta_error(f"Invalid argument! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException as error:
			self._reporting.add_report_message_system_error(f"Toggle button '{sound_state}' not found in screen '{enna_hcp_configuration.android.contexts.assistant.PROACTIVITY.name}'! {error}")
			return False
		except enna.core.exceptions.TimeoutException as error:
			self._reporting.add_report_message_system_error(f"Toggle button '{sound_state}' is not switched on! {error}")
			return False
		self._reporting.add_report_message_pass(f"The 'sound signals' is to'{self.values['STATE']}' ")
		return True
