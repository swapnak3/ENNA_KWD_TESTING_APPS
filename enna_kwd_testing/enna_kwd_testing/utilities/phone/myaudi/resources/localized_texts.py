# -*- coding: utf-8 -*-
"""Created on 27.05.2024.

@project: enna_kwd_testing.
@author: VJ28HSM: Kevin Brych.
Contains handler for localized texts CMS resources.
"""

import json


class LocalizedTexts:
    """CMS handler for localized texts."""

    def __init__(self, app_version: str):
        """Initialize object."""
        self.__data = self._get_cms_data(app_version)

    @staticmethod
    def _get_cms_data(app_version: str):
        """Get data from cms.

        :param str app_version: Version of the CMS-Data
        :return: localized texts from cms.
        :rtype: dict
        """

        # TODO: Workaround: Loading via URL is not working in Remote-VPN-Setup
        return json.load(open("C:\\SDKs\\Python\\enna_kwd_testing\\enna_kwd_testing\\utilities\\phone\\myaudi\\resources\\myaudi_localized_texts_4_26_0_de.json", encoding="utf-8"))

        #data = requests.get("https://content.app.my.audi.com/service/mobileapp/translations/De/de?v=" + app_version).content
        #return json.loads(data)

    def get_text(self, key):
        """Get text for specific key.

        :param str key: Key for specific localized text.
        :return: Localized text.
        :rtype: str
        """
        return self.__data[key]
