# -*- coding: utf-8 -*-
"""Created on 23.11.2023.

@project: enna_kwd_testing.
@author: splatzp, Pascal Platzer.

Contains color identification features.
"""
import colorsys
import statistics
from collections import Counter

import cv2
import numpy as np
from PIL import Image


def get_most_common_color(image, search_box):
	"""Get the most common color within a specified box in the image.

	:param Image image: Image Object representing the image data.
	:param Tuple search_box: Tuple (x1, y1, x2, y2) defining the box coordinates

	:return: the most common color
	:rtype: str
	"""

	pixel_colors = []

	for y in range(search_box[1], search_box[3]):
		for x in range(search_box[0], search_box[2]):
			r, g, b = image.getpixel((x, y))
			pixel_colors.append((r, g, b))

	most_common_value = statistics.mode(_color_names(pixel_colors))
	ctr = Counter(_color_names(pixel_colors))
	try:
		if most_common_value == "gray":
			second_most_common_value = ctr.most_common(2)[1]
			return second_most_common_value[0]
	except IndexError:
		pass

	return most_common_value


def _color_names(colors):
	"""Determine color names for a list of RGB color tuples.

	:param List colors: List of RGB color tuples.

	:return: list of color names
	:rtype: str
	"""
	color_names = []
	gray_upper_threshold = 120
	gray_lower_threshold = 50
	black_threshold = 50

	for color in colors:
		r, g, b = color

		if r == g == b:
			gray = sum(color) / len(color)
			if gray_upper_threshold > gray > gray_lower_threshold:
				color_name = "gray"
			elif gray < black_threshold:
				color_name = "black"
			else:
				color_name = "white"
		else:
			color_name = _hsv_color_definition(r, g, b)

		color_names.append(color_name)

	return color_names


def _hsv_color_definition(r, g, b):
	"""Determine color names based on HSV (Hue, Saturation and Values) values.

	:param int r: Red component.
	:param int g: Green component.
	:param int b: Blue component.

	:return: color name
	:rtype: str
	"""
	h, s, v = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)

	if s < 0.1:
		if v < 0.1:
			return "black"
		return "gray"

	hue = h * 360
	if 0 <= hue < 15 or 340 <= hue <= 360:
		return "red"
	if 15 <= hue < 45:
		return "orange"
	if 45 <= hue < 75:
		return "yellow"
	if 75 <= hue < 165:
		return "green"
	if 165 <= hue < 255:
		return "blue"
	if 255 <= hue < 285:
		return "purple"
	if 285 <= hue < 345:
		return "pink"

	return "unknown_color"


def template_matching_opencv(path_img, path_tpl):
	"""executes opencv templateMatching function
	Input values:
		:param str path_img:	path for input image
		:param str path_tpl:	path to the template image
	Output values:
		:return: True if match else False
		:rtype: bool
	"""
	# template Matching
	# Load the image with transparent background
	img = cv2.imread(path_tpl)
	img_np = np.asarray(img, dtype=np.uint8)

	# Load the screenshot image
	screenshot = cv2.imread(path_img)

	# Find the image in the screenshot using template matching with alpha channel
	res = cv2.matchTemplate(screenshot, img, cv2.TM_CCORR_NORMED)
	threshold = 0.8
	loc = np.where(res >= threshold)

	# Draw rectangles around the found image regions
	h, w, _ = img_np.shape
	for pt in zip(*loc[::-1]):
		cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

	# Save the modified screenshot with the rectangles drawn
	cv2.imwrite(path_img, screenshot)

	return loc[0].size > 0


def get_roi_template_matching(path_img, path_tpl):
	"""executes opencv templateMatching function
	Input values:
		:param str path_img:	path for input image
		:param str path_tpl:	path to the template image
	Output values:
		i_result:       matching result
		l_bestMatch:    position of detected icon (topleft) [x, y, w, h]
		:return: matching result and position of detected icon (topleft) [x, y, w, h]
		:rtype: list
	"""
	# template Matching
	m_img = cv2.imread(path_img)
	m_tpl = cv2.imread(path_tpl)
	res = cv2.matchTemplate(m_img, m_tpl, cv2.TM_CCORR_NORMED)
	_, matching_val, _, max_loc = cv2.minMaxLoc(res)
	top_left = max_loc
	h, w, _ = m_tpl.shape

	l_bestmatch = [top_left[0], top_left[1], top_left[0] + w, top_left[1] + h]

	return [matching_val, l_bestmatch]


def get_pixel_colors_names_search_box(image, search_box):
	"""Get the colors within a specified box in the image.

	:param Image image: Image Object representing the image data.
	:param Tuple search_box: Tuple (x1, y1, x2, y2) defining the box coordinates

	:return: a list of colors
	:rtype: list
	"""
	pixel_colors = []

	for y in range(search_box[1], search_box[3]):
		for x in range(search_box[0], search_box[2]):
			r, g, b = image.getpixel((x, y))
			pixel_colors.append((r, g, b))
	return _color_names(pixel_colors)


def get_pixel_colors_names(image):
	"""Get the colors in the image.

	:param Image image: Image Object representing the image data.

	:return: a list of colors
	:rtype: list
	"""
	pixel_colors = []
	for y in range(image.height):
		for x in range(image.width):
			r, g, b = image.getpixel((x, y))
			pixel_colors.append((r, g, b))

	return _color_names(pixel_colors)


def replace_rgb_colors_from_image(input_image, file_path, rgb_reference):
	"""Replace all colors that do not match the reference rgb value with a transparent pixel

	:param Image.pyi input_image: Image Object representing the image data.
	:param Path file_path: Path to store the new image data.
	:param list rgb_reference: RGB list e.g [20, 50, 60] .

	"""

	rgba_img = input_image.convert("RGBA")
	new_image = Image.new("RGBA", (rgba_img.width, rgba_img.height), (0, 0, 0, 0,))
	tolerance = 10
	r_max = rgb_reference[0] + tolerance
	r_min = rgb_reference[0] - tolerance
	g_max = rgb_reference[1] + tolerance
	g_min = rgb_reference[1] - tolerance
	b_max = rgb_reference[2] + tolerance
	b_min = rgb_reference[2] - tolerance
	for y in range(rgba_img.height):
		for x in range(rgba_img.width):
			pixel = rgba_img.getpixel((x, y))
			if not r_min <= pixel[0] <= r_max and not g_min <= pixel[1] <= g_max and not b_min <= pixel[2] <= b_max or all(element == pixel[0] for element in pixel[:-1]):
				new_image.putpixel((x, y), (0, 0, 0, 255))
			else:
				new_image.putpixel((x, y), pixel)
	new_image.save(f"{file_path}", "png")
