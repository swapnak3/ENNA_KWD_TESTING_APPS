# -*- coding: utf-8 -*-
"""Module contains xpath of launcher app."""
import enna_hcp_configuration.android.xpaths
from enna_hcp_configuration.texts import TextObject
from . import XpathString

# pylint: disable=line-too-long, fixme

if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.VTM import OnlineBordbook as obb
	obb.obb_settings_screen__imprint__text = TextObject(bs_BA="Impresum", cs_CZ="Impressum", da_DK="Kolofon", de_DE="Impressum", el_GR="Στοιχεία έκδοσης", en_GB="About us", es_ES="Nota legal", fi_FI="Julkaisutiedot", fr_FR="Mentions légales", hr_HR="Impresum", hu_HU="Impresszum", it_IT="Informazioni societarie (Impressum)", nl_NL="Impressum", no_NO="Utgiverinformasjon", pl_PL="Stopka redakcyjna", pt_PT="Aviso legal", ro_RO="Caseta redacţiei", ru_RU="Импрессум", sk_SK="Tiráž", sl_SI="Impresum", sr_RS="Impresum", sv_SE="Tryckinformation", tr_TR="Künye", uk_UA="Вихідні дані")
	obb.obb_settings_screen__data_protection_information__text = TextObject(bs_BA="Napomene o zaštiti podataka", cs_CZ="Pokyny k ochraně dat", da_DK="Databeskyttelsesinformationer", de_DE="Datenschutzhinweise", el_GR="Υποδείξεις προστασίας δεδομένων προσωπικού χαρακτήρα", en_GB="Data protection notes", es_ES="Aviso de privacidad", fi_FI="Tietosuojaohjeet", fr_FR="Informations relatives à la protection des données", hr_HR="Napomene o zaštiti podataka", hu_HU="Adatvédelmi irányelvek", it_IT="Avvertenze sulla protezione dati", nl_NL="Privacyrichtlijnen", no_NO="Informasjon om personvern", pl_PL="Polityka prywatności", pt_PT="Política de proteção de dados", ro_RO="Informaţii protecţia datelor", ru_RU="Примечания по защите персональных данных", sk_SK="Pokyny k ochrane údajov", sl_SI="Napotki za varovanje podatkov", sr_RS="Napomene o zaštiti podataka", sv_SE="Dataskydd", tr_TR="Veri koruma bilgileri", uk_UA="Вказівки із захисту даних")
	obb.obb_settings_screen__open_source_license__title = TextObject(bs_BA="Open Source Software Notice", cs_CZ="Open Source Software Notice", da_DK="Open Source Software Notice", de_DE="Open Source Software Notice", el_GR="Open Source Software Notice", en_GB="Open Source Software Notice", es_ES="Open Source Software Notice", fi_FI="Open Source Software Notice", fr_FR="Open Source Software Notice", hr_HR="Open Source Software Notice", hu_HU="Open Source Software Notice", it_IT="Open Source Software Notice", nl_NL="Open Source Software Notice", no_NO="Open Source Software Notice", pl_PL="Open Source Software Notice", pt_PT="Open Source Software Notice", ro_RO="Open Source Software Notice", ru_RU="Open Source Software Notice", sk_SK="Open Source Software Notice", sl_SI="Open Source Software Notice", sr_RS="Open Source Software Notice", sv_SE="Open Source Software Notice", tr_TR="Open Source Software Notice", uk_UA="Open Source Software Notice")
	obb.obb_settings_screen__title_line__title = TextObject(bs_BA="Postavke", cs_CZ="Nastavení", da_DK="Indstillinger", de_DE="Einstellungen", el_GR="Ρυθμίσεις", en_GB="Settings", es_ES="Ajustes", fi_FI="Asetukset", fr_FR="Réglages", hr_HR="Postavke", hu_HU="Beállítások", it_IT="Impostazioni", nl_NL="Instellingen", no_NO="Innstillinger", pl_PL="Ustawienia", pt_PT="Ajustes", ro_RO="Setări", ru_RU="Настройки", sk_SK="Nastavenia", sl_SI="Nastavitve", sr_RS="Podešavanja", sv_SE="Inställningar", tr_TR="Ayarlar", uk_UA="Настройки")
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.VTM import OnlineBordbook as obb
	obb.obb_settings_screen__imprint__text = TextObject(bs_BA="Impresum", cs_CZ="Impressum", da_DK="Kolofon", de_DE="Impressum", el_GR="Στοιχεία έκδοσης", en_GB="About us", es_ES="Nota legal", fi_FI="Julkaisutiedot", fr_FR="Mentions légales", hr_HR="Impresum", hu_HU="Impresszum", it_IT="Informazioni societarie (Impressum)", nl_NL="Impressum", no_NO="Utgiverinformasjon", pl_PL="Stopka redakcyjna", pt_PT="Aviso legal", ro_RO="Caseta redacţiei", ru_RU="Импрессум", sk_SK="Tiráž", sl_SI="Impresum", sr_RS="Impresum", sv_SE="Tryckinformation", tr_TR="Künye", uk_UA="Вихідні дані")
	obb.obb_settings_screen__data_protection_information__text = TextObject(bs_BA="Napomene o zaštiti podataka", cs_CZ="Pokyny k ochraně dat", da_DK="Databeskyttelsesinformationer", de_DE="Datenschutzhinweise", el_GR="Υποδείξεις προστασίας δεδομένων προσωπικού χαρακτήρα", en_GB="Data protection notes", es_ES="Aviso de privacidad", fi_FI="Tietosuojaohjeet", fr_FR="Informations relatives à la protection des données", hr_HR="Napomene o zaštiti podataka", hu_HU="Adatvédelmi irányelvek", it_IT="Avvertenze sulla protezione dati", nl_NL="Privacyrichtlijnen", no_NO="Informasjon om personvern", pl_PL="Polityka prywatności", pt_PT="Política de proteção de dados", ro_RO="Informaţii protecţia datelor", ru_RU="Примечания по защите персональных данных", sk_SK="Pokyny k ochrane údajov", sl_SI="Napotki za varovanje podatkov", sr_RS="Napomene o zaštiti podataka", sv_SE="Dataskydd", tr_TR="Veri koruma bilgileri", uk_UA="Вказівки із захисту даних")
	obb.obb_settings_screen__open_source_license__title = TextObject(bs_BA="Open Source Software Notice", cs_CZ="Open Source Software Notice", da_DK="Open Source Software Notice", de_DE="Open Source Software Notice", el_GR="Open Source Software Notice", en_GB="Open Source Software Notice", es_ES="Open Source Software Notice", fi_FI="Open Source Software Notice", fr_FR="Open Source Software Notice", hr_HR="Open Source Software Notice", hu_HU="Open Source Software Notice", it_IT="Open Source Software Notice", nl_NL="Open Source Software Notice", no_NO="Open Source Software Notice", pl_PL="Open Source Software Notice", pt_PT="Open Source Software Notice", ro_RO="Open Source Software Notice", ru_RU="Open Source Software Notice", sk_SK="Open Source Software Notice", sl_SI="Open Source Software Notice", sr_RS="Open Source Software Notice", sv_SE="Open Source Software Notice", tr_TR="Open Source Software Notice", uk_UA="Open Source Software Notice")
	obb.obb_settings_screen__title_line__title = TextObject(bs_BA="Postavke", cs_CZ="Nastavení", da_DK="Indstillinger", de_DE="Einstellungen", el_GR="Ρυθμίσεις", en_GB="Settings", es_ES="Ajustes", fi_FI="Asetukset", fr_FR="Réglages", hr_HR="Postavke", hu_HU="Beállítások", it_IT="Impostazioni", nl_NL="Instellingen", no_NO="Innstillinger", pl_PL="Ustawienia", pt_PT="Ajustes", ro_RO="Setări", ru_RU="Настройки", sk_SK="Nastavenia", sl_SI="Nastavitve", sr_RS="Podešavanja", sv_SE="Inställningar", tr_TR="Ayarlar", uk_UA="Настройки")
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.VTM import OnlineBordbook as obb
	obb.obb_settings_screen__imprint__text = TextObject(bs_BA="Impresum", cs_CZ="Impressum", da_DK="Kolofon", de_DE="Impressum", el_GR="Στοιχεία έκδοσης", en_GB="About us", es_ES="Nota legal", fi_FI="Julkaisutiedot", fr_FR="Mentions légales", hr_HR="Impresum", hu_HU="Impresszum", it_IT="Informazioni societarie (Impressum)", nl_NL="Impressum", no_NO="Utgiverinformasjon", pl_PL="Stopka redakcyjna", pt_PT="Aviso legal", ro_RO="Caseta redacţiei", ru_RU="Импрессум", sk_SK="Tiráž", sl_SI="Impresum", sr_RS="Impresum", sv_SE="Tryckinformation", tr_TR="Künye", uk_UA="Вихідні дані")
	obb.obb_settings_screen__data_protection_information__text = TextObject(bs_BA="Napomene o zaštiti podataka", cs_CZ="Pokyny k ochraně dat", da_DK="Databeskyttelsesinformationer", de_DE="Datenschutzhinweise", el_GR="Υποδείξεις προστασίας δεδομένων προσωπικού χαρακτήρα", en_GB="Data protection notes", es_ES="Aviso de privacidad", fi_FI="Tietosuojaohjeet", fr_FR="Informations relatives à la protection des données", hr_HR="Napomene o zaštiti podataka", hu_HU="Adatvédelmi irányelvek", it_IT="Avvertenze sulla protezione dati", nl_NL="Privacyrichtlijnen", no_NO="Informasjon om personvern", pl_PL="Polityka prywatności", pt_PT="Política de proteção de dados", ro_RO="Informaţii protecţia datelor", ru_RU="Примечания по защите персональных данных", sk_SK="Pokyny k ochrane údajov", sl_SI="Napotki za varovanje podatkov", sr_RS="Napomene o zaštiti podataka", sv_SE="Dataskydd", tr_TR="Veri koruma bilgileri", uk_UA="Вказівки із захисту даних")
	obb.obb_settings_screen__open_source_license__title = TextObject(bs_BA="Open Source Software Notice", cs_CZ="Open Source Software Notice", da_DK="Open Source Software Notice", de_DE="Open Source Software Notice", el_GR="Open Source Software Notice", en_GB="Open Source Software Notice", es_ES="Open Source Software Notice", fi_FI="Open Source Software Notice", fr_FR="Open Source Software Notice", hr_HR="Open Source Software Notice", hu_HU="Open Source Software Notice", it_IT="Open Source Software Notice", nl_NL="Open Source Software Notice", no_NO="Open Source Software Notice", pl_PL="Open Source Software Notice", pt_PT="Open Source Software Notice", ro_RO="Open Source Software Notice", ru_RU="Open Source Software Notice", sk_SK="Open Source Software Notice", sl_SI="Open Source Software Notice", sr_RS="Open Source Software Notice", sv_SE="Open Source Software Notice", tr_TR="Open Source Software Notice", uk_UA="Open Source Software Notice")
	obb.obb_settings_screen__title_line__title = TextObject(bs_BA="Postavke", cs_CZ="Nastavení", da_DK="Indstillinger", de_DE="Einstellungen", el_GR="Ρυθμίσεις", en_GB="Settings", es_ES="Ajustes", fi_FI="Asetukset", fr_FR="Réglages", hr_HR="Postavke", hu_HU="Beállítások", it_IT="Impostazioni", nl_NL="Instellingen", no_NO="Innstillinger", pl_PL="Ustawienia", pt_PT="Ajustes", ro_RO="Setări", ru_RU="Настройки", sk_SK="Nastavenia", sl_SI="Nastavitve", sr_RS="Podešavanja", sv_SE="Inställningar", tr_TR="Ayarlar", uk_UA="Настройки")
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.VTM import OnlineBordbook as obb
else:
	from enna_hcp_configuration.texts.CLU46.center.VTM import OnlineBordbook as obb

