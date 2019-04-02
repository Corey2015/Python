# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class RcSpider(CrawlSpider):
    name = 'rc'
    allowed_domains = ['circ.gov.cn']
    start_urls = ['http://circ.gov.cn/web/site0/tab5240/']

    rules = (
        Rule(LinkExtractor(allow=r'http://circ.gov.cn/web/site0/tab5240/info\w+\.htm'), callback='parse_item'),
    )

    def parse_item(self, response):
        item = {}
        res =re.findall("<!--TitleStart-->(.+)<!--TitleEnd-->",response.body.decode())
        print(res)
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
