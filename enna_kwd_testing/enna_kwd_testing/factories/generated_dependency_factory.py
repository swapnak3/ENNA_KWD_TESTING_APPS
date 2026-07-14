# -*- coding: utf-8 -*-
"""Module contains the stimulation factory to create dependencies for a stimulation factory.

Collected dependencies amount: 10

### Required dependencies for testset ###

enna_kwd_testing.stimulations.apps.settings.SetSystemLanguage
enna_kwd_testing.stimulations.apps.general.NavigateToScreen
enna_kwd_testing.stimulations.vehicle.simulation.SwitchClamp15
enna_kwd_testing.stimulations.apps.general.ClickOnElement
enna_kwd_testing.stimulations.apps.privacy.SetMobileData
enna_kwd_testing.stimulations.apps.general.CheckScreenIsVisible
enna_kwd_testing.stimulations.apps.general.ClickElementInList
enna_kwd_testing.stimulations.vehicle.simulation.SwitchClampS
enna_kwd_testing.stimulations.actions.basic.times.WaitTimeInMs
enna_kwd_testing.stimulations.actions.android_hmi.no_interaction.NoInteraction

Generation date: 2026-02-19 09:45:03.845754
"""

import enna.core.component_system.decorators
import enna_st12.instance_names
import enna_kwd_testing.utilities.testset.loader
import enna_kwd_testing.factories.testcasefactory

@enna.core.component_system.decorators.RequireComponent("enna.core.reporting")
@enna.core.component_system.decorators.RequireComponent("enna.data_interfaces.adb")
@enna.core.component_system.decorators.RequireComponent("enna_st12.data_interfaces.android_hmi", instance_name=enna_st12.instance_names.AndroidHMI.CENTER)
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.actions.android_hmi.no_interaction.NoInteraction", arg_name="enna_kwd_testing.stimulations.actions.android_hmi.no_interaction.NoInteraction")  # noqa # pylint: disable=line-too-long
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.actions.basic.times.WaitTimeInMs", arg_name="enna_kwd_testing.stimulations.actions.basic.times.WaitTimeInMs")  # noqa # pylint: disable=line-too-long
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.general.CheckScreenIsVisible", arg_name="enna_kwd_testing.stimulations.apps.general.CheckScreenIsVisible")  # noqa # pylint: disable=line-too-long
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.general.ClickElementInList", arg_name="enna_kwd_testing.stimulations.apps.general.ClickElementInList")  # noqa # pylint: disable=line-too-long
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.general.ClickOnElement", arg_name="enna_kwd_testing.stimulations.apps.general.ClickOnElement")  # noqa # pylint: disable=line-too-long
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.general.NavigateToScreen", arg_name="enna_kwd_testing.stimulations.apps.general.NavigateToScreen")  # noqa # pylint: disable=line-too-long
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.privacy.SetMobileData", arg_name="enna_kwd_testing.stimulations.apps.privacy.SetMobileData")  # noqa # pylint: disable=line-too-long
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.apps.settings.SetSystemLanguage", arg_name="enna_kwd_testing.stimulations.apps.settings.SetSystemLanguage")  # noqa # pylint: disable=line-too-long
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.vehicle.simulation.SwitchClamp15", arg_name="enna_kwd_testing.stimulations.vehicle.simulation.SwitchClamp15")  # noqa # pylint: disable=line-too-long
@enna.core.component_system.decorators.RequireStimulation("enna_kwd_testing.stimulations.vehicle.simulation.SwitchClampS", arg_name="enna_kwd_testing.stimulations.vehicle.simulation.SwitchClampS")  # noqa # pylint: disable=line-too-long
class DependencyFactory(enna_kwd_testing.factories.testcasefactory.TestcaseFactory):
    """Contains class responsible to initialize all components and requirements when initializing factory object."""

    def __init__(self, reporting, adb=None, android_hmi=None, testset_input_folder=None, *args, **kwargs):
        """Initialize dependency generator object.

        :param enna.core.reporting.interface.Interface reporting: instance of reporting interface
        :param enna.data_interfaces.adb.interface.Interface adb: instance of interface to Android Debug Bridge
        :param enna_st12.data_interfaces.android_hmi.interface.Interface android_hmi: instance of uiautomator
        :param testset_input_folder: folder where testset input is delivered from
        :type testset_input_folder: str | pathlib.Path
        :param args: positional arguments
        :param kwargs: keyword arguments
        """
        test_spec_list = enna_kwd_testing.utilities.testset.loader.load_testset_from_files(testset_input_folder)
        super().__init__(reporting, adb, android_hmi, test_spec_list, **kwargs)
