# -*- coding: utf-8 -*-
"""Created on 12.09.2023.

@project: .
@author: SPLATZP: Pascal Platzer.

Contains helper functions for adb context.
"""
import logging
import re
import enna.core.time
from datetime import datetime, time

import enna.data_interfaces.adb.exceptions
import enna.data_interfaces.adb.interface

MODULE_LOGGER = logging.getLogger(__name__)


def get_volume(adb: enna.data_interfaces.adb.interface.Interface, volume_group: str) -> int | bool:
    """Get volume via adb.

    :param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
    :param volume_group: str 'android.car.VOLUME_GROUP/0/0 - android.car.VOLUME_GROUP/0/4'
    :type volume_group: str
    :return: int volume
    :rtype: int | Bool
    """
    try:
        adb_command = f"settings list system | grep {volume_group}"
        adb_out = adb.execute_shell_command(adb_command)
        adb_out = adb_out.split("=")[1]
        return int(adb_out)
    except enna.data_interfaces.adb.exceptions.ADBException as exception:
        MODULE_LOGGER.error(f"Error: {exception}")
        return False


def is_media_session_playing(adb) -> bool:
    """Check if the Media Player is currently playing something

    :param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
    :return: bool True if the Media Player is active, False if is not active.
    :rtype: bool
    """
    try:
        adb_out = adb.execute_shell_command("dumpsys media_session | grep PlaybackState")
        adb_out = adb_out.split("position")[0]
        return "state=3" in adb_out
    except enna.data_interfaces.adb.exceptions.ADBException as exception:
        MODULE_LOGGER.error(f"Error: {exception}")
        return False


def get_active_user(adb) -> str | bool:
    """Get active user via adb.

    :param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
    :return: str user
    :rtype: str | bool
    """
    try:
        adb_command = "pm list users"
        adb_out = adb.execute_shell_command(adb_command)
        match = re.findall(r"UserInfo{(\d+):[^}]+} running", adb_out)
    except enna.data_interfaces.adb.exceptions.ADBException as exception:
        MODULE_LOGGER.error(f"Error: {exception}")
        return False
    return False if not match else match[1]


def get_time(adb) -> time | bool:
    """Get active user via adb.

    :param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
    :return: time time
    :rtype: time | bool
    """
    try:
        adb_command = " date +%H:%M"
        adb_out = adb.execute_shell_command(adb_command)
        adb_time = datetime.strptime(adb_out, "%H:%M").time()
        return adb_time
    except enna.data_interfaces.adb.exceptions.ADBException as exception:
        MODULE_LOGGER.error(f"Error: {exception}")
        return False


def check_package_is_installed(adb, package, user="current") -> bool:
    """Check installed package via adb.

    :param str user: The active user
    :param str package: The package name of the app you are looking for e.g. technology.cariad.navi.audi
    :param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
    :return: True if successful, False if an error occurs.
    :rtype: bool
    """
    try:
        adb_command = f" pm list packages --user {user}"
        adb_out = adb.execute_shell_command(adb_command)
    except enna.data_interfaces.adb.exceptions.ADBException as exception:
        MODULE_LOGGER.error(f"Error: {exception}")
        return False
    if package not in adb_out:
        return False
    return True


def set_development_settings(adb) -> bool:
    """Set development settings via adb.

    :param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
    :return: True if successful, False if an error occurs.
    :rtype: bool
    """
    try:
        adb_command = " settings put global development_settings_enabled 1"
        adb.execute_shell_command(adb_command)
    except enna.data_interfaces.adb.exceptions.ADBException as exception:
        MODULE_LOGGER.error(f"Error: {exception}")
        return False
    return True


def allow_to_set_position_in_navigation(adb) -> bool:
    """Allow to position set ccp via adb.

    :param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
    :return: True if successful, False if an error occurs.
    :rtype: bool
    """
    try:
        adb_command = "  appops set technology.cariad.navi.audi android:mock_location allow"
        adb.execute_shell_command(adb_command)
    except enna.data_interfaces.adb.exceptions.ADBException as exception:
        MODULE_LOGGER.error(f"Error: {exception}")
        return False
    return True


