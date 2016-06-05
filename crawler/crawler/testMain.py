import unittest

from test.testItem import TestItem

if __name__ == '__main__':
    suite = unittest.TestSuite()
    for test_class in (TestItem,):
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    unittest.TextTestRunner().run(suite)