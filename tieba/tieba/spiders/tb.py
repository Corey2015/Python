# -*- coding: utf-8 -*-
import scrapy


class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E6%99%92%E5%9B%BE&ie=utf-8']

    def parse(self, response):
        url_list = response.xpath(".//a[@class='j_th_tit ']/@href").extract()

        #获取每个帖子的地址
        for i in range(len(url_list)):
            url_list[i] ="https://tieba.baidu.com{}".format(url_list[i])
            yield scrapy.Request(
                url_list[i],
                callback=self.parse_imgaddress
            )
        #获取下一页的地址
        next_url = response.xpath(".//a[@class = 'next pagination-item ']/@href").extract_first()
        print(next_url)
        if next_url is not None:
            yield scrapy.Request(
                "https:"+next_url,
                callback=self.parse
            )

    #抓取贴吧的每个帖子的第1页里的img地址
    def parse_imgaddress(self,response):
        imglist = response.xpath(".//img[@class = 'BDE_Image']/@src").extract()
        for i in range(len(imglist)):
            yield  scrapy.Request(
                imglist[i],
                self.parse_getimage
            )

    #根据img地址保存图片
    def parse_getimage(self,response):
        filename = response.url.split("/")[-1]
        #print(filename)
        with open("./tmp/"+filename,"wb") as f:
            f.write(response.body)
