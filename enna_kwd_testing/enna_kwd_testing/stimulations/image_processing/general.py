# -*- coding: utf-8 -*-
"""Module contains stimulation image processing."""
import logging
import pathlib
import time

import enna.core.component_system.decorators
import enna.core.config
import enna.core.exceptions
import enna.core.image_processing.helper
import enna.core.image_processing.image
import enna.core.reporting.interface
import enna_st12.data_interfaces.android_hmi.exceptions
import enna_st12.data_interfaces.android_hmi.helper
import enna_st12.data_interfaces.android_hmi.interface
import enna_st12.instance_names

import enna_kwd_testing.stimulations.apps._internal
import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
import enna_kwd_testing.utilities.text_tool.helper
import enna_kwd_testing.utilities.xpath_collection.exceptions
import enna_kwd_testing.utilities.xpath_collection.helper

MODULE_LOGGER = logging.getLogger(__name__)
MODULE_CONFIG = enna.core.config.get(__name__)
OCR_MODULE_CONFIG = enna.core.config.get("enna.core.image_processing.helper")


# pylint: disable=too-many-locals, too-many-branches

class _BaseImageProcessing(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class contains basic methods for image processing. Temple Matching, OCR, ..."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface) -> None:
		"""Constructor for base stimulation of image processing.

		:param reporting: instance of reporting interface
		"""
		super().__init__(reporting=reporting)
		self._templates: pathlib.Path = pathlib.Path(__file__).parent.joinpath("templates")


	def _template_matching(self, image: enna.core.image_processing.image.Image, template_name: str, min_match: float = 0.95) -> bool:
		"""Make template matching in image.
		Template must exist in template folder

		:param image: image want to check
		:param template_name: name of searched template
		:param min_match: percent of minimum matching
		:return: True if matching successful, else false.
		"""
		template_path = self._templates.joinpath(f"CLU{enna.core.config.INFOTAINMENT_SYSTEM.cluster}/{template_name}.png")

		if not template_path.exists():
			self._reporting.add_report_message_ta_error(f"Template '{template_name}' not found! Path: {template_path}")
			return False

		try:
			template = enna.core.image_processing.helper.load_image_from_file(template_path)
			matches = enna.core.image_processing.helper.match_template(image=image, template=template, min_match=min_match)
		except enna.core.exceptions.ImageProcessingException as error:
			self._reporting.add_report_message_ta_error(f"Error by template matching! {error}")
			return False

		if len(matches) == 1:
			self._reporting.add_report_message_pass(f"Template '{template_name}' find in image on position {matches}.")
			return True
		if len(matches) > 1:
			self._reporting.add_report_message_system_error(f"Template '{template_name}' find in image on some positions {matches}!")
			return False
		self._reporting.add_report_message_system_error(f"Template '{template_name}' not found in image!")
		return False

	@staticmethod
	def _get_text_from_image(image: enna.core.image_processing.image.Image, language: str = enna.core.config.INFOTAINMENT_SYSTEM.system_language.value) -> str:
		"""Optical character recognition for this image.

		:param image: image want to check
		:param language: language of text
		:return: recognize text
		:raise enna.core.exceptions.ImageProcessingException: if error by ocr process
		"""
		language = OCR_MODULE_CONFIG.get("ocr_configs", {}).get(language, "deu")
		text, area = enna.core.image_processing.helper.get_text(image=image, language=language, preprocessing_parameters=enna.core.image_processing.helper.PreprocessingParameters(skip_binarizing=True))

		if text == "":
			MODULE_LOGGER.info("No text found by normal image. It try it with reverse image.")
			inverse_image = enna.core.image_processing.image.Image(~image.as_ndarray)
			text, area = enna.core.image_processing.helper.get_text(image=inverse_image, language=language, preprocessing_parameters=enna.core.image_processing.helper.PreprocessingParameters(skip_binarizing=True))

		if text == "":
			MODULE_LOGGER.info("No text found by inverse image. It try it with binarizing on image.")
			text, area = enna.core.image_processing.helper.get_text(image=image, language=language, preprocessing_parameters=enna.core.image_processing.helper.PreprocessingParameters(skip_binarizing=False, blurring=enna.core.image_processing.helper.Blurring.GAUSSIAN)) # pylint: disable=line-too-long

		if text == "":
			MODULE_LOGGER.info("No text found by inverse image. It try it with binarizing on inverse image.")
			inverse_image = enna.core.image_processing.image.Image(~image.as_ndarray)
			text, area = enna.core.image_processing.helper.get_text(image=inverse_image, language=language, preprocessing_parameters=enna.core.image_processing.helper.PreprocessingParameters(skip_binarizing=False, blurring=enna.core.image_processing.helper.Blurring.GAUSSIAN)) # pylint: disable=line-too-long


		# MODULE_LOGGER.info(f"Text: '{text}', Area in screen: {area}")
		MODULE_LOGGER.info(f"Text:\n{text}\nArea in screen: {area}")
		# debug: enna.core.image_processing.helper.save_image(enna_image=image, path=pathlib.Path("./ocr_image"))
		return text


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class MatchTemplate(_BaseImageProcessing):
	"""Stimulation of matching template."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of Stimulation

		:param reporting: instance of reporting interface
		:param android_hmi: instance of interface for android UI
		"""
		super().__init__(reporting=reporting)
		self._android_hmi = android_hmi
		self.allowed_parameter_keys = ["TEMPLATE_DATA", "ROI", "ROI_XPATH", "MIN_MATCH"]
		MODULE_LOGGER.info(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Make screenshot from current android device. And match template in image.

		:return: True if matching successful, else false.
		"""

		template_name = self.values.get("TEMPLATE_DATA", "unknown")
		min_match = self.values.get("MIN_MATCH", 0.85)
		roi = None

		if "ROI" in self.values:
			roi = self.values["ROI"]
			if len(roi) != 4:
				self._reporting.add_report_message_ta_error(f"Region of interest need 4 integers! roi = {roi}")
				return False
		elif "ROI_XPATH" in self.values:
			try:
				xpath = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler.get_xpath_app_screen_id(reporting=self._reporting, android_hmi=self._android_hmi, element=self.values["ROI_XPATH"])
				coordinates_size = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(layout=self._android_hmi.layout.value , xpath=xpath)
				roi = [coordinates_size["x"], coordinates_size["y"], coordinates_size["x"] + coordinates_size["width"], coordinates_size["y"] + coordinates_size["height"]]
			except (enna_kwd_testing.utilities.xpath_collection.exceptions.ElementNotFound, enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException) as error:
				self._reporting.add_report_message_ta_error(f"Region of interest could not be set by xpath! {error}")
				return False

		try:
			image = self._android_hmi.take_screenshot().get_roi(mask=roi) if isinstance(roi, list) else  self._android_hmi.take_screenshot()
		except enna_st12.data_interfaces.android_hmi.exceptions.NoDeviceConnectedException:
			self._reporting.add_report_message_warning("Lost connection to Android HMI. Reconnecting...")
			self._android_hmi.connect()
			image = self._android_hmi.take_screenshot().get_roi(mask=roi) if isinstance(roi, list) else  self._android_hmi.take_screenshot()

		return self._template_matching(image=image, template_name=template_name, min_match=min_match)


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckText(_BaseImageProcessing):
	"""Stimulation of checking Text in Android UI."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of Stimulation

		:param reporting: instance of reporting interface
		:param android_hmi: instance of interface for android UI
		"""
		super().__init__(reporting=reporting)
		self._android_hmi = android_hmi
		self.allowed_parameter_keys = ["LABEL", "LABEL_SOURCE", "LANG", "XPATH_NAME", "LABEL_LIST"]
		MODULE_LOGGER.info(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Check text is in current screen.

		:return: True if matching successful, else false.
		"""

		language: str = self.values.get("LANG", enna.core.config.INFOTAINMENT_SYSTEM.system_language.value)
		label_list: list[str] = self.values.get("LABEL_LIST") # will be ignored if 'LABEL' is given
		label: str = self.values.get("LABEL")
		source: str = self.values.get("LABEL_SOURCE", "center")
		xpath: str | None = self.values.get("XPATH_NAME", None)

		expected_text = "No text to check is specified via LABEL or LABEL_LIST!"
		if label is not None:
			expected_text = enna_kwd_testing.utilities.text_tool.helper.get_text_from_configuration(text_id=label, source=source, language=language)
		xpath_text = f"//*[contains(@text,'{expected_text}')]"
		if label is None and label_list is not None:
			test_parts=[enna_kwd_testing.utilities.text_tool.helper.get_text_from_configuration(text_id=text, source=source, language=language) for text in label_list]
			# find xpath with @text that contains all sub parts so we can handle zero white spaces, which are ignored by ocr anyway
			expected_text = "".join(test_parts)
			xpath_text = f"//*[{ " and ".join([f"contains(@text,'{text_part}')" for text_part in test_parts])}]"
		# find area of text
		try:
			if isinstance(xpath,str):
				xpath = enna_kwd_testing.utilities.xpath_collection.helper.XpathHandler(self._reporting, "unset").get_xpath("unset", xpath)
				self._android_hmi.wait_for_element_visible(xpath=xpath, max_time=3.0)
				coordinates_size = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(layout=self._android_hmi.layout.value, xpath=xpath)
				roi = [coordinates_size["x"], coordinates_size["y"], coordinates_size["x"] + coordinates_size["width"], coordinates_size["y"] + coordinates_size["height"]]
			else:
				self._android_hmi.wait_for_element_visible(xpath=xpath_text, max_time=3.0)
				coordinates_size = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(layout=self._android_hmi.layout.value, xpath=xpath_text)
				roi = [coordinates_size["x"], coordinates_size["y"], coordinates_size["x"] + coordinates_size["width"], coordinates_size["y"] + coordinates_size["height"]]
			time.sleep(0.7)  # delay between android ui dump and visible screen
			current_screen = self._android_hmi.take_screenshot().get_roi(mask=roi)
		except enna.core.exceptions.TimeoutException as error:
			self._reporting.add_report_message_system_error(f"Region of interest not found in android UI! {error}")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_ta_error(f"Error by checking text! {error}")
			return False
		except enna_kwd_testing.utilities.xpath_collection.exceptions.ElementNotFound as error:
			self._reporting.add_report_message_ta_error(f"XPATH_NAME {xpath} not found!")
			return False
		try:
			current_text = self._get_text_from_image(image=current_screen, language=language).strip()
		except enna.core.exceptions.ImageProcessingException as error:
			self._reporting.add_report_message_ta_error(f"Error by image processing! {error}")
			return False
		if current_text != expected_text:
			self._reporting.add_report_message_system_error(f"Current Text '{current_text.replace('\n', '\\n')}' is not equal expected text '{expected_text.replace('\n', '\\n')}'!")
			return False
		self._reporting.add_report_message_pass(f"Expected text is correct displayed in UI. Current Text: '{current_text.replace('\n', '\\n')}'")
		return True


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckTextOrientation(_BaseImageProcessing):
	"""Stimulation of checking Text orientation (left/right) in Android UI."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of Stimulation

		:param reporting: instance of reporting interface
		:param android_hmi: instance of interface for android UI
		"""
		super().__init__(reporting=reporting)
		self._android_hmi = android_hmi
		self.allowed_parameter_keys = ["LABEL", "LABEL_SOURCE", "LANG", "ORIENTATION", "TOLERANCE"]
		MODULE_LOGGER.info(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Check text is in current screen and the orientation .

		:return: True if matching successful, else false.
		"""

		language: str = self.values.get("LANG", enna.core.config.INFOTAINMENT_SYSTEM.system_language.value)
		label: str = self.values.get("LABEL", "No text get from specification!")
		source: str = self.values.get("LABEL_SOURCE", "center")
		orientation: str = self.values.get("ORIENTATION", "left")
		tolerance: int = self.values.get("TOLERANCE", 5)
		if orientation not in ["left", "right", "center"]:
			self._reporting.add_report_message_system_error(f"ORIENTATION is: '{orientation}' and not one of: 'left', 'right', 'center'.")
			return False
		if not 0 <= tolerance <= 100:
			self._reporting.add_report_message_system_error(f"TOLERANCE is: '{tolerance}' but should be between 0 and 100.")
			return False

		expected_text = enna_kwd_testing.utilities.text_tool.helper.get_text_from_configuration(text_id=label, source=source, language=language)
		xpath_text = f"//*[contains(@text, '{expected_text}')]"
		xpath_parent = f"//*[contains(@text, '{expected_text}')]/../."
		# find area of text
		try:
			self._android_hmi.wait_for_element_visible(xpath=xpath_text, max_time=3.0)
			text_coordinates_size = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(layout=self._android_hmi.layout.value, xpath=xpath_text)
			parent_coordinates_size = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(layout=self._android_hmi.layout.value, xpath=xpath_parent)
			bounds_text = [text_coordinates_size["x"], text_coordinates_size["y"], text_coordinates_size["x"] + text_coordinates_size["width"], text_coordinates_size["y"] + text_coordinates_size["height"]]
			# bounds_parent = [parent_coordinates_size["x"], parent_coordinates_size["y"], parent_coordinates_size["x"] + parent_coordinates_size["width"], parent_coordinates_size["y"] + parent_coordinates_size["height"]]
		except enna.core.exceptions.TimeoutException:
			self._reporting.add_report_message_system_error(f"Text '{expected_text.replace("\n", "\\n")}' not found in android UI!")
			return False
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException as error:
			self._reporting.add_report_message_ta_error(f"Error by checking text! {error}")
			return False

		# checked displayed text.
		time.sleep(0.7)  # delay between android ui dump and visible screen
		current_text, area = enna.core.image_processing.helper.get_text(image=self._android_hmi.take_screenshot().get_roi(mask=bounds_text), language="deu" if language == "de_DE" else "eng")
		x_middle_text = area[0] + ((area[2] - area[0]) / 2)
		x_middle_parents = (parent_coordinates_size['width'] - parent_coordinates_size['x']) / 2
		if current_text != expected_text:
			self._reporting.add_report_message_system_error(f"OCR Text is not equal expected text! Expected Text: '{expected_text.replace('\n', '\\n')}'")
			self._reporting.add_report_message_system_error(f"OCR Text is not equal expected text! Current Text : '{current_text.replace('\n', '\\n')}'")
			return False
		if orientation == "left":
			if tolerance >= abs(text_coordinates_size['x'] - parent_coordinates_size['x']) + area[0]:
				self._reporting.add_report_message_pass(f"Expected text '{expected_text}' orientaion is 'left' with delta: '{abs(text_coordinates_size['x'] - parent_coordinates_size['x']) + area[0]}', OK, is in TOLERANCE {tolerance}.")
			else:
				self._reporting.add_report_message_system_error(f"Expected text '{expected_text}' orientation is 'left', but not in TOLERANCE: '{tolerance}', difference is '"
				                                                f"{abs(text_coordinates_size['x'] - parent_coordinates_size['x']) + area[0]}'.")
				return False
		elif orientation == "right":
			if tolerance >= abs((parent_coordinates_size['x'] + parent_coordinates_size['width']) - (text_coordinates_size['x'] + text_coordinates_size['width'])) + area[2]:
				self._reporting.add_report_message_pass(f"Expected text '{expected_text}' orientaion is 'right' with delta: '"
				                                        f"{abs((parent_coordinates_size['x'] + parent_coordinates_size['width']) - (text_coordinates_size['x'] + text_coordinates_size['width'])) + area[2]}', OK, is in TOLERANCE {tolerance}.")
			else:
				self._reporting.add_report_message_system_error(f"Expected text '{expected_text}' orientation is 'right', but not in TOLERANCE: '{tolerance}', difference is "
				                                                f"'{abs((parent_coordinates_size['x'] + parent_coordinates_size['width']) - (text_coordinates_size['x'] + text_coordinates_size['width'])) + area[2]}'.")
				return False
		elif orientation == "center":
			if tolerance >= abs(x_middle_parents - x_middle_text):
				self._reporting.add_report_message_pass(f"Expected text '{expected_text}' orientaion is 'center' with delta: '{abs(x_middle_parents - x_middle_text)}', OK, is in TOLERANCE {tolerance}.")
			else:
				self._reporting.add_report_message_system_error(f"Expected text '{expected_text}' orientation is center, but not in TOLERANCE: '{tolerance}', difference is '{abs(x_middle_parents - x_middle_text)}'.")
				return False

		return True

# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckPositionInScreen(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement, _BaseImageProcessing):
	"""Stimulation check region of interest from current screen contains expected icon or text.
	Take a screenshot from current selected menu. Cut region of interest from image.
	Check region of interest contains text or template image.
	"""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation for checking position.

		:param reporting: interface to write report messages
		:param android_hmi: interfaces to control Android UI
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		_BaseImageProcessing.__init__(self, reporting=reporting)
		self.allowed_parameter_keys = ["TEXT", "ICON","XPATH_NAME", "COORDINATES", "LANG", "MIN_MATCH"]
		MODULE_LOGGER.info(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Check text or icon is an area.

		:return: true if success, else false
		"""
		language = self.values.get("LANG", enna.core.config.INFOTAINMENT_SYSTEM.system_language.value)
		min_match = self.values.get("MIN_MATCH", 0.85)

		if "COORDINATES" in self.values:
			area = self.values["COORDINATES"]
			if len(area) != 4:
				self._reporting.add_report_message_ta_error(f"Get invalid coordinates! Coordinates = {area}")
				return False
		if "XPATH_NAME" in self.values:
			try:
				self._android_hmi.wait_for_element_visible(xpath=self._xpath, max_time=1.0)
				coordinates_size = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(layout=self._android_hmi.layout.value, xpath=self._xpath)
				area = [coordinates_size["x"], coordinates_size["y"], coordinates_size["x"] + coordinates_size["width"], coordinates_size["y"] + coordinates_size["height"]]
			except KeyError:
				self._reporting.add_report_message_ta_error(f"Xpath name '{self.values["XPATH_NAME"]}' does not exist! Please create it.")
				return False
		else:
			self._reporting.add_report_message_ta_error("Missing parameter for xpath name! Must get parameters 'coordinates' or 'xpath_name'.")
			return False
		try: # pylint: disable=too-many-try-statements
			if "ICON" in self.values:
				if self._template_matching(image=self._android_hmi.take_screenshot().get_roi(mask=area), template_name=self.values["ICON"], min_match=min_match):
					self._reporting.add_report_message_pass(f"ICON is in area {area}")
					return True
				self._reporting.add_report_message_system_error(f"Icon '{self.values['ICON']}' does not found in area {area}!")
			if "TEXT" in self.values:
				expected_text = enna_kwd_testing.utilities.text_tool.helper.get_text_from_configuration(text_id=self.values["TEXT"], source=enna_st12.instance_names.AndroidHMI.CENTER, language=language)
				if expected_text in self._get_text_from_image(image=self._android_hmi.take_screenshot().get_roi(mask=area), language=language):
					self._reporting.add_report_message_pass(f"Text is in area {area}")
					return True
				self._reporting.add_report_message_system_error(f"Text '{expected_text.replace('\n','\\n')}' does not found in area {area}!")
			if "COORDINATES" in self.values and "XPATH_NAME" in self.values:
				if self.values["COORDINATES"] == area:
					self._reporting.add_report_message_pass(f"XPATH is in expected area {self.values["COORDINATES"]}")
					return True
				self._reporting.add_report_message_system_error(f"XPATH position '{area}' is not in expected area {self.values["COORDINATES"]}!")
		except enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException:
			self._reporting.add_report_message_ta_error("Could not take a screenshot from Android device!")
			return False
		return False


@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckToastIsVisible(_BaseImageProcessing):
	"""Stimulation check is an expected Toast is visible."""

	def __init__(self, reporting: enna.core.reporting.interface.Interface, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface) -> None:
		"""Constructor of stimulation for checking position.

		:param reporting: interface to write report messages
		:param android_hmi: interfaces to control Android UI
		"""
		super().__init__(reporting=reporting)
		self.__android_hmi = android_hmi
		self.allowed_parameter_keys = ["TEXT", "LANG"]
		self._maximal_duration = 5.0
		self._toast_area = (685, 585, 1985, 805)
		MODULE_LOGGER.info(f"Allowed Parameters: {self.allowed_parameter_keys}")

	def _action(self) -> bool:
		"""Check Toast is visible on MMI Display.

		:return: true if success, else false
		"""
		language = self.values.get("LANG", enna.core.config.INFOTAINMENT_SYSTEM.system_language.value)
		expected_text = enna_kwd_testing.utilities.text_tool.helper.get_text_from_configuration(text_id=self.values["TEXT"], source=enna_st12.instance_names.AndroidHMI.CENTER, language=language)
		toast_text = "unknown"
		end_time = time.time() + self._maximal_duration
		while time.time() < end_time:
			try:
				current_toast_image = self.__android_hmi.take_screenshot().get_roi(mask=self._toast_area)
				toast_text = self._get_text_from_image(image=current_toast_image, language=language)
				if toast_text == expected_text:
					self._reporting.add_report_message_pass(f"Toast with Text '{expected_text.replace('\n', ' ')}' is visible.")
					return True
				time.sleep(0.5) # delay for a new check
			except (enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException, enna.core.exceptions.ImageProcessingException) as error:
				MODULE_LOGGER.error(f"Error by checking Toast! {error}")

		self._reporting.add_report_message_info(f"Current text: '{toast_text.replace('\n', ' ')}'")
		self._reporting.add_report_message_system_error(f"Toast with Text '{expected_text.replace('\n', ' ')}' is not visible inner {self._maximal_duration} seconds.")
		return False


# pylint: disable=protected-access
@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
class CheckSliderValue(enna_kwd_testing.stimulations.apps._internal.BaseOfUsageElement):
	"""Class containing functionality to set a new value on a slider."""

	def __init__(self, reporting, android_hmi: enna_st12.data_interfaces.android_hmi.interface.Interface):
		"""Initialize stimulation.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface
		:param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: Instance of android_hmi interface
		"""
		super().__init__(reporting=reporting, android_hmi=android_hmi)
		self.allowed_parameter_keys = ["XPATH_NAME", "VALUE", "STEPS"]
		self._template_folder = pathlib.Path(__file__).parent.joinpath(f"templates/CLU{enna.core.config.INFOTAINMENT_SYSTEM.cluster}")

	def _action(self) -> bool:
		"""Check a new value on a slider

		:return: True if successful, False if an error occurs in any step.
		:rtype: bool
		"""

		check_value: float = float(self.values.get("VALUE", -1.0))
		steps: int = int(self.values.get("STEPS", 25))
		if check_value < 0.0 or check_value > 1.0:
			self._reporting.add_report_message_ta_error("Mandatory parameter 'VALUE' is missing or out of range!")
			return False
		if steps <= 0:
			self._reporting.add_report_message_ta_error("Steps is out of range!")
			return False
		try: # pylint: disable=too-many-try-statements
			seekbar_coordinates_size = enna_st12.data_interfaces.android_hmi.helper.get_element_coordinates_and_size(layout=self._android_hmi.layout.value, xpath=self._xpath)
			seekbar_coordinates_roi: list[int] = [seekbar_coordinates_size["x"], seekbar_coordinates_size["y"],
												  seekbar_coordinates_size["x"] + seekbar_coordinates_size["width"],
												  seekbar_coordinates_size["y"] + seekbar_coordinates_size["height"]]
			seekbar_image = self._android_hmi.take_screenshot().get_roi(mask=seekbar_coordinates_roi)

			slider_template = enna.core.image_processing.helper.load_image_from_file(self._template_folder.joinpath("SLIDER.png"))
			position_slider = enna.core.image_processing.helper.match_template(image=seekbar_image, template=slider_template, min_match=0.90)

			if len(position_slider) >= 1:
				precision = 1 / (steps * 2)
				current_value = (position_slider[0][0] + slider_template.width / 2) / seekbar_coordinates_size["width"]
				if (check_value - precision) <= current_value <= (check_value + precision):
					self._reporting.add_report_message_pass(f"Current value '{round(current_value, 3)}' is approximately expected value '{round(check_value, 2)}'.  Allowed range: {check_value - precision} - {check_value + precision}")
					return True
				self._reporting.add_report_message_system_error(f"Current value '{round(current_value, 3)}' is not expected value '{round(check_value, 2)}'! Allowed range: {check_value - precision} - {check_value + precision}")
				return False
		except enna_st12.data_interfaces.android_hmi.exceptions.ElementNotPresentException as error:
			self._reporting.add_report_message_ta_error(f"element '{self._xpath}' not found in screen! {error}")
			return False
		except (enna_st12.data_interfaces.android_hmi.exceptions.AndroidHMIException, enna.core.exceptions.ImageProcessingException) as error:
			self._reporting.add_report_message_ta_error(f"Error while check value of slider {error}")
			return False

		self._reporting.add_report_message_ta_error("Slider-Button was not found!")
		return False
