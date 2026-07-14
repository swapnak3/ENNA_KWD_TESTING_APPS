# -*- coding: utf-8 -*-
"""The factory to create proxies and servers that implement the interface in this package."""

import enna.core.component_system.decorators
import enna.core.interfaces.factory


class Factory(enna.core.interfaces.factory.Factory, multi_instance=True):
	"""Create proxies and servers for text tools."""

	def __init__(self, create_servers):
		"""Initialize an Interface object for factory.

		:param bool create_servers: if True, servers will be created, otherwise proxies
		"""
		enna.core.interfaces.factory.Factory.__init__(self, create_servers=create_servers)
