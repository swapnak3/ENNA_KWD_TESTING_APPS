# -*- coding: utf-8 -*-
"""Created on 28.03.2022.

@project: enna_tc_connect_apps_hcp3.
@author: DYX34ZN: Jakob Kein.
Module contains server for data_logcat utility.
"""

import logging

import enna.core.interfaces.server
import enna.data_interfaces.adb.interface
import enna_kwd_testing.utilities.data_logcat.interface

MODULE_LOGGER = logging.getLogger(__name__)


class Server(enna_kwd_testing.utilities.data_logcat.interface.Interface, enna.core.interfaces.server.Server):
	"""Server implementation of the data interface."""

	def __init__(self, instance_name: str, adb: enna.data_interfaces.adb.interface.Interface):
		"""Initialize server.

		:param str instance_name: Name of instance to initialize for server for
		:param enna.data_interfaces.adb.interface.Interface adb: adb interface
		"""
		enna_kwd_testing.utilities.data_logcat.interface.Interface.__init__(self)
		enna.core.interfaces.server.Server.__init__(self, instance_name=instance_name)

		self.__adb = adb
		self.__adb.start_logcat_reading([
			# "logcat",
			# Backup from older version -> Integrate again if performance is too bad:
			# "*:S",
			# "ConnectivityService:D",
			# "ActivityManager:I",
			# "UIAutomatorStub:V",
			# "de.eso.launcheraudi.ui.dashboard.custom.CustomTileViewModel:V",
			# "AccessControlClient:D",
			# "phone.domain.calls:I",
			# "C2P:V",
			# "ZeroConfManager:V",
		])

		self.__register()
		self._set_online()

	def __register(self):
		"""Register on all required events from adb."""
		self.__adb.register("APP_FORCE_STOP", self.__cb_app_force_stop)
		self.__adb.register("TOAST_APPEARED", self.__cb_toast_appeared)
		self.__adb.register("ACTIVE_TILES", self.__cb_active_tiles)
		self.__adb.register("UPDATE_SERVICELIST_ENTRY", self.__sl_entry_updated)
		self.__adb.register("PHONE_CALL_TRIGGERED", self.__phone_call_triggered)
		self.__adb.register("ZERO_CONF_MANAGER_STARTING", self.__zero_conf_started)
		self.__adb.register("ZERO_CONF_MANAGER_STARTING", self.__zero_conf_started)
		self.__adb.register("UPDATE_SERVICELIST__OBB_V1", self.__sl_entry__obb_v1)
		self.__adb.register("UPDATE_SERVICELIST__CARAPP_OBB", self.__sl_entry__carapp_obb)
		self.__adb.register("DIGITAL_ASSISTANT_STATE_CHANGED", self.__audi_assistant_state_changed)

		MODULE_LOGGER.info("Registered adb data_logcat server.")

	def __cb_app_force_stop(self, data) -> None:
		"""Receive app which was force closed.

		:param data: valtech_mobility app which was force closed on target.
		:type data: enna.core.interfaces.Data(dict, enna.core.time.timebase.Timestamp)
		"""
		app = data.value["extractedParameters"]["app"]
		MODULE_LOGGER.info(f"App force stopped: {app}")
		self._app_force_stopped = app
		self._signal_property("app_force_stopped", self.app_force_stopped)

	def __cb_toast_appeared(self, data) -> None:
		"""Receive toast text which appeared.

		:param data: Toast event which appeared on target.
		:type data: enna.core.interfaces.Data(dict, enna.core.time.timebase.Timestamp)
		"""
		self._toast = None
		toast = data.value["extractedParameters"]["toast_text"]
		MODULE_LOGGER.info(f"Toast with text appeared: {toast}")
		self._toast = toast
		self._signal_property("toast", self.toast)

	def __cb_active_tiles(self, data) -> None:
		"""Receive active tile apps.

		:param data: Active apps on tile screen.
		:type data: enna.core.interfaces.Data(dict, enna.core.time.timebase.Timestamp)
		"""
		active_tiles = data.value["extractedParameters"]["active_tiles"]
		active_tiles_splitted_by_comma = [element.strip() for element in data.value["extractedParameters"]["active_tiles"].split(",")]
		for element in active_tiles_splitted_by_comma:
			try:
				self._active_tiles.update({element.split("=")[0]: element.split("=")[1]})
			except (IndexError, AttributeError):
				MODULE_LOGGER.debug("An index was not available for a tile binding.")
		MODULE_LOGGER.debug(f"Active tiles: {active_tiles}")
		self._signal_property("active_tiles", self.active_tiles)

	def __sl_entry_updated(self, data) -> None:
		"""Receive app which was force closed.

		:param data: valtech_mobility app which was force closed on target.
		:type data: enna.core.interfaces.Data(dict, enna.core.time.timebase.Timestamp)
		"""
		self.servicelist_entry = data.value["extractedParameters"]["servicelist_entry"]
		self._signal_property("servicelist_entry", self.servicelist_entry)

	def __phone_call_triggered(self, data) -> None:
		"""Check if a phone call shall be triggered via adb logcat (Does not check if phone call was executed).

		:param data: Phone call which was triggered (phone number of call).
		:type data: enna.core.interfaces.Data(dict, enna.core.time.timebase.Timestamp)
		"""
		self.triggered_call_phone_number = data.value["extractedParameters"]["phone_number"]
		self._signal_property("triggered_call_phone_number", self.triggered_call_phone_number)

	def __zero_conf_started(self, data) -> None:  # pylint: disable=unused-argument
		"""Check if an event to indicate starting zero conf manager occurred.

		:param data: Starting Zero Conf event.
		:type data: enna.core.interfaces.Data(dict, enna.core.time.timebase.Timestamp)
		"""
		self._zero_conf_started = True
		self._signal_property("zero_conf_started", self.zero_conf_started)

	def __sl_entry__carapp_obb(self, data) -> None:  # pylint: disable=unused-argument
		"""Signal service list carapp_obb entry event.

		:param data: Event data
		:type data: enna.core.interfaces.Data(dict, enna.core.time.timebase.Timestamp)
		"""
		self._signal_event("sl_entry__carapp_obb", enna.core.interfaces.Data())

	def __sl_entry__obb_v1(self, data) -> None:  # pylint: disable=unused-argument
		"""Signal service list obb_v1 entry event.

		:param data: Event data
		:type data: enna.core.interfaces.Data(dict, enna.core.time.timebase.Timestamp)
		"""
		self._signal_event("sl_entry__obb_v1", enna.core.interfaces.Data())

	def __audi_assistant_state_changed(self, data) -> None:  # pylint: disable = unused-argument
		"""Signal that a state change for audi assistant happened.

		:param data: event data
		:type data: enna.core.interfaces.Data(dict, enna.core.time.timebase.Timestamp)
		"""
		self.audi_assistant_state = data.value["extractedParameters"]["assistant_state"]
		print(self.audi_assistant_state)
		self._signal_property("audi_assistant_state", self.audi_assistant_state)
