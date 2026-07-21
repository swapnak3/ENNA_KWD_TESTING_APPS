"""Created on 26.05.2025.

@project: enna_kwd_testing.
@author: WD43WDV: TEC: Teubner Claus.

Contains stimulations for keyword driven testing in context of obb.app functions.
"""
import enum
import logging
import time
import numpy

import enna.core.component_system.decorators
import enna.core.config
import enna.core.exceptions
import enna.core.reporting.interface
import enna.core.image_processing.helper
import enna_st12.data_interfaces.android_hmi.helper
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.instance_names
import enna_st12.utilities.menu_navigation.interface

import enna_hcp_configuration.android.xpaths.obb
from enna_hcp_configuration.android.contexts import obb

import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.stimulations.image_processing.click_on_image
import enna_kwd_testing.stimulations.image_processing.colors
import enna_kwd_testing.stimulations.apps._internal
import enna_kwd_testing.utilities.xpath_collection.helper

MODULE_LOGGER = logging.getLogger(__name__)

# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckObbLanguage(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Class containing functionality to check the language in obb settings.

		parameter LANG: String defining the language '"""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation.__init__(self, reporting=reporting, based_on_kwd_spec_version='1.0.3')
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, menu_navigation=menu_navigation, android_hmi=android_hmi)
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="obb")

		self.allowed_parameter_keys = ['LANG']
		self.allowed_parameter_values = ['bs_ba', 'cs_cz', 'da_dk', 'de_de', 'el_gr', 'en_gb', 'en_uk', 'es_es', 'fi_fi', 'fr_fr', 'hr_hr', 'hu_hu',
		                                 'it_it', 'nl_nl', 'no_no', 'pl_pl', 'pt_pt', 'ro_ro', 'ru_ru', 'sk_sk', 'sl_si', 'sr_rs', 'sv_se', 'tr_tr', 'uk_ua', 'ar_sa']
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")
		MODULE_LOGGER.debug(f"Allowed Parameter values: {self.allowed_parameter_values}")
		MODULE_LOGGER.info("Stimulation of menu navigation is initialized!")

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
		str_language = str(self.values.get('LANG', "en_GB")).lower()
		if str_language in self.allowed_parameter_values:
			MODULE_LOGGER.info(f"Parameter for LANG: '{str_language}'")
		else:
			MODULE_LOGGER.error(f"Wrong parameter for LANG: '{str_language}', should be a valid language, eg: {self.allowed_parameter_values}.")
			return False

		if not self._go_to_screen(obb.MAIN):
			MODULE_LOGGER.error("Could not go to screen: 'OBB -> MAIN. Something went wrong while navigating to screen.")
			return False
		if not self._go_to_screen(obb.SETTINGS):
			MODULE_LOGGER.error("Could not go to screen: 'OBB -> SETTINGS. Something went wrong while navigating to screen.")
			return False

		try:
			self._android_hmi.wait_for_event("screen_id", condition=lambda msg: self._android_hmi.screen_id.value == obb.SETTINGS.name, max_time=3.0)
		except enna.core.exceptions.TimeoutException:
			MODULE_LOGGER.error("Screen-ID is not: 'OBB -> SETTINGS. Something went wrong while navigating to screen.")
			self._reporting.add_report_message_ta_error("Screen-ID is not: 'OBB -> SETTINGS. Something went wrong while navigating to screen.")
			return False
		xpath_text_change_language: str = self.__xpathloader.get_xpath(screen="settings", element=str_language)
		try:
			self._android_hmi.wait_for_element_visible(xpath_text_change_language, max_time=10.0)
		except enna.core.exceptions.TimeoutException:
			MODULE_LOGGER.error(f"Wrong LANG: '{str_language}', {xpath_text_change_language} is not set.")
			self._reporting.add_report_message_ta_error(f"Wrong LANG: '{str_language}', {xpath_text_change_language} is not set.")
			return False
		MODULE_LOGGER.info(f"Current language is '{str_language}'.")
		return True


