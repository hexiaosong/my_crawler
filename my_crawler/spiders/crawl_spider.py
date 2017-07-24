# -*- coding: utf-8 -*-

import datetime
from bson import json_util
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from my_crawler.items import MyCrawlerItem


class MyCrawlSpider(CrawlSpider):
    name = 'my_crawler'               # Spider名，必须唯一，执行爬虫命令时使用
    allowed_domains = ['bjhee.com']   # 限定允许爬的域名，可设置多个
    start_urls = [
        "http://www.bjhee.com",       # 种子URL，可设置多个
    ]
 
    rules = (    # 对应特定URL，设置解析函数，可设置多个
        Rule(LinkExtractor(allow=r'/page/[0-9]+'),  # 指定允许继续爬取的URL格式，支持正则
                           callback='parse_item',   # 用于解析网页的回调函数名
                           follow=True
        ),
    )

    @staticmethod
    def jprint(d):
        s = json_util.dumps(d, ensure_ascii=False, indent=4)
        print s
        return s

    def parse_item(self, response):
        # 通过XPath获取Dom元素
        articles = response.xpath('//main[@class="site-main"]/article')
 
        for article in articles:
            d = {}
            d['title'] = article.css('header.entry-header h2 a::text').extract_first()
            d['url'] = article.css('header.entry-header h2 a::attr(href)').extract_first()
            d['summary'] = article.css('div.entry-content p::text').extract_first()
            d['create_time'] = datetime.datetime.now()
            item = MyCrawlerItem(**d)
            self.jprint(d)
            yield item