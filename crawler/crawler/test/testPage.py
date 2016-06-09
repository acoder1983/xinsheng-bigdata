import unittest
import sys
sys.path.insert(0, '../pages')
from topicListPage import TopicListPage

class TestPage(unittest.TestCase):

    def testTopicListPage(self):
        f=open('data/topic-list1.html')
        body=f.read()
        page=TopicListPage(body)
        self.assertEqual([], page.getTopicUrls())
