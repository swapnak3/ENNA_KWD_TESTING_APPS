"""Created on 14.12.2023.
   Repaired on 26.10.2024.

@project: enna_kwd_testing.
@author: T6B0NVV: Frank Isselhard.
@author: WD43WDV: TEC: Teubner Claus.

Contains stimulations for keyword driven testing in context of android_hmi settings functions.
"""

import logging
import time

import enna.core.component_system.decorators
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import obb

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.xpath_collection.helper
from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


@enna.core.component_system.decorators.RequireComponent('enna.core.reporting')
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetObbLanguage(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set the language in obb settings.

		parameter LANG: String defining the language eg 'de_DE', 'en_GB'"""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version='1.0.3')
		self.__reporting = reporting
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="obb")
		self.allowed_parameter_keys = ['LANG']
		self.allowed_parameter_values = ['bg_bg', 'cs_cz', 'bs_me', 'da_dk', 'de_de', 'et_ee', 'el_gr', 'en_gb', 'en_uk', 'es_es', 'en_ir', 'fr_fr', 'it_it', 'ar_sa']

	def _action(self) -> bool:
		"""Execute action.

		Set language for obb

		1. Navigate to 'OBB ->  settings' screen
		1.1 Navigate to 'OBB ->  settings_change_language' screen
		2. Click on the 'Change language' section of the settings
		3. Scroll to the language button corresponding to the 'LANG' parameter
		4. Activate the button 

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""
		enna_kwd_testing.utilities.helper.android_hmi_helper.wait_till_screen_id_is_not_empty(self._reporting, self.__android_hmi, timeout=30)

		str_language = str(self.values.get('LANG', "en_GB")).lower()
		if str_language in self.allowed_parameter_values:
			MODULE_LOGGER.info(f"Parameter for LANG: '{str_language}'")
		else:
			MODULE_LOGGER.error(f"Wrong parameter for LANG: '{str_language}', should be a valid language")
			return False

		if not wrapper_android_hmi.go_to_screen(obb.SETTINGS, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'OBB -> SETTINGS. Something went wrong while navigating to screen.")
			return False

		if not wrapper_android_hmi.go_to_screen(obb.SETTINGS_CHANGE_LANGUAGE, self._reporting, self.__menu_navigation):
			MODULE_LOGGER.error("Could not go to screen: 'OBB -> SETTINGS_CHANGE_LANGUAGE. Something went wrong while navigating to screen.")
			return False

		time.sleep(1.5)
		str_button_xpath = self.__xpathloader.get_xpath(screen='settings_change_language', element=str_language)
		str_xpath_language_container = self.__xpathloader.get_xpath(screen='settings_change_language', element='main_list')
		if not wrapper_android_hmi.wait_and_scroll_in_list(xpath_element=str_button_xpath, xpath_container=str_xpath_language_container, android=self.__android_hmi, additional_message=f"click on: {str_button_xpath}."):
			MODULE_LOGGER.error((f"Could not scroll to: {str_button_xpath} in {str_xpath_language_container}. Something went wrong."))
			return False
		time.sleep(0.1)
		if not wrapper_android_hmi.wait_and_click_in_list(xpath_element=str_button_xpath, xpath_container=str_xpath_language_container, android=self.__android_hmi, reporting=self.__reporting):
			MODULE_LOGGER.error((f"Could not click on: {str_button_xpath}. Something went wrong."))
			return False

		MODULE_LOGGER.info((f"Click on: {str_button_xpath} to set the language was i.O."))
		return True
