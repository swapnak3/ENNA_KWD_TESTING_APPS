 # -*- coding: utf-8 -*-
"""Created on 07.08.2023.

Contains runner to run a campaign.
"""
import enna_kwd_testing.campaigns.campaign_connect_apps
from enna_kwd_testing.runner._internal import parse_args


def main():
	"""Main function to run a keyword driven campaign with parameters."""
	path, login, _ = parse_args()
	enna_kwd_testing.campaigns.campaign_connect_apps.run(path, login)

if __name__ == "__main__":
	main()
