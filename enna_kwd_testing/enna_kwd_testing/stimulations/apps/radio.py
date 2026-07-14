# -*- coding: utf-8 -*-
"""Module contains stimulations for radio app."""
import logging
import time
import enna.core.exceptions
import enna.core.component_system.decorators
import enna.core.reporting.interface

import enna_st12.instance_names
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.utilities.menu_navigation.interface

from enna_hcp_configuration.android.contexts import radio as contents_radio
from enna_hcp_configuration.android.xpaths import radio as xpaths_radio

import enna_kwd_testing.utilities.xpath_collection.helper
import enna_kwd_testing.utilities.xpath_collection.exceptions
import enna_kwd_testing.stimulations.apps._internal
import enna_kwd_testing.stimulations.base.keyword_stim_baseclass

MODULE_LOGGER = logging.getLogger(__name__)

# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class GemTriggerAnnouncement(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Stimulation for trigger a radio announcement """

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Constructor for trigger a radio announcement

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, menu_navigation=menu_navigation, android_hmi=android_hmi)
		self.allowed_parameter_keys=["TYPE","ACTIVE"]
		self.current_type_field = xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_DOMAIN_ANNOUNCEMENT_TYPE
		self.next_type_button = xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_DOMAIN_ANNOUNCEMENT_TYPE_NEXT_BUTTON
		self.previous_type_button = xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_DOMAIN_ANNOUNCEMENT_TYPE_PREVIOUS_BUTTON
		self.activate_button = xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_DOMAIN_ANNOUNCEMENT_ACTIVE_BUTTON
		self.available_announcement_types = None
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _precondition(self) -> bool:
		"""Navigate to radio settings custum bl gems domain announcement screen.

		:return: True if success, else False
		"""
		return self._go_to_screen(destination=contents_radio.SETTINGS_CUSTOM_BL_GEMS_DOMAIN_ANNOUNCEMENT)

	def get_current_announcement_type(self) -> str:
		""" determines the currently selected announcement type from text attribute which is enclosed by >>CURRENT_ANNOUNCEMENT_TYPE<<
		
		:return: currently selected announcement type
		:raises ValueError: if current type element is not found
		"""
		found_elements=self._android_hmi.layout.value.xpath(self.current_type_field.get())
		if len(found_elements)==0:
			raise ValueError(f"current type element not found: {self.current_type_field.get()}")
		text=found_elements[0].attrib['text']
		parts=text.replace("<<", ">>").split(">>")
		if self.available_announcement_types is None:
			self.available_announcement_types = text.replace(">>","").replace("<<","").replace(" ]","").replace("Type [ ","").split(" | ")
		return parts[1]

	def get_active_state(self)->bool:
		""" determines the active state from text attribute which is indicated by [X] in the text attribute<<

		:return: active state
		:raises ValueError: if activate element is not found
		"""
		found_elements=self._android_hmi.layout.value.xpath(self.activate_button.get())
		if len(found_elements)==0:
			raise ValueError(f"active element not found: {self.current_type_field.get()}")
		text=found_elements[0].attrib['text']
		return "Active [x]" in text

	def set_active_state(self, state: bool)->bool:
		""" set the announcement active state
		
		:param state: active state which should be set
		:return: True if success, else False
		"""
		retry = 3
		while retry > 0:
			retry -= 1
			request_tries = 20
			waiting = False
			while request_tries > 0:
				request_tries -= 1
				current_state=self.get_active_state()
				if current_state==state:
					return True
				if not waiting: # click on element once and wait up to two seconds to see if it worked
					self._android_hmi.click_element(xpath=self.activate_button.get())
					waiting = True
				time.sleep(0.1)
		return False

	def _action(self) -> bool:
		"""Set announcement type and activation state

		:return: True if success, else false
		"""
		announcement_type = self.values.get("TYPE", "")
		active = self.values.get("ACTIVE", True)
		try:
			if not active: # we do not care which is the currently selected announcement type
				if not self.set_active_state(active):
					self._reporting.add_report_message_ta_error(f"'Could not set accouncement state to {"" if active else "in"}active within three attempts'")
					return False
			else:
				current_type = self.get_current_announcement_type()
				# print(current_type, self.available_announcement_types)
				if current_type!=announcement_type:
					if announcement_type not in self.available_announcement_types:
						self._reporting.add_report_message_ta_error(f"'{announcement_type}' is not an available announcement type {self.available_announcement_types}'")
						return False
					target_index=self.available_announcement_types.index(announcement_type)
					current_index=self.available_announcement_types.index(current_type)
					step = 20
					while (current_index!=target_index) and (step>0):
						step -= 1
						self._android_hmi.click_element(xpath=self.previous_type_button.get() if target_index<current_index else self.next_type_button.get())
						time.sleep(2)
						current_index = self.available_announcement_types.index(self.get_current_announcement_type())
					if step == 0:
						self._reporting.add_report_message_ta_error(f"could not reach '{announcement_type}' in 20 steps'")
						return False
				if not self.set_active_state(active):
					self._reporting.add_report_message_ta_error(f"'Could not set accouncement state to {"" if active else "in"}active within three attempts'")
					return False
		except ValueError as error:
			self._reporting.add_report_message_system_error(error)
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException:
			self._reporting.add_report_message_system_error("Failed to Click on Android HMI")
			return False
		self._reporting.add_report_message_pass(f"Announcement {"" if announcement_type=="" else f"'{announcement_type}'"} is {"" if active else "in"}active")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class GemCodingSimulation(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Stimulation set simulated radio coding """

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Constructor of stimulation to set simulated radio coding

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, menu_navigation=menu_navigation, android_hmi=android_hmi)
		self.allowed_parameter_keys = ["CODING"]
		self.current_coding_field = xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_GENERAL_CODING_SIMULATION_MODE
		self.next_type_button = xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_GENERAL_CODING_SIMULATION_MODE_NEXT_BUTTON
		self.previous_type_button = xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_GENERAL_CODING_SIMULATION_MODE_PREVIOUS_BUTTON
		self.trigger_restart_button = xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_GENERAL_CODING_SIMULATION_TRIGGER_RESTART_BUTTON
		self.available_coding_types = None
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _precondition(self) -> bool:
		"""Navigate to radio settings custum bl gems general screen.

		:return: True if success, else False
		"""
		return self._go_to_screen(destination=contents_radio.SETTINGS_CUSTOM_BL_GEMS_GENERAL)

	def get_current_coding(self) -> str:
		""" determines the currently selected coding simulation<<

		:return: currently selected announcement type
		:raises ValueError: if current type element is not found
		"""
		found_elements = self._android_hmi.layout.value.xpath(self.current_coding_field.get())
		if len(found_elements) == 0:
			raise ValueError(f"current coding element not found: {self.current_coding_field.get()}")
		text = found_elements[0].attrib['text']
		parts = text.replace("<<", ">>").split(">>")
		if self.available_coding_types is None:
			self.available_coding_types = text.replace(">>", "").replace("<<", "").replace(" ]", "").replace("Coding Simulation Mode [ ", "").split(" | ")
		return parts[1]

	def _action(self) -> bool:
		"""Set radio coding simulation.

		:return: True if success, else false
		"""
		coding = self.values.get("CODING", "")
		try: # pylint: disable=too-many-try-statements
			current_coding = self.get_current_coding()
			# print(current_coding, self.available_coding_types)
			if current_coding != coding:
				if coding not in self.available_coding_types:
					self._reporting.add_report_message_ta_error(f"'{coding}' is not an available coding {self.available_coding_types}'")
					return False
				target_index = self.available_coding_types.index(coding)
				current_index = self.available_coding_types.index(current_coding)
				step = 20
				while (current_index != target_index) and (step > 0):
					step -= 1
					self._android_hmi.click_element(xpath=self.previous_type_button.get() if target_index < current_index else self.next_type_button.get())
					time.sleep(2)
					current_index = self.available_coding_types.index(self.get_current_coding())
				if step == 0:
					self._reporting.add_report_message_ta_error(f"could not reach '{coding}' in 20 steps'")
					return False
			self._android_hmi.click_element(xpath=self.trigger_restart_button.get())
			time.sleep(5)
		except ValueError as error:
			self._reporting.add_report_message_system_error(error)
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException:
			self._reporting.add_report_message_system_error("Failed to Click on Android HMI")
			return False
		self._reporting.add_report_message_pass(f"Coding {coding} is active and restart was triggered")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class GemSetRadioManager(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Stimulation set simulated radio station lists """

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface) -> None:
		"""Constructor of stimulation to set simulated radio station lists

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		:param menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, menu_navigation=menu_navigation, android_hmi=android_hmi)
		self.allowed_parameter_keys = ["MODE"]
		self.current_coding_field = xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_GENERAL_RADIOMANAGER_SIMULATION_MODE
		self.next_type_button = xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_GENERAL_RADIOMANAGER_SIMULATION_MODE_NEXT_BUTTON
		self.previous_type_button = xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_GENERAL_RADIOMANAGER_SIMULATION_MODE_PREVIOUS_BUTTON
		self.trigger_restart_button = xpaths_radio.SETTINGS_CUSTOM_BL_GEMS_GENERAL_CODING_SIMULATION_TRIGGER_RESTART_BUTTON
		self.available_coding_types = None
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _precondition(self) -> bool:
		"""Navigate to radio settings custum bl gems general screen.

		:return: True if success, else False
		"""
		return self._go_to_screen(destination=contents_radio.SETTINGS_CUSTOM_BL_GEMS_GENERAL)

	def get_current_mode(self) -> str:
		""" determines the currently selected simulation mode<<

		:return: currently selected announcement type
		:raises ValueError: if current type element is not found
		"""
		found_elements = self._android_hmi.layout.value.xpath(self.current_coding_field.get())
		if len(found_elements) == 0:
			raise ValueError(f"current mode not found: {self.current_coding_field.get()}")
		text = found_elements[0].attrib['text']
		parts = text.replace("<<", ">>").split(">>")
		if self.available_coding_types is None:
			self.available_coding_types = text.replace(">>", "").replace("<<", "").replace(" ]", "").replace("RadioManager Simulation Mode [ ", "").split(" | ")
		return parts[1]

	def _action(self) -> bool:
		"""Set radio station list simulation mode.

		:return: True if success, else false
		"""
		mode = self.values.get("MODE", "")
		try: # pylint: disable=too-many-try-statements
			current_mode = self.get_current_mode()
			if current_mode != mode:
				if mode not in self.available_coding_types:
					self._reporting.add_report_message_ta_error(f"'{mode}' is not an available simulation mode {self.available_coding_types}'")
					return False
				target_index = self.available_coding_types.index(mode)
				current_index = self.available_coding_types.index(current_mode)
				step = 20
				while (current_index != target_index) and (step > 0):
					step -= 1
					self._android_hmi.click_element(xpath=self.previous_type_button.get() if target_index < current_index else self.next_type_button.get())
					time.sleep(2)
					current_index = self.available_coding_types.index(self.get_current_mode())
				if step == 0:
					self._reporting.add_report_message_ta_error(f"could not reach '{mode}' in 20 steps'")
					return False
			self._android_hmi.click_element(xpath=self.trigger_restart_button.get())
			time.sleep(5)
		except ValueError as error:
			self._reporting.add_report_message_system_error(error)
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException:
			self._reporting.add_report_message_system_error("Failed to Click on Android HMI")
			return False
		self._reporting.add_report_message_pass(f"Mode {mode} is active and restart was triggered")
		return True
