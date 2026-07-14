# -*- coding: utf-8 -*-
"""Module contains xpath of permissioncontroler app."""
import enna_hcp_configuration.android.xpaths
from enna_hcp_configuration.texts import TextObject
from . import XpathString

if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.de.eso.car import audi as car_settings
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.de.eso.car import audi as car_settings
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.de.eso.car import audi as car_settings
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.de.eso.car import audi as car_settings
else:
	from enna_hcp_configuration.texts.CLU46.center.de.eso.car import audi as car_settings

# pylint: disable=line-too-long

permission_allow = TextObject(bs_BA="Dozvoli", cs_CZ="Povolit", da_DK="Tillad", de_DE="Zulassen", el_GR="Να επιτρέπεται", en_GB="Allow", es_ES="Permitir", fi_FI="Salli", fr_FR="Autoriser", hr_HR="Dopusti", hu_HU="Engedélyezés", it_IT="Consenti", nl_NL="Toestaan", no_NO="Tillat", pl_PL="Zezwalaj", pt_PT="Permitir", ro_RO="Permite", ru_RU="Разрешить", sk_SK="Povoliť", sl_SI="Dovoli", sr_RS="Dozvoli", sv_SE="Tillåt", tr_TR="İzin ver", uk_UA="Дозволити")
permission_deny = TextObject(bs_BA="Nemoj dozvoliti", cs_CZ="Nepovolovat", da_DK="Tillad ikke", de_DE="Nicht zulassen", el_GR="Να μην επιτρέπεται", en_GB="Not allowed", es_ES="No permitir", fi_FI="Älä salli", fr_FR="Ne pas autoriser", hr_HR="Nemoj dopustiti", hu_HU="Tiltás", it_IT="Non consentire", nl_NL="Niet toestaan", no_NO="Ikke tillat", pl_PL="Nie zezwalaj", pt_PT="Não permitir", ro_RO="Nu permite", ru_RU="Запретить", sk_SK="Nepovoliť", sl_SI="Ne dovoli", sr_RS="Ne dozvoli", sv_SE="Tillåt inte", tr_TR="İzin verme", uk_UA="Не дозволяти")
permission_usage = TextObject(bs_BA="Dozvoli samo dok se aplikacija koristi", cs_CZ="Povolit jen při používání aplikace", da_DK="Tillad kun, mens appen er i brug", de_DE="Zugriff nur während der Nutzung der App zulassen", el_GR="Μόνο με τη χρήση της εφαρμογής", en_GB="Allow only while using the app", es_ES="Permitir solo mientras se usa la aplicación", fi_FI="Salli vain käytön aikana", fr_FR="Autoriser seulement si l'appli est en cours d'utilisation", hr_HR="Dopusti samo dok se aplikacija koristi", hu_HU="Csak az alkalmazás használatakor engedélyezett", it_IT="Consenti solo mentre l'app è in uso", nl_NL="Toestaan bij gebruik van app", no_NO="Bare tillat når appen brukes", pl_PL="Zezwalaj tylko podczas używania aplikacji", pt_PT="Permitir apenas enquanto uso a app", ro_RO="Permite numai când folosești aplicația", ru_RU="Разрешить только во время использования приложения", sk_SK="Povoliť iba pri používaní aplikácie", sl_SI="Dovoli samo med uporabo aplikacije", sr_RS="Dozv. samo dok se apl. koristi", sv_SE="Tillåt bara när appen används", tr_TR="Yalnızca uygulama kullanılırken izin ver", uk_UA="Дозволяти, лише коли додаток використовується")

