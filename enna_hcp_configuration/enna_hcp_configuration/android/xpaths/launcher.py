# -*- coding: utf-8 -*-
"""Module contains xpath of launcher app."""
from . import XpathString, APP_LIST_BUTTON

# pylint: disable=line-too-long
APP_LIST_BUTTON_SELECTED = XpathString(f"{APP_LIST_BUTTON.get()}[@selected='true']")
APP_GRID_BUTTON = APP_LIST_BUTTON

HOME_BUTTON = XpathString("//*[@resource-id='com.android.systemui:id/home_button']")
HOME_BUTTON_SELECTED = XpathString(f"{HOME_BUTTON.get()}[@selected='true']")
HOME_SCREEN_DASHBOARD = XpathString("//*[@resource-id='DashboardPager']")
LIST_CONTAINER = XpathString(clu46="//*[@resource-id='MainGridComposable']",
                             clu48="//*[@resource-id='MainGridComposable']",
                             clu53="//*[@resource-id='de.eso.launcheraudi:id/appGrid']",
                             clu55="//*[@resource-id='de.eso.launcheraudi:id/action_bar_root']/.//*[@resource-id='MainGridComposable'][@scrollable='true']")
APP_LIST_CONTAINER = XpathString(clu46="//*[@resource-id='MainGridComposable']",
                             clu48="//*[@resource-id='MainGridComposable']",
                             clu53="//*[@resource-id='de.eso.launcheraudi:id/appGrid']",
                             clu55="//*[@resource-id='de.eso.launcheraudi:id/action_bar_root']/.//*[@resource-id='MainGridComposable'][@scrollable='true']")

APP_TILE_SETTINGS = XpathString(clu46="//*[@resource-id='com.android.car.settings/com.android.car.settings.Settings_Launcher_Homepage']",
                                clu48="//*[@resource-id='com.android.car.settings/com.android.car.settings.Settings_Launcher_Homepage']",
                                clu53="//*[contains(@content-desc, '###Tile:com.android.car.settings/com.android.car.settings.Settings_Launcher_Homepage')]",
                                clu55="//*[@resource-id='com.android.car.settings/com.android.car.settings.Settings_Launcher_Homepage']")
APP_TILE_NAVIGATION = XpathString(clu46="//*[@resource-id='technology.cariad.navi.audi/de.eso.navi.ui.main.NavMainDelegateActivity']",
                                  clu48="//*[@resource-id='technology.cariad.navi.oi.audi/de.eso.navi.ui.main.NavMainDelegateActivity']",
                                  clu53="//*[contains(@content-desc, '###Tile:technology.cariad.navi.oi.audi/de.eso.navi.ui.main.NavMainDelegateActivity')]",
                                  clu55="//*[@resource-id='technology.cariad.navi.audi/de.eso.navi.ui.main.NavMainDelegateActivity']")
APP_TILE_RADIO = XpathString(clu46="//*[@resource-id='de.eso.radio/de.eso.radio.headless.mediabrowser.RadioBrowserService']",
                             clu48="//*[@resource-id='de.eso.radio/de.eso.radio.headless.mediabrowser.RadioBrowserService']",
                             clu53="//*[contains(@content-desc, '###Tile:de.eso.radio/de.eso.radio.headless.mediabrowser.RadioBrowserService')]",
                             clu55="//*[@resource-id='de.eso.radio/de.eso.radio.headless.mediabrowser.RadioBrowserService']")
APP_TILE_PHONE = XpathString(clu46="//*[@resource-id='de.eso.phone/de.eso.phone.ui.MainActivity']",
                             clu48="//*[@resource-id='de.eso.phone/de.eso.phone.ui.MainActivity']",
                             clu53="//*[contains(@content-desc, '###Tile:de.eso.phone/de.eso.phone.ui.MainActivity')]",
                             clu55="//*[@resource-id='de.eso.phone/de.eso.phone.ui.MainActivity']")
APP_TILE_CAR = XpathString(clu46="//*[@resource-id='de.eso.car.audi/de.eso.car.MainActivityAliasPPE']",
                           clu48="//*[@resource-id='de.eso.car.audi/de.eso.car.MainActivityAliasPPE']",
                           clu53="//*[contains(@content-desc, '###Tile:de.eso.car.audi/de.eso.car.MainActivityAliasPPE')]",
                           clu55="//*[@resource-id='de.eso.car.audi/de.eso.car.MainActivityAliasPPE']")
