# -*- coding: utf-8 -*-
"""Created on Wed Mar 17 13:03:33 2021 --Update for KWD 31.10.23

@author: AS7LMY5
@author: WD43WDV
@author: SPLATZP
"""
import os
import pathlib

import enna.core.exceptions
import pandas

from enna_kwd_testing import ROOT_PATH

# pylint: disable=too-many-locals, too-many-branches

def get_text_from_texttool_csv(text_id_s: str = "com.android.car.blocking_disclaimer_text", language_s: str = "de_DE", display_s: str = "panorama", str_filename: str = "Panorama") -> str | bool:
	""" search for 'text_id_s' in GUI_FILENAME_s
		:param str_filename: (str) Name of the texttool file
		:param text_id_s: (str) search for this id in csv file (e.g. "com.android.car.blocking_disclaimer_text")
		:param language_s: (str) select output language, default is "de_DE"
		:param display_s: (str) select between "panorama" or "pid" display, default is "panorama"
		:return:
			- str__text_display (str): Text from csv
			- False (bool): when an error occurs
		:rtype: str | bool
	"""

	language_dict = {"bs_BA": "Bosnisch\\nText",
					 "cs_CZ": "Tschechisch\\nText",
					 "da_DK": "Daenisch\\nText",
					 "de_DE": "Deutsch\\nText",
					 "el_GR": "Griechisch\\nText",
					 "en_GB": "Englisch (Britisch)\\nText",
					 "es_ES": "Spanisch (Traditionell)\\nText",
					 "fi_FI": "Finnisch\\nText",
					 "fr_FR": "Franzoesisch\\nText",
					 "hr_HR": "Kroatisch\\nText",
					 "hu_HU": "Ungarisch\\nText",
					 "it_IT": "Italienisch\\nText",
					 "nl_NL": "Niederlaendisch\\nText",
					 "no_NO": "Norwegisch (Bokmal)\\nText",
					 "pl_PL": "Polnisch\\nText",
					 "pt_PT": "Portugiesisch\\nText",
					 "ro_RO": "Rumaenisch\\nText",
					 "ru_RU": "Russisch\\nText",
					 "sk_SK": "Slowakisch\\nText",
					 "sl_SI": "Slowenisch\\nText",
					 "sr_RS": "Serbisch\\nText",
					 "sv_SE": "Schwedisch\\nText",
					 "tr_TR": "Tuerkisch\\nText",
					 "uk_UA": "Ukrainisch\\nText",
					 "en_US": "Englisch(USA)\\nText",
					 "fr_CA": "Franzoesisch(Kanada)\\nText",
					 "es_MX": "Spanisch (Mexiko)\\nText",
					 "pt_BR": "Portugiesisch (brasilien)\\nText",
					 "en_MY": "Malaysisch\\nText",
					 "ar_EH": "Arabisch (Saudi-Arabien)\\nText",
					 "cn_CN": "Chinesisch\\nText",
					 "ja_JP": "Japanisch\\nText",
					 "ko_KR": "Koreanisch\\nText",
					 "zh_TW": "Taiwanesisch\\nText",
					 "ka_00": "Kantonesisch\\nText",
					 "en_CN": "Englisch (Chinesisch) (Master = Englisch (USA))\\nText",
					 "en_JP": "Englisch (japanisch) (Master = Englisch (USA))\\nText",
					 "en_KR": "Englisch (Koreanisch) (Master = Englisch (USA))\\nText",
					 "en_TW": "Englisch (Taiwanesisch) (Master = Englisch (USA))\\nText"
					 }

	print("cluster: ", enna.core.config.INFOTAINMENT_SYSTEM.cluster)
	str__path_to_textool_folder = f"{ROOT_PATH}/enna_kwd_testing/resources/texttool/till_cluster43" if enna.core.config.INFOTAINMENT_SYSTEM.cluster < 44 else f"{ROOT_PATH}/enna_kwd_testing/resources/texttool/higher_cluster45"

	str__path_filename = ""
	for file in os.listdir(str__path_to_textool_folder):
		if file.endswith(".csv") and str_filename in file:
			str__path_filename = os.path.join(str__path_to_textool_folder, file)

	pandas_data_frame = pandas.DataFrame()
	text_tool_data_frame = None

	try:
		pandas.read_csv(str__path_filename, sep="\t", encoding="utf_16_le", low_memory=False, chunksize=100000)
	except (FileNotFoundError, UnicodeError, enna.core.exceptions.ENNAException) as e:
		print("ERROR: ", e)
		return False

	for chunk in pandas.read_csv(str__path_filename, sep="\t", encoding="utf_16_le", low_memory=False, chunksize=100000):
		text_tool_data_frame = pandas.concat([pandas_data_frame, chunk], ignore_index=True)

	if text_tool_data_frame.columns.values.tolist()[2] == "Eigenschaft" or text_tool_data_frame.columns.values.tolist()[2] == "Property name":
		header_property_s = list(text_tool_data_frame)[2]
	elif "Eigenschaft" in text_tool_data_frame.columns.values.tolist():
		header_property_s = "Eigenschaft"
	elif "Property name" in text_tool_data_frame.columns.values.tolist():
		header_property_s = "Property name"
	else:
		return False

	str__text_display = ""
	text = text_tool_data_frame[text_tool_data_frame[header_property_s] == text_id_s]
	try:
		if display_s == "panorama":
			str__text_display = text.iloc[0][language_dict[language_s]]
		elif display_s == "pid":
			if text.iloc[0][language_dict[language_s]] == "[nan]":
				str__text_display = text.iloc[0][language_dict[language_s]]
			else:
				str__text_display = text.iloc[1][language_dict[language_s]]
		return str__text_display
	except IndexError as ex:
		print(ex)
		return False


