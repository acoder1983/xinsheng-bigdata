# -*- coding:utf-8 -*-
import re
import sys
sys.path.insert(0, '..')
from items import Topic
from items import Member
from bs4 import BeautifulSoup


class TopicPage(object):

    def __init__(self, responseBody):
        self.body = responseBody
        self.soup = BeautifulSoup(responseBody, "html5lib")

    def getTopic(self):
        topic = Topic()
        topic['title'] = self.soup.title.string.encode('utf-8')

        users = self.soup.find_all('div', 'bbs_info_user', limit=1)
        users = users[0].find_all('a')
        topic['author'] = Member()
        topic['author']['name'] = users[1]['title'].encode('utf-8')
        return topic
