# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
 
class MyCrawlerItem(scrapy.Item):
    title = scrapy.Field()    # 文章标题
    url = scrapy.Field()      # 文章地址
    summary = scrapy.Field()  # 文章摘要
    create_time = scrapy.Field()
