# -*- coding: utf-8 -*-
"""Module for the HMI graph."""
import collections
import logging
import pathlib
import importlib

import enna_hcp_configuration.android.xpaths

MODULE_LOGGER = logging.getLogger(__name__)


# pylint:disable=unused-argument
def initialize(enna_main_config):
	"""Initialize the graph according to the ENNA config.

	:param dict enna_main_config: the configuration dict stored in enna.core.config.MAIN
	"""
	enna_hcp_configuration.android.xpaths.LANG = enna_main_config.get("system_language", "unknown")
	enna_hcp_configuration.android.xpaths.CLUSTER = f"clu{enna_main_config.get("cluster", "unknown")}"
	GRAPH.__init__() # pylint: disable=unnecessary-dunder-call
	for subgraph in pathlib.Path(__file__).parent.joinpath("subgraphs").iterdir():
		subgraph = subgraph.name.replace(".py", "")
		if not subgraph.startswith("_"):
			importlib.import_module(f"enna_hcp_configuration.android.subgraphs.{subgraph}").initialize(GRAPH)
			MODULE_LOGGER.debug(f"Add subgraph for '{subgraph}'")

	MODULE_LOGGER.info(f"Graph initialization is success! Cluster = {enna_hcp_configuration.android.xpaths.CLUSTER} and System Language = {enna_hcp_configuration.android.xpaths.LANG}")


class Graph:
	"""Container for a graph."""

	def __init__(self):
		"""Initialize the graph object."""
		self._vertices = []
		self._edges = []

	def add_transition(self, from_node, to_node, action_map):
		"""Add a transition between two nodes with an action for that transition.

		:param enna_hcp_configuration.common.base.Element from_node: the start node for this transition
		:param enna_hcp_configuration.common.base.Element to_node: the end node for this transition
		:param action_map: the action for this transition
		:type action_map: tuple(enna_hcp_configuration.android.base.HMIActionType, list[str])
		"""
		self._edges.append((from_node, to_node, action_map))
		if from_node.name not in self._vertices:
			self._vertices.append(from_node)
		if to_node.name not in self._vertices:
			self._vertices.append(to_node)

	def find_shortest_path(self, start, destination): # pylint: disable=inconsistent-return-statements
		"""Find the shortest path from start to destination.

		This method calls the algorithm to be used for graph traversal.
		Currently, there is only one algorithm (bfs) available but there might be other algorithms in the future.

		:param enna_hcp_configuration.common.base.Element start: start node
		:param enna_hcp_configuration.common.base.Element destination: destination node
		:return: tuple of list of elements and list of action map to traverse the graph. Returns None if no path is found
		:rtype: (list[enna_hcp_configuration.common.base.Element], list[(enna_hcp_configuration.android.base.HMIActionType, list[str])]) or None
		"""
		if start == destination:
			return [start], []
		to_examine = collections.deque()
		seen = set()
		path_data = {}

		# will hold vertices as str and not object. this will make usage of data types much easier since str is hashable
		to_examine.append(start.name)

		while to_examine:
			vertex = to_examine.popleft()
			seen.add(vertex)

			neighbors = [x[1].name for x in self._edges if vertex == x[0]]

			for neighbor in neighbors:
				if neighbor in seen:
					continue

				if neighbor == destination:
					path_data[neighbor] = vertex
					return (shortest_path := self.__construct_path(path_data, start.name, neighbor)), self.__construct_action_list(collections.deque(shortest_path))

				if neighbor not in to_examine:
					path_data[neighbor] = vertex
					to_examine.append(neighbor)

	def get_vertex_by_name(self, name):
		"""Get vertex by name if it's present in graph.

		:param str name: name of the vertex
		:return: vertex if found else None
		:rtype: enna_hcp_configuration.common.base.Element or None
		"""
		if result := [vertex for vertex in self._vertices if vertex.name == name]:
			return result[0]
		return None

	def __construct_path(self, path_data, start, destination):
		"""Construct a path from start to destination.

		:param dict(str,str) path_data: mapping of vertex.name to preceding vertex.name in the path
		:param str start: name of start vertex
		:param str destination: name of destination vertex
		:return: found path
		:rtype: list[enna_hcp_configuration.common.base.Element]
		"""
		path = []
		while destination is not start:
			path.append(destination)
			destination = path_data[destination]
		path.append(start)
		path.reverse()
		return [self.get_vertex_by_name(vertex_str) for vertex_str in path]

	def __construct_action_list(self, path):
		"""Construct an action list from a path.

		:param deque(str) path: path as a deque of screen names
		:return: actions
		:rtype: list[(enna_hcp_configuration.android.base.HMIActionType, list[str])]
		"""
		action_list = []
		vertex = path.popleft()
		while path:
			neighbor = path.popleft()
			action_list.append([x[2] for x in self._edges if vertex == x[0] and neighbor == x[1]][0])
			vertex = neighbor
		return action_list

	@property
	def vertices(self):
		"""Property contains all vertices of the graph.

		:return: vertices
		:rtype: list[enna_hcp_configuration.common.base.Element]
		"""
		return self._vertices

	@property
	def edges(self):
		"""Property contains all edges of the graph.

		:return: edges
		:rtype: list[tuple(enna_hcp_configuration.android.base.HMIActionType, list[str])]
		"""
		return self._edges


GRAPH = Graph()
