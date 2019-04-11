# -*- coding: utf-8 -*-
import scrapy
import re

class Login2Spider(scrapy.Spider):
    name = 'login2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login/']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response, #自动从response里找from表单
            formdata={"login":"xudong.l@163.com","password":"virus1981"},
            callback = self.parse_detile
        )

    def parse_detile(self,response):
        print(re.findall("Corey", response.body.decode()))

