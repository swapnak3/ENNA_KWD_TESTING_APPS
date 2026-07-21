# -*- coding: utf-8 -*-
"""Module contains stimulation for general commands to android debug bridge."""
import logging

import enna.core.config
import enna.core.exceptions
import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.data_interfaces.adb.interface
import enna.data_interfaces.adb.exceptions

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.json_loader.interface
import enna_kwd_testing.stimulations.adb
from enna_kwd_testing.utilities.helper.adb import set_driving_side

MODULE_LOGGER = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 10.0

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class SendAdbShellCommand(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
    """Send adb shell command to test bench."""

    def __init__(self, reporting: enna.core.reporting.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface) -> None:
        """Constructor of stimulation to send an android debug bridge shell command.

        :param reporting: instance of reporting handler
        :param adb: instance of interface to android debug bridge
        """

        super().__init__(reporting=reporting)
        self._adb = adb
        self.allowed_parameter_keys = ["COMMAND", "TIMEOUT"]

    def _action(self) -> bool:
        """Execute action.
        Send command to shell of android debug bridge

        :return: True if success, else false.
        """
        command = self.values.get("COMMAND", "dir unknown")
        command = enna_kwd_testing.stimulations.adb.COMMANDS.get(command, command)
        timeout = self.values.get("TIMEOUT", DEFAULT_TIMEOUT)

        try:
            self._adb.execute_shell_command(command, timeout=timeout)
        except enna.data_interfaces.adb.exceptions.ADBException as error:
            self._reporting.add_report_message_ta_error(f"Error by sending shell command '{command}'! Error: {error}")
            return False
        self._reporting.add_report_message_pass(f"Send shell command '{command}' success.")
        return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class CheckCurrentSystemLanguage(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
    """Check current language via ADB commmad."""

    def __init__(self, reporting: enna.core.reporting.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface) -> None:
        """Constructor of stimulation to send an android debug bridge shell command.

        :param reporting: instance of reporting handler
        :param adb: instance of interface to android debug bridge
        """

        super().__init__(reporting=reporting, based_on_kwd_spec_version="1.0.3")
        self._adb = adb
        self.allowed_parameter_keys = ["LANG"]

    def _action(self) -> bool:
        """Execute action.
        Send command to shell of android debug bridge

        :return: True if success, else false.
        """
        expected_language = self.values.get("LANG", "unknown")

        try:
            current_language: str = self._adb.execute_shell_command(command="getprop persist.sys.locale", timeout=DEFAULT_TIMEOUT)
            MODULE_LOGGER.debug(f"Reading current language = '{current_language}', Type: {type(current_language)}")
        except enna.data_interfaces.adb.exceptions.ADBException as error:
            self._reporting.add_report_message_ta_error(f"Error by reading current language! Error: {error}")
            return False
        if expected_language.replace("-", "_") == current_language.replace("-", "_"):
            self._reporting.add_report_message_pass(f"Current language '{current_language}' equal expected '{expected_language}'.")
            return True
        self._reporting.add_report_message_system_error(f"Current language '{current_language}' not equal expected '{expected_language}'!")
        return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class ReportingAllPackagesAndVersions(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
    """Class containing stimulation to read all package with version."""

    def __init__(self, reporting: enna.core.reporting.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface):
        """Initialize stimulation.

        :param reporting: Instance of reporting interface.
        :param adb: Instance of adb interface
        """
        super().__init__(reporting, based_on_kwd_spec_version="1.0.5")
        self._adb = adb

    def _action(self) -> bool:
        """Read version for all packages.
        Report version per package name

        :return: True if successful, False it exception occurs
        """
        try:
            self._adb.connected.wait_for_value(True, max_time=120.0)
            # read all packages

            package_list = self._adb.execute_shell_command("pm list packages", timeout=10.0, stream=False).replace("package:", "").split("\n")
            for package in package_list:
                # read version per package
                version = self._adb.execute_shell_command(f"dumpsys package {package} | grep versionName", timeout=10.0, stream=False).replace("versionName=", "").strip()
                self._reporting.add_report_message_info(f"Package: {package} Version: {version}")
        except (enna.core.exceptions.TimeoutException, enna.data_interfaces.adb.exceptions.ADBException) as exception:
            MODULE_LOGGER.error(f"Error by using ADB interface! {exception}")
            return False
        return True


class _BaesADBShellCommadForPackage(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
    """Class containing base excution for ADB Shell commands of an package. e.g. Force-Stop, Clear-Cache, Clear-Storage, ..."""

    def __init__(self, reporting: enna.core.reporting.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface):
        """Instancing stimulation.

        :param reporting: Instance of reporting interface.
        :param adb: Instance of adb interface
        """
        super().__init__(reporting=reporting)
        self.allowed_parameter_keys = ["APP_NAME"]
        self._adb = adb
        self._packages: dict = enna.core.config.get_system_specific_mapping(__name__, subfolder_name="data", file_key="packages")
        self._command: str = ""
        self._out: str = ""

    def _action(self) -> bool:
        """Send a ADB shell for a package.

        :return: True if successful, False it exception occurs
        """
        try:
            app = self.values["APP_NAME"].lower()
        except KeyError as error:
            msg = f"Missing parameter 'APP_NAME'! {error}"
            self._reporting.add_report_message_ta_error(msg)
            return False
        package = self._packages.get(app, app)
        self._command = f"{self._command} {package}"
        try:
            self._out =self._adb.execute_shell_command(command=self._command, timeout=30.0)
        except enna.data_interfaces.adb.exceptions.ADBException as error:
            MODULE_LOGGER.error(f"Error by eccuting comand: '{self._command}'! {error}")
            return False
        self._reporting.add_report_message_pass(f"Executing '{self._command}'. {self._out}")
        return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class ForceStop(_BaesADBShellCommadForPackage):
    """Stimulation for force stop a package in MMI."""

    def __init__(self, reporting: enna.core.reporting.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface):
        """Instancing stimulation.

        :param reporting: Instance of reporting interface.
        :param adb: Instance of adb interface
        """
        super().__init__(reporting=reporting, adb=adb)
        self._command = "am force-stop"


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class ClearCacheStorage(_BaesADBShellCommadForPackage):
    """Stimulation for clear cache and storage on a package in MMI."""

    def __init__(self, reporting: enna.core.reporting.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface):
        """Instancing stimulation.

        :param reporting: Instance of reporting interface.
        :param adb: Instance of adb interface
        """
        super().__init__(reporting=reporting, adb=adb)
        self._command = "pm clear"

    def _postcondition(self) -> bool:
        """Checking clearing app was success.

        :return: True if clearing was success else False.
        """
        if self._out.lower() == "success":
            self._reporting.add_report_message_pass(f"Execution of '{self._command}' is {self._out}!")
            return True
        self._reporting.add_report_message_system_error(f"Execution of '{self._command}' is {self._out}!")
        return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class CheckAppIsInstalledOnSystem(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
    """Stimulation check app is installed in MMI."""

    def __init__(self, reporting: enna.core.reporting.interface.Interface, adb: enna.data_interfaces.adb.interface.Interface):
        """Initialize stimulation.

        :param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
        :param enna.data_interfaces.adb.interface.Interface adb: instance of adb interface
        """
        super().__init__(reporting)
        self._adb = adb

    def _action(self) -> bool:
        """Check app is installed in android system

        :return: True if successful, False if an error occurs in any step.
        """
        try:
            app_name = self.values.get("APP_NAME", "").lower()
            if not app_name:
                app_name = self.values["APP_PACKAGE_NAME"]
            if app_name == "in_car_office":
                app_name = "ico"
            expected_installed_state: bool = self.values["INSTALLED"]
        except KeyError as error:
            self._reporting.add_report_message_info(f"Missing parameter! {error}")
            return False

        try:
            output = self._adb.execute_shell_command(command="pm list packages")
        except enna.data_interfaces.adb.exceptions.ADBException as error:
            self._reporting.add_report_message_ta_error(f"Error by reading installed packages! {error}")
            return False

        current_installed_state = app_name in output

        if current_installed_state == expected_installed_state:
            state_message = "installed" if expected_installed_state else "not installed"
            self._reporting.add_report_message_pass(f"App '{app_name}' is {state_message}.")
            return True

        state_message = "not installed" if expected_installed_state else "installed"
        self._reporting.add_report_message_system_error(f"App '{app_name}' is {state_message}.")
        return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
class SetDrivingSide(_BaesADBShellCommadForPackage):
    """Set vehicle driving side via ADB."""

    def __init__(
            self,
            reporting: enna.core.reporting.interface.Interface,
            adb: enna.data_interfaces.adb.interface.Interface) -> None:
        """Initialize stimulation."""

        super().__init__(
            reporting=reporting,
            adb = adb)

        self._adb = adb
        self.allowed_parameter_keys = ["SIDE"]

    def _action(self) -> bool:
        """Set driving side."""

        side = self.values.get("SIDE", "").upper()

        if side not in ["LHD", "RHD"]:
            self._reporting.add_report_message_ta_error(f"Invalid SIDE '{side}'. Use LHD or RHD.")
            return False

        try:
            result = set_driving_side(
                adb=self._adb,
                side=side
            )
        except enna.data_interfaces.adb.exceptions.ADBException as error:
            self._reporting.add_report_message_ta_error(
                f"Failed to set driving side: {error}"
            )
            return False

        if not result:
            self._reporting.add_report_message_system_error(
                f"Failed to change driving side to {side}")
            return False

        self._reporting.add_report_message_pass(
            f"Driving side successfully changed to {side}")

        return True
