# -*- coding:utf-8 -*-
import unittest
import sys
sys.path.insert(0, '../pages')
from topicListPage import TopicListPage
from topicPage import TopicPage
sys.path.insert(0, '..')
from items import Topic


class TestTopicListPage(unittest.TestCase):

    def setUp(self):
        f = open('data/topic-list1.html')
        self.body = f.read()

    def testTopicListPage(self):
        page = TopicListPage(self.body)
        self.assertEqual(91, len(page.getTopicUrls()))

    def testGetNextPageUrl(self):
        page = TopicListPage(self.body)
        nextPage = page.getNextPageUrl()
        self.assertEqual(
            "http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=461&p=2", nextPage)


class TestTopicPage(unittest.TestCase):

    def setUp(self):
        f = open('data/topic1-1.html')
        self.body = f.read()

    def testGetTopic(self):
        page = TopicPage(self.body)
        topic = page.getTopic()

        self.assertEqual("【枪林弹雨中成长】系列故事汇总贴，最新上映：《沸腾的战场》", topic['title'])

        self.assertEqual("华为家事", topic['author']['name'])
