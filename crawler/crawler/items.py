# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TopicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    author=scrapy.Field()
    date=scrapy.Field()
    reads=scrapy.Field()
    forum=scrapy.Field()

class Member:
	name=scrapy.Field()
	link=scrapy.Field()