# obb does not seem to use texttool completely
BACK_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][contains(@content-desc, 'Back')]")
CHAPTERS_ADAPTIVE_CRUISE_ASSIST_BUTTON = XpathString("//*[@resource-id='chapter-QURBUFRJVkVSLUZBSFJBU1NJU1RFTlQ']")
CHAPTERS_ADAPTIVE_CRUISE_ASSIST_TITLE = XpathString("//*[@text='Adaptiver Fahrassistent' or @text='Adaptive cruise assist'][contains(@resource-id, 'com.valtech_mobility.obb.audi:id/titleTextView')]") #_todo
CHAPTERS_COMBINED_ASSIST_FUNCTIONS_BUTTON = XpathString("//*[@resource-id='chapter-SEtBUC1LT01CSU5JRVJURUFTU0lTVEVOWkZVTktUSU9ORU4']")
CHAPTERS_COMBINED_ASSIST_FUNCTIONS_TITLE = XpathString("//*[@text='Kombinierte Assistenzfunktionen' or @text='Combined assist functions'][contains(@resource-id, 'com.valtech_mobility.obb.audi:id/titleTextView')]") #_todo
CHAPTERS_DISPLAYS_AND_CONTROLS_BUTTON = XpathString("//*[@resource-id='chapter-SUJBM19wZS1ldVZzTFpITmhTYjlvR3FzQnNWM2JR']")
CHAPTERS_DISPLAYS_AND_CONTROLS_TITLE = XpathString("//*[@text='Anzeige und Bedienung' or @text='Displays and controls'][contains(@resource-id, 'com.valtech_mobility.obb.audi:id/titleTextView')]") #_todo
CHAPTERS_DRIVER_ASSIST_SYSTEMS_BUTTON = XpathString("//*[@resource-id='chapter-SUJBM19wZS1EMGRGdDVhYVpiXzB3Y2Y3OUhkOEpR']")
CHAPTERS_DRIVER_ASSIST_SYSTEMS_TITLE = XpathString("//*[@text='Assistenzsysteme' or @text='Driver assist systems'][contains(@resource-id, 'com.valtech_mobility.obb.audi:id/titleTextView')]") #_todo
CHAPTERS_FRONT_SEATS_BUTTON = XpathString("//*[@resource-id='chapter-U0lUWkU']")
CHAPTERS_FRONT_SEATS_TITLE = XpathString("//*[@text='Vordersitze' or @text='Front seats'][contains(@resource-id, 'com.valtech_mobility.obb.audi:id/titleTextView')]") #_todo
CHAPTERS_INSTRUMENT_CLUSTER_BUTTON = XpathString("//*[@resource-id='chapter-S09NQklJTlNUUlVNRU5U']")
CHAPTERS_INSTRUMENT_CLUSTER_TITLE = XpathString("//*[@text='Kombiinstrument' or @text='Instrument cluster'][contains(@resource-id, 'com.valtech_mobility.obb.audi:id/titleTextView')]") #_todo
CHAPTERS_OVERVIEW_AND_CONTROLS_BUTTON = XpathString("//*[@resource-id='chapter-S09NQklJTlNUUlVNRU5ULVVFQkVSU0lDSFQtVU5ELUFOWkVJR0VO']")
CHAPTERS_OVERVIEW_AND_CONTROLS_TITLE = XpathString("//*[@text='Übersicht und Bedienung' or @text='Overview and controls'][contains(@resource-id, 'com.valtech_mobility.obb.audi:id/titleTextView')]") #_todo
CHAPTERS_QUICK_REFERENCE_BUTTON = XpathString("//*[@resource-id='chapter-SUJBM19wZS0zTDNMYXlETXc5MFEwTC0zMGxSRWxR']")
CHAPTERS_QUICK_REFERENCE_TITLE = XpathString("//*[@text='Kurz und bündig' or @text='Quick reference'][contains(@resource-id, 'com.valtech_mobility.obb.audi:id/titleTextView')]") #_todo
CHAPTERS_SETTING_OFF_BUTTON = XpathString("//*[@resource-id='chapter-SUJBM19wZS1xNWdRc0xPOWhSNVlDcTRJN1pSei13']")
CHAPTERS_SETTING_OFF_TITLE = XpathString("//*[@text='Start und Fahrt' or @text='Setting off'][contains(@resource-id, 'com.valtech_mobility.obb.audi:id/titleTextView')]") #_todo
CHAPTERS_SITTING_CORRECTLY_AND_SAFELY_BUTTON = XpathString("//*[@resource-id='chapter-U0lDSEVSLVNJVFpFTg']")
CHAPTERS_SITTING_CORRECTLY_AND_SAFELY_TITLE = XpathString("//*[@text='Richtig und sicher sitzen' or @text='Sitting correctly and safely'][contains(@resource-id, 'com.valtech_mobility.obb.audi:id/titleTextView')]") #_todo
CHAPTERS_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.obb.audi:id/titleArea']/.//*[@text='Kapitel' or @text='Chapters']") #_todo
CONNECTIVITY_ERROR_TEXT_TITLE = XpathString(f"//*{obb.obb_error_screen__no_internet_connection__text}")
FAQ_BEFORE_SET_OFF_TITLE = XpathString("//*[@text='FAQ' or @text='FAQs'][contains(@resource-id, 'com.valtech_mobility.obb.audi:id/titleTextView')] and //*[@text='Wie stelle ich den Sitz ein?' or @text='How do I adjust the seats?']") #_todo
FAQ_FRONT_SEATS_TITLE = XpathString("//*[@text='Vordersitze' or @text='Front seats'][contains(@resource-id, 'com.valtech_mobility.obb.audi:id/titleTextView')]") #_todo
FAQ_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.obb.audi:id/titleArea']/.//*[@text='FAQ' or @text='FAQs']") #_todo
FAQ_SEARCH_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.obb.audi:id/tabLayoutTitleLineContainer']/./*[@class='android.view.ViewGroup']/./*[@class='android.widget.LinearLayout'][@index='0']/./*[@index='2']")
FUNCTION_BLOCKED_TITLE = XpathString(f"//*{obb.obb_driving_screen__main_content__text}")

