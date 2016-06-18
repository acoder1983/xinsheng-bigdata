# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup


class TopicListPage(object):

    def __init__(self, responseBody):
        self.body = responseBody
        self.soup = BeautifulSoup(responseBody, "html5lib")

    def getTopicUrls(self):
        urls = []
        for link in self.soup.find_all('a'):
            if link.has_attr('href'):
                if link['href'].startswith('http://xinsheng.huawei.com/cn/index.php?app=forum&mod=Detail&act=index&id='):
                    urls.append(link['href'])
        return urls

    def getNextPageUrl(self):
        key = "changeToPage"
        try:
            p = self.body.index(key)
            key = "href=\""
            beg = self.body.index(key, p)
            beg += len(key)
            key = "\">"
            end = self.body.index(key, beg)
            url = "http://xinsheng.huawei.com" + self.body[beg:end]
            return url.replace("amp;", "")
        except Exception, e:
            print e
            return None
