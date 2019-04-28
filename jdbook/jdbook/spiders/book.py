# -*- coding: utf-8 -*-
import scrapy
from copy import  deepcopy
import json
import re

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['jd.com','p.3.cn']
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
                    meta={"item":deepcopy(item)}

                )

    def parse_sub(self,response):
        #print("parse_sub is called")
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
            if item["book_sku"] is None:
                item["book_sku"] = re.findall(r"https://item.jd.com/(\d+).html", item["book_url"])[0]
            #     callback=self.parse_getprice,
            #     meta = {"item":deepcopy(item)}
            # )
            yield scrapy.Request(
                item["book_url"],
                callback=self.parse_bookdetail,
                meta={"item": deepcopy(item)}
            )

        next_url = response.xpath(".//a[@class='pn-next']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                "https://list.jd.com{}".format(next_url),
                callback=self.parse_sub,
                meta={"item": item}
            )


    def parse_bookdetail(self,response):
        item = response.meta["item"]
        #//it//*[@id="parameter2"]/li[2]
        li_list = response.xpath(".//ul[@id='parameter2']/li")
        #item["book_ISBN"] = response.xpath(".//ul[@id='parameter2']/li")
        for li in li_list:
            tmp = li.xpath("./text()").extract_first()
            if tmp.startswith("ISBN："):
                item["book_ISBN"] = tmp[5:]
                #print(item["book_ISBN"])
        yield scrapy.Request(
            "https://p.3.cn/prices/mgets?skuIds=J_{}".format(item["book_sku"]),
            callback=self.parse_getprice,
            meta = {"item":deepcopy(item)}
        )


        #print(li_list)

    #https://p.3.cn/prices/mgets?callback=jQuery4600978&skuIds=J_12090377
    def parse_getprice(self,response):
        item = response.meta["item"]
        item["jprice"] = json.loads(response.body.decode())[0]["op"]
        item["oprice"] = json.loads(response.body.decode())[0]["m"]
        yield item
