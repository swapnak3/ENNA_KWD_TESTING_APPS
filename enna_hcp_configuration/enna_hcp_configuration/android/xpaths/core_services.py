# -*- coding: utf-8 -*-
"""Module contains xpath of core_services app."""

from . import XpathString

HOME_TITLE = XpathString("//*[@package='de.esolutions.coreservices'][@selected='true']//*[@package='de.esolutions.coreservices'][@text='Home']")
HOME_EXPAND_TITLE = XpathString("//*[@content-desc='Expand']")
HOME_COLLAPSE_TITLE = XpathString("//*[@content-desc='Collapse']")
HEALTH_CHECK_TITLE = XpathString("//*[@package='de.esolutions.coreservices'][@selected='true']//*[@package='de.esolutions.coreservices'][@text='HealthCheck']")
BACKEND_SETTINGS_TITLE = XpathString("//*[@package='de.esolutions.coreservices'][@selected='true']//*[@package='de.esolutions.coreservices'][@text='BackendSettings']")
CONFIGURATION_TITLE = XpathString("//*[@package='de.esolutions.coreservices'][@selected='true']//*[@package='de.esolutions.coreservices'][@text='Configuration']")
PSO_LOGIN_TITLE = XpathString("//*[@package='de.esolutions.coreservices'][@selected='true']//*[@package='de.esolutions.coreservices'][@text='PSO Login']")
SERVICE_LIST_DISABLE_REASONS_TITLE = XpathString("//*[@package='de.esolutions.coreservices'][@selected='true']//*[@package='de.esolutions.coreservices'][@text='ServiceList/DisableReasons']")
MQTT_TITLE = XpathString("//*[@package='de.esolutions.coreservices'][@selected='true']//*[@package='de.esolutions.coreservices'][@text='Mqtt']")
TOKENS_TITLE = XpathString("//*[@package='de.esolutions.coreservices'][@selected='true']//*[@package='de.esolutions.coreservices'][@text='Tokens']")
THIRD_PARTY_TRUSTSTORE_TITLE = XpathString("//*[@package='de.esolutions.coreservices'][@selected='true']//*[@package='de.esolutions.coreservices'][@text='Third-Party Truststore']")

BURGER_DEVELOPMENT_BUTTON = XpathString("//*[@package='de.esolutions.coreservices'][@text='Development']/..")
BURGER_HEALTH_CHECK_BUTTON = XpathString("//*[@package='de.esolutions.coreservices'][@text='HealthCheck']/..")
BURGER_BACKEND_SETTINGS_BUTTON = XpathString("//*[@package='de.esolutions.coreservices'][@text='BackendSettings']/..")
BURGER_CONFIGURATION_BUTTON = XpathString("//*[@package='de.esolutions.coreservices'][@text='Configuration']/..")
BURGER_PSO_LOGIN_BUTTON = XpathString("//*[@package='de.esolutions.coreservices'][@text='PSO Login']/..")
BURGER_SERVICE_LIST_DSIABLE_REASON_BUTTON = XpathString("//*[@package='de.esolutions.coreservices'][@text='ServiceList/DisableReasons']/..")
BURGER_MQTT_BUTTON = XpathString("//*[@package='de.esolutions.coreservices'][@text='Mqtt']/..")
BURGER_TOKENS_BUTTON = XpathString("//*[@package='de.esolutions.coreservices'][@text='Tokens']/..")
BURGER_THIRD_PARTY_TRUSTSTORE_BUTTON = XpathString("//*[@package='de.esolutions.coreservices'][@text='Third-Party Truststore']/..")

BURGER_HOME_BUTTON = XpathString("//*[@package='de.esolutions.coreservices'][@text='Home']/..")

# xpath_collection
# "Home"
HOME = XpathString("//*[@text='Home'][@package='de.esolutions.coreservices']")
APN1_TEXT = XpathString("//*[contains(@text, 'APN1 ')]")
APN1_TEXT_CONNECTED = XpathString("//*[@text='APN1 CONNECTED']")
APN1_TEXT_BLOCKED = XpathString("//*[@text='APN1 BLOCKED']")
APN1_STATE_CHECKBOX = XpathString("//*[contains(@text, 'APN1 ')]/..//*[@class='android.widget.ImageView'][@content-desc='Checked']")
APN2_TEXT = XpathString("//*[contains(@text, 'APN2 ')]")
APN2_TEXT_CONNECTED = XpathString("//*[@text='APN2 CONNECTED']")
APN2_TEXT_BLOCKED = XpathString("//*[@text='APN2 BLOCKED']")
APN2_STATE_CHECKBOX = XpathString("//*[contains(@text, 'APN2 ')]/..//*[@class='android.widget.ImageView'][@content-desc='Checked']")