HOME_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][contains(@content-desc, 'Home')]")
#_todo: Are further letters needed for different languages?
INDEX_SEARCH_LETTER_A = XpathString("//*[@class='android.widget.TextView'][@text='A']")
INDEX_SEARCH_LETTER_B = XpathString("//*[@class='android.widget.TextView'][@text='B']")
INDEX_SEARCH_LETTER_C = XpathString("//*[@class='android.widget.TextView'][@text='C']")
INDEX_SEARCH_LETTER_D = XpathString("//*[@class='android.widget.TextView'][@text='D']")
INDEX_SEARCH_LETTER_E = XpathString("//*[@class='android.widget.TextView'][@text='E']")
INDEX_SEARCH_LETTER_F = XpathString("//*[@class='android.widget.TextView'][@text='F']")
INDEX_SEARCH_LETTER_G = XpathString("//*[@class='android.widget.TextView'][@text='G']")
INDEX_SEARCH_LETTER_H = XpathString("//*[@class='android.widget.TextView'][@text='H']")
INDEX_SEARCH_LETTER_I = XpathString("//*[@class='android.widget.TextView'][@text='I']")
INDEX_SEARCH_LETTER_J = XpathString("//*[@class='android.widget.TextView'][@text='J']")
INDEX_SEARCH_LETTER_K = XpathString("//*[@class='android.widget.TextView'][@text='K']")
INDEX_SEARCH_LETTER_L = XpathString("//*[@class='android.widget.TextView'][@text='L']")
INDEX_SEARCH_LETTER_M = XpathString("//*[@class='android.widget.TextView'][@text='M']")
INDEX_SEARCH_LETTER_N = XpathString("//*[@class='android.widget.TextView'][@text='N']")
INDEX_SEARCH_LETTER_O = XpathString("//*[@class='android.widget.TextView'][@text='O']")
INDEX_SEARCH_LETTER_P = XpathString("//*[@class='android.widget.TextView'][@text='P']")
INDEX_SEARCH_LETTER_Q = XpathString("//*[@class='android.widget.TextView'][@text='Q']")
INDEX_SEARCH_LETTER_R = XpathString("//*[@class='android.widget.TextView'][@text='R']")
INDEX_SEARCH_LETTER_S = XpathString("//*[@class='android.widget.TextView'][@text='S']")
INDEX_SEARCH_LETTER_T = XpathString("//*[@class='android.widget.TextView'][@text='T']")
INDEX_SEARCH_LETTER_U = XpathString("//*[@class='android.widget.TextView'][@text='U']")
INDEX_SEARCH_LETTER_V = XpathString("//*[@class='android.widget.TextView'][@text='V']")
INDEX_SEARCH_LETTER_W = XpathString("//*[@class='android.widget.TextView'][@text='W']")
INDEX_SEARCH_LETTER_X = XpathString("//*[@class='android.widget.TextView'][@text='X']")
INDEX_SEARCH_LETTER_Y = XpathString("//*[@class='android.widget.TextView'][@text='Y']")
INDEX_SEARCH_LETTER_Z = XpathString("//*[@class='android.widget.TextView'][@text='Z']")
INDEX_SEARCH_TEXT_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.obb.audi:id/titleArea']/.//*[contains(@text, 'Stichwort') or contains(@text, 'Index')]") #_todo
INFO_TITLE = XpathString("//*[@text='Info'][contains(@resource-id, 'com.valtech_mobility.obb.audi:id/titleTextView')]") #_todo
INIT_REQUEST_TITLE = XpathString("//*[@content-desc='https://qa.retailservices.audi.de/ccsabo/app/v1/abo2-car-hcp3/']")
INIT_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.obb.audi:id/init_loading_screen']")

