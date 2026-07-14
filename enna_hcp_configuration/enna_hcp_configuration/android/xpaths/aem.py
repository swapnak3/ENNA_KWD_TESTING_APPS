# -*- coding: utf-8 -*-
"""Module contains xpath of Audi Engineering Menu."""
from . import XpathString

# pylint: disable=line-too-long
MAIN_TITLE = XpathString("//*[@text='Activity List'][@class='android.widget.TextView'][@package='de.eso.aem']", context="aem.main") # language independent
KEYBOARD = XpathString("//*[@package='com.audi.automotive.input']", context="aem.main") # language independent
SEARCH_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]", context="aem.search") # language independent
LIST = XpathString("//*[@resource-id='de.eso.aem:id/recyclerViewList']", context="aem.main") #ok

NAV_GEM = XpathString("//*[contains(@text, 'Navigation GEM')][@package='de.eso.aem']", context="aem.main") # language independent

MAP_MATCHER_GEM = XpathString("//*[contains(@text, 'MapMatcher GEM')][@package='de.eso.aem']", context="aem.main") # language independent

IGNITE_STORE_ENGINEERING_MENU_BUTTON = XpathString("//*[contains(@text,'com.harman.ignite.appstore.audi / Ignite Store Engineering Menu')]", context="aem.main") # language independent
IGNITE_STORE_ENGINEERING_MENU_TITLE = XpathString("//*[@text='Ignite Store Engineering Menu'][@resource-id='com.harman.ignite.appstore.audi:id/titleTextViewRef'][@package='com.harman.ignite.appstore.audi']", context="ignite_store.aem_ignite_store_engineering_menu") # language independent
IGNITE_STORE_ENGINEERING_MENU_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]", context="ignite_store.aem_ignite_store_engineering_menu") # language independent

VEHICLE_POWERMODING_CLIENT_SETTINGS_BUTTON = XpathString("//*[contains(@text,'com.harman.vehicle.powermoding / Client - Settings')]", context="aem.main") # language independent
VEHICLE_POWERMODING_CLIENT_SETTINGS_TITLE = XpathString("//*[@text='VehiclePowerModingService'][@package='com.harman.vehicle.powermoding']", context="aem_vehicle_powermoding.client_settings") # language independent
VEHICLE_POWERMODING_CLIENT_SETTINGS_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Nach oben navigieren') or contains(@content-desc,'Navigate up')]", context="aem_vehicle_powermoding.client_settings") #_todo missing in texttool

ECALL_TEST_MENU_BUTTON = XpathString("//*[contains(@text, 'de.eso.emergencycall / ECall Test Menu')]", context="aem.main") # language independent
ECALL_TEST_MENU_TITLE = XpathString("//*[@text='ECall Settings 16'][@resource-id='de.eso.emergencycall:id/titleTextViewRef']", context="aem_emergencycall.ecall_settings") # language independent
ECALL_TEST_MENU_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]", context="aem_emergencycall.ecall_settings") # language independent

CONNECTIVITY_TEST_MENU_BUTTON = XpathString("//*[contains(@text, 'de.eso.phone / Connectivity Test Menu')]", context="aem.main") # language independent
CONNECTIVITY_TEST_MENU_TITLE = XpathString("//*[@text='Connectivity Settings: Wifi, Hotspot, Bluetooth'][@resource-id='de.eso.phone:id/titleTextViewRef'][@package='de.eso.phone']", context="phone.aem_connectivity_test_menu") # language independent
CONNECTIVITY_TEST_MENU_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]", context="phone.aem_connectivity_test_menu") # language independent

PREDICTION_SERVICES_AEM_BUTTON = XpathString("//*[contains(@text, 'technology.cariad.assistant / Prediction Services')]", context="aem.main") # language independent
PREDICTION_SERVICES_AEM_PACKAGE_CONTEXT_IDENTIFIER = XpathString("//*[@text='PredictionServices AEM' or @text='PCL Settings' or @text='PSC Settings' or @text='SAP Settings' or @text='PSC Backend' or @text='SAP Frontend' or @text='App Prediction'][@resource-id='technology.cariad.assistant:id/titleTextViewRef'][@package='technology.cariad.assistant']",
    context=["aem_predictionservices.psc_settings_aem",
             "aem_predictionservices.psc_settings_aem_pcl_settings",
             "aem_predictionservices.psc_settings_aem_psc_settings",
             "aem_predictionservices.psc_settings_aem_sap_settings",
			 "aem_predictionservices.psc_settings_aem_psc_backend",
			 "aem_predictionservices.psc_settings_aem_sap_frontend"]) # language independent
PREDICTION_SERVICES_AEM_TITLE = XpathString("//*[@text='PredictionServices AEM'][@resource-id='technology.cariad.assistant:id/titleTextViewRef'][@package='technology.cariad.assistant']", context="aem_predictionservices.psc_settings_aem") # language independent
PREDICTION_SERVICES_AEM_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]", context="aem_predictionservices.psc_settings_aem") # language independent

