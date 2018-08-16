"""
This file aims to load configurations from both setting.ini and
put them into a static class named Configer

"""

import ConfigParser
from distutils.util import strtobool
import datetime
from constant import *


class Singleton(type):

    """Summary
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Summary

        Args:
            *args: Description
            **kwargs: Description

        Returns:
            TYPE: Description
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Configer(object):
    """
    This class will load all parameters from setting.ini

    Attributes:
        app_name (TYPE): Description
        date_from (TYPE): Description
        is_testing (TYPE): Description
        limit (TYPE): Description
        num_characters (TYPE): Description
        setting_file_path (TYPE): Description
        threshold (TYPE): Description

    """
    __metaclass__ = Singleton

    def __init__(self, setting_file_path):
        """
        Init Configer class and load all settings from file

        Args:
            setting_file_path (str): full path to setting file
        """
        self.setting_file_path = setting_file_path

        section_name = 'SectionSample'

        self.app_name = self.load_configuration(section_name, 'AppName')
        self.limit = int(self.load_configuration(section_name, 'Limit'))
        self.threshold = float(
            self.load_configuration(section_name, 'Threshold'))
        self.is_testing = bool(
            strtobool(self.load_configuration(section_name, 'IsTesting')))

        # date type
        self.date_from = None
        date_from_str = self.load_configuration(section_name, 'DateFrom')
        if date_from_str is not None and len(date_from_str) > 0:
            self.date_from = datetime.datetime.strptime(
                date_from_str,
                DATETIME_FROMAT)

        # array of integer
        self.num_characters = [int(s) for s in self.load_configuration(
            section_name, "NumberCharacters").split(',')]

    def load_configuration(self, section, config_name):
        """
        Description: load configuration from setting file using ConfigParser

        Args:
            section (str): name of section in setting file
            config_name (str): name of configuration

        Returns:
            STR: value of configuration

        Raises:
            IOError: Description

        """

        config = ConfigParser.ConfigParser()
        if not config.read(self.setting_file_path):
            raise IOError('cannot load ' + self.setting_file_path)

        return config.get(section, config_name)