permission_no_permission = TextObject(bs_BA="", cs_CZ="", da_DK="", de_DE="Keine Berechtigungen zugelassen", el_GR="", en_GB="No Permissions allowed", es_ES="", fi_FI="", fr_FR="", hr_HR="", hu_HU="", it_IT="", nl_NL="", no_NO="", pl_PL="", pt_PT="", ro_RO="", ru_RU="", sk_SK="", sl_SI="", sr_RS="", sv_SE="", tr_TR="", uk_UA="")
permission_call_logs = TextObject(bs_BA="", cs_CZ="", da_DK="", de_DE="", el_GR="", en_GB="Call logs", es_ES="", fi_FI="", fr_FR="", hr_HR="", hu_HU="", it_IT="", nl_NL="", no_NO="", pl_PL="", pt_PT="", ro_RO="", ru_RU="", sk_SK="", sl_SI="", sr_RS="", sv_SE="", tr_TR="", uk_UA="")
permission_contacts = TextObject(bs_BA="", cs_CZ="", da_DK="", de_DE="", el_GR="", en_GB="Contacts", es_ES="", fi_FI="", fr_FR="", hr_HR="", hu_HU="", it_IT="", nl_NL="", no_NO="", pl_PL="", pt_PT="", ro_RO="", ru_RU="", sk_SK="", sl_SI="", sr_RS="", sv_SE="", tr_TR="", uk_UA="")
permission_files_media = TextObject(bs_BA="", cs_CZ="", da_DK="", de_DE="", el_GR="", en_GB="Files_Media", es_ES="", fi_FI="", fr_FR="", hr_HR="", hu_HU="", it_IT="", nl_NL="", no_NO="", pl_PL="", pt_PT="", ro_RO="", ru_RU="", sk_SK="", sl_SI="", sr_RS="", sv_SE="", tr_TR="", uk_UA="")

permission_notifications = TextObject(bs_BA="Obavještenja", cs_CZ="Oznámení", da_DK="Notifikationer", de_DE="Benachrichtigungen", el_GR="Ειδοποιήσεις", en_GB="Notifications", es_ES="Notificaciones", fi_FI="Ilmoitukset", fr_FR="Notifications", hr_HR="Obavijesti", hu_HU="Értesítések", it_IT="Notifiche", nl_NL="Meldingen", no_NO="Varsler", pl_PL="Powiadomienia", pt_PT="Notificações", ro_RO="Notificări", ru_RU="Уведомления", sk_SK="Upozornenia", sl_SI="Obvestila", sr_RS="Obaveštenja", sv_SE="Aviseringar", tr_TR="Bildirimler", uk_UA="Сповіщення")
permission_nearby_devices = TextObject(bs_BA="Uređaji u blizini", cs_CZ="Zařízení v okolí", da_DK="Enheder i nærheden", de_DE="Geräte in der Nähe", el_GR="Συσκευές σε κοντινή απόσταση", en_GB="Nearby devices", es_ES="Dispositivos cercanos", fi_FI="Lähellä olevat laitteet", fr_FR="Appareils à proximité", hr_HR="Uređaji u blizini", hu_HU="Közeli eszközök", it_IT="Dispositivi nelle vicinanze", nl_NL="Apparaten in de buurt", no_NO="Enheter i nærheten", pl_PL="Urządzenia w pobliżu", pt_PT="Dispositivos próximos", ro_RO="Dispozitive din apropiere", ru_RU="Уведомления", sk_SK="Zariadenia v okolí", sl_SI="Naprave v bližini", sr_RS="Uređaji u blizini", sv_SE="Enheter i närheten", tr_TR="Yakındaki cihazlar", uk_UA="Пристрої поблизу")
permission_microphone = TextObject(bs_BA="Mikrofon", cs_CZ="Mikrofon", da_DK="Mikrofon", de_DE="Mikrofon", el_GR="Μικρόφωνο", en_GB="Microphone", es_ES="Micrófono", fi_FI="Mikrofoni", fr_FR="Microphone", hr_HR="Mikrofon", hu_HU="Mikrofon", it_IT="Microfono", nl_NL="Microfoon", no_NO="Mikrofon", pl_PL="Mikrofon", pt_PT="Microfone", ro_RO="Microfon", ru_RU="Микрофон", sk_SK="Mikrofón", sl_SI="Mikrofon", sr_RS="Mikrofon", sv_SE="Mikrofon", tr_TR="Mikrofon", uk_UA="Мікрофон")
permission_location = TextObject(bs_BA="Lokacija", cs_CZ="Poloha", da_DK="Lokation", de_DE="Standort", el_GR="Τοποθεσία", en_GB="Location", es_ES="Ubicación", fi_FI="Sijainti", fr_FR="Position", hr_HR="Lokacija", hu_HU="Helyadatok", it_IT="Posizione", nl_NL="Locatie", no_NO="Posisjon", pl_PL="Lokalizacja", pt_PT="Localização", ro_RO="Locație", ru_RU="Местоположение", sk_SK="Poloha", sl_SI="Lokacija", sr_RS="Lokacija", sv_SE="plats", tr_TR="Konum", uk_UA="Геодані")
permission_phone = TextObject(bs_BA="Telefon", cs_CZ="Telefon", da_DK="Telefon", de_DE="Telefon", el_GR="Τηλέφωνο", en_GB="Phone", es_ES="Teléfono", fi_FI="Puhelin", fr_FR="Téléphone", hr_HR="Telefon", hu_HU="Telefon", it_IT="Telefono", nl_NL="Telefoon", no_NO="Telefon", pl_PL="Telefon", pt_PT="Telemóvel", ro_RO="Telefon", ru_RU="Телефон", sk_SK="Telefón", sl_SI="Telefon", sr_RS="Telefon", sv_SE="Telefon", tr_TR="Telefon", uk_UA="Телефон")
permission_additional = TextObject(bs_BA="Dodatna odobrenja", cs_CZ="Další oprávnění", da_DK="Yderligere tilladelser", de_DE="Zusätzliche Berechtigungen", el_GR="Πρόσθετες άδειες", en_GB="Additional permissions", es_ES="Permisos adicionales", fi_FI="Lisäluvat", fr_FR="Autorisations supplémentaires", hr_HR="Dodatna dopuštenja", hu_HU="További engedélyek", it_IT="Altre autorizzazioni", nl_NL="Aanvullende rechten", no_NO="Flere tillatelser", pl_PL="Dodatkowe uprawnienia", pt_PT="Autorizações adicionais", ro_RO="Permisiuni suplimentare", ru_RU="Ещё разрешения", sk_SK="Ďalšie povolenia", sl_SI="Dodatna dovoljenja", sr_RS="Uređaji u blizini", sv_SE="Ytterligare behörigheter", tr_TR="Ek izinler", uk_UA="Додаткові дозволи")

