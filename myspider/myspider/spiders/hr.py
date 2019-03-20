# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem

class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php/']

    def parse(self, response):
        tr_list = response.xpath("//table[@class = 'tablelist']/tr")

        for tr in tr_list[1:-1]:
            item = MyspiderItem()
            item["position"] = tr.xpath(".//a/text()").extract_first()
            item["location"] = tr.xpath(".//td[4]/text()").extract_first()
            item["data"] = tr.xpath(".//td[5]/text()").extract_first()
            yield item
        next_url = tr_list.xpath(".//a[@id = 'next']/@href").extract_first()

        if next_url != "javascript:;":
            next_url = "https://hr.tencent.com/{}".format(next_url)
            yield scrapy.Request(
                next_url,
                callback= self.parse,
            )
