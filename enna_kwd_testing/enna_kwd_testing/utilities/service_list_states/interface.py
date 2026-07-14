# -*- coding: utf-8 -*-
"""Interface for reading service list states."""
import enna.core.component_system.decorators
import enna.core.interfaces.component


@enna.core.component_system.decorators.GenerateProxy()
class Interface(enna.core.interfaces.component.Component):
	"""Interface for data that will be used by the proxy and server."""

	def __init__(self) -> None:
		"""Interface for service list states."""
		self._apn1 = enna.core.interfaces.Data(True)
		self._apn2 = enna.core.interfaces.Data(True)

		self._ignitestore_v1 = enna.core.interfaces.Data(True)
		self._ico_v1 = enna.core.interfaces.Data(True)
		self._obb_v1 = enna.core.interfaces.Data(True)
		self._olb_v1 = enna.core.interfaces.Data(True)

	@property
	def apn1(self) -> enna.core.interfaces.Data[bool]:
		"""Return last state of APN1 from Logging. States are unknown, blocked or connected.

		:return: True if connected else False
		"""
		return self._apn1

	@property
	def apn2(self) -> enna.core.interfaces.Data[bool]:
		"""Return last state of APN2 from Logging. States are unknown, blocked or connected.

		:return: True if connected else False
		"""
		return self._apn2

	@property
	def ignitestore_v1(self) -> enna.core.interfaces.Data[bool]:
		"""Return last disable of service ignitestore_v1.

		:return: exist a disable reason
		"""
		return self._ignitestore_v1

	@property
	def ico_v1(self) -> enna.core.interfaces.Data[bool]:
		"""Return last disable of service ico_v1.

		:return: exist a disable reason
		"""
		return self._ico_v1

	@property
	def obb_v1(self) -> enna.core.interfaces.Data[bool]:
		"""Return last disable of service obb_v1.

		:return: exist a disable reason
		"""
		return self._obb_v1

	@property
	def olb_v1(self) -> enna.core.interfaces.Data[bool]:
		"""Return last disable of service obb_v1.

		:return: exist a disable reason
		"""
		return self._olb_v1
