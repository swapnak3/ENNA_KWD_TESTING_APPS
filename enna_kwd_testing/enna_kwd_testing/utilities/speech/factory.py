# -*- coding: utf-8 -*-
"""The factory to create proxies and servers that implement the interface in this package."""

import logging

import enna.core.component_system.decorators
import enna.core.interfaces.factory

import enna_kwd_testing.utilities.speech.interface

MODULE_LOGGER = logging.getLogger(__name__)


class Factory(enna.core.interfaces.factory.Factory, multi_instance=False):
	"""Create proxies and servers for text tools."""

	def __init__(self, create_servers):
		"""Initialize an Interface object for factory.

		:param bool create_servers: if True, servers will be created, otherwise proxies
		"""
		enna.core.interfaces.factory.Factory.__init__(self, create_servers=create_servers)

	def _create_server(self, instance_name: str) -> enna_kwd_testing.utilities.speech.interface.Interface:
		"""Create server object with given instance name.

		:param instance_name: Name of instance that should be created
		:return: Object of Server type
		:raises enna.core.exceptions.ConfigurationException: if instance is using unknown implementation
		"""
		server_class = self.get_server_class_for_implementation(instance_name)
		return self._call_with_needed_args(server_class, instance_name=instance_name)
