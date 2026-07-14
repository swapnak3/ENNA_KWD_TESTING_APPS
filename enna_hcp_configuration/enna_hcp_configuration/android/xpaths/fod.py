# -*- coding: utf-8 -*-
"""Module contains xpath of r2f app (Functions on demand - Overview of functions)."""

import enna_hcp_configuration.android.xpaths
from . import XpathString

if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.de.eso.audi import fod
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.de.eso.audi import fod
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.de.eso.audi import fod
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.de.eso.audi import fod
else:
	from enna_hcp_configuration.texts.CLU46.center.de.eso.audi import fod


OVERVIEW_OF_FUNCTIONS_TITLE = XpathString(f"//*[@resource-id='de.eso.audi.fod:id/titleTextViewRef']{fod.titlebar_title}")
BACK_BUTTON = XpathString("//*[@resource-id='de.eso.audi.fod:id/actionButtons']/./*[@class='android.widget.ImageButton']")