@enna.core.component_system.decorators.RequireComponent('enna.core.reporting')
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class SetObbLanguage(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Class containing functionality to set the language in obb settings.

		parameter LANG: String defining the language eg 'de_DE', 'en_GB'"""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation.__init__(self, reporting, based_on_kwd_spec_version='1.0.3')
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, menu_navigation=menu_navigation, android_hmi=android_hmi)
		self.__xpathloader = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(reporting=self._reporting, app="obb")
		self.allowed_parameter_keys = ['LANG']
		self.allowed_parameter_values = ['bg_bg', 'cs_cz', 'bs_me', 'da_dk', 'de_de', 'et_ee', 'el_gr', 'en_gb', 'en_uk', 'es_es', 'en_ir', 'fr_fr', 'it_it', 'ar_sa']
		self._language = {"de_de": "Deutsch", "en_gb": "English", "es_es": "Espanol", "fr_fr": "Francais", "it_it": "Italiano"}

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
		str_language = str(self.values.get('LANG', "en_GB")).lower()
		if str_language in self._language:
			MODULE_LOGGER.info(f"Parameter for LANG: '{str_language}'")
		else:
			MODULE_LOGGER.error(f"Wrong parameter for LANG: '{str_language}'! Valid languages {self._language.keys()}")
			return False

		if not self._go_to_screen(obb.SETTINGS_CHANGE_LANGUAGE):
			MODULE_LOGGER.error("Could not go to screen: 'OBB -> SETTINGS_CHANGE_LANGUAGE. Something went wrong while navigating to screen.")
			return False
		try:
			self._android_hmi.wait_for_event("screen_id", condition=lambda msg: self._android_hmi.screen_id.value == obb.SETTINGS_CHANGE_LANGUAGE.name, max_time=3.0)
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_ta_error("Screen not found: obb.SETTINGS_CHANGE_LANGUAGE. Something went wrong.")
			return False

		str_button_xpath = self.__xpathloader.get_xpath(screen='settings_change_language', element=str_language)
		# "main_list": "//*[@scrollable='true'][@class='android.view.View'][@package='com.valtech_mobility.obb.audi']",
		str_xpath_language_container = self.__xpathloader.get_xpath(screen='settings_change_language', element='main_list')
		# "main_list_text": "//*[contains(@text, 'Danish Dansk German Deutsch German Deutsch')]",
		str_xpath_main_list_text = self.__xpathloader.get_xpath(screen='settings_change_language', element='main_list_text')

		try:
			MODULE_LOGGER.debug("Try language set via UI-Automator.")
			self._android_hmi.wait_for_element_visible(xpath=str_xpath_language_container, max_time=10.0)
			self._android_hmi.click_element_in_list(xpath=str_button_xpath, list_container_xpath=str_xpath_language_container)
		except enna.core.exceptions.TimeoutException:
			MODULE_LOGGER.debug("Try language set via OCR.")
			if not self.__scroll_to_language(language=str_language, container=str_xpath_main_list_text) or not self.__click_on_language(language=str_language, container=str_xpath_main_list_text):
				return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_system_error(f"Could not set language'{str_language}' on Online Board Book! {error}")
			return False
		self._reporting.add_report_message_pass(f"Set language to '{str_language}' in Online Board Book")
		return True

	def __get_area_container(self, container: str) -> list[int] | None:
		"""Get area of list container:

		:param container: xpath of list container
		:return: list of coordinates from area [x1, y1, x2, y2,
		"""
		try:
			coordinate_size = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(layout=self._android_hmi.layout.value, xpath=container)
			rio = [coordinate_size["x"], coordinate_size["y"], coordinate_size["x"] + coordinate_size["width"], coordinate_size["y"] + coordinate_size["height"]]
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException:
			self._reporting.add_report_message_ta_error(f"List container '{container}' not found! Cold not investigate region of interest.")
			return None
		return rio


	def __scroll_to_language(self, language: str, container: str) -> bool:
		"""Scroll to language if show in current screen

		:param language: language to select
		:param container: xpath of list container
		:return: True if success, else false
		"""
		roi = self.__get_area_container(container)
		if isinstance(roi, list):
			try:
				self._android_hmi.scroll_list_to_top(list_container_xpath=container)
				time.sleep(1.0)
			except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
				MODULE_LOGGER.error(f"Could not swipe in list container! {error}")

			try:
				# pylint: disable=unused-variable
				for i in range(5):
					image_of_list = self._android_hmi.take_screenshot().get_roi(roi)
					text_of_list, _ = enna.core.image_processing.helper.get_text(image=image_of_list, language="deu" if language == "de_DE" else "eng")
					if self._language[language] in text_of_list:
						MODULE_LOGGER.debug(f"Language '{language}' found in screen")
						return True

					self._android_hmi.swipe_element(xpath=container, direction=enna_st12.data_interfaces.android_hmi.Direction.Down)
					time.sleep(1.0)
				self._reporting.add_report_message_system_error(f"Could not found language '{language}' via OCR!")
				return False

			except enna.core.exceptions.ImageProcessingException as error:
				self._reporting.add_report_message_ta_error(f"OCR error! {error}")
				return False
			except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
				self._reporting.add_report_message_ta_error(f"Could not swipe in list container! {error}")
				return False
		return False

	def __click_on_language(self, language: str, container: str) -> bool:
		"""Search position of language text via ocr and click on this position.

		:param language: language to select
		:param container: xpath of list container
		:return: True if success, else false
		"""
		text_height = 40
		step = 3

		roi = self.__get_area_container(container)
		if isinstance(roi, list):
			roi[3] = roi[1] + text_height
			try:
				current_screen = self._android_hmi.take_screenshot()
				while True:
					text, _ =enna.core.image_processing.helper.get_text(image=current_screen.get_roi(roi), language="deu" if language == "de_DE" else "eng")
					if text.strip() == self._language[language]:
						MODULE_LOGGER.debug(f"Position of language '{text}' is found!")
						self._android_hmi.click_coordinates(x_coord=int((roi[0] + roi[2])/2), y_coord=int((roi[1] + roi[3])/2))
						return True
					roi[1] += step
					roi[3] += step
			except (enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException, enna.core.exceptions.ImageProcessingException) as error:
				self._reporting.add_report_message_system_error(f"Could not click to language '{language}' on screen! {error}")
				return False
		return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireComponent("enna_st12.utilities.menu_navigation", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckColorOfWarningLampsInObb(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation, enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation):
	"""Class containing functionality to check color of warning lamps in obb."""

	class WarningLampColors(enum.Enum):
		"""Constants of colors. BGR Color"""
		RED = ((0, 50, 150), (120, 140, 255))
		YELLOW = ((0, 160, 245), (5, 180, 255))
		GREEN = ((0, 150, 0), (20, 255, 20))
		BLUE = ((215, 150, 0), (255, 170, 5))
		WHITE = ((250, 250,250), (255, 255, 255))
		BLACK = ((200, 200,200), (255, 255, 255))

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface, menu_navigation: enna_st12.utilities.menu_navigation.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		:param enna_st12.utilities.menu_navigation.interface.Interface menu_navigation: Instance of menu_navigation interface
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		enna_kwd_testing.stimulations.apps._internal.BaseMenuNavigation.__init__(self, reporting=reporting, android_hmi=android_hmi, menu_navigation=menu_navigation)
		self.allowed_parameter_keys = ["COLOUR"]

	def _precondition(self) -> bool:
		"""Navigate to warning lamps menu in OBB.

		:return: True if success, else False.
		"""
		return self._go_to_screen(obb.WARNING_LAMPS)


	def _action(self) -> bool:
		"""Check color of warning lamps.

		:return: True if successful, False otherwise
		:rtype: bool
		"""
		list_container = enna_hcp_configuration.android.xpaths.obb.LIST_CONTAINER.get()
		expected_color = self.values.get("COLOUR", "unknown")
		try: # pylint: disable=too-many-try-statements
			color_range = getattr(self.WarningLampColors, expected_color.upper())
			self._android_hmi.wait_for_element_visible(xpath=list_container, max_time=60.0)
			self._android_hmi.scroll_list_to_top(list_container_xpath=list_container)

			for i in range(10): # pylint: disable=unused-variable
				coordinates_size = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(layout=self._android_hmi.layout.value, xpath=list_container)
				roi = [coordinates_size["x"], coordinates_size["y"], coordinates_size["x"] + coordinates_size["width"],	 coordinates_size["y"] + coordinates_size["height"]]

				image = self._android_hmi.take_screenshot().get_roi(mask=roi)
				mask = enna_kwd_testing.stimulations.image_processing.colors._get_color_mask(image=image, dark_threshold=color_range.value[0],  bright_threshold=color_range.value[1]) # pylint: disable=protected-access

				if numpy.count_nonzero(mask) >= 1000:
					self._reporting.add_report_message_pass(f"Find a '{expected_color}' warning lamp in screen. Found {numpy.count_nonzero(mask)} pixels.")
					return True
				self._android_hmi.swipe_element(xpath=list_container, direction=enna_st12.data_interfaces.android_hmi.Direction.Up, scale=0.9)
			MODULE_LOGGER.error("Maximum of tries to find a ICON with expected color!")
		except (enna.core.exceptions.TimeoutException, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as error:
			self._reporting.add_report_message_ta_error(f"Error by checking color of OBB warning lamps! {error}")
			return False
		except AttributeError:
			self._reporting.add_report_message_ta_error(f"Color '{expected_color}' not supported! Supported colors: {list(self.WarningLampColors)}")
			return False
		self._reporting.add_report_message_system_error(f"Not found an icon in color '{expected_color}'! Not enough pixels with this color range. Minimum is 500 pixels.")
		return False

# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class ClickOnIndex(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Stimulation for click an element with one alphabetic letter in the Text in android hmi."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation.

		:param reporting: instance of report handler
		:param android_hmi: instance of android hmi control interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.allowed_parameter_keys = ["INDEX"]
		MODULE_LOGGER.debug(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Click an element with one alphabetic letter in the Text on android hmi context.

		:return: True if success, else False
		"""
		index_value:str = self.values.get("INDEX")
		if len(index_value) > 1:
			self._reporting.add_report_message_ta_error(f"Index '{index_value}' is invalid - Must be exactly one letter!")
			return False
		if not index_value.isalpha():
			self._reporting.add_report_message_ta_error(f"Index '{index_value}' is invalid - Must be an alphabetic letter!")
			return False

		try:
			index_xpath = f"//*[@text='{index_value}']"
			self._android_hmi.wait_for_element_visible(xpath=index_xpath, max_time=self._timeout)
			self._android_hmi.click_element(index_xpath)
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException:
			self._reporting.add_report_message_ta_error(f"No connection to android device! Click on element '{self.values}' is not possible.")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' not find in current screen!")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotEnabledException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' is currently not clickable!")
			return False
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error(f"Element '{self.values}' not found in screen, during TIMEOUT: {self._timeout}!")
			return False
		self._reporting.add_report_message_pass(f"Element '{self.values}' is clicked.")
		return True
