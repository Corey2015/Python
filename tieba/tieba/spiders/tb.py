# -*- coding: utf-8 -*-
import scrapy


class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E6%99%92%E5%9B%BE&ie=utf-8']

    def parse(self, response):
        url_list = response.xpath(".//a[@class='j_th_tit ']/@href").extract()
        title_list = response.xpath(".//a[@class='j_th_tit ']/@title").extract()
        print(title_list)
        print(url_list)