#_todo: no texts found in texttool and current definitions seem to be outdated
# pylint: disable=line-too-long
BACK_BUTTON = XpathString(f"//*{str(car_settings.departure_time_setup_back).replace('@text', '@content-desc')}")
LIST_CONTAINER = XpathString("//*[contains(@content-desc, 'com.android.car.ui.utils.ROTARY_CONTAINER') or @content-desc='android.rotary.VERTICALLY_SCROLLABLE' or contains(@resource-id,'de.eso.launcheraudi:id/appGrid')]")

FILES_AND_MEDIA_BUTTON = XpathString("//*[contains(@text, 'Dateien und Medien')]")
MEDIACORESERVICE_BUTTON = XpathString("//*[contains(@text, 'MediaCoreService')]")

POPUP_NOTIFICATIONS_DIALOG_ERLIN_LOCATION_TITLE = XpathString("//*[@resource-id='com.android.permissioncontroller:id/car_ui_alert_title'][contains(@text, 'erlauben, den Gerätestandort abzurufen?')]")
POPUP_NOTIFICATIONS_DIALOG_ERLIN_LOCATION_BUTTON_ALLOW = XpathString("//*[contains(@text, 'Allow') or contains(@text, 'Zulassen')]")
POPUP_NOTIFICATIONS_DIALOG_ERLIN_SOUND_TITLE = XpathString("//*[@resource-id='com.android.permissioncontroller:id/car_ui_alert_title'][contains(@text, 'erlauben, Audioaufnahmen zu machen?')]")
POPUP_NOTIFICATIONS_DIALOG_ERLIN_SOUND_BUTTON_USE = XpathString("//*[contains(@text, 'While using the app') or contains(@text, 'Bei Nutzung der App')]")
POPUP_NOTIFICATIONS_DIALOG_ERLIN_NOTIFICATIONS_TITLE = XpathString("//*[@resource-id='com.android.permissioncontroller:id/car_ui_alert_title'][contains(@text, 'erlauben, dir Benachrichtigungen zu senden?')]")
POPUP_NOTIFICATIONS_DIALOG_ERLIN_NOTIFICATIONS_BUTTON_ALLOW = XpathString("//*[contains(@text, 'Allow') or contains(@text, 'Zulassen')]")