def get_text_from_texttool_sds_csv(text_id: str, language_s: str = "de_DE", str_filename: str = "20240212_HCP3_SDS_v77203.csv") -> str | bool:
	""" search for 'text_id_s' in GUI_FILENAME_s
		:param str_filename: (str) Name of the texttool file
		:param text_id: (str) search for this id in csv file (e.g. "AssistantPrompts.ReportOnTask_ActivateScreenReader.PROMPT-CONVERSATIONAL-0000")
		:param language_s: (str) select output language, default is "de_DE"
		:return:
			- str__output_text_from_csv (str): Text from csv
			- False (bool): when an error occurs
		:rtype: str | bool
	"""

	language_dict = {"bs_BA": "Bosnisch\\nText",
					 "cs_CZ": "Tschechisch\\nText",
					 "da_DK": "Daenisch\\nText",
					 "de_DE": "Deutsch\\nText",
					 "el_GR": "Griechisch\\nText",
					 "en_GB": "Englisch (Britisch)\\nText",
					 "es_ES": "Spanisch (Traditionell)\\nText",
					 "fi_FI": "Finnisch\\nText",
					 "fr_FR": "Franzoesisch\\nText",
					 "hr_HR": "Kroatisch\\nText",
					 "hu_HU": "Ungarisch\\nText",
					 "it_IT": "Italienisch\\nText",
					 "nl_NL": "Niederlaendisch\\nText",
					 "no_NO": "Norwegisch (Bokmal)\\nText",
					 "pl_PL": "Polnisch\\nText",
					 "pt_PT": "Portugiesisch\\nText",
					 "ro_RO": "Rumaenisch\\nText",
					 "ru_RU": "Russisch\\nText",
					 "sk_SK": "Slowakisch\\nText",
					 "sl_SI": "Slowenisch\\nText",
					 "sr_RS": "Serbisch\\nText",
					 "sv_SE": "Schwedisch\\nText",
					 "tr_TR": "Tuerkisch\\nText",
					 "uk_UA": "Ukrainisch\\nText",
					 "en_US": "Englisch(USA)\\nText",
					 "fr_CA": "Franzoesisch(Kanada)\\nText",
					 "es_MX": "Spanisch (Mexiko)\\nText",
					 "pt_BR": "Portugiesisch (brasilien)\\nText",
					 "en_MY": "Malaysisch\\nText",
					 "ar_EH": "Arabisch (Saudi-Arabien)\\nText",
					 "cn_CN": "Chinesisch\\nText",
					 "ja_JP": "Japanisch\\nText",
					 "ko_KR": "Koreanisch\\nText",
					 "zh_TW": "Taiwanesisch\\nText",
					 "ka_00": "Kantonesisch\\nText",
					 "en_CN": "Englisch (Chinesisch) (Master = Englisch (USA))\\nText",
					 "en_JP": "Englisch (japanisch) (Master = Englisch (USA))\\nText",
					 "en_KR": "Englisch (Koreanisch) (Master = Englisch (USA))\\nText",
					 "en_TW": "Englisch (Taiwanesisch) (Master = Englisch (USA))\\nText"
					 }

	path_filename_sds = pathlib.Path(__file__).resolve().parent.parent.parent.joinpath("resources", "texttool_sds", "till_cluster43", str_filename) \
		if enna.core.config.INFOTAINMENT_SYSTEM.cluster < 44 \
		else pathlib.Path(__file__).resolve().parent.parent.parent.joinpath("resources", "texttool_sds", "higher_cluster45", str_filename)

	pandas_data_frame = pandas.DataFrame()
	text_tool_data_frame = None

	try:
		pandas.read_csv(path_filename_sds, sep="\t", encoding="utf_16_le", low_memory=False, chunksize=100000)
	except (FileNotFoundError, UnicodeError, enna.core.exceptions.ENNAException) as e:
		print("ERROR: ", e)
		return False

	for chunk in pandas.read_csv(path_filename_sds, sep="\t", encoding="utf_16_le", low_memory=False, chunksize=100000):
		text_tool_data_frame = pandas.concat([pandas_data_frame, chunk], ignore_index=True)

	if text_tool_data_frame.columns.values.tolist()[2] == "Eigenschaft" or text_tool_data_frame.columns.values.tolist()[2] == "Property name":
		header_property_s = list(text_tool_data_frame)[2]
	elif "Eigenschaft" in text_tool_data_frame.columns.values.tolist():
		header_property_s = "Eigenschaft"
	elif "Property name" in text_tool_data_frame.columns.values.tolist():
		header_property_s = "Property name"
	else:
		return False

	text = text_tool_data_frame[text_tool_data_frame[header_property_s] == text_id]
	str__output_text_from_csv = text.iloc[0][language_dict[language_s]]
	str__output_text_from_csv = "".join(ch for ch in str__output_text_from_csv if ch.isalnum() or ch.isspace()).lower().strip()
	return str__output_text_from_csv


