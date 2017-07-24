# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
 
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
 
class MyCrawlerPipeline(object):
    def __init__(self):
        # 设置MongoDB连接
        connection = pymongo.MongoClient(
            host=settings['MONGO_SERVER'],
            port=settings['MONGO_PORT']
        )
        db = connection[settings['MONGO_DB']]
        self.collection = db[settings['MONGO_COLLECTION']]
 
    # 处理每个被抓取的MyCrawlerItem项
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:  # 过滤掉存在空字段的项
                valid = False
                raise DropItem("Missing {0}!".format(data))
 
        if valid:
            # 也可以用self.collection.insert(dict(item))，使用upsert可以防止重复项
            self.collection.update({'url': item['url']}, dict(item), upsert=True)
 
        return item

