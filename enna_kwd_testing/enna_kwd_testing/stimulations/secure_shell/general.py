# -*- coding: utf-8 -*-
"""Module contains stimulation for send commands via secure shell on test bench."""
import logging

import enna.core.exceptions
import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.utilities.ssh_client.interface
import enna.utilities.ssh_client.exceptions

import enna.data_interfaces.adb.interface

import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.instance_names

import enna_kwd_testing.enna_kwd_testing.stimulations.base.keyword_stim_baseclass

from enna_kwd_testing.enna_kwd_testing.utilities.helper.adb import set_driving_side

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.utilities.ssh_client")
class SendShellCommand(enna_kwd_testing.enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
    """Stimulation send a command via ssh client on MMI."""

    def __init__(self, reporting: enna.core.reporting.interface.Interface, ssh_client: enna.utilities.ssh_client.interface.Interface) -> None:
        """Constructor of stimulation.

        :param reporting: instance of reporting handler
        :param ssh_client: instance of interface for secure shell client
        """
        super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.3")
        self._ssh = ssh_client
        self.allowed_parameter_keys = ["COMMAND", "TIMEOUT"]

    def _action(self) -> bool:
        """Send command on MMI.

        :return: True if success, else false.
        """
        command = self.values.get("COMMAND", None)
        timeout = self.values.get("TIMEOUT", 10.0)
        if not isinstance(command, str):
            self._reporting.add_report_message_ta_error(f"Command '{command}' is wrong type! Only could send string as command.")
            return False
        try:
            MODULE_LOGGER.debug(f"Send command: '{command}'")
            response = self._ssh.execute_command(command=command, max_time=timeout)
        except enna.utilities.ssh_client.exceptions.SSHException as error:
            self._reporting.add_report_message_system_error(f"Could not send command '{command}'! {error}")
            return False
        self._reporting.add_report_message_pass(f"Send command '{command}' success.")
        MODULE_LOGGER.debug(f"Response for command '{command}': '{response}'")
        return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.utilities.ssh_client")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class ResetWithPersistence(SendShellCommand):
    """MMI reset with persistence. Send command to start a reset via GEM."""

    def __init__(self, reporting: enna.core.reporting.interface.Interface, ssh_client: enna.utilities.ssh_client.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
        """Constructor of stimulation.

        :param reporting: instance of reporting handler
        :param ssh_client: instance of interface for secure shell client
        :param android_hmi: instance of android hmi control interface
        """
        super().__init__(reporting=reporting, ssh_client=ssh_client)
        self._android_hmi = android_hmi
        self.values.update({"COMMAND": "echo gem_reset > /tmp/ooc-debug"})

    def _postcondition(self) -> bool:
        """Check Restart of MMI is successful.

        :return: True if success, else false.
        """
        try:
            self._android_hmi.connected.wait_for_value(False, max_time=120.0)
        except enna.core.exceptions.TimeoutException:
            self._reporting.add_report_message_system_error("Shutdown is not triggered! MMI keeps online after reset over GEM.")
            return False
        try:
            self._android_hmi.connected.wait_for_value(True, max_time=300.0)
            self._android_hmi.wait_for_event("screen_id", condition=lambda msg: "." in self._android_hmi.screen_id.value, max_time=60.0)
        except enna.core.exceptions.TimeoutException:
            self._reporting.add_report_message_system_error("MMI not start up after reset over GEM!")
            return False
        self._reporting.add_report_message_pass("MMI restart is successful.")
        return True
