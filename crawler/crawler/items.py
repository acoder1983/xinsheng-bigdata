# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Member(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()


class Reply(scrapy.Item):
    author = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()

    def __init__(self):
        scrapy.Item.__init__(self)
        self['author'] = Member()


class Topic(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    reads = scrapy.Field()
    replies = scrapy.Field()

    def __init__(self):
        scrapy.Item.__init__(self)
        self['author'] = Member()
        self['replies'] = []
