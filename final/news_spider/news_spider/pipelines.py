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


class SQLitePipeline(object):
    def __init__(self):
        # settings = get_project_settings()
        # self.__class__.sqlite_name = settings.get('sqlite_name')
        # self.conn = sqlite3.connect(str(self.__class__.sqlite_name))
        self.conn = sqlite3.connect('sample.db')
    def process_item(self, item, spider):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS news 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    news_url TEXT NOT NULL,
                    raw_html TEXT NOT NULL)""")
            record = (item['news_url'], item['raw_html'])

            cursor.execute('INSERT INTO news VALUES (null, ?, ?)', record)
            self.conn.commit()
        except sqlite3.ProgrammingError as e:
            logger.error('SQLite ERROR: ' + e.message)

    def __del__(self):
        self.conn.close()