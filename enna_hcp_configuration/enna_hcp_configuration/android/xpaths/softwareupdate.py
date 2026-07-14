# -*- coding: utf-8 -*-
"""Module contains xpath of softwareupdate app."""

from . import XpathString


MAIN_TITLE = XpathString("//*[@content-desc='UpdateAvailableScreen']")
BACK_BUTTON = XpathString("//*[@resource-id='de.eso.audi.softwareupdate:id/actionButtons']/./*[@class='android.widget.ImageButton']")
