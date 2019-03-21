# -*- coding: utf-8 -*-
import scrapy
from ygspider.items import YgspiderItem
import  logging

logger  = logging.getLogger(__name__)

class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        tr_list = response.xpath("//div[@class ='greyframe']/table[2]/tr/td/table/tr")
        next_url = response.xpath("//a[text() = '>']/@href").extract_first()

        for tr in tr_list:
            item = YgspiderItem()
            item["title"] = tr.xpath("./td[2]/a[@class = 'news14']/text()").extract_first()
            item["url"] = tr.xpath("./td[2]/a[@class = 'news14']/@href").extract_first()
            item["location"] = tr.xpath("./td[2]/a[@class = 't12h']/text()").extract_first()
            item["status"] = tr.xpath("./td[3]/span/text()").extract_first()
            item["data"] = tr.xpath(".//td[@class = 't12wh']/text()").extract_first()

            #logger.warning(item)
            #logger.warning(item["url"])
            yield scrapy.Request(
                item["url"],
                callback=self.parse_detail,
                meta={"item": item}

            )
            # yield item
        logger.warning(next_url)
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    def parse_detail(self,response):
        #print("parse_detail is called")
        item = response.meta["item"]
        item["content"] = response.xpath("//td[@class='txt16_3']/text()").extract()
        #logger.warning(item)
        yield item

