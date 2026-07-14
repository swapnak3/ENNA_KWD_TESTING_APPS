# -*- coding: utf-8 -*-
"""Contains arguments parsing of campaign runners ."""
import argparse


def parse_args() -> tuple[str, tuple[str, str, str, str], bool]:
	"""Argument parser to parse the command line interface arguments.

	:return: path of control files, login for TMDB and flag to activate RSI simulation
	"""
	# pylint: disable=line-too-long
	parser = argparse.ArgumentParser(description="Run a keyword driven testing campaign by it´s id")
	parser.add_argument("-tc_path", "--testcycle_path", dest="testcycle_path", metavar="testcycle_path", type=str, help="Test path to the testcycle to run.")
	parser.add_argument("--user_server_access", dest="user_server_access", type=str, help="user to database host", default="")
	parser.add_argument("--password_server_access", dest="password_server_access", type=str, help="password to database host", default="")
	parser.add_argument("--user_database_access", dest="user_database_access", type=str, help="user to login database", default="")
	parser.add_argument("--password_database_access", dest="password_database_access", type=str, help="password to login database", default="")
	parser.add_argument("--usage_rsi_simulation", dest="usage_rsi_simulation", action="store_true", help="on/off switch to usage the RSI simulation", default=False)
	parsed_args = parser.parse_args()
	login = (parsed_args.user_server_access, parsed_args.password_server_access, parsed_args.user_database_access, parsed_args.password_database_access)
	path = parsed_args.testcycle_path
	rsi_simulation = parsed_args.usage_rsi_simulation
	return path, login, rsi_simulation
