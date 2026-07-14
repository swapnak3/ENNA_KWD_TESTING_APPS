# -*- coding: utf-8 -*-
"""Created on 04.06.2024.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Claus Teubner.

Contains stimulations for KWD-TA in context of android_hmi settings system language functions.
"""

import logging

import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface

import enna_hcp_configuration.android.xpaths
from enna_hcp_configuration.android.contexts import settings

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.helper.android_hmi_helper
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckSystemLanguage(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check the system language in settings - languages and input.

		parameter LANG: String defining the language '"""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version='1.0.3')
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="settings")

		self._parameter_keys = ['LANG']
		self._parameter_values = {'bs_BA': 'Bosanski (Bosna i Hercegovina)',
		                          'hr_HR': 'Hrvatski (Hrvatska)',
		                          'cs_CZ': 'Čeština (Česko)',
		                          'da_DK': 'Dansk (Danmark)',
		                          'nl_NL': 'Nederlands (Nederland)',
		                          'en_GB': 'English (United Kingdom)',
		                          'fi_FI': 'Suomi (Suomi)',
		                          'fr_FR': 'Français (France)',
		                          'de_DE': 'Deutsch (Deutschland)',
		                          'el_GR': 'Ελληνικά (Ελλάδα)',
		                          'hu_HU': 'Magyar (Magyarország)',
		                          'it_IT': 'Italiano (Italia)',
		                          'nb_NO': 'Norsk (Norge)',
		                          'no_NO': 'Norsk (Norge)',
		                          'pl_PL': 'Polski (Polska)',
		                          'pt_PT': 'Português (Portugal)',
		                          'ro_RO': 'Română (România)',
		                          'ru_RU': 'Русский (Россия)',
		                          'sr_Latn_RS': 'Srpski (latinica, Srbija)',
		                          'sr_RS': 'Srpski (latinica, Srbija)',
		                          'sk_SK': 'Slovenčina (Slovensko)',
		                          'sl_SI': 'Slovenščina (Slovenija)',
		                          'es_ES': 'Español (España)',
		                          'sv_SE': 'Svenska (Sverige)',
		                          'tr_TR': 'Türkçe (Türkiye)',
		                          'uk_UA': 'Українська (Україна)'
		                          }

	def _action(self) -> bool:
		"""Execute action.

		Set language for settings - system - languages and input - languages

		1. Navigate to 'languages and input ->  settings.system_languagesinput_input' screen
		2. Check second line on the 'language' menu of the settings and compare with given 'LANG'

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		enna_kwd_testing.utilities.helper.android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)

		str_language = str(self.values['LANG'])
		if str_language in self._parameter_values:
			MODULE_LOGGER.info(f"Parameter for LANG:'{str_language}'")
		else:
			MODULE_LOGGER.error(f"Wrong parameter for LANG:'{str_language}', should be a valid language from this list:\n{self._parameter_values.keys()}")
			return False

		if not wrapper_android_hmi.go_to_screen(settings.SYSTEM_LANGUAGESINPUT_INPUT, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'settings -> SYSTEM_LANGUAGESINPUT_INPUT. Something went wrong while navigating to screen.")
			return False

		# Get the language from xpaths and assume that the first element is the language settings entry
		language_text = self.__xpathloader.get_xpath(screen='system_languagesinput_input', element='summary_language')

		str_language_hmi = self.__android_hmi.layout.value.xpath(language_text)[0].attrib["text"]

		if self._parameter_values[str_language] == str_language_hmi:
			MODULE_LOGGER.info(f"language from HMI is: '{str_language}', '{self._parameter_values[str_language]}'")
			enna_hcp_configuration.android.xpaths.LANG = str_language
		else:
			MODULE_LOGGER.error(f"Expected LANG: '{str_language}' '{self._parameter_values[str_language]}' is not identical to selectet HMI language: '{str_language_hmi}'.")
			return False
		return True
