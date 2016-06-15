# -*- coding:utf-8 -*-
import unittest
import sys
sys.path.insert(0, '..')
from items import Topic
from items import Member


class TestItem(unittest.TestCase):

    def testTopicItem(self):
        item1 = Topic()
        item1['title'] = "a"
        item2 = Topic()
        item2['title'] = "b"
        self.assertNotEqual(item1['title'], item2['title'])

        item3 = Topic()
        item3['title'] = "a"
        self.assertEqual(item1, item3)
