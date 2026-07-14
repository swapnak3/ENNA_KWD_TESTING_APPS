# -*- coding: utf-8 -*-
"""The factory to create proxies and servers that implement the interface in this package."""

import logging

import enna.core.component_system.decorators
import enna.core.interfaces.factory
import enna_st12.instance_names

import enna_kwd_testing.utilities.data_logcat.interface

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb", for_implementation="server_adb", instance_name=enna_st12.instance_names.Ecu.HCP3)
class Factory(enna.core.interfaces.factory.Factory, multi_instance=False):
	"""Factory class for instantiating and obtaining data_logcat objects.

	More information about factories can be found in :py:class:`enna.core.interfaces.factory.Factory`.
	"""

	def __init__(self, create_servers, adb=None):
		"""Initialize factory object.

		:param bool create_servers: If True, servers will be created. Otherwise, proxies
		:param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
		"""
		self.__adb = adb
		enna.core.interfaces.factory.Factory.__init__(self, create_servers)

	def _create_server(self, instance_name: str) -> enna_kwd_testing.utilities.data_logcat.interface.Interface:
		"""Create server object with given instance name.

		:param instance_name: Name of instance that should be created
		:return: Object of Server type
		:raises enna.core.exceptions.ConfigurationException: if instance is using unknown implementation
		"""
		server_class = self.get_server_class_for_implementation(instance_name)
		return self._call_with_needed_args(server_class, instance_name=instance_name, adb=self.__adb)
