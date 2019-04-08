# -*- coding: utf-8 -*-
import scrapy
from suning.items import SuningItem

class SnbookSpider(scrapy.Spider):
    name = 'snbook'
    allowed_domains = ['www.suning.com']
    start_urls = ['http://book.suning.com/']

    def parse(self, response):

        menu_book = response.xpath("//div[@class = 'menu-item']")
        print(len(menu_book))
        for i in range(10):
        #for tmp in menu_book:
            item = SuningItem()
            item["main_dir"] = menu_book[i].xpath(".//h3/a/text()").extract_first()
            print(item)