WARNING_BUTTON = XpathString("//*[@resource-id='cGUtYUo0SC1Vd0toMzBQUkx3bXN0TjUwdw']")
CAUTION_ICON = XpathString("//*[@content-desc='CAUTION' or @content-desc='VORSICHT']")
RELATED_TOPICS_ICON = XpathString("//*[@content-desc='Related topics' or @content-desc='Verwandte Themen']")
MOBILE_VERSION_ICON = XpathString("//*[@content-desc='Mobile version' or @content-desc='Mobile Version']")

MAIN_TITLE = XpathString("//*[@class='android.widget.TextView'][contains(@resource-id, 'dashboard-')]/../../../*[@index='2']")
MAIN_LIST_CONTAINER = XpathString(clu46="//*[@scrollable='true'][@class='android.view.View']//*[contains(@resource-id, 'dashboard-')]/../../..",
								  clu55="//*[@scrollable='true'][@class='android.view.View']//*[contains(@resource-id, 'dashboard-')]/../../../..")
MAIN_CHAPTERS_BUTTON = XpathString("//*[@class='android.widget.ListView']/.//*[@resource-id='dashboard-CHAPTERS']")
MAIN_SUPPLEMENTS_BUTTON = XpathString("//*[@class='android.widget.ListView']/.//*[@resource-id='dashboard-SUPPLEMENTS']")
MAIN_FAQ_BUTTON = XpathString("//*[@class='android.widget.ListView']/.//*[@resource-id='dashboard-FAQ']")
MAIN_WARNING_LAMPS_BUTTON = XpathString("//*[@class='android.widget.ListView']/.//*[@resource-id='dashboard-LAMPS']")
MAIN_INDEX_BUTTON = XpathString("//*[@class='android.widget.ListView']/.//*[@resource-id='dashboard-INDEX']")
MAIN_INDEX_BUTTON = XpathString("//*[@class='android.widget.ListView']/.//*[@resource-id='dashboard-INDEX']")
MAIN_INFO_BUTTON = XpathString("//*[@class='android.widget.ListView']/.//*[@resource-id='dashboard-INFO']")
NIX = XpathString("//*[@text='nur als platzhalter fuer obb nix']") #_todo

