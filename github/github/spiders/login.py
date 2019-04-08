# -*- coding: utf-8 -*-
import scrapy
import re

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['github.com/']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        print("-" *20)
        authenticity_token = response.xpath("//input[@name = 'authenticity_token']/@value").extract_first()
        utf8 = response.xpath("//input[@name = 'utf8']/@value").extract_first()
        print(utf8)
        print(authenticity_token)
        post_data = dict(
            login="xudong.l@163.com",
            password="virus1981",
            authenticity_token=authenticity_token,
            utf8=utf8,
            commit="Sign in"
        )
        yield scrapy.FormRequest(
            "https://github.com/session",
            formdata=post_data,
            callback = self.after_login,
            dont_filter=True

        )

    def after_login(self,response):
        print("2"*10)
        print(re.findall("Corey",response.body.decode()))
        print(response.status)