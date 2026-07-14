# -*- coding: utf-8 -*-
"""Module contains stimulation of general touching and checking methods on android hmi system."""
import logging
import time

import enna.core.component_system.decorators
import enna.core.config
import enna.core.exceptions
import enna.core.image_processing.helper
import enna.core.image_processing.image
import enna.core.reporting.interface
import enna_st12.data_interfaces.android_hmi
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.data_interfaces.android_hmi.helper
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.instance_names
import enna_st12.utilities.menu_navigation.exceptions
import enna_st12.utilities.menu_navigation.interface

import enna_hcp_configuration.common.base

import enna_kwd_testing.stimulations.apps._internal
import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.exceptions
import enna_kwd_testing.utilities.xpath_collection.helper

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=protected-access too-many-try-statements
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class NavigateToScreen(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Class containing stimulation to navigate to screen."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Initialize stimulation.

		:param reporting: Instance of reporting interface.
		:param menu_navigation: menu navigation interface
		:param android_hmi: ui-automator interface
		"""
		super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, menu_navigation=menu_navigation, android_hmi=android_hmi)
		self._destination: enna_hcp_configuration.common.base.Element | None = None
		self.allowed_parameter_keys = ["SCREEN_NAME"]
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")
		MODULE_LOGGER.info("Stimulation of menu navigation is initialized!")


	def _precondition(self) -> bool:
		"""Execute Pre-Condition.
		Find destination context.

		:return: True if success, else False
		"""
		try:
			self._destination = self._get_destination_context(self.values["SCREEN_NAME"])
		except enna_st12.utilities.menu_navigation.exceptions.MenuNavigationException:
			return False
		return True

	def _action(self) -> bool:
		"""Execute Action.
		Navigate to screen.

		:return: True if success, else False
		"""
		return self._go_to_screen(self._destination)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckScreenIsVisible(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class contains stimulation to check current screen is visible."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Initialization of stimulation	

		:param reporting: Instance of reporting interface.
		:param android_hmi: ui-automator interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__android_hmi = android_hmi
		self.allowed_parameter_keys = ["SCREEN_NAME", "TIMEOUT"]
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Check is current screen is expected screen.

		:return: True if successful, False if an error occurs in any step.
		"""
		expected_screen = self.values.get("SCREEN_NAME", "'missing expected value!'").lower()
		start = time.time()
		try:
			self.__android_hmi.screen_id.wait_for_value(expected_screen, max_time=self.values.get("TIMEOUT", 3.0))
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_ta_error(f"Error by checking screen! {error}")
			return False
		except  enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error(f"Expected screen not equal current screen! Expected: '{expected_screen}'; Current screen '{self.__android_hmi.screen_id.value}'. Duration of timeout {time.time() - start} seconds.")
			return False
		self._reporting.add_report_message_pass(f"Expected screen '{expected_screen}' == current screen '{self.__android_hmi.screen_id.value}'. Duration of visible {time.time() - start} seconds.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckScreenIsNotVisible(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class contains stimulation to check current screen is not visible."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Initialization of stimulation

		:param reporting: Instance of reporting interface.
		:param android_hmi: ui-automator interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__android_hmi = android_hmi
		self.allowed_parameter_keys = ["SCREEN_NAME", "TIMEOUT"]
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Check is current screen not equal unexpected screen.

		:return: True if successful, False if an error occurs in any step.
		"""
		unexpected_screen = self.values.get("SCREEN_NAME", "'missing expected value!'").lower()
		start = time.time()
		max_time = float(self.values.get("TIMEOUT", 3.0))

		try:
			self.__android_hmi.wait_for_event("screen_id", condition=lambda msg: self.__android_hmi.screen_id.value != unexpected_screen, max_time=max_time)
			self.__android_hmi.wait_for_event("screen_id", condition=lambda msg: self.__android_hmi.screen_id.value != "" and "unknown" not in self.__android_hmi.screen_id.value, max_time=3.0)
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_ta_error(f"Error by checking screen is not visible! {error}")
			return False
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error(f"Screen '{unexpected_screen}' is not disappear within the period {max_time} sec. Current Screen: {self.__android_hmi.screen_id.value}")
			return False
		self._reporting.add_report_message_pass(f"Forbidden screen '{unexpected_screen}' != current screen '{self.__android_hmi.screen_id.value}'. Duration of invisible '{time.time() - start}' seconds.")
		return True


# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class ClickOnElement(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Stimulation for click an element in android hmi."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: instance of report handler
		:param android_hmi: instance of android hmi control interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Click an element on android hmi context.

		:return: True if success, else False
		"""
		try:
			self._android_hmi.wait_for_element_visible(xpath=self._xpath, max_time=self._timeout)
			self._android_hmi.click_element(self._xpath)
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException:
			self._reporting.add_report_message_ta_error(f"No connection to android device! Click on element '{self.values}' is not possible.")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' not find in current screen!")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' is currently not clickable!")
			return False
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' not found in screen, during TIMEOUT: {self._timeout}!")
			return False
		self._reporting.add_report_message_pass(f"Element '{self.values}' is clicked.")
		return True


# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class LongClickOnElement(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Stimulation for click an element in android hmi."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: instance of report handler
		:param android_hmi: instance of android hmi control interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.allowed_parameter_keys.append("DURATION")
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Click an element on android hmi context.

		:return: True if success, else False
		"""
		duration = float(self.values.get("DURATION", 1.0))
		try:
			self._android_hmi.wait_for_element_visible(xpath=self._xpath, max_time=self._timeout)
			self._android_hmi.long_click_element(self._xpath, duration=duration)
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException:
			self._reporting.add_report_message_ta_error(f"No connection to android device! Click on element '{self.values}' is not possible.")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' not find in current screen!")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' is currently not clickable!")
			return False
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' not found in screen, during TIMEOUT: {self._timeout}!")
			return False
		self._reporting.add_report_message_pass(f"Element '{self.values}' is clicked.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetSwitchButtonState(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Stimulation for set state on a switch button in android hmi."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: instance of report handler
		:param android_hmi: instance of android hmi control interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.allowed_parameter_keys.append("STATE")
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""set state on a switch button in android hmi.

		:return: True if success, else False
		"""
		state = self.values.get("STATE", False)
		try:
			self._android_hmi.set_toggle_button_state(xpath=self._xpath, button_state=state)
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException:
			self._reporting.add_report_message_ta_error(f"No connection to android device! Cl on element '{self.values}' is not possible.")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			self._reporting.add_report_message_system_error(f"Switch button '{self.values}' not find in current screen!")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
			self._reporting.add_report_message_system_error(f"Switch button '{self.values}' is currently not clickable!")
			return False
		self._reporting.add_report_message_pass(f"Switch button '{self.values}' set to {state}.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetCheckBoxState(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Stimulation for set a state on check box in android hmi."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: instance of report handler
		:param android_hmi: instance of android hmi control interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.allowed_parameter_keys.append("STATE")
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""set a state on check box in android hmi.

		:return: True if success, else False
		"""
		state = self.values.get("STATE", False)
		try:
			self._android_hmi.set_checkbox_state(xpath=self._xpath, checkbox_state=state)
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException:
			self._reporting.add_report_message_ta_error(f"No connection to android device! Set Check box on element '{self.values}' is not possible.")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' not find in current screen!")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' is currently not clickable!")
			return False
		self._reporting.add_report_message_pass(f"Check box '{self.values}' is set to {state}.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckSwitchButtonState(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Stimulation for check state on switch button in android hmi."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: instance of report handler
		:param android_hmi: instance of android hmi control interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.allowed_parameter_keys.append("STATE")
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""check state on switch button in android hmi.

		:return: True if success, else False
		"""
		expected_state = self.values.get("STATE", False)
		try:
			current_state = enna_st12.data_interfaces.android_hmi.helper.get_toggle_button_state(layout=self._android_hmi.layout.value, xpath=self._xpath)
			if expected_state != current_state:
				self._reporting.add_report_message_system_error(f"Switch button state '{current_state}' not equal expected state '{expected_state}'!")
				return False
		except enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException as error:
			self._reporting.add_report_message_ta_error(f"Invalid xpath! Error: {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException as error:
			self._reporting.add_report_message_system_error(f"Missing Switch button! Error: {error}")
			return False
		self._reporting.add_report_message_pass(f"Switch button state '{current_state}' equal expected state '{expected_state}'.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckCheckBoxState(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Stimulation for check state on check box in android hmi."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface,
	             android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: instance of report handler
		:param android_hmi: instance of android hmi control interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.allowed_parameter_keys.append("STATE")
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""check state on check box in android hmi.

		:return: True if success, else False
		"""
		expected_state = self.values.get("STATE", False)
		try:
			current_state = enna_st12.data_interfaces.android_hmi.helper.get_checkbox_state(layout=self._android_hmi.layout.value, xpath=self._xpath)
			if expected_state != current_state:
				self._reporting.add_report_message_system_error(f"Check box state '{current_state}' not equal expected state '{expected_state}'!")
				return False
		except enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException as error:
			self._reporting.add_report_message_ta_error(f"Invalid xpath! Error: {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException as error:
			self._reporting.add_report_message_system_error(f"Missing Switch button! Error: {error}")
			return False
		self._reporting.add_report_message_pass(
			f"Check box state '{current_state}' equal expected state '{expected_state}'.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class DragAndDrop(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Stimulation for drag and drop a UI element in an area from screen."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: instance of report handler
		:param android_hmi: instance of android hmi control interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self._layout_area = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="launcher")
		self.allowed_parameter_keys.append("LAYOUT_AREA")
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Drag element in area in current screen.

		:return: True if success, else False
		"""
		# get coordinates
		if "COORDINATES" in self.values:
			target_coordinates = self.values["COORDINATES"]
		elif "LAYOUT_AREA" in self.values:
			xpath_layout_area: str = self.values["LAYOUT_AREA"].lower()
			try:
				xpath_layout_area = self._get_xpath_by_parameters(xpath_name=xpath_layout_area, screen_name=self._screen_name)
				target_coordinates = enna_st12.data_interfaces.android_hmi.helper.get_element_center_coordinates(layout=self._android_hmi.layout.value, xpath=xpath_layout_area)
			except enna_kwd_testing.utilities.xpath_collection.exceptions.ElementNotFound as error:
				self._reporting.add_report_message_ta_error(f"Missing layout area '{xpath_layout_area}' in Xpath Collection! {error}")
				return False
			except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException as error:
				self._reporting.add_report_message_system_error(f"Could not find drop of area in screen! {error}")
				return False
		else:
			self._reporting.add_report_message_ta_error("Missing a parameter to get drop area! Must use parameter 'COORDINATES' or 'LAYOUT_AREA'.")
			return False
		# execute drag and drop
		try:
			self._android_hmi.wait_for_element_visible(xpath=self._xpath, max_time=1.0)
			source_coordinates = enna_st12.data_interfaces.android_hmi.helper.get_element_center_coordinates(layout=self._android_hmi.layout.value, xpath=self._xpath)
			self._android_hmi.drag_coordinates(x_start=source_coordinates[0], y_start=source_coordinates[1], x_end=target_coordinates[0], y_end=target_coordinates[1], drag_time=0.5)
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error(f"Could not find element to drag! Element = '{self._xpath}'")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_system_error(f"Drag and drop could not executed! {error}")
			return False
		except (IndexError, ValueError, TypeError):
			self._reporting.add_report_message_ta_error(f"Coordinates {target_coordinates} are not correct format! Must (int: x, int: y)")
			return False
		self._reporting.add_report_message_pass(f"Drag element '{self._xpath}' from coordinates '{source_coordinates}' to coordinates '{target_coordinates}'.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetRadioButtonState(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Stimulation for set a state on radio box in android hmi."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: instance of report handler
		:param android_hmi: instance of android hmi control interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.allowed_parameter_keys.append("STATE")
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""set a state on radio box in android hmi.

		:return: True if success, else False
		"""
		target_state = self.values.get("STATE", False)

		try:
			self._android_hmi.wait_for_element_visible(xpath=self._xpath, max_time=self._timeout)
			checked_state = self._android_hmi.layout.value.xpath(self._xpath)[0].attrib["checked"] == "true"
			if target_state != checked_state:
				self._android_hmi.click_element(self._xpath)
				self._reporting.add_report_message_pass(f"Radio-Button with xpath '{self._xpath}' switched correctly to the target state '{target_state}'")
				return True
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException:
			self._reporting.add_report_message_ta_error(f"No connection to android device! Click on element '{self.values}' is not possible.")
			return False
		except (enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException, IndexError, KeyError):
			self._reporting.add_report_message_system_error(f"Element '{self.values}' not find in current screen!")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' is currently not clickable!")
			return False
		self._reporting.add_report_message_pass(f"Radio-Button with xpath '{self._xpath}' is already in the target state '{target_state}'")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckRadioButtonState(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Stimulation for check state on radio box in android hmi."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: instance of report handler
		:param android_hmi: instance of android hmi control interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.allowed_parameter_keys.append("STATE")
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""check state on radio box in android hmi.

		:return: True if success, else False
		"""
		expected_state = self.values.get("STATE", False)

		try:
			checked_state = self._android_hmi.layout.value.xpath(self._xpath)[0].attrib["checked"]
		except (KeyError, IndexError):
			self._reporting.add_report_message_system_error(f"Element '{self.values}' not find in current screen!")
			return False

		if str(expected_state).lower() != checked_state:
			self._reporting.add_report_message_ta_error(f"Radio-Button with xpath '{self._xpath}' is not in the expected state '{expected_state}'")
			return False

		self._reporting.add_report_message_pass(f"Radio-Button with xpath '{self._xpath}' is in the expected state '{expected_state}'")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class ScrollInList(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Stimulation for scroll to an element in list on android hmi context."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Scroll to an element in list on android hmi context.

		:return: True if success, else False
		"""
		try:
			self._android_hmi.wait_for_element_visible(xpath=self._get_list_container(), max_time=3.0)
			self._android_hmi.scroll_to_element_in_list(list_container_xpath=self._get_list_container(), target_xpath=self._xpath)
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException as error:
			self._reporting.add_report_message_ta_error(f"No connection to MMI! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException as error:
			self._reporting.add_report_message_ta_error(f"Invalid argument! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException as error:
			self._reporting.add_report_message_system_error(f"Scroll element '{self._xpath}' not found in screen! {error}")
			return False
		except enna.core.exceptions.TimeoutException as error:
			self._reporting.add_report_message_system_error(f"List container not found in screen! {error}")
			return False
		self._reporting.add_report_message_pass(f"Scroll to element '{self._xpath}' in list '{self._get_list_container()}' on screen!")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class ClickElementInList(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Stimulation for click an element in list on android hmi context."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android hmi interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.__android_hmi = android_hmi
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Click an element in list on android hmi context.

		:return: True if success, else False
		"""
		try:
			self.__android_hmi.wait_for_element_visible(xpath=self._get_list_container(), max_time=1.0)
			self.__android_hmi.click_element_in_list(list_container_xpath=self._get_list_container(), xpath=self._xpath)
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException as error:
			self._reporting.add_report_message_ta_error(f"No connection to MMI! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException as error:
			self._reporting.add_report_message_ta_error(f"Invalid argument! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException as error:
			self._reporting.add_report_message_system_error(f"Scroll element '{self._xpath}' not found in screen! {error}")
			return False
		except enna.core.exceptions.TimeoutException as error:
			self._reporting.add_report_message_system_error(f"List container not found in screen! {error}")
			return False
		self._reporting.add_report_message_pass(f"Scroll to element '{self._xpath}' in list '{self._get_list_container()}' on screen!")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckElementIsVisible(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Check Element is visible in UI dump."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android hmi interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.allowed_parameter_keys.append("TIMEOUT")
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Check element exist on UI dump.

		:return: True if success, else False
		"""
		try:
			timeout = self.values.get("TIMEOUT", 1.0)
			self._android_hmi.wait_for_element_visible(xpath=self._xpath, max_time=timeout)
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error(f"Element '{self._xpath}' not exist in ui dump after {timeout} seconds.")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_ta_error(f"Error by checking element '{self._xpath}'! {error}")
			return False
		self._reporting.add_report_message_pass(f"Element '{self._xpath}' exist.")
		return True

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckElementsAreVisibleInGroup(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Check if Elements are visible in a group on a UI dump."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android hmi interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.allowed_parameter_keys=["GROUP","ELEMENTS","TIMEOUT"]
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Check elements exist in a group on UI dump.

		:return: True if success, else False
		"""
		group=self.values.get("GROUP")
		elements=[element.strip() for element in self.values.get("ELEMENTS")]
		group_xpath=self._get_xpath_by_parameters(xpath_name=group)
		elements_not_found={}
		for element in elements:
			element_xpath=self._get_xpath_by_parameters(xpath_name=element)
			try:
				timeout = self.values.get("TIMEOUT", 1.0)
				self._android_hmi.wait_for_element_visible(xpath=group_xpath+element_xpath, max_time=timeout)
			except (enna.core.exceptions.TimeoutException, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException):
				elements_not_found[element]=element_xpath
		if len(elements_not_found) > 0:
			self._reporting.add_report_message_system_error(f"Elements not found: {elements_not_found}")
			return False
		self._reporting.add_report_message_pass(f"Elements [{",".join(elements)}] found.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckElementIsNotVisible(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Check Element is not visible in UI dump."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android hmi interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.allowed_parameter_keys.append("TIMEOUT")
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Check element exist on UI dump.

		:return: True if success, else False
		"""
		try:
			timeout = self.values.get("TIMEOUT", 1.0)
			self._android_hmi.wait_for_element_invisible(xpath=self._xpath, max_time=timeout)
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error(
				f"Element '{self._xpath}' exist in ui dump after {timeout} seconds.")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_ta_error(f"Error by checking element '{self._xpath}'! {error}")
			return False
		self._reporting.add_report_message_pass(f"Element '{self._xpath}' does not exist.")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckElementNotInList(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Stimulation for check element is not in list."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Try to scroll element.

		:return: True is not found, else False
		"""
		try:
			self._android_hmi.wait_for_element_visible(xpath=self._get_list_container(), max_time=3.0)
			self._android_hmi.scroll_to_element_in_list(list_container_xpath=self._get_list_container(), target_xpath=self._xpath)
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException as error:
			self._reporting.add_report_message_ta_error(f"No connection to MMI! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.InvalidArgumentException as error:
			self._reporting.add_report_message_ta_error(f"Invalid argument! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException as error:
			self._reporting.add_report_message_pass(f"Scroll element '{self._xpath}' not found in screen! {error}")
			return True
		except enna.core.exceptions.TimeoutException as error:
			self._reporting.add_report_message_system_error(f"List container not found in screen! {error}")
			return False
		self._reporting.add_report_message_system_error(f"Scroll to element '{self._xpath}' in list '{self._get_list_container()}' on screen!")
		return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckSize(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Class containing functionality to check the size of an element."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param reporting: Instance of reporting interface
		:param android_hmi: ui-automator interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.allowed_parameter_keys = ["XPATH_NAME", "WIDTH", "HEIGHT"]
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Execute action.

		Check size of an element.

		1. Check size of an element

		:return: True if successful, False if an error occurs in any step.
		"""
		element_width = int(self.values.get("WIDTH", -1))
		element_height = int(self.values.get("HEIGHT", -1))

		try:
			coordinates_size = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(layout=self._android_hmi.layout.value, xpath=self._xpath)

			if element_width == coordinates_size["width"] and element_height == coordinates_size["height"]:
				self._reporting.add_report_message_pass(f"Current Size [{coordinates_size['width']}, {coordinates_size['height']} is equal to expected size [{element_width}, {element_height}].")
				return True
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException as error:
			self._reporting.add_report_message_ta_error(f"Could not found XPath '{self._xpath}'! {error}")
			return False

		self._reporting.add_report_message_system_error(f"Current Size [{coordinates_size['width']}, {coordinates_size['height']} is not equal to expected size [{element_width}, {element_height}]!")
		return False

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class Swipe(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Class containing functionality to swipe by coordinates."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.allowed_parameter_keys = ["XPATH_NAME", "DIRECTION", "START_X", "START_Y", "STOP_X", "STOP_Y", "SCALE"]
		self.__directions = {
			"UP": enna_st12.data_interfaces.android_hmi.Direction.Up,
			"DOWN": enna_st12.data_interfaces.android_hmi.Direction.Down,
			"LEFT": enna_st12.data_interfaces.android_hmi.Direction.Left,
			"RIGHT": enna_st12.data_interfaces.android_hmi.Direction.Right
		}

	def _action(self) -> bool:
		"""Execute action.

		Swipe direction.

		1. Swipe direction by coordinates

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		MODULE_LOGGER.debug(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.debug(f"USING VALUES FOR EXECUTION: '{self.values}'")

		direction: str = self.values.get("DIRECTION", "UNKNOWN").upper()
		start_x: int = self.values.get("START_X", -1)
		start_y: int = self.values.get("START_Y", -1)
		stop_x: int = self.values.get("STOP_X", -1)
		stop_y: int = self.values.get("STOP_Y", -1)
		scale: float = self.values.get("SCALE", 0.9)

		try:
			if start_x != -1 and start_y != -1 and stop_x != -1 and stop_y != -1:
				self._android_hmi.swipe_coordinates(x_start=start_x, y_start=start_y, x_end=stop_x, y_end=stop_y, swipe_time=0.1)
			elif "XPATH_NAME" in self.values:
				self._android_hmi.wait_for_element_visible(xpath=self._xpath, max_time=1.0)
				self._android_hmi.swipe_element(xpath=self._xpath, direction=self.__directions[direction], scale=scale)
			else:
				complete_screen = f"//*[@bounds='[0,0][{self._android_hmi.window_size.value[0]},{self._android_hmi.window_size.value[1]}]']"
				self._android_hmi.swipe_element(xpath=complete_screen, direction=self.__directions[direction], scale=scale)

		except (enna.core.exceptions.TimeoutException, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as error:
			self._reporting.add_report_message_ta_error(f"Could not swipe in display! {error}")
			return False
		except KeyError:
			self._reporting.add_report_message_ta_error(f"Direction '{direction}' is not supported! Supported directions are {self.__directions.keys()}")
			return False

		self._reporting.add_report_message_ta_error("Swipe successful.")
		return True
