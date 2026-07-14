# -*- coding: utf-8 -*-
"""Created on 07.09.2023.

@project: enna_kwd_testing
@author: DYX34ZN: Jakob Kein
"""
from unittest import mock

import enna.core.campaign
import enna.core.campaign_runner
import enna.core.custom_extensions
import enna.core.logger

from enna_kwd_testing.campaigns.alignments.alignment import DEFAULT_ALIGNMENT


# Property 'values' for keyword to test
KEYWORD_STIMULATION_TO_TEST = "enna_kwd_testing.stimulations.apps.audi_assistant.SetAudiAssistantProactiveSoundSignals"
# KEYWORD_STIMULATION_TO_TEST__PROPERTY__VALUES = {"XPATH_NAME": "sound.PRESET_INDIVIDUAL_BUTTON", "LABEL": "de.eso.sound_presets__preset_individual"}
# KEYWORD_STIMULATION_TO_TEST__PROPERTY__VALUES = {"LABEL": "de.eso.phone.connection_mgr__main_menu__bluetooth_settings__text"}
# KEYWORD_STIMULATION_TO_TEST__PROPERTY__VALUES = {"LABEL": "Gering"}
KEYWORD_STIMULATION_TO_TEST__PROPERTY__VALUES = {"STATE": "Speech_and_Sounds"}


def main():
	"""Start keyword stimulation test."""
	enna.core.logger.basic_setup()
	testsuite = enna.core.campaign.Campaign("android_hmi_test_campaign")
	testsuite.add_testgroup("TESTS")

	with mock.patch(f"{KEYWORD_STIMULATION_TO_TEST}.values", new_callable=mock.PropertyMock) as mock_obj:
		mock_obj.return_value = KEYWORD_STIMULATION_TO_TEST__PROPERTY__VALUES
		testsuite.add_testcase(KEYWORD_STIMULATION_TO_TEST)

		enna.core.campaign_runner.start_campaign(testsuite, log_directory_suffix="test_campaign", process_alignments=DEFAULT_ALIGNMENT)


if __name__ == "__main__":
	main()
