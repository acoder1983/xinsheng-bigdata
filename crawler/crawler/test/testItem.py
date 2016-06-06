import unittest
import sys
sys.path.insert(0, '..')
from items import TopicItem
from items import Member

class TestItem(unittest.TestCase):

    def testTopicItem(self):
        item1=TopicItem()
        item1['title']="a"
        item2=TopicItem()
        item2['title']="b"
        self.assertNotEqual(item1['title'],item2['title'])

    def testMember(self):
    	m1=Member()
    	m1.name="a"
    	m2=Member()
    	m2.name="b"
    	self.assertNotEqual(m1.name,m2.name)