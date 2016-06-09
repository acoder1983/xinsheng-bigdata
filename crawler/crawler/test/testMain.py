import unittest

from testItem import TestItem
from testPage import TestPage

if __name__ == '__main__':
    suite = unittest.TestSuite()
    for test_class in (TestItem,TestPage):
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    unittest.TextTestRunner().run(suite)