PREDICTION_SERVICES_AEM_PCL_SETTINGS_BUTTON = XpathString("//*[contains(@content-desc,'technology.cariad.assistant:string/aem_PCL_settings')]", context="aem_predictionservices.psc_settings_aem") # language independent
PREDICTION_SERVICES_AEM_PCL_SETTINGS_PACKAGE_CONTEXT_IDENTIFIER = XpathString("//*[@text='PCL Settings'][@resource-id='technology.cariad.assistant:id/titleTextViewRef'][@package='technology.cariad.assistant']", context="aem_predictionservices.psc_settings_aem_pcl_settings") # language independent
PREDICTION_SERVICES_AEM_PCL_SETTINGS_TITLE = XpathString("//*[@resource-id='technology.cariad.assistant:id/logoAndTitleLineContainer']/.//*[@text='PCL Settings'][@resource-id='technology.cariad.assistant:id/titleTextViewRef']", context="aem_predictionservices.psc_settings_aem_pcl_settings") # language independent
PREDICTION_SERVICES_AEM_PCL_SETTINGS_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]", context="aem_predictionservices.psc_settings_aem_pcl_settings") # language independent

PREDICTION_SERVICES_AEM_PSC_SETTINGS_BUTTON = XpathString("//*[contains(@content-desc, 'technology.cariad.assistant:string/aem_PSC_settings')]", context="aem_predictionservices.psc_settings_aem") # language independent
PREDICTION_SERVICES_AEM_PSC_SETTINGS_PACKAGE_CONTEXT_IDENTIFIER = XpathString("//*[@text='PSC Settings'][@resource-id='technology.cariad.assistant:id/titleTextViewRef'][@package='technology.cariad.assistant']", context="aem_predictionservices.psc_settings_aem_psc_settings") # language independent
PREDICTION_SERVICES_AEM_PSC_SETTINGS_TITLE = XpathString("//*[@resource-id='technology.cariad.assistant:id/logoAndTitleLineContainer']/.//*[@text='PSC Settings'][@resource-id='technology.cariad.assistant:id/titleTextViewRef']", context="aem_predictionservices.psc_settings_aem_psc_settings") # language independent
PREDICTION_SERVICES_AEM_PSC_SETTINGS_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]", context="aem_predictionservices.psc_settings_aem_psc_settings") # language independent

PREDICTION_SERVICES_AEM_SAP_SETTINGS_BUTTON = XpathString("//*[contains(@content-desc,'technology.cariad.assistant:string/aem_SAP_settings')]", context="aem_predictionservices.psc_settings_aem") # language independent
PREDICTION_SERVICES_AEM_SAP_SETTINGS_PACKAGE_CONTEXT_IDENTIFIER = XpathString("//*[@text='SAP Settings'][@resource-id='technology.cariad.assistant:id/titleTextViewRef'][@package='technology.cariad.assistant']", context="aem_predictionservices.psc_settings_aem_sap_settings") # language independent
PREDICTION_SERVICES_AEM_SAP_SETTINGS_TITLE = XpathString("//*[@resource-id='technology.cariad.assistant:id/logoAndTitleLineContainer']/.//*[@text='SAP Settings'][@resource-id='technology.cariad.assistant:id/titleTextViewRef']", context="aem_predictionservices.psc_settings_aem_sap_settings") # language independent
PREDICTION_SERVICES_AEM_SAP_SETTINGS_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]", context="aem_predictionservices.psc_settings_aem_sap_settings") # language independent

PREDICTION_SERVICES_AEM_PSC_BACKEND_BUTTON = XpathString("//*[contains(@content-desc, 'technology.cariad.assistant:string/aem_PSC_backend')]", context="aem_predictionservices.psc_settings_aem") # language independent
PREDICTION_SERVICES_AEM_PSC_BACKEND_PACKAGE_CONTEXT_IDENTIFIER = XpathString("//*[@text='PSC Backend'][@resource-id='technology.cariad.assistant:id/titleTextViewRef'][@package='technology.cariad.assistant']", context="aem_predictionservices.psc_settings_aem_psc_backend") # language independent
PREDICTION_SERVICES_AEM_PSC_BACKEND_TITLE = XpathString("//*[@resource-id='technology.cariad.assistant:id/logoAndTitleLineContainer']/.//*[@text='PSC Backend'][@resource-id='technology.cariad.assistant:id/titleTextViewRef']", context="aem_predictionservices.psc_settings_aem_psc_backend") # language independent
PREDICTION_SERVICES_AEM_PSC_BACKEND_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]", context="aem_predictionservices.psc_settings_aem_psc_backend") # language independent

