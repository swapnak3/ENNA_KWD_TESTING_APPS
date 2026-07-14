# -*- coding: utf-8 -*-
"""Created on 01.03.2024.

@project: enna_kwd_testing.
@author: SPLATZP: Platzer Pascal.
"""
import logging

import enna.core.component_system.decorators
import enna.core.exceptions
import enna.data_interfaces.rsi.exceptions
import enna.data_interfaces.rsi.interface
import enna_st12.instance_names

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
from enna_kwd_testing.utilities.helper.notifications_data import get_warning_notification_data

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.rsi", instance_name=enna_st12.instance_names.Rsi.MAIN_UNIT)
class CreateRsiElementDriverNotificationNotification(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing stimulation to create DriverNotification/notifications service via rsi data interface."""

	def __init__(self, reporting, rsi: enna.data_interfaces.rsi.interface.Interface):
		"""Initialize keyword stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param enna.data_interfaces.rsi.interface.Interface rsi: Instance of rsi interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.1")
		self.__rsi = rsi

	def _action(self) -> bool:
		"""Execute action.

		1. Get DriverNotification/notifications data
		2. Create DriverNotification/notifications service via rsi data interface.

		:return: True if value was set correctly, False otherwise
		:rtype: bool
		"""

		str__warn_id = self.values["WARN_ID"]

		dict__warning_notification_data = get_warning_notification_data(str__warn_id)

		try:
			self.__rsi.create_element("DriverNotification/notifications",
									  {"name": dict__warning_notification_data["warn_id"],
									   "classification": dict__warning_notification_data["classification"],
									   "notificationId": dict__warning_notification_data["notificationId"],
									   "presentationState": dict__warning_notification_data["presentationState"],
									   "priority": dict__warning_notification_data["priority"],
									   "shownAt": dict__warning_notification_data["shownAt"],
									   "userConfirmationRequired": dict__warning_notification_data["userConfirmationRequired"]})

		except (enna.core.exceptions.EventNotFoundException, enna.data_interfaces.rsi.exceptions.RSIException, KeyError) as exception:
			self._reporting.add_report_message_system_error(f"{exception}: The RSI Server did not react, value can not be post with Service '{str__warn_id}'.")
			return False

		self._reporting.add_report_message_pass(f"The Service DriverNotification.notifications with '{str__warn_id}' is set.")

		return True
