# -*- coding: utf-8 -*-
"""Setup file."""
import pathlib

import setuptools

import version

NAME = "enna_kwd_testing"
DESCRIPTION = "ENNA keyword driven testing support for HCP."
AUTHOR = "PSW automotive engineering GmbH"
AUTHOR_EMAIL = ""
CLASSIFIERS = ["Development Status :: 4 - Beta", "Programming Language :: Python :: 3.11"]
PACKAGES = setuptools.find_packages(exclude=["tests*", "ide_tools*"])
LICENSE = "ENNA currently has no license model."

# Version data
PYTHON_REQUIRES = "~=3.13"
VERSION = version.VERSION

ROOT_PATH = pathlib.Path(__file__).resolve().parent
PACKAGE_PATH = ROOT_PATH / NAME

# Read requirements from requirement file
INSTALL_REQUIRES = []
with pathlib.Path("requirements.txt").open(encoding="utf-8") as f:
	LINES = f.readlines()
	for line in LINES:
		INSTALL_REQUIRES.append(line.rstrip())

	setuptools.setup(
		name=NAME,
		version=VERSION,
		description=DESCRIPTION,
		classifiers=CLASSIFIERS,
		packages=PACKAGES,
		install_requires=INSTALL_REQUIRES,
		include_package_data=True,
		python_requires=PYTHON_REQUIRES,
		license=LICENSE
	)
