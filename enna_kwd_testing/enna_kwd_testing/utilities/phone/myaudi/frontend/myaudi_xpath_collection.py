# -*- coding: utf-8 -*-
"""Created on 27.05.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
Specialized xpath collection for myaudi app
"""
from pathlib import Path

from enna_kwd_testing.utilities.xpath_collection.helper import XpathHandler


class MyAudiXpathLoader(XpathHandler):

	def __init__(self, app: str = "myaudi", package_name: str = "de.myaudi.mobile.assistant.r"):
		super().__init__(app)
		self.__package_name = package_name

	def get_xpath(self, screen, element) -> str:
		xpath = super().get_xpath(screen, element)

		return xpath.replace("$PACKAGE$", self.__package_name)
