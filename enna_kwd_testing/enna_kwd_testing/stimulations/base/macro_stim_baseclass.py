# -*- coding: utf-8 -*-
"""Created on 02.06.2025.

@project: enna_kwd_testing.
@author: VDGA3GV: Andreas Ampferl.

Contains the abstract base class for a stimulation macro.
"""
import logging

import enna.core.deployment.debug
import enna.core.interfaces.testing
import enna_kwd_testing.stimulations.base.exceptions
import enna_kwd_testing.stimulations.base.keyword_stim_baseclass
from enna_kwd_testing.core.logging import colors

MODULE_LOGGER = logging.getLogger(__name__)

class MacroStimulation(enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation):
	"""Class that can call other stimulations as sub_routines."""

	def __init__(self, reporting, **kwargs):
		r"""Initialize keyword object.

		:param enna.core.reporting.interface.Interface reporting: Instance of reporting interface.
		:param dict \**kwargs: for handling stimulations passed via decorator
		"""
		super().__init__(reporting, based_on_kwd_spec_version="1.0.3")
		self.sequence=[]
		self.default_values={}
		self.kwd_instances={}
		self.success=True # if no stimulations are executed, result is successful
		for _, arg in kwargs.items():
			if isinstance(arg, (enna_kwd_testing.stimulations.base.keyword_stim_baseclass.KeywordStimulation,enna.core.interfaces.testing.Stimulation)):
				kwd_stim_class = f"{type(arg).__module__}.{type(arg).__name__}"
				default_values = None if not hasattr(arg,"values") else {} if arg.values is None else arg.values
				self.default_values[kwd_stim_class] = default_values # remember original stimulation values to recall them after possible modifications
				self.kwd_instances[kwd_stim_class] = arg # create index for stimulation instances by class_name
				self.sequence.insert(0,kwd_stim_class) # autocreate sequence with stimulations declared by decorators (order needs to be revered)

	def _run(self, sequence: list | str | tuple | dict | None) -> bool:
		"""run sequence or command while a negative result will only set the returned value to false, not the whole macro result

		:param sequence: sequence or command that shall be executed
		:return: Merged result executed sequence or command. True if everything worked as expected, False otherwise
		:rtype: bool
		"""
		success = True
		if sequence is None:
			sequence=[]
		if isinstance(sequence,(str,tuple,dict)):
			sequence=[sequence]
		for keyword in sequence:
			if isinstance(keyword,str):
				keyword_name=keyword
				keyword_values={}
			elif isinstance(keyword,tuple):
				keyword_name, keyword_values=keyword
			elif isinstance(keyword,dict):
				for name, values in keyword.items():
					keyword_name=name
					keyword_values=values
					break
			stim_instance = self.kwd_instances.get(keyword_name)
			if stim_instance is None:
				MODULE_LOGGER.error(f"tried to run undefined stimulation \"{keyword_name}\". Did you forget to add the RequireStimulation decorator?")
				return False
			if self.default_values[keyword_name] is not None: # we only have values if it is a KWD-Class
				stim_instance.values=self.default_values[keyword_name] | keyword_values
			success &= stim_instance.start()
		return success

	def run(self, sequence: list | str | tuple | dict | None) -> bool:
		"""run sequence or command while a negative result will set the success of the whole macro to failed

		:param sequence: sequence or command that shall be executed
		:return: Merged result executed sequence or command. True if everything worked as expected, False otherwise
		:rtype: bool
		"""
		self.success &= self._run(sequence)
		return self.success

	def run_if(self, check_sequence: list | str | tuple | dict | bool, run_if_true: list | str | tuple | dict | None = None, run_if_false:list | str | tuple | dict | None= None) -> bool:
		"""run sequence or command while a negative result will set the success of the whole macro to failed

		:param check_sequence: sequence or command that shall be checked or directly the result of a check as boolean
		:param run_if_true: sequence or command that shall be executed if check result is True
		:param run_if_false: sequence or command that shall be executed if check result is True
		:return: Merged result executed sequence or command. True if everything worked as expected, False otherwise
		:rtype: bool
		"""
		MODULE_LOGGER.info(colors.RESET+ f"EXECUTION INFO: CONDITIONAL EXECUTION: Checking {check_sequence}")
		check = check_sequence if isinstance(check_sequence,bool) else self._run(check_sequence)
		sequence=run_if_true if self._run(check_sequence) else run_if_false
		MODULE_LOGGER.info(colors.RESET+ f"EXECUTION INFO: CONDITIONAL EXECUTION: {check_sequence} was {check}, so {sequence} will be executed")
		self.success &= self._run(sequence)
		return self.success

	def _action(self, run_sequence: bool = True) -> bool:
		"""Overwrite enna.core.interfaces.testing.Stimulation.start method to add functionality for reporting metadata of stimulation.

		Attention! Please avoid changes in the sequence during _action as multiple executions of the Stimulation-Instance might end up in different results

		:param bool run_sequence: shall the commands waiting in self.sequence be exectued or ignored?
		:return: Merged result of stimulation. True if everything worked as expected, False otherwise
		:rtype: bool
		"""
		if len(self.sequence)>0 and run_sequence:
			self.run(self.sequence)
		return self.success
