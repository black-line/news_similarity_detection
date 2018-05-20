# -*- coding: utf-8 -*-

# read raw_html & (wtite cleaned_text & simhash)

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
from MySimHash import MySimHash


class post_crawl(object):
    def __init__(self):
        self.MONGODB_SERVER = "localhost"
        self.MONGODB_PORT = 27017
        self.MONGODB_DB = "news_spider_40"
        self.MONGODB_COLLECTION = "news"

        client = MongoClient(self.MONGODB_SERVER, self.MONGODB_PORT)
        db = client[self.MONGODB_DB]
        self.coll = db[self.MONGODB_COLLECTION]

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

pc = post_crawl()
tag_rank = pc.get_tag_rank()
with open("ha111h.log", 'w') as f:
    f.write(str(list(tag_rank)))

# first_news = coll.find_one()
#
# scores = []
# for news in coll.find({}):
#     simhash = eval(news['simhash'])
#     score = MySimHash().get_distance(eval(first_news['simhash']), simhash)
#     print('['+str(score)+']')
#     print(first_news['cleaned_text'])
#     print('--------')
#     print(news['cleaned_text'])
#     print('\n\n\n\n\n\n\n')
#     scores.append(score)
#
# scores.sort()
# print(scores)
