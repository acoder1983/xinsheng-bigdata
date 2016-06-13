# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup


class TopicPage(object):

    def __init__(self, responseBody):
        self.body = responseBody
        self.soup = BeautifulSoup(responseBody, "html5lib")

    def getTitle(self):
        return self.soup.title.string.encode('utf-8')
