# -*- coding:utf-8 -*-
import unittest

from testItem import TestItem
from testPage import TestTopicListPage
from testPage import TestTopicPage

if __name__ == '__main__':
    suite = unittest.TestSuite()
    for test_class in (TestItem, TestTopicListPage, TestTopicPage):
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    unittest.TextTestRunner().run(suite)
