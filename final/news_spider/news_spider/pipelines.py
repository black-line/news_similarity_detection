# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from pymongo import MongoClient
from scrapy.conf import settings
from scrapy.exceptions import DropItem
import logging

logger = logging.getLogger('news_spider_logger')

class MongoDBPipeline(object):
    def __init__(self):
        self.client = MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        self.db = self.client[settings['MONGODB_DB']]
        self.coll = self.db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid=True
        for data in item:
            if not data:
                valid=False
                logger.error("Missing {0}".format(data))
        if valid:
            self.coll.insert(dict(item))
            logger.debug("news add to MongoDB database")
