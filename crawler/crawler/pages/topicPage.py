# -*- coding:utf-8 -*-
import re
import sys
sys.path.insert(0, '..')
from items import Topic
from items import Member
from items import Reply
from bs4 import BeautifulSoup


class TopicPage(object):

    def __init__(self, responseBody):
        self.body = responseBody
        self.soup = BeautifulSoup(responseBody, "html5lib")

    def getTopic(self):
        topic = Topic()
        topic['title'] = self.soup.title.string.encode('utf-8')

        users = self.soup.find_all('div', 'bbs_info_user', limit=1)[
            0].find_all('a')
        for user in users:
            if user.has_attr('title'):
                topic['author']['name'] = user['title'].encode('utf-8')
                topic['author']['url'] = user['href']
                break

        info = self.soup.find_all('span', 'bbs_info_right_pro fl', limit=1)[0]
        topic['time'] = TopicPage.extractTime(info.text)

        read = info.find_all('span', 'fl', limit=1)[0]
        topic['reads'] = read.text

        content = self.soup.find_all(
            'div', 'bbs_info_right_text breakword ')[0]
        # remove all the <>
        topic['content'] = TopicPage.removeAllBras(str(content))
        return topic

    @classmethod
    def extractTime(cls, text):
        pattern = re.compile(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d')
        match = pattern.search(text)
        return match.group()

    @classmethod
    def removeAllBras(cls, text):
        p = re.compile(r'<[\w\W]*?>')
        while True:
            m = p.search(text)
            if m:
                text = text[0:m.start()] + text[m.end():]
            else:
                return text


class ReplyPage(object):

    def __init__(self, responseBody):
        self.body = responseBody
        self.soup = BeautifulSoup(responseBody, "html5lib")

    def getReplies(self):
        pass
