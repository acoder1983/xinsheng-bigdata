# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Topic(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    reads = scrapy.Field()
    forum = scrapy.Field()
    replies = scrapy.Field()


class Member(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()


class Reply(scrapy.Item):
    author = scrapy.Field()
    content = scrapy.Field()
