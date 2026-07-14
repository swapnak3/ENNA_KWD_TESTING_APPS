# -*- coding: utf-8 -*-
"""The factory to create proxies and servers that implement the interface in this package."""
import enna.core.interfaces.factory
import enna.core.component_system.decorators
import enna.data_interfaces.adb
import enna.utilities.susan

import enna_kwd_testing.utilities.vehicle.interface


@enna.core.component_system.decorators.RequireComponent(enna.data_interfaces.adb, for_implementation="server_mqbw")
@enna.core.component_system.decorators.RequireComponent(enna.utilities.susan, for_implementation="server_ppe")
class Factory(enna.core.interfaces.factory.Factory[enna_kwd_testing.utilities.vehicle.interface.Interface], multi_instance=False):
	"""Factory class for instantiating and obtaining Esotrace objects which require a JSON-based configuration.

   More information about factories can be found in [`enna.core.interfaces.factory.Factory`][].
   """
