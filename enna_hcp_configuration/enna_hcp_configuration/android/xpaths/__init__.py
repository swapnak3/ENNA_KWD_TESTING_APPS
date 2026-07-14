# -*- coding: utf-8 -*-
"""Module contains all XPath expressions."""
import enum

class SupportedClusters(enum.StrEnum):
	"""Constants of supported clusters."""
	CLU46 = "clu46"
	CLU48 = "clu48"
	CLU51 = "clu51"
	CLU53 = "clu53"
	CLU55 = "clu55"

LANG = "en_GB"
CLUSTER = "clu46"

CLUSTERS_PPE = [SupportedClusters.CLU46, SupportedClusters.CLU48]
CLUSTERS_MQBW = [SupportedClusters.CLU53, SupportedClusters.CLU51, SupportedClusters.CLU55]

class XpathString:
	"""A container for an XPath string which may exist in multiple languages.

	The current cluster must always be set in this module in the attribute ``CLUSTER``
	"""

	def __init__(self, general: str | None = None, **kwargs):
		"""Initialize the XpathString object.

		:param general: cluster undepented XPath
		:param kwargs: optional cluster specific XPath
		"""
		self.__general_xpath = general
		self.__specific_xpath = kwargs

	def get(self) -> str:
		"""Get the XPath expression matching the optional language.

		If a cluster specific XPath expression exist returns that
		Else returns a general XPath expression.
		If nothing expression found returns string "XPath is not define!"

		:return: return xpath
		"""
		# pylint: disable=consider-ternary-expression
		xpath = self.__specific_xpath.get(CLUSTER, None) # try to get a cluster specific definition
		if isinstance(xpath, str):
			return xpath
		if isinstance(self.__general_xpath, str):
			return self.__general_xpath
		# fond XPath defination from cluster beforr
		if "clu5" in CLUSTER:
			xpath = self.__search_cluster_before(cluster=CLUSTER, available_clusters=CLUSTERS_MQBW)
			if isinstance(xpath, str):
				return xpath
		else:
			xpath = self.__search_cluster_before(cluster=CLUSTER, available_clusters=CLUSTERS_PPE)
			if isinstance(xpath, str):
				return xpath

		return f"//*[@text='undefined for cluster {CLUSTER}']"


	def __search_cluster_before(self, cluster: str, available_clusters: list[str]) -> str | None:
		"""Search a Xpath if define for a cluster before.

		:param cluster: current cluster
		:param available_clusters:
		:return: xpath or None if nothing found
		"""
		_xpath = None
		start = available_clusters.index(cluster)
		if start > 0:
			for i in range(start, -1, -1):
				_xpath = self.__specific_xpath.get(available_clusters[i], None)
				if isinstance(_xpath, str):
					break
		return _xpath

	def __str__(self) -> str:
		"""returns the result of get-method as default string

		:return: return xpath string
		"""
		return self.get()


APP_LIST_BUTTON = XpathString("//*[@resource-id='com.android.systemui:id/navigation_bar_app_grid_button']") # needed for call in enna_st12.data_interfaces.android_hmi
MEDIA_PLAYER_CURRENT_PLAYTIME = XpathString("//*[@resource-id='com.android.car.media:id/current_time']") # needed for blacklist by scroll to top or bottom
UNDEFINED = XpathString("//*[@state='undefined']")
