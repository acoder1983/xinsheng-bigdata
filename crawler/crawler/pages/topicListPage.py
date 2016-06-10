# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

class TopicListPage(object):
	def __init__(self, responseBody):
		self.soup=BeautifulSoup(responseBody,"html5lib")


	def getTopicUrls(self):
		return len(self.soup.find_all('a'))

	def getNextPageUrl(self):
		pass
		