PRIVACY_MODE_BUTTON = XpathString(f"//*{obb.obb_error_privacy_active_screen__confirm_button__label}")
PRIVACY_MODE_TITLE = XpathString("//*[contains(@content-desc, 'OperationPanelItem-Datenschutzeinstellungen') or contains(@content-desc, 'OperationPanelItem-Privacy settings')]")
SEARCH_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.obb.audi:id/tabLayoutTitleLineContainer']/./*[@class='android.view.ViewGroup']/./*[@class='android.widget.LinearLayout'][@index='0']")
SETTINGS_SEARCH_BUTTON  = XpathString("//*[@resource-id='com.valtech_mobility.obb.audi:id/tabLayoutTitleLineContainer']/./*[@class='android.view.ViewGroup']/./*[@class='android.widget.LinearLayout'][@index='0']//*[@index='2']")
INDEX_SEARCH_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.obb.audi:id/tabLayoutTitleLineContainer']/./*[@class='android.view.ViewGroup']/./*[@class='android.widget.LinearLayout'][@index='0']//*[@index='2']")
OSSN_SEARCH_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.obb.audi:id/tabLayoutTitleLineContainer']/./*[@class='android.view.ViewGroup']/./*[@class='android.widget.LinearLayout'][@index='0']//*[@index='2']")
SEARCH_EDIT_TEXT_BOX_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.obb.audi:id/editText']")
SEARCH_RESULT = XpathString("//*[contains(@text, 'No search results for:') or contains(@text, 'Search results for:') or contains(@text, 'Suchergebnisse für:') or contains(@text, 'Kein Suchergebnis für:')]") #_todo
SEARCH_WEBCONTENT_TITLE = XpathString("//*[@class-id='android.webkit.WebView'] or //*[@resource-id='com.valtech_mobility.obb.audi:id/web_content']")
SETTINGS_BUTTON = XpathString("//*[@resource-id='com.valtech_mobility.obb.audi:id/menuActionContainer']/..//*[@class='android.widget.ImageButton']")###Einstellungen für Online-Bordbuch' or @content-desc='Settings for Online manuals###Settings for Online manuals']")

