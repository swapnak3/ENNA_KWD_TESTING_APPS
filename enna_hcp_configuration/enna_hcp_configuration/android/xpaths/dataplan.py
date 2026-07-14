# -*- coding: utf-8 -*-
"""Module contains xpath of launcher app."""
from . import XpathString

# pylint: disable=line-too-long

# 46+53 were equal
MAIN_TITLE = XpathString("//*[@resource-id='de.eso.audi.dataplan:id/titleTextViewRef'][contains(@content-desc,'de.eso.audi.dataplan:string/texttool_globals_application_label___dataplan__app_name')]")
#unused: BACK_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][@bounds='[420,0][551,119]']")
#unused: SEARCH_BUTTON = XpathString("//*[@class='android.widget.ImageButton'][@bounds='[551,0][682,119]']")
