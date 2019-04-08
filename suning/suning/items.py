# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SuningItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    main_dir = scrapy.Field() #1级目录
    sub_dir = scrapy.Field() #2级目录
    thrid_dir = scrapy.Field()#3级目录
    dir_url = scrapy.Field() #目录地址
    book_url = scrapy.Field() #书籍地址

    pass
