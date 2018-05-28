# -*- coding: utf-8 -*-
from goose3 import Goose
from goose3.configuration import Configuration
from goose3.text import StopWordsChinese
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
from goose3 import Goose
from goose3.text import StopWordsChinese
import jieba.analyse
import chardet
import logging
from bson.code import Code
from bson import json_util
logger = logging.getLogger('finalwr_logger')
import hashlib
import mmh3

class MySimHash(object):
    def __init__(self):
        self.f = 32

    def get_simhash(self, pairs):
        s = [0] * self.f
        for p in pairs:
            feature = p[0]
            weight = p[1]
            h = list(bin(mmh3.hash(feature.encode('utf-8'), signed=False))[2:])
            #h = list(bin(int(hashlib.md5(feature.encode('utf-8')).hexdigest(), 16))[2:])
            h = ['0'] * (self.f - len(h)) + h
            for i in range(self.f):
                s[i] += weight * (-1) ** (int(h[i]) + 1)
        for i in range(self.f):
            if s[i] < 0:
                s[i] = 0
            else:
                s[i] = 1
        return s

    def get_distance(self, s1, s2):
        hamdis = []
        for i in range(self.f):
            hamdis.append(s1[i] ^ s2[i])

        # print(hamdis)
        hamdis = hamdis.count(1)
        return hamdis

class myGoose(object):
    def __init__(self, url):
        self.url = url
        self.cleaned_text = None
        self.config = Configuration()
        self.config.browser_user_agent = 'Mozilla 5.0'
        self.config.stopwords_class = StopWordsChinese

    def get_cleaned_text(self):
        with Goose(config=self.config, ) as g:
            article = g.extract(url=self.url)
            self.cleaned_text = article.cleaned_text
            self.title = article.title
        return self.cleaned_text, self.title





class post_crawl(object):
    def __init__(self):
        self.MONGODB_SERVER = "localhost"
        self.MONGODB_PORT = 27017
        self.MONGODB_DB = "news_spider_40"
        self.MONGODB_COLLECTION = "news_xjp_test"

        client = MongoClient(self.MONGODB_SERVER, self.MONGODB_PORT)
        db = client[self.MONGODB_DB]
        self.coll = db[self.MONGODB_COLLECTION]

    def get_title_list(self):
        title_list= []
        for news in self.coll.find({}):
            title_list.append(news['title'])
        return title_list

    def get_text_by_title(self,title):
        if title:
            result = self.coll.find_one({"title": title})
            return result['cleaned_text']

    def get_tag_rank(self):
        # pprint.pprint(coll.find_one())
        # g = Goose({'stopwords_class': StopWordsChinese})
        # for news in self.coll.find({}):
        #     id = news['_id']
        #     raw_html = news['raw_html']
        #     #charset = chardet.detect(raw_html)
        #     #cleaned_text = g.extract(raw_html=raw_html.decode(charset['encoding'])).cleaned_text
        #     cleaned_text = g.extract(raw_html=raw_html).cleaned_text
        #     if cleaned_text:
        #         pair = jieba.analyse.extract_tags(cleaned_text, topK=20, withWeight=True)
        #         simhash = MySimHash().get_simhash(pair)
        #         self.coll.update_one({'_id': id}, {'$set': {'simhash': str(simhash), 'cleaned_text':cleaned_text, 'tags': pair}})
        #     else:
        #         self.coll.remove({'_id': id})


        map = Code("function () {"
                   "  this.tags.forEach(function(z) {"
                   "    emit(z[0], z[1]);"
                   "  });"
                   "}")

        reduce = Code("function (key, values) {"
                      "  var total = 0;"
                      "  for (var i = 0; i < values.length; i++) {"
                      "    total += values[i];"
                      "  }"
                      "  return total;"
                      "}")

        result = self.coll.map_reduce(map, reduce, "myresults").find().sort('value', -1)
        return list(result)

