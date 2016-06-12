import unittest
import sys
sys.path.insert(0, '../pages')
from topicListPage import TopicListPage

class TestPage(unittest.TestCase):

    def setUp(self):
        f=open('data/topic-list1.html')
        self.body=f.read()
        

    def testTopicListPage(self):
        page=TopicListPage(self.body)
        self.assertEqual(91, len(page.getTopicUrls()))

    def testGetNextPageUrl(self):
        page=TopicListPage(self.body)
        nextPage=page.getNextPageUrl()
        self.assertEqual("http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=461&p=2",nextPage)
