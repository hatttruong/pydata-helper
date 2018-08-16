#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Testcases for text_preprocessing module

"""
import sys
import unittest
import os
import datetime

sys.path.append('../')
from src.configer import Configer
from src import constant


class TestConfigerMethods(unittest.TestCase):

    """
    Test cases for functions of Configer module

    """

    def test_configer(self):
        """Summary
        """
        app_name = 'Sample Name'
        limit = 10000
        threshold = 0.9123
        date_from = datetime.datetime.strptime(
            '2017-10-12 00:00:00', constant.DATETIME_FROMAT)
        is_testing = False
        nb_characters = [3, 4, 5, 6]
        cfg = Configer(os.path.join('test-data', 'setting.ini'))
        self.assertEqual(app_name, cfg.app_name)


if __name__ == '__main__':
    unittest.main()