def set_position_in_navigation(adb, latitude: float, longitude: float) -> bool:
    """Allow to set position ccp via adb.

    :param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
    :param latitude: latitude position e.g. "48.76718"
    :param longitude: longitude position e.g. "11.42875"
    :return: True if successful, False if an error occurs.
    :rtype: bool
    """
    try:
        if not (float(latitude) and float(longitude)):
            MODULE_LOGGER.error("Error: latitude or longitude is not a float")
            return False

        adb_command = f"  am broadcast -a de.esolutions.navigation.SET_POSITION --ef latitude {latitude} --ef longitude {longitude}"
        adb.execute_shell_command(adb_command)
    except enna.data_interfaces.adb.exceptions.ADBException as exception:
        MODULE_LOGGER.error(f"Error: {exception}")
        return False
    return True


def set_ambient_color(adb, color_index) -> bool:
    """Set ambient color via adb.

    :param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
    :param int color_index: Instance of adb interface
    :return: True if successful, False if an error occurs.
    :rtype: bool
    """
    try:
        adb_command = f" am broadcast -a com.android.systemui.eso.car.ambient_color.intent.action.DEBUG_DATA --ei index {color_index}"
        adb.execute_shell_command(adb_command)
    except enna.data_interfaces.adb.exceptions.ADBException as exception:
        MODULE_LOGGER.error(f"Error: {exception}")
        return False
    return True


def set_keyboard_fast_input(adb) -> bool:
    """Activate FastInputIME for android.
    Activating FastInputIME activates the visible keyboard.
    :return: True if successful

    :param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
    :return: True if successful, False if an error occurs.
    :rtype: bool
    """
    try:
        adb_command_enable = " ime enable com.github.uiautomator/.FastInputIME"
        adb.execute_shell_command(adb_command_enable)
        adb_command_set = " ime set com.github.uiautomator/.FastInputIME"
        adb.execute_shell_command(adb_command_set)
    except enna.data_interfaces.adb.exceptions.ADBException as exception:
        MODULE_LOGGER.error(f"Error: {exception}")
        return False
    return True


def set_keyboard(adb) -> bool:
    """Deactivate FastInputIME for android.
    Deactivating FastInputIME activates the visible keyboard.

    :param enna.data_interfaces.adb.interface.Interface adb: Instance of adb interface
    :return: True if successful
    :rtype: bool
    """
    try:
        adb_command_disable = " ime disable com.github.uiautomator/.FastInputIME"
        adb.execute_shell_command(adb_command_disable, timeout=60)
        adb_command_set = " ime set com.audi.automotive.input/com.nuance.swype.input.IME"
        adb.execute_shell_command(adb_command_set, timeout=60)
    except enna.data_interfaces.adb.exceptions.ADBException as exception:
        MODULE_LOGGER.error(f"Error: {exception}")
        return False
    return True
def set_driving_side(adb, side: str) -> bool:
    """Set vehicle driving side via adb."""

    try:
        side = side.upper()

        if side not in ["LHD", "RHD"]:
            MODULE_LOGGER.error(
                f"Invalid driving side '{side}'."
            )
            return False

        MODULE_LOGGER.info("Executing adb root")
        adb.execute_shell_command(" root")

        MODULE_LOGGER.info("Waiting 2 minutes after root")
        enna.core.time.sleep(120)

        MODULE_LOGGER.info("Executing adb remount")
        adb.execute_shell_command(" remount")

        MODULE_LOGGER.info("Waiting 4 minutes after remount")
        enna.core.time.sleep(240)

        value = (
            "000000100000000000000000"
            if side == "RHD"
            else "000000000000000000000000"
        )

        adb_command = (
            f"diag-tester -n and uds -s ext "
            f"write -i 0x0600 -v {value}"
        )

        MODULE_LOGGER.info(
            f"Changing driving side to {side}"
        )

        adb.execute_shell_command(adb_command)

        MODULE_LOGGER.info(
            "Waiting 5 minutes after writing driving-side coding"
        )

        enna.core.time.sleep(60)

        MODULE_LOGGER.info("Rebooting IVI")

        adb.execute_shell_command(" reboot")

        enna.core.time.sleep(300)

        return True

    except enna.data_interfaces.adb.exceptions.ADBException as exception:
        MODULE_LOGGER.error(f"Error: {exception}")
        return False