# HealthCheck
# Development
# "BackendSettings"
# "Configuration"
VIN_EDIT = XpathString("//*[@package='de.esolutions.coreservices'][@class='android.widget.EditText']")
SLENTRIES = XpathString("//*[@package='de.esolutions.coreservices'][contains(@text, 'SL entries:')]")
CHANGECARSETTINGS = XpathString("//*[@package='de.esolutions.coreservices'][contains(@text, 'Save Configuration')]")
POPUP_CONFIRM_BUTTON = XpathString("//*[@package='de.esolutions.coreservices'][@text='Confirm']")
# "PSO Login"
# "MemoryTracking"
# "ServiceList/DisableReasons"
SERVICE_ID = XpathString("//*[@package='de.esolutions.coreservices'][@class='android.widget.TextView']")
LICENSE = XpathString("//*[@text='ServiceList Details']/..//*[@class='android.widget.TextView'][@index='6']")
REASON_CONNECTIVITY = XpathString("//*[@text='Disable Reasons']/..//*[@class='android.widget.ScrollView']//*[@class='android.widget.TextView'][@index='0']")
REASON_BACKEND = XpathString("//*[@text='Disable Reasons']/..//*[@class='android.widget.ScrollView']//*[@class='android.widget.TextView'][@index='1']")
REASON_LICENSE = XpathString("//*[@text='Disable Reasons']/..//*[@class='android.widget.ScrollView']//*[@class='android.widget.TextView'][@index='2']")
REASON_CONFIG = XpathString("//*[@text='Disable Reasons']/..//*[@class='android.widget.ScrollView']//*[@class='android.widget.TextView'][@index='3']")
SERVICE_LIST = XpathString("//*[@package='de.esolutions.coreservices'][@class='android.view.View'][@scrollable='true']")
# Mqtt
# Tokens
# Third Party Truststore
# "unknown"
EDITABLETEXT = XpathString("//*[@resource-id='de.esolutions.coreservices:id/editabletext']")
CANCEL = XpathString("//*[@resource-id='android:id/button2']")
OK = XpathString("//*[@package='de.esolutions.coreservices'][@text='Confirm']")


# ----- CoreServices 1.0 ? -------------
# "health_check"
# APN1_STATE = XpathString("//*[contains(@resource-id, 'de.esolutions.coreservices:id/health_check_online_state')]")
# APN2_STATE = XpathString("//*[contains(@resource-id, 'de.esolutions.coreservices:id/health_check_online_state_apn2')]")
# DISMISS = XpathString("//*[@text='DISMISS'][@resource-id='de.esolutions.coreservices:id/snackbar_action']")

# "disable_reasons"
# DISABLE_REASONS = XpathString("//*[@text='DisableReasons'][@class='android.widget.TextView']")
# DISABLE_REASONS_RECYCLERVIEW = XpathString("//*[@resource-id='de.esolutions.coreservices:id/disable_reasons_recycler_view'][@class='androidx.recyclerview.widget.RecyclerView']")
# SERVICE_ID = XpathString("//*[@resource-id='de.esolutions.coreservices:id/disable_reasons_service_id']")
# REASON_CONNECTIVITY = XpathString("//*[@resource-id='de.esolutions.coreservices:id/disable_reasons_connectivity']")
# REASON_BACKEND = XpathString("//*[@resource-id='de.esolutions.coreservices:id/disable_reasons_backend']")
# REASON_LICENSE = XpathString("//*[@resource-id='de.esolutions.coreservices:id/disable_reasons_license']")
# REASON_CONFIG = XpathString("//*[@resource-id='de.esolutions.coreservices:id/disable_reasons_config']")
# DISMISS = XpathString("//*[@text='DISMISS'][@resource-id='de.esolutions.coreservices:id/snackbar_action']")

# "service_list"
# SERVICE_ID = XpathString("//*[contains(@resource-id, 'de.esolutions.coreservices:id/serviceID')]")
# LICENSE = XpathString("//*[contains(@resource-id, 'de.esolutions.coreservices:id/license')]")
# SERVICE_LIST = XpathString("//*[contains(@resource-id, 'de.esolutions.coreservices:id/my_recycler_view')]")
# DISMISS = XpathString("//*[@text='DISMISS'][@resource-id='de.esolutions.coreservices:id/snackbar_action']")

# "view_group"
# LIST_ENTRY = XpathString("//*[contains(@resource-id, 'listItem')]")
# DISMISS = XpathString("//*[@text='DISMISS'][@resource-id='de.esolutions.coreservices:id/snackbar_action']")
