# -*- coding:utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request, FormRequest


class JiashiSpider(scrapy.Spider):
    name = "xinsheng"
    allowed_domains = ["xinsheng.huawei.com"]
    start_urls = [
        "http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=461&p=3553"]

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=461&p=3553"
    }

    #重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        return [Request("https://uniportal.huawei.com/uniportal/", meta={'testcookie': 1}, callback=self.post_login)]

    # FormRequeset出问题了
    def post_login(self, response):
        print 'Preparing login'
        #下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        #登陆成功后, 会调用after_login回调函数
        return [FormRequest.from_response(response,
                                          headers=self.headers,  # 注意此处的headers
                                          formdata={
                                              'uid': 'c00344060',
                                              'password': 'Giszorro@1983'
                                          },
                                          callback=self.after_login,
                                          dont_filter=True
                                          )]

    def after_login(self, response):
        print "after_login"
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        print 'parse'
        # problem = Selector(response)
        # item = ZhihuItem()
        # item['url'] = response.url
        # item['name'] = problem.xpath('//span[@class="name"]/text()').extract()
        # print item['name']
        # item['title'] = problem.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        # item['description'] = problem.xpath('//div[@class="zm-editable-content"]/text()').extract()
        # item['answer']= problem.xpath('//div[@class=" zm-editable-content clearfix"]/text()').extract()
        # return item
        page = new TopicListPage(response.body)
        topicUrls = page.getTopicUrls()
        for url in topicUrls:
            yield scrapy.Request(url, callback=parse_topic)
        nextPageUrl = page.getNextPageUrl()
        yield scrapy.Request(nextPageUrl, callback=parse)

    def parse_topic(self, response):
