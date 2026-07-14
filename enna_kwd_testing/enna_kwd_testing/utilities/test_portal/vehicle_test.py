# -*- coding: utf-8 -*-
"""Module contains testing test portal for vehicle."""
import logging

import enna.core.deployment.debug
import enna.core.logger

import enna_kwd_testing.utilities.test_portal.interface


MODULE_LOGGER = logging.getLogger(__name__)


def main():
	"""Reading vehicle by vin"""
	# Initialize ENNA logger framework
	enna.core.logger.basic_setup()

	instantiation_helper = enna.core.deployment.debug.DebugContainer()
	portal: enna_kwd_testing.utilities.test_portal.interface.Interface = instantiation_helper.add_model("enna_kwd_testing.utilities.test_portal")
	instantiation_helper.deploy()
	portal.wait_for_online()

	portal.read_vehicle_by_vin()

if __name__ == "__main__":
	main()
