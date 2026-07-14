# -*- coding: utf-8 -*-
"""Created on 23.01.2024.

@project: enna_kwd_testing.
@author: SPLATZP: Platzer Pascal.

Contains stimulations for keyword driven testing in context of android_hmi aem functions.
"""

import logging

import enna.core.component_system.decorators
import enna.core.reporting.interface
import enna.data_interfaces.adb.interface
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.utilities.menu_navigation.interface
from enna_hcp_configuration.android.contexts import assistant

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.helper.android_hmi_helper
import enna_kwd_testing.utilities.speller

from enna_kwd_testing.utilities.helper import wrapper_android_hmi

MODULE_LOGGER = logging.getLogger(__name__)


# pylint: disable=too-many-branches

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation",  instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetAemGdaDevloperSettingsCdfwExternalUserConfigs(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class containing functionality to set external user configs in aem gda."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface,
				 menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.2")
		self._reporting = reporting
		self.__android_hmi = android_hmi
		self.__menu_navigation = menu_navigation
		self._xpaths = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="aem")
		self.allowed_parameter_keys = ["VALUE"]

	def _action(self) -> bool:
		"""Execute action.

		set switch in aem.cdfw_and_speech.

		1. Navigate to 'aem.CDFW_AND_SPEECH' screen
		2. Scroll to 'read external user configs' in list on screen
		3. Set switch to read external user configs State "ON" or "OFF"

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""

		try:
			str__toggle_button_state = self.values["STATE"]
			bool_toggle_button_state = str__toggle_button_state == "ON"
		except KeyError as exception:
			MODULE_LOGGER.error(f"{exception}: Wrong parameter for STATE:'{str__toggle_button_state}', should be 'ON' or 'OFF")
			return False

		str__cdfw_and_speech_list_xpath = self._xpaths.get_xpath("cdfw_and_speech", "scroll_view")
		str__switch_xpath = self._xpaths.get_xpath("cdfw_and_speech", "toggle_read_external_user_configs")

		if not wrapper_android_hmi.go_to_screen(assistant.AEM_GDA_CDFW_AND_SPEECH, self._reporting, self.__menu_navigation):
			self._reporting.add_report_message_ta_error("Could not go to screen: 'AEM.CDFW_AND_SPEECH. Something went wrong while navigating to screen.")
			return False

		if not wrapper_android_hmi.wait_and_scroll_in_list(str__switch_xpath, str__cdfw_and_speech_list_xpath, self.__android_hmi):
			self._reporting.add_report_message_ta_error(f"Could not scroll to element: {str__switch_xpath} in list {str__cdfw_and_speech_list_xpath}.")
			return False

		error_massage = f"Could not get toggle button state for '{str__switch_xpath}' button. An error occurred."

		if not wrapper_android_hmi.wait_and_set_toggle_button_state(str__switch_xpath, bool_toggle_button_state, self.__android_hmi, self._reporting):
			self._reporting.add_report_message_system_error(error_massage)
			return False

		MODULE_LOGGER.info(f"The read external user config is set to '{str__toggle_button_state}' ")

		return True