def main():
	"""-- Text_id/Text_id List erstellen, mit dem die bezogenen Texte in CSV gesucht werden könnte. --"""

	text_id_list_sds = ["AssistantPrompts.ReportOnTask_ActivateVoiceAccess.PROMPT-CONVERSATIONAL-0000"]
	text_id_list_audi_apps = ["CARI.Interior Experience.int_ex_dialog_lifescore_button_cancel_mode"]
	text_id_list_pano = ["com.android.car.settings.aosp_settings_title_text___locktype_android_pin_info"]

	for text_id_s in text_id_list_audi_apps:
		print(f"text_id_s: {text_id_s}", " ---> audiApps")
		print(get_text_from_texttool_csv(text_id_s=text_id_s, language_s="de_DE", display_s="panorama", str_filename="AudiApps"))
		print(get_text_from_texttool_csv(text_id_s=text_id_s, language_s="es_ES", display_s="panorama", str_filename="AudiApps"))
		print("---------------------------")
	for text_id_s in text_id_list_pano:
		print(f"text_id_s: {text_id_s}", " ---> GUI Panorama")
		print(get_text_from_texttool_csv(text_id_s=text_id_s, language_s="de_DE", display_s="panorama"))
		print("---------------------------")

	for text_id_s in text_id_list_sds:
		print(f"text_id_sds: {text_id_s}", " ---> SDS")
		print(get_text_from_texttool_sds_csv(text_id=text_id_s, language_s="de_DE"))
		print("---------------------------")


if __name__ == "__main__":
	main()