#TITLE = XpathString("//*[@resource-id='com.android.permissioncontroller:id/recycler_view'][contains(@text, 'App-Berechtigungen')] or //*[@resource-id='com.android.permissioncontroller:id/car_ui_toolbar_title'][@text='App permissions']") # was SETTINGS_APP_PERMISSION_TITLE
APP_PERMISSION_TITLE = XpathString("//*[@resource-id='com.android.permissioncontroller:id/recycler_view'] and //*[contains(@text, 'App-Berechtigungen') or contains(@text, 'App permissions')]")
DATA_AND_MEDIA_TITLE = XpathString("//*[@resource-id='com.android.permissioncontroller:id/car_ui_toolbar_title'][contains(@text, 'Files and media permission') or contains(@text, 'Dateien und Medien')]") # was SETTINGS_APP_PERMISSION_DATA_AND_MEDIA_TITLE

MEDIACORESERVICE_TITLE = XpathString("//*[@resource-id='android:id/title' or @resource-id='com.android.permissioncontroller:id/car_ui_toolbar_title'][contains(@text, 'Berechtigung: Dateien und Medien')]") # was

PRIVACY_APP_PERMISSIONS_TITLE = XpathString("//*[@resource-id='com.android.permissioncontroller:id/car_ui_toolbar_title'] and //*[contains(@text, 'App permissions') or contains(@text, 'App-Berechtigungen')]") # was SETTINGS_PRIVACY_APP_PERMISSIONS_TITLE

# Dialog Buttons
DIALOG_DENY_PERMISSION_ACCEPT_BUTTON = XpathString("//*[@resource-id='android:id/buttonPanel']/.//*[@resource-id='android:id/button1']")
DIALOG_DENY_PERMISSION_CANCEL_BUTTON = XpathString("//*[@resource-id='android:id/buttonPanel']/.//*[@resource-id='android:id/button2']")


# for settings.SetSystemAppPermission
MAIN_LIST = XpathString("//*[contains(@resource-id,'car_ui_internal_recycler_view')]")
PERMISSION_BACK_BUTTON = XpathString("//*[@resource-id='com.android.permissioncontroller:id/car_ui_toolbar_nav_icon_container'][@index='1']")
PERMISSION_ALLOW = XpathString(f"//*{permission_allow}")
PERMISSION_DENY = XpathString(f"//*{permission_deny}")
PERMISSION_USAGE = XpathString(f"//*{permission_usage}")

PERMISSION_NO_PERMISSIONS = XpathString(f"//*{permission_no_permission}")

PERMISSION_CALL_LOGS = XpathString(f"//*{permission_call_logs}")
PERMISSION_CONTACTS = XpathString(f"//*{permission_contacts}")
PERMISSION_LOCATION = XpathString(f"//*{permission_location}")
PERMISSION_MICROPHONE = XpathString(f"//*{permission_microphone}")
PERMISSION_NEARBY_DEVICES = XpathString(f"//*{permission_nearby_devices}")
PERMISSION_PHONE = XpathString(f"//*{permission_phone}")

PERMISSION_FILES_MEDIA = XpathString(f"//*{permission_files_media}")
PERMISSION_ADDITIONAL = XpathString(f"//*{permission_additional}")
PERMISSION_NOTIFICATIONS = XpathString(f"//*{permission_notifications}")
PERMISSION_CARINFO  = XpathString("//*[@content-desc='CARINFO']")
