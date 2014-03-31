#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**constants.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Defines **Manager** package default constants through the :class:`Constants` class.

**Others:**

"""

#**********************************************************************************************************************
#***	Future imports.
#**********************************************************************************************************************
from __future__ import unicode_literals

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import os
import platform

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
import manager

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["Constants"]

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class Constants():
	"""
	Defines **Manager** package default constants.
	"""

	applicationName = "Manager"
	"""
	:param applicationName: Package Application name.
	:type applicationName: unicode
	"""
	majorVersion = "2"
	"""
	:param majorVersion: Package major version.
	:type majorVersion: unicode
	"""
	minorVersion = "0"
	"""
	:param minorVersion: Package minor version.
	:type minorVersion: unicode
	"""
	changeVersion = "4"
	"""
	:param changeVersion: Package change version.
	:type changeVersion: unicode
	"""
	releaseVersion = ".".join((majorVersion, minorVersion, changeVersion))
	"""
	:param releaseVersion: Package release version.
	:type releaseVersion: unicode
	"""

	logger = "Manager_Logger"
	"""
	:param logger: Package logger name.
	:type logger: unicode
	"""
	verbosityLevel = 3
	"""
	:param verbosityLevel: Default logging verbosity level.
	:type verbosityLevel: int
	"""
	verbosityLabels = ("Critical", "Error", "Warning", "Info", "Debug")
	"""
	:param verbosityLabels: Logging verbosity labels.
	:type verbosityLabels: tuple
	"""
	loggingDefaultFormatter = "Default"
	"""
	:param loggingDefaultFormatter: Default logging formatter name.
	:type loggingDefaultFormatter: unicode
	"""
	loggingSeparators = "*" * 96
	"""
	:param loggingSeparators: Logging separators.
	:type loggingSeparators: unicode
	"""

	defaultCodec = manager.DEFAULT_CODEC
	"""
	:param defaultCodec: Default codec.
	:type defaultCodec: unicode
	"""
	codecError = manager.CODEC_ERROR
	"""
	:param codecError: Default codec error behavior.
	:type codecError: unicode
	"""

	applicationDirectory = os.sep.join(("Manager", ".".join((majorVersion, minorVersion))))
	"""
	:param applicationDirectory: Package Application directory.
	:type applicationDirectory: unicode
	"""
	if platform.system() == "Windows" or platform.system() == "Microsoft" or platform.system() == "Darwin":
		providerDirectory = "HDRLabs"
		"""
		:param providerDirectory: Package provider directory.
		:type providerDirectory: unicode
		"""
	elif platform.system() == "Linux":
		providerDirectory = ".HDRLabs"
		"""
		:param providerDirectory: Package provider directory.
		:type providerDirectory: unicode
		"""

	nullObject = "None"
	"""
	:param nullObject: Default null object string.
	:type nullObject: unicode
	"""