APP_TILE_DRIVER_ASSIST = XpathString(clu46="//*[@resource-id='de.eso.car.audi/de.eso.car.FasAppGridActivity']",
                                     clu48="//*[@resource-id='de.eso.car.audi/de.eso.car.FasAppGridActivity']",
                                     clu53="//*[contains(@content-desc, '###Tile:de.eso.car.audi/de.eso.car.FasAppGridActivity')]")
APP_TILE_ANDROID_AUTO = XpathString(clu46="//*[@resource-id='com.harman.connectivity.androidauto']",
                                    clu48="//*[@resource-id='com.google.android.embedded.projection']",
                                    clu53="//*[contains(@content-desc, '###Tile:com.google.android.embedded.projection/com.google.android.apps.auto.aareceiver.ui.ProjectionDeviceDisambiguationActivity')]")
APP_TILE_CAR_PLAY = XpathString(clu46="//*[@resource-id='com.harman.connectivity.carplay.app']",
                                clu48="//*[@resource-id='de.eso.carplay']",
                                clu53="//*[contains(@content-desc, '###Tile:de.eso.carplay')]",
                                clu55="//*[@resource-id='com.harman.connectivity.carplay.app']")
APP_TILE_STORE = XpathString(clu46="//*[@resource-id='com.harman.ignite.appstore.audi/com.harman.ignite.appstore.mainactivity.MainActivity']",
                             clu48="//*[@resource-id='com.harman.ignite.appstore.audi/com.harman.ignite.appstore.mainactivity.MainActivity']",
                             clu53="//*[contains(@content-desc, '###Tile:com.harman.ignite.appstore.audi/com.harman.ignite.appstore.mainactivity.MainActivity')]",
                             clu55="//*[@resource-id='com.harman.ignite.appstore.audi/com.harman.ignite.appstore.mainactivity.MainActivity']")
APP_TILE_LEGAL = XpathString(clu46="//*[@resource-id='com.valtech_mobility.legal.audi/com.valtech_mobility.legal.MainActivity']",
                             clu48="//*[@resource-id='com.valtech_mobility.legal.audi/com.valtech_mobility.legal.MainActivity']",
                             clu53="//*[contains(@content-desc, '###Tile:com.valtech_mobility.legal.audi/com.valtech_mobility.legal.MainActivity')]",
                             clu55="//*[@resource-id='com.valtech_mobility.legal.audi/com.valtech_mobility.legal.MainActivity']")
APP_TILE_ONLINE_MANUALS = XpathString(clu46="//*[@resource-id='com.valtech_mobility.obb.audi/com.valtech_mobility.obb.MainActivity']",
                                      clu48="//*[@resource-id='com.valtech_mobility.obb.audi/com.valtech_mobility.obb.MainActivity']",
                                      clu53="//*[contains(@content-desc, '###Tile:com.valtech_mobility.obb.audi/com.valtech_mobility.obb.MainActivity')]",
                                      clu55="//*[@resource-id='com.valtech_mobility.obb.audi/com.valtech_mobility.obb.MainActivity']")
APP_TILE_GLOBAL_SEARCH = XpathString(clu46="//*[@resource-id='de.eso.globalsearch/de.eso.globalsearch.ui.GlobalSearchActivity']",
                                     clu48="//*[@resource-id='de.eso.globalsearch/de.eso.globalsearch.ui.GlobalSearchActivity']",
                                     clu53="//*[contains(@content-desc, '###Tile:de.eso.globalsearch/de.eso.globalsearch.ui.GlobalSearchActivity')]",
                                     clu55="//*[@resource-id='de.eso.globalsearch/de.eso.globalsearch.ui.GlobalSearchActivity']")
APP_TILE_IN_CAR_OFFICE = XpathString(clu46="//*[@resource-id='com.valtech_mobility.ico.audi/com.valtech_mobility.ico.MainActivity']",
                                     clu53="//*[contains(@content-desc, 'In-Car Office')]",
                                     clu55="//*[@resource-id='com.valtech_mobility.ico.audi/com.valtech_mobility.ico.MainActivity']")
APP_TILE_AEM = XpathString(clu46="//*[@resource-id='de.eso.aem/de.eso.aem.ui.MainActivity']",
                           clu48="//*[@resource-id='de.eso.aem/de.eso.aem.ui.MainActivity']",
                           clu53="//*[contains(@content-desc, 'Tile:de.eso.aem/de.eso.aem.ui.MainActivity')]",
                           clu55="//*[@resource-id='de.eso.aem/de.eso.aem.ui.MainActivity']")
