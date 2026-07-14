# -*- coding: utf-8 -*-
"""Created on 19.10.2023.
   Changed on 04.06.2024 for CL46 TEC

@project: enna_kwd_testing.
@author: SPLATZP: PASCAL PLATZER.

Contains stimulations for keyword driven testing in context of android_hmi time values.
"""
import logging
from datetime import datetime

import enna.core.component_system.decorators
import enna.core.time
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import car

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi
from enna_kwd_testing.utilities.helper.time import next_date_by_weekday, get_date_by_type

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=consider-ternary-expression, too-many-branches


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetSpecificDateInSystem(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to set time."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self.__month_list = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember",
							 "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		self._str_time = 7
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["DATE"]

	def _action(self) -> bool:
		"""Execute action.

		Set Time for target to value defined in instance attribute "values" under key "DATE".

		:return: True if successful, False it susan exception occurs
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		try:
			str_date = self.values["DATE"]
			if str_date in {"YESTERDAY", "TODAY", "TOMORROW"}:
				str_date = str(get_date_by_type(str_date))
				str_year, str_month_number, str_day = str_date.split("-")
			else:
				str_year, str_month_number, str_day = str_date.split("-")
		except KeyError as e:
			MODULE_LOGGER.info(f"{e}: No key 'DATE' set, continue with key 'DAY'. ")
		try:
			str_day_value = self.values["WEEKDAY"]
			str_date = str(next_date_by_weekday(str_day_value))
			str_year, str_month_number, str_day = str_date.split("-")
		except KeyError as e:
			MODULE_LOGGER.info(f"{e}: No key 'DAY' set, continue with key 'DATE'. ")

		str_month = self.__month_list[int(str_month_number) - 1]

		MODULE_LOGGER.info(f"The date '{str_date}' will be set.")

		if not wrapper_android_hmi.go_to_screen(car.SETTINGS_SYSTEM_DATE_AND_TIME, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'car.SETTINGS_SYSTEM_DATE_AND_TIME'. Something went wrong while navigating to screen.")
			return False

		str__xpath_date_time_subtext = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.DATE_TIME_SUBTEXT")
		str__hcp3_day, str__hcp3_month, str__hcp3_year = self.__android_hmi.layout.value.xpath(str__xpath_date_time_subtext)[0].attrib["text"].split(" ")[0].split(".")

		if int(str__hcp3_day) == int(str_day):
			if int(str__hcp3_month) == int(str_month_number):
				if int(str__hcp3_year) == int(str_year):
					MODULE_LOGGER.info(f"The time '{str_day}.{str_month_number}.{str_year}' is already set to '{str__hcp3_day}.{str__hcp3_month}.{str__hcp3_year}'.")
					return True
		MODULE_LOGGER.info(f"The time '{str_day}.{str_month_number}.{str_year}' is not set to '{str__hcp3_day}.{str__hcp3_month}.{str__hcp3_year}'.")

		str__xpath_switch_set_automatic = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.SWITCH_SET_AUTOMATIC")
		if self.__android_hmi.layout.value.xpath(str__xpath_switch_set_automatic)[0].attrib["checked"] == "true":
			if not wrapper_android_hmi.wait_and_click(str__xpath_switch_set_automatic, self.__android_hmi, self._reporting):
				self._reporting.add_report_message_ta_error(f"Could not click element: {str__xpath_switch_set_automatic}.")
				return False

		if not wrapper_android_hmi.go_to_screen(car.SETTINGS_SYSTEM_DATE_AND_TIME_MANUALLY, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'car.SETTINGS_SYSTEM_DATE_AND_TIME_MANUALLY'. Something went wrong while navigating to screen.")
			return False

		if not self._set_year(str_year):
			return False

		if not self._set_month(str_month):
			return False

		if not self._set_day(str_day):
			return False

		if not wrapper_android_hmi.go_to_screen(car.SETTINGS_SYSTEM_DATE_AND_TIME, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'car.SETTINGS_SYSTEM_DATE_AND_TIME'. Something went wrong while navigating to screen.")
			return False

		MODULE_LOGGER.info(f"The date '{str_date}' is set.")

		return True

	def _set_day(self, str_day: str) -> bool:
		"""Set the day.

		:param str_day: as string
		:return: True if successful, False if day has not set
		:rtype: bool
		"""

		str_xpath_day = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.LABEL_DAY")
		if not wrapper_android_hmi.element_exists(str_xpath_day, self.__android_hmi, max_time=self._str_time):
			MODULE_LOGGER.error(f"Element: '{str_xpath_day}' is not visible.")
			return False
		str_xpath_date_day = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.DATE_DAY")
		str_xpath_button_up_day = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.BUTTON_UP_DAY")
		str_xpath_button_down_day = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.BUTTON_DOWN_DAY")
		for _ in range(32):
			enna.core.time.sleep(1.5)
			day = self.__android_hmi.layout.value.xpath(str_xpath_date_day)[0].attrib["text"].replace("\u200b", "")
			if int(str_day) == int(day):
				break
			int__str_day = int(str_day) + 31
			int__day = int(day)
			if 31 > (int__str_day - int__day) > 15:
				if not wrapper_android_hmi.element_exists(str_xpath_button_up_day, self.__android_hmi, max_time=self._str_time):
					MODULE_LOGGER.error(f"Element: '{str_xpath_button_up_day}' is not visible.")
					return False
				self.__android_hmi.swipe_element(str_xpath_button_up_day, enna_st12.data_interfaces.android_hmi.Direction.Down, scale=1.0)
			else:
				if not wrapper_android_hmi.element_exists(str_xpath_button_down_day, self.__android_hmi, max_time=self._str_time):
					MODULE_LOGGER.error(f"Element: '{str_xpath_button_down_day}' is not visible.")
					return False
				self.__android_hmi.swipe_element(str_xpath_button_down_day, enna_st12.data_interfaces.android_hmi.Direction.Up, scale=1.0)
		return True

	def _set_month(self, str_month: str) -> bool:
		"""Set the day.

		:param str_month: as string
		:return: True if successful, False if day has not set
		:rtype: bool
		"""

		str_xpath_date_month = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.DATE_MONTH")
		str_xpath_button_up_month = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.BUTTON_UP_MONTH")
		str_xpath_button_down_month = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.BUTTON_DOWN_MONTH")
		for _ in range(26):
			enna.core.time.sleep(1.5)
			month = self.__android_hmi.layout.value.xpath(str_xpath_date_month)[0].attrib["text"].replace("\u200b", "")
			int_month = self.__month_list.index(month) % 12
			int_str_month = (self.__month_list.index(str_month) % 12) + 24
			if int_month == int_str_month - 24:
				break
			if 24 > (int_str_month - int_month) > 12:
				if not wrapper_android_hmi.element_exists(str_xpath_button_up_month, self.__android_hmi, max_time=self._str_time):
					MODULE_LOGGER.error(f"Element: '{str_xpath_button_up_month}' is not visible.")
					return False
				self.__android_hmi.swipe_element(str_xpath_button_up_month, enna_st12.data_interfaces.android_hmi.Direction.Down, scale=1.0)
			else:
				if not wrapper_android_hmi.element_exists(str_xpath_button_down_month, self.__android_hmi, max_time=self._str_time):
					MODULE_LOGGER.error(f"Element: '{str_xpath_button_down_month}' is not visible.")
					return False
				self.__android_hmi.swipe_element(str_xpath_button_down_month, enna_st12.data_interfaces.android_hmi.Direction.Up, scale=1.0)
		return True

	def _set_year(self, str_year: str) -> bool:
		"""Set the day.

		:param str_year: as string
		:return: True if successful, False if day has not set
		:rtype: bool
		"""

		str_xpath_date_year = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.DATE_YEAR")
		if not wrapper_android_hmi.element_exists(str_xpath_date_year, self.__android_hmi, max_time=self._str_time):
			MODULE_LOGGER.error(f"Element: '{str_xpath_date_year}' is not visible.")
			return False

		str_year_car = self.__android_hmi.layout.value.xpath(str_xpath_date_year)[0].attrib["text"]
		if int(str_year) < int(str_year_car):
			direction = enna_st12.data_interfaces.android_hmi.Direction.Down
		else:
			direction = enna_st12.data_interfaces.android_hmi.Direction.Up
		str_xpath_button_down_year = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.BUTTON_DOWN_YEAR")
		int_range_year = int(abs(int(str_year) - int(str_year_car)) * 2.5)
		if str_year != str_year_car:
			for _ in range(int_range_year):
				enna.core.time.sleep(1.5)
				str_year_car = self.__android_hmi.layout.value.xpath(str_xpath_date_year)[0].attrib["text"].replace("\u200b", "")
				if int(str_year) == int(str_year_car):
					break
				if not wrapper_android_hmi.element_exists(str_xpath_button_down_year, self.__android_hmi, max_time=self._str_time):
					MODULE_LOGGER.error(f"Element: '{str_xpath_button_down_year}' is not visible.")
					return False
				self.__android_hmi.swipe_element(str_xpath_button_down_year, direction, scale=1.0)
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetSpecificTime(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to set time in settings -> system -> time."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self._str_time = 7
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["HOUR", "MINUTE"]

	def _action(self) -> bool:
		"""Execute action.

		1. Navigate to 'settings -> system -> time -> date time manually'
		2. Set Time for target to value defined in instance attribute "values" under key "DATE".

		:return: True if successful, False it susan exception occurs
		:rtype: bool
		"""
		MODULE_LOGGER.info(f"EXECUTING KEYWORD CLASS: '{self.__class__}'")
		MODULE_LOGGER.info(f"USING VALUES FOR EXECUTION: '{self.values}'")

		# initialize values
		str__hour = ""
		str__minute = ""

		try:
			str__hour = self.values["HOUR"]
			str__minute = self.values["MINUTE"]
		except KeyError as exception:
			self._reporting.add_report_message_ta_error(f"Value {exception} not found")

		MODULE_LOGGER.info(f"The time '{str__hour}:{str__minute}' will be set.")

		if not wrapper_android_hmi.go_to_screen(car.SETTINGS_SYSTEM_DATE_AND_TIME, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'car.SETTINGS_SYSTEM_DATE_AND_TIME'. Something went wrong while navigating to screen.")
			return False
		str__xpath_date_time_subtext = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.DATE_TIME_SUBTEXT")
		str__hcp3_hour, str__hcp3_minute = self.__android_hmi.layout.value.xpath(str__xpath_date_time_subtext)[0].attrib["text"].split(" ")[1].split(":")

		if int(str__hcp3_hour) == int(str__hour):
			if int(str__hcp3_minute) == int(str__minute):
				MODULE_LOGGER.info(f"The time '{str__hour}:{str__minute}' is already set.")
				return True

		str__xpath_switch_set_automatic = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.SWITCH_SET_AUTOMATIC")
		if self.__android_hmi.layout.value.xpath(str__xpath_switch_set_automatic)[0].attrib["checked"] == "true":
			if not wrapper_android_hmi.wait_and_click(str__xpath_switch_set_automatic, self.__android_hmi, self._reporting):
				self._reporting.add_report_message_ta_error(f"Could not click element: {str__xpath_switch_set_automatic}.")
				return False

		if not wrapper_android_hmi.go_to_screen(car.SETTINGS_SYSTEM_DATE_AND_TIME_MANUALLY, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'car.SETTINGS_SYSTEM_DATE_AND_TIME_MANUALLY'. Something went wrong while navigating to screen.")
			return False

		if not self.set_hour(str__hour):
			return False

		if not self.set_minute(str__minute):
			return False

		if not wrapper_android_hmi.go_to_screen(car.SETTINGS_SYSTEM_DATE_AND_TIME, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'car.SETTINGS_SYSTEM_DATE_AND_TIME'. Something went wrong while navigating to screen.")
			return False

		MODULE_LOGGER.info(f"The time '{str__hour}:{str__minute}' is set.")

		return True

	def set_hour(self, str__hour: str) -> bool:
		"""Set the hour.

		:param str__hour: as string
		:return: True if successful, False if hour not set
		:rtype: bool
		"""

		str_xpath_hour = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.TIME_HOURS")
		if not wrapper_android_hmi.element_exists(str_xpath_hour, self.__android_hmi, max_time=self._str_time):
			MODULE_LOGGER.error(f"Element: '{str_xpath_hour}' is not visible.")
			return False
		str_xpath_button_up_hour = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.BUTTON_UP_HOURS")
		str_xpath_button_down_hour = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.BUTTON_DOWN_HOURS")
		for _ in range(25):
			enna.core.time.sleep(1.5)
			hour = self.__android_hmi.layout.value.xpath(str_xpath_hour)[0].attrib["text"].replace("\u200b", "")
			if int(str__hour) == int(hour):
				break
			int__str_hour = int(str__hour) + 24
			int__hour = int(hour)
			if 24 > (int__str_hour - int__hour) > 12:
				if not wrapper_android_hmi.element_exists(str_xpath_button_up_hour, self.__android_hmi, max_time=self._str_time):
					MODULE_LOGGER.error(f"Element: '{str_xpath_button_up_hour}' is not visible.")
					return False
				self.__android_hmi.swipe_element(str_xpath_button_up_hour, enna_st12.data_interfaces.android_hmi.Direction.Down, scale=1.0)
			else:
				if not wrapper_android_hmi.element_exists(str_xpath_button_down_hour, self.__android_hmi, max_time=self._str_time):
					MODULE_LOGGER.error(f"Element: '{str_xpath_button_down_hour}' is not visible.")
					return False
				self.__android_hmi.swipe_element(str_xpath_button_down_hour, enna_st12.data_interfaces.android_hmi.Direction.Up, scale=1.0)
		return True

	def set_minute(self, str__minute: str) -> bool:
		"""Set the minute.

		:param str__minute: as string
		:return: True if successful, False if minute not set
		:rtype: bool
		"""

		str_xpath_date_minutes = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.TIME_MINUTES")
		str_xpath_button_up_minutes = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.BUTTON_UP_MINUTES")
		str_xpath_button_down_minutes = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.BUTTON_DOWN_MINUTES")

		for _ in range(61):
			enna.core.time.sleep(1.5)
			minute = self.__android_hmi.layout.value.xpath(str_xpath_date_minutes)[0].attrib["text"].replace("\u200b", "")
			if int(str__minute) == int(minute):
				break
			int__str_minute = int(str__minute) + 60
			int__minute = int(minute)
			if 60 > (int__str_minute - int__minute) > 30:
				if not wrapper_android_hmi.element_exists(str_xpath_button_up_minutes, self.__android_hmi, max_time=self._str_time):
					MODULE_LOGGER.error(f"Element: '{str_xpath_button_up_minutes}' is not visible.")
					return False
				self.__android_hmi.swipe_element(str_xpath_button_up_minutes, enna_st12.data_interfaces.android_hmi.Direction.Down, scale=1.0)
			else:
				if not wrapper_android_hmi.element_exists(str_xpath_button_down_minutes, self.__android_hmi, max_time=self._str_time):
					MODULE_LOGGER.error(f"Element: '{str_xpath_button_down_minutes}' is not visible.")
					return False
				self.__android_hmi.swipe_element(str_xpath_button_down_minutes, enna_st12.data_interfaces.android_hmi.Direction.Up, scale=1.0)
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetTimeFormatInSystem(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to time in settings -> system -> time."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="settings")
		self.allowed_parameter_keys = ["HOUR", "MINUTE"]

	def _action(self) -> bool:
		"""Execute action.

		1. Navigate to 'settings -> system -> date&time -> 24h-Timeformat'
		2. Change the value-button 12-24h

		:return: True if successful, False it susan exception occurs
		:rtype: bool
		"""

		toggle_button = self.__xpathloader.get_xpath("unknown", "car.TIME_FORMAT")
		time_settings_list = self.__xpathloader.get_xpath("unknown", "car.TIME_CONTAINER")

		if not wrapper_android_hmi.go_to_screen(car.SETTINGS_SYSTEM_DATE_AND_TIME_MANUALLY, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'car.SETTINGS_SYSTEM_DATE_AND_TIME_MANUALLY'. Something went wrong while navigating to screen.")
			return False

		enna.core.time.sleep(2)
		self.__android_hmi.scroll_list_to_bottom(time_settings_list)

		if self.values["FORMAT"] == "12h":
			wrapper_android_hmi.wait_and_set_toggle_button_state(toggle_button, False, self.__android_hmi, reporting=self._reporting)
		elif self.values["FORMAT"] == "24h":
			wrapper_android_hmi.wait_and_set_toggle_button_state(toggle_button, True, self.__android_hmi, reporting=self._reporting)
		else:
			return False

		if not wrapper_android_hmi.go_to_screen(car.SETTINGS_SYSTEM_DATE_AND_TIME, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'car.SETTINGS_SYSTEM_DATE_AND_TIME'. Something went wrong while navigating to screen.")
			return False

		MODULE_LOGGER.info(f"Time format: {self.values['FORMAT']} is set.")

		return True


def _get_current_hour() -> str:
	"""Get the hour of the current time.

	:return: The hour of the current time as str value.
	:rtype: string """

	now = datetime.now()

	current_hour = now.strftime("%H")
	return current_hour


def _get_current_minute() -> str:
	"""Get the minute of the current time.

	:return: The minute of the current time as str value.
	:rtype: string """

	now = datetime.now()

	current_minute = now.strftime("%M")
	return current_minute


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetCurrentTime(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set the current time in system settings.

	parameter HOUR: NOW for the current time, or a number between 0 and 23
			MINUTE: MOW for the current time, or a number between 0 and 59 """

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self._str_time = 10
		self._str_current_hour = ""
		self._str_current_minute = ""
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler
		self.allowed_parameter_keys = ["HOUR", "MINUTE"]

	def _action(self) -> bool:
		"""Execute action.

		Set the current time in system settings.

		1. Check given parameters for HOUR, MINUTE.
		2. Navigate to 'car.SETTINGS_SYSTEM_DATE_TIME' screen.
		3. Check if time is already set.
		4. Set the switch to manual set time.
		5. Navigate to 'car.SETTINGS_SYSTEM_DATE_TIME_MANUALLY' screen.
		6. Set HOUR and MINUTE

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		enna_kwd_testing.utilities.helper.android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)

		# check the parameter values for HOUR and MINUTE
		str_hour = str(self.values.get("HOUR", "NOW"))
		if str_hour == "NOW":
			self._str_current_hour = _get_current_hour()
		elif int(str_hour) < 0 or int(str_hour) > 23:
			MODULE_LOGGER.error(f"Wrong parameter for HOUR:'{str_hour}', should be 'NOW' or a number between 0 and 23.")
			return False
		else:
			self._str_current_hour = str_hour

		str_minute = str(self.values.get("MINUTE", "NOW"))
		if str_minute == "NOW":
			self._str_current_minute = _get_current_minute()
		elif int(str_minute) < 0 or int(str_minute) > 59:
			MODULE_LOGGER.error(f"Wrong parameter for MINUTE:'{str_minute}', should be 'NOW' or a number between 0 and 59.")
			return False
		else:
			self._str_current_minute = str_minute

		MODULE_LOGGER.info(f"Current time '{self._str_current_hour}:{self._str_current_minute}' will set.")

		if not wrapper_android_hmi.go_to_screen(car.SETTINGS_SYSTEM_DATE_AND_TIME, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'SYSTEM_DATE_TIME -> SYSTEM. Something went wrong while navigating to screen.")
			return False

		str__xpath_date_time_subtext = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.DATE_TIME_SUBTEXT")
		str__hcp3_hour, str__hcp3_minute = self.__android_hmi.layout.value.xpath(str__xpath_date_time_subtext)[0].attrib["text"].split(" ")[1].split(":")

		if int(str__hcp3_hour) == int(self._str_current_hour):
			MODULE_LOGGER.info(f"The hour of time '{self._str_current_hour}' is already set.")
			if int(str__hcp3_minute) == int(self._str_current_minute):
				MODULE_LOGGER.info(f"The hour and minute of time '{self._str_current_hour}:{self._str_current_minute}' is already set.")
				return True

		str__xpath_switch_set_automatic = self.__xpathloader.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self.__android_hmi, element="car.SWITCH_SET_AUTOMATIC")
		if self.__android_hmi.layout.value.xpath(str__xpath_switch_set_automatic)[0].attrib["checked"] == "true":
			if not wrapper_android_hmi.wait_and_click(str__xpath_switch_set_automatic, self.__android_hmi, self._reporting):
				self._reporting.add_report_message_ta_error(f"Could not click element: {str__xpath_switch_set_automatic}.")
				return False

		if not wrapper_android_hmi.go_to_screen(car.SETTINGS_SYSTEM_DATE_AND_TIME_MANUALLY, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'car.SETTINGS_SYSTEM_DATE_AND_TIME_MANUALLY -> SYSTEM. Something went wrong while navigating to screen.")
			return False

		specific_time = SetSpecificTime(reporting=self._reporting, android_hmi=self.__android_hmi, menu_navigation=self.__menu_navigation)
		if str_hour == "NOW":
			tries = 3
			while tries > 0:
				tries -= 1
				self._str_current_hour = _get_current_hour()
				if not specific_time.set_hour(self._str_current_hour):
					return False
		elif not specific_time.set_hour(self._str_current_hour):
			return False

		if str_minute == "NOW":
			tries = 3
			while tries > 0:
				tries -= 1
				self._str_current_minute = _get_current_minute()
				if not specific_time.set_minute(self._str_current_minute):

					return False
		elif not specific_time.set_minute(self._str_current_minute):
			return False

		if not wrapper_android_hmi.go_to_screen(car.SETTINGS_SYSTEM_DATE_AND_TIME, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'car.SETTINGS_SYSTEM_DATE_AND_TIME'. Something went wrong while navigating to screen.")
			return False

		MODULE_LOGGER.info(f"Current time '{self._str_current_hour}:{self._str_current_minute}' is set.")

		return True
