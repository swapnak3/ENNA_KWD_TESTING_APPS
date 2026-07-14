# -*- coding: utf-8 -*-
"""Module contains xpath of r2f app (Restore to factory settings)."""

import enna_hcp_configuration.android.xpaths
from . import XpathString

if enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.de.eso import r2f
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.de.eso import r2f
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.de.eso import r2f
elif enna_hcp_configuration.android.xpaths.CLUSTER == enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.de.eso import r2f
else:
	from enna_hcp_configuration.texts.CLU46.center.de.eso import r2f


RESTORE_FACTORY_SETTINGS_TITLE = XpathString(f"//*[@resource-id='de.eso.r2f:id/titleTextViewRef']{r2f.r2f_title}")
BACK_BUTTON = XpathString("//*[@resource-id='de.eso.r2f:id/actionButtons']/./*[@class='android.widget.ImageButton']")
