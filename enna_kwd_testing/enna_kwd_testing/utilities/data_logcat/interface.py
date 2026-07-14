# -*- coding: utf-8 -*-
"""Created on 28.03.2022.

@project: enna_tc_connect_apps_hcp3.
@author: DYX34ZN: Jakob Kein.
Module contains interface for data_logcat utility.
"""

import enna.core.component_system.decorators
import enna.core.interfaces.component


@enna.core.component_system.decorators.GenerateProxy()
class Interface(enna.core.interfaces.component.Component):
	"""Interface for data that will be used by the proxy and server."""

	def __init__(self):
		"""Initialize data utility interface."""
		self._app_force_stopped = None
		self._toast = None
		self._active_tiles: dict = {}
		self._servicelist_entry = None
		self._triggered_call_phone_number = None
		self._zero_conf_started = False
		self._audi_assistant_state = ""

		self._additional_events = ["sl_entry__obb_v1", "sl_entry__carapp_obb"]

	@property
	def app_force_stopped(self):
		"""Return name of valtech_mobility app which was force stopped.

		:return: Name of app which was force stopped (valtech_mobility app).
		:rtype: str
		"""
		return self._app_force_stopped

	@property
	def toast(self):
		"""Return text of appearing toast.

		:return: Text of appearing toast.
		:rtype: str
		"""
		return self._toast

	@toast.setter
	def toast(self, value=None):
		"""Setter for toast property.

		:param str value: Value to set for toast property.
		"""
		self._toast = value

	@property
	def active_tiles(self):
		"""Return currently active tiles from dashboard.

		:return: Active tiles.
		:rtype: dict
		"""
		return self._active_tiles

	@active_tiles.setter
	def active_tiles(self, value: dict):
		"""Set active_tiles.

		:param dict value: Value to set for active tiles
		:raises ValueError: If active_tiles would be set with other value than dictionary type
		"""
		if not isinstance(value, dict):
			raise ValueError("active_tiles must be a dictionary.")
		self._active_tiles = value

	@property
	def servicelist_entry(self):
		"""Return name of the last service list entry which was updated.

		:return: Name of last service list entry which was updated.
		:rtype: str
		"""
		return self._servicelist_entry

	@servicelist_entry.setter
	def servicelist_entry(self, value):
		"""Set last service list entry property.

		:param str value: Value to set service list entry property to
		"""
		self._servicelist_entry = value

	@property
	def triggered_call_phone_number(self) -> str:
		"""Return phone number of last triggered phone call.

		:return: Phone number of phone call
		:rtype: str
		"""
		return self._triggered_call_phone_number

	@triggered_call_phone_number.setter
	def triggered_call_phone_number(self, value: str | None):
		"""Return phone number of last triggered phone call.

		:param str value: Phone number to from last phone call to set.
		"""
		self._triggered_call_phone_number = value

	@property
	def zero_conf_started(self):
		"""Return state of started zero conf manager if it is started.

		:return: State of zero conf manager
		:rtype: bool
		"""
		return self._zero_conf_started

	@property
	def audi_assistant_state(self) -> str:
		"""Get current audi assistant state.

		:return: Current audi assistant state
		:rtype: str
		"""
		return self._audi_assistant_state

	@audi_assistant_state.setter
	def audi_assistant_state(self, value: str):
		"""Set current audi assistant state.

		:param value: value to set for audi assistant state.
		:type value: str
		"""
		self._audi_assistant_state = value
