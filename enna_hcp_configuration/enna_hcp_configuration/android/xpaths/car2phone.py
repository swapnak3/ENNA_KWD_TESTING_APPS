# -*- coding: utf-8 -*-
"""Module contains xpath of launcher app."""
import enna_hcp_configuration.android.xpaths
from . import XpathString


if enna_hcp_configuration.android.xpaths.CLUSTER in enna_hcp_configuration.android.xpaths.SupportedClusters.CLU55:
	from enna_hcp_configuration.texts.CLU55.center.de.eso import phone
elif enna_hcp_configuration.android.xpaths.CLUSTER in enna_hcp_configuration.android.xpaths.SupportedClusters.CLU53:
	from enna_hcp_configuration.texts.CLU53.center.de.eso import phone
elif enna_hcp_configuration.android.xpaths.CLUSTER in enna_hcp_configuration.android.xpaths.SupportedClusters.CLU51:
	from enna_hcp_configuration.texts.CLU51.center.de.eso import phone
elif enna_hcp_configuration.android.xpaths.CLUSTER in enna_hcp_configuration.android.xpaths.SupportedClusters.CLU48:
	from enna_hcp_configuration.texts.CLU48.center.de.eso import phone
else:
	from enna_hcp_configuration.texts.CLU46.center.de.eso import phone


# pylint: disable=line-too-long

MAIN_TITLE = XpathString(f"//*[@resource-id='technology.cariad.hcp3.car2phone.audi:id/titleTextViewRef']{phone.connection_mgr__main_menu__car_2_phone__text}[@content-desc='###technology.cariad.hcp3.car2phone.audi:string/connections_tabLayoutTitleLine_title_appName']")
INFO_MESSAGE_TEXT = XpathString("//*[@resource-id='technology.cariad.hcp3.car2phone.audi:id/popupMessage']")