PREDICTION_SERVICES_AEM_SAP_FRONTEND_BUTTON = XpathString("//*[contains(@content-desc,'technology.cariad.assistant:string/aem_SAP_frontend')]", context="aem_predictionservices.psc_settings_aem") # language independent
PREDICTION_SERVICES_AEM_SAP_FRONTEND_PACKAGE_CONTEXT_IDENTIFIER = XpathString("//*[@text='App Prediction'][@resource-id='technology.cariad.assistant:id/titleTextViewRef'][@package='technology.cariad.assistant']", context="aem_predictionservices.psc_settings_aem_sap_frontend") # language independent
PREDICTION_SERVICES_AEM_SAP_FRONTEND_TITLE = XpathString("//*[@resource-id='technology.cariad.assistant:id/logoAndTitleLineContainer']/.//*[@text='App Prediction'][@resource-id='technology.cariad.assistant:id/titleTextViewRef']", context="aem_predictionservices.psc_settings_aem_sap_frontend") # language independent
PREDICTION_SERVICES_AEM_SAP_FRONTEND_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]", context="aem_predictionservices.psc_settings_aem_sap_frontend") # language independent

SMART_SERVICES_BUTTON = XpathString("//*[contains(@text, 'technology.cariad.assistant / Smart Services')]", context="aem.main") # language independent
SMART_SERVICES_PACKAGE_CONTEXT_IDENTIFIER = XpathString("//*[@text='MainFragment'][@resource-id='technology.cariad.assistant:id/titleTextViewRef'][@package='technology.cariad.assistant']", context="aem_smartservice.main_fragment") # language independent
SMART_SERVICES_TITLE = XpathString("//*[@text='MainFragment'][@resource-id='technology.cariad.assistant:id/titleTextViewRef'][@package='technology.cariad.assistant']", context="aem_smartservice.main_fragment")
SMART_SERVICES_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]", context="aem_smartservice.main_fragment")

GDA_BUTTON = XpathString("//*[contains(@text, 'technology.cariad.assistant / GDA Developer Settings')]", context="aem.main") # language independent
# GDA = XpathString("//*[contains(@content-desc, 'GDA Developer Settings')][@package='de.eso.aem']") #_todo: not working, seems to be unused
GDA_DEVELOPER_SETTINGS_PACKAGE_CONTEXT_IDENTIFIER = XpathString("//*[@resource-id='technology.cariad.assistant:id/debug_fragment_container'] and //*[contains(@content-desc,'Online and Connectivity')] and //*[contains(@content-desc,'CDFW and Speech')] and //*[contains(@content-desc,'Dialog Configuration')]")
GDA_BACK_BUTTON = XpathString("//*[contains(@content-desc,'Back')]", context=[
		"aem_gda.online_and_connectivity"
	]) # language independent
GDA_ONLINE_AND_CONNECTIVITY_TITLE = XpathString("//*[contains(@content-desc, 'Online and Connectivity')][@package='technology.cariad.assistant'][@selected='true']", context="aem_gda.online_and_connectivity") # language independent
GDA_CDFW_AND_SPEECH_TITLE = XpathString("//*[contains(@content-desc, 'CDFW and Speech')][@package='technology.cariad.assistant'][@selected='true']", context="aem_gda.online_and_connectivity") # language independent
GDA_DIALOG_CONFIGURATION_TITLE = XpathString("//*[contains(@content-desc, 'Dialog Configuration')][@package='technology.cariad.assistant'][@selected='true']", context="aem_gda.dialog_configuration") # language independent
GDA_ONLINE_AND_CONNECTIVITY_BUTTON = XpathString("//*[contains(@content-desc, 'Online and Connectivity')][@package='technology.cariad.assistant']", context="aem_gda.online_and_connectivity") # language independent
GDA_CDFW_AND_SPEECH_BUTTON = XpathString("//*[contains(@content-desc, 'CDFW and Speech')][@package='technology.cariad.assistant']", context="aem_gda.online_and_connectivity") # language independent
GDA_DIALOG_CONFIGURATION_BUTTON = XpathString("//*[contains(@content-desc, 'Dialog Configuration')][@package='technology.cariad.assistant']", context="aem_gda.online_and_connectivity") # language independent
GDA_ONLINE_AND_CONNECTIVITY_VIN_EDIT_BUTTON = XpathString("//*[contains(@content-desc, 'debug_edit_vin')][@package='technology.cariad.assistant']", context="aem_gda.online_and_connectivity") # language independent
GDA_ONLINE_AND_CONNECTIVITY_VIN_EDIT_TITLE  = XpathString("//*[contains(@content-desc, 'technology.cariad.assistant:string/debug_hint_vin')][@package='technology.cariad.assistant']", context="aem_gda.online_and_connectivity_vin_edit") # language independent
GDA_ONLINE_AND_CONNECTIVITY_VIN_EDIT_CANCEL_BUTTON = XpathString("//*[@resource-id='android:id/button2'][@text='CANCEL']", context="aem_gda.online_and_connectivity_vin_edit") # language independent
GDA_ONLINE_AND_CONNECTIVITY_VIN_EDIT_SAVE_BUTTON = XpathString("//*[@resource-id='android:id/button1'][@text='SAVE']", context="aem_gda.online_and_connectivity_vin_edit") # language independent