SETTINGS_CHANGE_LANGUAGE_BUTTON = XpathString("//*[@class='android.widget.ListView']/.//*[@class='android.widget.Image'][@package='com.valtech_mobility.obb.audi']")
SETTINGS_CHANGE_LANGUAGE_TITLE = XpathString("//*[@class='android.widget.ListView']/.//*[contains(@resource-id, 'language-')]")
SETTINGS_ABOUT_US_BUTTON = XpathString(f"//*[@class='android.widget.ListView']/.//*[@class='android.widget.TextView']{str(obb.obb_settings_screen__imprint__text).replace("About us", "Imprint")}")  # ToDo TextTool
SETTINGS_DATA_PROTECTION_NOTES_BUTTON = XpathString(f"//*[@class='android.widget.ListView']/.//*[@class='android.widget.TextView']{str(obb.obb_settings_screen__data_protection_information__text).replace("Datenschutzhinweise", "Datenschutzhinweis").replace("Data protection notes", "Privacy policy")}")  # ToDo TextTool
SETTINGS_OSSN_BUTTON = XpathString(f"//*[@class='android.widget.ListView']/.//*[@class='android.widget.TextView']{str(obb.obb_settings_screen__open_source_license__title)}")

SETTINGS_TITLE = XpathString(f"//*[@class='android.view.View']/.//*[@class='android.view.View']/.//*[@class='android.widget.TextView']{obb.obb_settings_screen__title_line__title}")
SETTINGS_OSSN_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.obb.audi:id/titleArea']/.//*[@text='Rechtliches' or @text='Legal information']") #_todo

SUPPLEMENTS_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.obb.audi:id/titleArea']/.//*[@text='Nachträge' or @text='Supplements']") #_todo
WARNING_LAMPS_TITLE = XpathString("//*[@resource-id='com.valtech_mobility.obb.audi:id/titleArea']/.//*[@text='Kontrollleuchten' or @text='Warning lamps']") #_todo

LIST_CONTAINER = XpathString("//*[@scrollable='true'][@class='android.view.View'][@package='com.valtech_mobility.obb.audi']")

ADAPTIVE_CRUISE_ASSIST_ICON = XpathString("//*[@index='180']")
ADAPTIVE_CRUISE_ASSIST_TITLE = XpathString("//*[@text='Geschwindigkeitsassistenzsysteme' or @text='Speed assist systems'][contains(@resource-id, 'com.valtech_mobility.obb.audi:id/titleTextViewRef')]")

NAVIGATION_BAR_FAVORITE = XpathString("//*[contains(@content-desc, 'com.valtech_mobility.obb.audi/com.valtech_mobility.obb.MainActivity')][contains(@resource-id,'com.android.systemui:id/navigation_bar_favorite_button')]")
