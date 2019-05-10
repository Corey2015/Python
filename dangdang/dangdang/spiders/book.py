# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider


class BookSpider(RedisSpider):
    name = 'book'
    #手动指定 allow domains
    allowed_domains = ['dangdang.com']
    #启动的时候只需要往对应的键中存入start url地址
    #1.scrapy crawl book 启动爬虫
    #2.在redis输入lpush dangdang "http://book.dangdang.com/" 爬虫自动从该地址进行爬取
    redis_key = 'dangdang'

    def parse(self, response):
        pass
