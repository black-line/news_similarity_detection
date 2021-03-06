# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    news_url = scrapy.Field()
    raw_html = scrapy.Field()
    title = scrapy.Field()
    cleaned_text = scrapy.Field()
    tags = scrapy.Field()
    simhash = scrapy.Field()

