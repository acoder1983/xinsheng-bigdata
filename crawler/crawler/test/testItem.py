import unittest
import sys
sys.path.insert(0, '..')
from items import TopicItem


class TestItem(unittest.TestCase):

    def testItem(self):
        item1=TopicItem()
        item1['title']="a"
        item2=TopicItem()
        item2['title']="b"
        self.assertTrue(item1['title'],item2['title'])