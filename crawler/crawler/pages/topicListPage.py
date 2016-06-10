# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

class TopicListPage(object):
    def __init__(self, responseBody):
        self.soup=BeautifulSoup(responseBody,"html5lib")


    def getTopicUrls(self):
        n=0
        for link in self.soup.find_all('a'):
            if link.has_attr('href'):
                if link['href'].startswith('http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id='):
                    n+=1
        print n
        return len(self.soup.find_all('a'))

    def getNextPageUrl(self):
        pass
        