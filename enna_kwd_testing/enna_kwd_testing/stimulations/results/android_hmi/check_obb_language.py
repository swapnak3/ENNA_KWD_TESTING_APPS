"""Created on 29.02.2024.
   Repaired on 15.10.2024

@project: enna_kwd_testing.
@author: T6B0NVV: Frank Isselhard.
@author: WD43WDV: TEC: Teubner Claus.

Contains stimulations for keyword driven testing in context of android_hmi obb functions.
"""

import logging

import enna.core.component_system.decorators
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import obb

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckObbLanguage(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to check the language in obb settings.

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
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="obb")

		self.allowed_parameter_keys = ['LANG']
		self.allowed_parameter_values = ['bs_ba', 'cs_cz', 'da_dk', 'de_de', 'el_gr', 'en_gb', 'en_uk', 'es_es', 'fi_fi', 'fr_fr', 'hr_hr', 'hu_hu',
		                                 'it_it', 'nl_nl', 'no_no', 'pl_pl', 'pt_pt', 'ro_ro', 'ru_ru', 'sk_sk', 'sl_si', 'sr_rs', 'sv_se', 'tr_tr', 'uk_ua', 'ar_sa']

	def _action(self) -> bool:
		"""Execute action.

		Check language for obb

		0. Navigate to 'OBB ->  main' screen, because setting headline is only renewed when screen is changed.
		1. Navigate to 'OBB ->  settings' screen.
		2. Get text from first line 'Sprache ändern'
		3. Compare shown text with checked language.
		4. Get state to return.

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		enna_kwd_testing.utilities.helper.android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)

		str_language = str(self.values.get('LANG', "en_GB")).lower()
		if str_language in self.allowed_parameter_values:
			MODULE_LOGGER.info(f"Parameter for LANG: '{str_language}'")
		else:
			MODULE_LOGGER.error(f"Wrong parameter for LANG: '{str_language}', should be a valid language, eg: {self.allowed_parameter_values}.")
			return False

		if not wrapper_android_hmi.go_to_screen(obb.SETTINGS, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'OBB -> SETTINGS. Something went wrong while navigating to screen.")
			return False

		str_xpath_text_is_change_language = self.__xpathloader.get_xpath(screen="settings", element="change_language")
		str_text_is_change_language = self.__android_hmi.layout.value.xpath(str_xpath_text_is_change_language)[0].attrib["text"]
		MODULE_LOGGER.info(f"language: '{str_text_is_change_language}' is set.")

		str_xpath_text_change_language = self.__xpathloader.get_xpath(screen="settings", element=str_language)

		if not wrapper_android_hmi.element_exists(str_xpath_text_change_language, self.__android_hmi):
			MODULE_LOGGER.error(f"Wrong LANG: '{str_language}', {str_xpath_text_change_language} is not set.")
			return False

		MODULE_LOGGER.info(f"Current language is set to '{str_language}'.")
		return True
