# -*- coding: utf-8 -*-
"""Module contains constants for ADB Stimulation."""

# pylint: disable=line-too-long
COMMANDS = {
  "start_climate_popup": "am start -n de.eso.car.audi/de.eso.car.ui.climate.ClimatePopupActivity -S",
  "start_first_time_wizard":  "am start -n 'de.eso.setupwizard/.main.SetupWizardUserActivity' -a android.intent.action.MAIN",
  "start_video_handsfree_driving": "am start -n \"com.valtech_mobility.legal.audi/com.valtech_mobility.legal.MainActivity\" -d \"content://com.valtech_mobility.legal?ACTION=PLAY_ACA_EXPLANATORY_VIDEO\" --es \"VIDEO_NAME\" \"HandsfreeDriving\"",
  "start_legal_app": "am start -a android.intent.action.VIEW -d \"content://com.valtech_mobility.legal?service_id=legal&document=legal_overview&language=de_DE\"",
  "check_TLI_service_starts": "dumpsys activity services technology.cariad.trafficlightinformation",
  "allow_debug_app_location_mock": "appops set com.app.hcp3.aio.debug android:mock_location allow",
  "crash_GBK_app": "am crash technolog.cariad.navi.audi",
  "set_turn_signal_state_left": "dumpsys activity service com.android.car inject-vhal-event 0x11400408 2",
  "set_turn_signal_state_right": "dumpsys activity service com.android.car inject-vhal-event 0x11400408 1",
  "deactivate_turn_signal_state": "dumpsys activity service com.android.car inject-vhal-event 0x11400408 0",
  "set_clamp_15_on": "dumpsys activity service com.android.car inject-vhal-event 0x11400409 4",
  "set_clamp_15_off": "dumpsys activity service com.android.car inject-vhal-event 0x11400409 2",
  "check_input_field_500_chars": 	"input keyboard text .abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz_100ZEICHEN.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz_200ZEICHEN.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz_300ZEICHEN.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz_400ZEICHEN.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz_500ZEICHENabjetztmehrwie500Zeichen",
  "get_all_package_versions": "dumpsys package | awk '/^[ ]*Package \\[.*\\] (.*)/ { i = index($0, \"[\") + 1; pkg = substr($0, i, index($0, \"]\") - i); } /[ ]*versionName=/ { { print pkg \": \" substr($0, index($0, \"=\") + 1); pkg = \"\"; } }'\n"
}
