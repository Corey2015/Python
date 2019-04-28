# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl
import os
#{'jprice': '31.00', 'book_pub_data': '2015-07', 'book_author': ' 付遥 ',
# 'subline': '职场', 'suburl': 'https://list.jd.com/1713-3258-3314.html',
# 'book_pub': '中信出版社', 'headline': '小说', 'book_name': '创业时代', 'book_ISBN': '9787508651460',
# 'book_url': 'https://item.jd.com/11722424.html', 'book_sku': '11722424', 'oprice': '39.80'}
class JdbookPipeline(object):
    filepath = r"./jdbook.xlsx"

    def isFileExists(self):

        return os.path.exists(self.filepath)

    def parse_item(self,item):
        li = list(item)
        if not self.isFileExists():
            print("xlsx file is not exist")
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "jdBook"
            ws.append(sorted(li))
            print(sorted(li))
            wb.save(self.filepath)

        wb =openpyxl.load_workbook(self.filepath)
        ws = wb['jdBook']
        additem = []
        for each in sorted(li):
            additem.append(item[each])
        ws.append(additem)
        wb.save(self.filepath)


    def process_item(self, item, spider):
        self.parse_item(item)
        print(item)
        return item
