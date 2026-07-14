# coding=utf-8
"""Module contains stimulation for set primary user."""
import time
import logging

import enna.core.exceptions
import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.data_interfaces.adb.interface
import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.rsi.exceptions
import enna.data_interfaces.rsi.interface

import enna_st12.instance_names
import enna_st12.data_interfaces.android_hmi.interface

from enna_hcp_configuration.android.xpaths import user_management
import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.stimulations.adb
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 10.0
WAIT_AFTER_CLICK = 1.0
WAIT_AFTER_USER_CHANGE = 30.0

PRIMARY_USER = 'primaryUser'
GUEST_USER = 'anonymousGuestUser'

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.rsi", instance_name=enna_st12.instance_names.Rsi.MAIN_UNIT)
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetUser(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Send adb shell command to test bench."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface, rsi: enna.data_interfaces.rsi.interface.Interface,
	             android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation to send an android debug bridge shell command.

		:param reporting: instance of reporting handler
		:param adb: instance of interface to android debug bridge
		:param enna.data_interfaces.rsi.interface.Interface rsi: Instance of rsi interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		"""

		super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.3")
		self._reporting = reporting
		self._adb = adb
		self._rsi = rsi
		self._android_hmi = android_hmi
		self.allowed_parameter_keys = ["STATE","USER"] # parameter is marked as deprecated and will not be used
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Execute action.
		Send "setenforce 0" to shell of android debug bridge to enable rsi query
		Query usermanagement.settings.activeUser.name to determine active user
		Query usermanagement.users to determine role of active user

		:return: True if success, else false.
		"""

		command = "setenforce 0"
		requested_role=self.values.get("USER",PRIMARY_USER)

		try:
			self._adb.execute_shell_command(command=command, timeout=DEFAULT_TIMEOUT)
		except enna.data_interfaces.adb.exceptions.ADBException as error:
			self._reporting.add_report_message_warning(f"RSI Query for active user might fail because of error sending adb shell command '{command}' Error: {error}")

		try:
			settings = self._rsi.get("usermanagement/settings")
			username=settings[0]["activeUser"]["name"]
			users = self._rsi.get("usermanagement/users")
		except (enna.core.exceptions.EventNotFoundException, enna.data_interfaces.rsi.exceptions.RSIException, IndexError, KeyError) as exception:
			self._reporting.add_report_message_warning(f"{exception}: The RSI Server did not react, user could not be checked, so there is a risk this testcase might fail.")
			return True

		available_users=[]
		current_user_role = None
		role_user = None

		for user_attributes in users:
			available_users.append(f'{user_attributes["name"]} ({user_attributes["role"]})')
			if user_attributes["role"].upper()==requested_role.upper():
				role_user = user_attributes["name"]
			if user_attributes["name"]==username:
				current_user_role = user_attributes["role"]
		self._reporting.add_report_message_info(f"Available users: {available_users}")
		if current_user_role.upper()==requested_role.upper():
			self._reporting.add_report_message_pass(f"The currently active user {username} is already {current_user_role}. No user change will be done.")
			return True

		if role_user is None:
			self._reporting.add_report_message_ta_error(f"No user with role '{requested_role}' available on this testcube.")
			return False

		if role_user=="#defaultUser":
			self._reporting.add_report_message_ta_error(f"user '{role_user}' cannot be selected")
			return False

		select_user_button = user_management.SELECT_GUEST_USER_BUTTON.get() if requested_role==GUEST_USER else user_management.SELECT_USER_BUTTON.get()+f"[@text='{role_user}']"

		wrapper_android_hmi.wait_and_click(user_management.USER_BUTTON.get(), self._android_hmi, self._reporting)
		time.sleep(WAIT_AFTER_CLICK)
		wrapper_android_hmi.wait_and_click(select_user_button, self._android_hmi, self._reporting)
		time.sleep(WAIT_AFTER_CLICK)
		wrapper_android_hmi.wait_and_click(user_management.CHANGE_USER_BUTTON.get(), self._android_hmi, self._reporting)
		time.sleep(WAIT_AFTER_USER_CHANGE)

		if requested_role==GUEST_USER:
			for _ in range(4): # click away upcoming popups
				wrapper_android_hmi.wait_and_click(user_management.POPUP_CLOSE_BUTTON.get(), self._android_hmi, self._reporting)

		try:
			settings = self._rsi.get("usermanagement/settings")
			username = settings[0]["activeUser"]["name"]
		except (enna.core.exceptions.EventNotFoundException, enna.data_interfaces.rsi.exceptions.RSIException, KeyError) as exception:
			self._reporting.add_report_message_warning(f"{exception}: The RSI Server did not react, user could not be checked, so there is a risk this testcase might fail.")
			return True

		if username == role_user:
			self._reporting.add_report_message_pass(f"The currently active user is {username} ({requested_role}). User switch was successful.")
			return True

		self._reporting.add_report_message_ta_error(f"Switch user to {role_user} ({requested_role}) failed.")
		return False


#		self._reporting.add_report_message_pass(f"The role of the currently active user could not be determined. Continuing anyway.")
#		return True
