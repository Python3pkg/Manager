#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**component.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines the :class:`Component` class.

**Others:**

"""



import foundations.exceptions
import foundations.verbose

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER", "Component"]

LOGGER = foundations.verbose.install_logger()


class Component(object):
    """
    Defines the base class for **Manager** package Components.
    """

    def __init__(self, name=None):
        """
        Initializes the class.

        :param name: Component name.
        :type name: unicode
        """

        LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

        # --- Setting class attributes. ---
        self.__name = None
        self.name = name

        self.__activated = False
        self.__initialized = False
        self.__deactivatable = True

    @property
    def name(self):
        """
        Property for **self.__name** attribute.

        :return: self.__name.
        :rtype: unicode
        """

        return self.__name

    @name.setter
    @foundations.exceptions.handle_exceptions(AssertionError)
    def name(self, value):
        """
        Setter for **self.__name** attribute.

        :param value: Attribute value.
        :type value: unicode
        """

        if value is not None:
            assert type(value) is str, "'{0}' attribute: '{1}' type is not 'unicode'!".format("name", value)
        self.__name = value

    @name.deleter
    @foundations.exceptions.handle_exceptions(foundations.exceptions.ProgrammingError)
    def name(self):
        """
        Deleter for **self.__name** attribute.
        """

        raise foundations.exceptions.ProgrammingError(
            "{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "name"))

    @property
    def activated(self):
        """
        Property for **self.__activated** attribute.

        :return: self.__activated.
        :rtype: bool
        """

        return self.__activated

    @activated.setter
    @foundations.exceptions.handle_exceptions(AssertionError)
    def activated(self, value):
        """
        Setter for **self.__activated** attribute.

        :param value: Attribute value.
        :type value: bool
        """

        if value is not None:
            assert type(value) is bool, "'{0}' attribute: '{1}' type is not 'bool'!".format("activated", value)
        self.__activated = value

    @activated.deleter
    @foundations.exceptions.handle_exceptions(foundations.exceptions.ProgrammingError)
    def activated(self):
        """
        Deleter for **self.__activated** attribute.
        """

        raise foundations.exceptions.ProgrammingError(
            "{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "activated"))

    @property
    def initialized(self):
        """
        Property for **self.__initialized** attribute.

        :return: self.__initialized.
        :rtype: bool
        """

        return self.__initialized

    @initialized.setter
    @foundations.exceptions.handle_exceptions(AssertionError)
    def initialized(self, value):
        """
        Setter for **self.__initialized** attribute.

        :param value: Attribute value.
        :type value: bool
        """

        if value is not None:
            assert type(value) is bool, "'{0}' attribute: '{1}' type is not 'bool'!".format("initialized", value)
        self.__initialized = value

    @initialized.deleter
    @foundations.exceptions.handle_exceptions(foundations.exceptions.ProgrammingError)
    def initialized(self):
        """
        Deleter for **self.__initialized** attribute.
        """

        raise foundations.exceptions.ProgrammingError(
            "{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "initialized"))

    @property
    def deactivatable(self):
        """
        Property for **self.__deactivatable** attribute.

        :return: self.__deactivatable.
        :rtype: bool
        """

        return self.__deactivatable

    @deactivatable.setter
    @foundations.exceptions.handle_exceptions(AssertionError)
    def deactivatable(self, value):
        """
        Setter for **self.__deactivatable** attribute.

        :param value: Attribute value.
        :type value: bool
        """

        if value is not None:
            assert type(value) is bool, "'{0}' attribute: '{1}' type is not 'bool'!".format("deactivatable", value)
        self.__deactivatable = value

    @deactivatable.deleter
    @foundations.exceptions.handle_exceptions(foundations.exceptions.ProgrammingError)
    def deactivatable(self):
        """
        Deleter for **self.__deactivatable** attribute.
        """

        raise foundations.exceptions.ProgrammingError(
            "{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "deactivatable"))

    @foundations.exceptions.handle_exceptions(NotImplementedError)
    def activate(self):
        """
        Sets Component activation state.

        :return: Method success.
        :rtype: bool
        """

        raise NotImplementedError("{0} | '{1}' must be implemented by '{2}' subclasses!".format(
            self.__class__.__name__, self.activate.__name__, self.__class__.__name__))

    @foundations.exceptions.handle_exceptions(NotImplementedError)
    def deactivate(self):
        """
        Unsets Component activation state.

        :return: Method success.
        :rtype: bool
        """

        raise NotImplementedError("{0} | '{1}' must be implemented by '{2}' subclasses!".format(
            self.__class__.__name__, self.deactivate.__name__, self.__class__.__name__))

    @foundations.exceptions.handle_exceptions(NotImplementedError)
    def initialize(self):
        """
        Initializes the Component.
        """

        raise NotImplementedError("{0} | '{1}' must be implemented by '{2}' subclasses!".format(
            self.__class__.__name__, self.deactivate.__name__, self.__class__.__name__))

    @foundations.exceptions.handle_exceptions(NotImplementedError)
    def uninitialize(self):
        """
        Uninitializes the Component.
        """

        raise NotImplementedError("{0} | '{1}' must be implemented by '{2}' subclasses!".format(
            self.__class__.__name__, self.deactivate.__name__, self.__class__.__name__))
