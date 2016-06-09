# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TopicItem(scrapy.Item):
    # define the fields for your item here like:
    title=scrapy.Field()
    author=scrapy.Field()
    date=scrapy.Field()
    content=scrapy.Field()
    reads=scrapy.Field()
    forum=scrapy.Field()
    replies=scrapy.Field()


class Member:
    def __init__(self):
        name=None
        link=None

class Reply:
    def __init__(self):
        author=Member()
        content=None


