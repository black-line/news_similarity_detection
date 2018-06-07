# -*- coding: utf-8 -*-

import scrapy
from news_spider.items import NewsSpiderItem
import logging
from goose3 import Goose
from goose3.configuration import Configuration
from goose3.text import StopWordsChinese
import jieba.analyse
from exceptUI import MySimHash

logger = logging.getLogger('news_spider_logger')


class NewsSpider(scrapy.Spider):
    name = "news_spider"

    kw="友谊勋章"

    def start_requests(self):
        urls = [
            'http://news.baidu.com/ns?word={0}&pn=0&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0'.format(self.kw)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url)

    def parse_url(self, response):
        for url in response.xpath('//h3[@class="c-title"]/a/@href').extract():
            yield scrapy.Request(url=url, callback=self.parse_raw_html)

        next_page = response.xpath('//a[@class="n"]/@href').extract()
        if next_page is not None:
            if 'pn=20' not in next_page[-1]:
                next_page = response.urljoin(next_page[-1])
                yield scrapy.Request(next_page, callback=self.parse_url)

    def parse_raw_html(self, response):
        item = NewsSpiderItem()
        item['news_url'] = response.url
        # try:
        #     chatset = response.encoding
        #     body = response.body.decode(chatset, errors='ignore')
        #     item['raw_html'] = body
        # except UnicodeDecodeError as e:
        #     logger.error(e)
        #     item['raw_html'] = None
        item['raw_html'] = response.body

        try:
            g = Goose({'stopwords_class': StopWordsChinese})

            extr = g.extract(raw_html=item['raw_html'])
            cleaned_text =extr.cleaned_text
            title = extr.title

            if cleaned_text:
                title_pair = jieba.analyse.extract_tags(title, topK=20, withWeight=True)
                cleaned_text_pair = jieba.analyse.extract_tags(cleaned_text, topK=20, withWeight=True)
                title_pair_list = [[k[0], k[1]] for k in title_pair]
                cleaned_text_pair_list = [[k[0], k[1]] for k in cleaned_text_pair]
                for ti_va in title_pair_list:
                    flag = True
                    for te_va in cleaned_text_pair_list:
                        if ti_va[0] == te_va[0]:
                            te_va[1] += ti_va[1] * 0.5
                            flag = False
                    if flag:
                        cleaned_text_pair_list.append(ti_va)
                cleaned_text_pair_list.sort(key=self.takeSecond,reverse=True)
                simhash = MySimHash().get_simhash(cleaned_text_pair_list[:20])
                item['title']=title
                item['simhash'] = str(simhash)
                item['cleaned_text'] = cleaned_text
                item['tags'] = cleaned_text_pair_list[:20]
                yield item
            else:
                pass
        except UnicodeDecodeError as e:
            logger.error("Something unexpected happened")


    def takeSecond(self, elem):
        return elem[1]
