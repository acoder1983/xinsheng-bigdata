# -*- coding:utf-8 -*-
import re
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

    def testGetTopic1(self):
        f = open('data/topic1-1.html')
        self.body = f.read()
        page = TopicPage(self.body)
        topic = page.getTopic()

        self.assertEqual("【枪林弹雨中成长】系列故事汇总贴，最新上映：《沸腾的战场》", topic['title'])

        self.assertEqual("华为家事", topic['author']['name'])
        self.assertEqual(
            "http://xinsheng.huawei.com/cn/index.php?app=space&mod=Index&act=view&maskId=115", topic['author']['url'])

        self.assertEqual("2015-12-10 09:30", topic['time'])

        self.assertEqual("51685", topic['reads'])

    def testGetTopic2(self):
        f = open('data/topic2-1.html')
        self.body = f.read()
        page = TopicPage(self.body)
        topic = page.getTopic()

        self.assertEqual("海外常驻，老婆在家，两地分居，怎么办？", topic['title'])

        self.assertEqual("用心生活", topic['author']['name'])
        self.assertEqual("javascript:void(0);", topic['author']['url'])

        self.assertEqual("2008-07-02 12:42", topic['time'])

        self.assertEqual("6471", topic['reads'])

    def testSearchTime(self):
        actual = TopicPage.extractTime(
            '\xa0\u4e8e 2008-07-02 12:42\xa0\u53d1\u8868')
        self.assertEqual('2008-07-02 12:42', actual)

    def testRemoveAllBras(self):
        actual = TopicPage.removeAllBras(
            '<div>abc <span>123</span>\n<div>')
        self.assertEqual('abc 123\n', actual)
