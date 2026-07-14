# -*- coding: utf-8 -*-
"""Created on 31.01.2024.

@project: enna_kwd_testing.
@author: splatzp, Pascal Platzer.

Contains functions to save and recreate rsi resource elements.
"""

import logging
import os
from importlib import reload

import enna.core.deployment.debug
import enna.data_interfaces.rsi
import enna_st12.instance_names

import enna_kwd_testing.core.rsi.buffered_rsi_resource_element as resource_element
from enna_kwd_testing import ROOT_PATH

MODULE_LOGGER = logging.getLogger(__name__)


def recreate_buffered_rsi_element():
	"""Create a rsi resource element and delete buffered rsi data if data is buffered

	"""
	reload(resource_element)
	buffered_rsi_data = resource_element.RSI_DATA

	if buffered_rsi_data:
		instantiation_helper = enna.core.deployment.debug.DebugContainer()
		rsi_server = instantiation_helper.add_model("enna.data_interfaces.rsi", instance_name=enna_st12.instance_names.Rsi.MAIN_UNIT)
		instantiation_helper.deploy()
		rsi_server.connected.wait_for_value(True, max_time=10.0)

		for service, resource in buffered_rsi_data.items():
			rsi_server.create_element(service, resource)
			MODULE_LOGGER.info(f"The Service {service, resource} is restored.")

		_delete_rsi_resource_element()


def save_rsi_resource_element(rsi_data):
	"""Save rsi resource element.

	:param dict rsi_data: dict with rsi resource element.
	"""

	str__rsi_service = str(rsi_data["uri"]).rsplit("/", 1)[0]
	str__rsi_service = str(str__rsi_service).split("/", 1)[1]
	del rsi_data["uri"]
	del rsi_data["id"]
	rsi_data = {str__rsi_service: rsi_data}

	path = os.path.join(f"{ROOT_PATH}/enna_kwd_testing/core/rsi/", "buffered_rsi_resource_element.py")

	with open(path, "w", encoding="utf-8") as data:
		data.write(f'# -*- coding: utf-8 -*-\n"""Created on 07.02.2024.\n\n@project: enna_kwd_testing.\n\nContains Rsi data."""\nRSI_DATA = {rsi_data}\n')


def _delete_rsi_resource_element():
	"""Delete rsi resource element.

	"""
	path = os.path.join(f"{ROOT_PATH}/enna_kwd_testing/core/rsi/", "buffered_rsi_resource_element.py")

	with open(path, "w", encoding="utf-8") as data:
		data.write('# -*- coding: utf-8 -*-\n"""Created on 07.02.2024.\n@project: enna_kwd_testing.\n Contains Rsi data."""\nRSI_DATA = {}\n')
