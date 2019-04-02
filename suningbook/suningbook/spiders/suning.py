# -*- coding: utf-8 -*-
import scrapy


class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['www.suning.com']
    start_urls = ['http://book.suning.com/']

    def parse(self, response):
        pass