APP_TILE_DIGITAL_KEY = XpathString(clu46="//*[@resource-id='de.eso.mobiledevicekey/de.eso.mobiledevicekey.ui.MainActivity']",
                                   clu48="//*[@resource-id='de.eso.mobiledevicekey/de.eso.mobiledevicekey.ui.MainActivity']",
                                   clu53="//*[contains(@content-desc, '###Tile:de.eso.mobiledevicekey/de.eso.mobiledevicekey.ui.MainActivity')]",
                                   clu55="//*[@resource-id='de.eso.mobiledevicekey/de.eso.mobiledevicekey.ui.MainActivity']")
APP_TILE_CORE_SERVICE = XpathString("//*[@resource-id='de.esolutions.coreservices/de.esolutions.coreservices.gem2.ui.MainActivity']")
APP_TILE_EXPERIENCES = XpathString(clu46="//*[@resource-id='technology.cariad.interiorexperience.audi.experiences/technology.cariad.interiorexperience.ui.main.MainActivity']",
                                   clu48="//*[@resource-id='technology.cariad.interiorexperience.audi.experiences/technology.cariad.interiorexperience.ui.main.MainActivity']",
                                   clu55="//*[@resource-id='technology.cariad.interiorexperience.icc.mqb.audi.experiences/technology.cariad.interiorexperience.ui.main.MainActivity']")
APP_TILE_CHARGING = XpathString("//*[@resource-id='de.eso.car.audi/de.eso.car.ChargingActivityBevAlias' or @resource-id='de.eso.car.audi/de.eso.car.ChargingActivityPhevAlias']")
APP_TILE_USB_DRIVE = XpathString(clu46="//*[@resource-id='com.harman.mediacoreservice/com.harman.mediacoreservice.harmanlocalplayer.HarmanUSBPort1Player']",
                                 clu53="//*[contains(@content-desc, '###Tile:de.esolutions.mediaapp/de.esolutions.mediaapp.service.browserservice.USB1MediaBrowserService')]",
                                 clu55="//*[@resource-id='com.harman.mediacoreservice/com.harman.mediacoreservice.harmanlocalplayer.HarmanUSBPort1Player']")
APP_TILE_MAGIC_ENGINEERING = XpathString(clu48="//*[@resource-id='technology.cariad.magic.engineering/technology.cariad.magic.engineering.ui.MainActivity']",
                                         clu53="//*[contains(@content-desc, '###Tile:technology.cariad.magic.engineering/technology.cariad.magic.engineering.ui.MainActivity')]",
                                         clu55="//*[@resource-id='technology.cariad.magic.engineering/technology.cariad.magic.engineering.ui.MainActivity']")
APP_TILE_THEMES = XpathString("//*[@resource-id='com.valtech_mobility.aaam.audi/com.valtech_mobility.aaam.ui.AaamActivity']")

MEDIA_SOURCES = XpathString("//*[@resource-id='de.eso.launcheraudi:id/mediaAppGrid']")
MEDIA_SOURCE_TILE_CONNECTION_MANAGER = XpathString("//*[contains(@content-desc, '###Tile:ConnectDevice')]")
MEDIA_SOURCE_TILE_ALEXA = XpathString("//*[contains(@content-desc, '###Tile:de.esolutions.alexa.audi/com.amazon.alexa.auto.media.browse.AlexaMediaBrowseService')]")
MEDIA_SOURCE_TILE_BLUETOOTH = XpathString("//*[contains(@content-desc, '###Tile:com.harman.mediacoreservice/com.harman.mediacoreservice.harmaniapplayer.HarmanBTIAPPlayer')]")
MEDIA_SOURCE_TILE_RADIO = XpathString("//*[contains(@content-desc, '###Tile:de.eso.radio/de.eso.radio.headless.mediabrowser.RadioBrowserService')]")
MEDIA_SOURCE_TILE_SPOTIFY = XpathString("//*[contains(@content-desc, '###Tile:com.spotify.music/com.spotify.automotive.mediabrowserservice.AutomotiveMediaBrowserService')]")
MEDIA_SOURCE_TILE_USB_DEVICE = XpathString("//*[contains(@content-desc, '###Tile:com.harman.mediacoreservice/com.harman.mediacoreservice.harmanlocalplayer.HarmanUSBPort1Player')]")
