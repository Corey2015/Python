# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list=response.xpath(".//div[@class='mc']/dl/dt")
        for dt in dt_list:
            item ={}
            item['headline'] = dt.xpath("./a/text()").extract_first()
            em_list = dt.xpath("./following-sibling::dd[1]/em")
            for em in em_list:
                item["subline"] = em.xpath("./a/text()").extract_first()
                item["suburl"] = "https:{}".format(em.xpath("./a/@href").extract_first())
                #print(item)
                yield scrapy.Request(
                    item["suburl"],
                    callback=self.parse_sub,
                    meta={"item":item}

                )

    def parse_sub(self,response):
        print("parse_sub is called")
        item = response.meta["item"]
        li_list  = response.xpath(".//li[@class = 'gl-item']")
        for li in li_list:
            item["book_name"] = li.xpath(".//div[@class='p-name']/a/em/text()").extract_first().strip()
            item["book_sku"] =li.xpath("./div/@data-sku").extract_first()
            item["book_author"] = li.xpath(".//div[@class = 'p-bookdetails']/span/span/a/text()").extract_first()
            if item["book_author"] is None:
                item["book_author"] = "no more information"
            item["book_pub"] =li.xpath(".//div[@class = 'p-bookdetails']/span[@class = 'p-bi-store']/a/text()").extract_first()
            if item["book_pub"] is None:
                item["book_pub"] = "no more information"
            item["book_pub_data"]=li.xpath(".//div[@class = 'p-bookdetails']/span[@class = 'p-bi-date']/text()").extract_first().strip()
            item["book_url"]= "https:{}".format(li.xpath(".//div[@class='p-img']/a/@href").extract_first())
            print(item)
