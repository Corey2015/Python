# -*- coding: utf-8
import requests
from lxml import etree
from Code.Spider import *
import threading
from queue import Queue
import time

class SpiderMusic(Spider):
    def __init__(self, url):
        self.base_url = ""
        super().__init__(url)

    def get_url_list(self):
        pass


def main():
    # spider = SpiderMusic("https://music.163.com/discover/playlist")

    spider = SpiderMusic("https://music.163.com/#/discover/playlist/?order=hot&limit=35&offset=70")
    print(spider.url)
    html_str = spider.parse_url()
    xml_str = etree.HTML(html_str)
    print(etree.tostring(xml_str).decode())
    music_list = xml_str.xpath("//ul[@id ='m-pl-container']/li")
    #tmp_url = xml_str.xpath("//a[@class = 'zbtn znxt']/@href")[0]# if len(xml_str.xpath("//a[@class = 'zbtn znxt']/@href"))>0 else None
    #print(tmp_url)
    #next_url = "https://music.163.com/#{}".format(tmp_url) if tmp_url is not None else None
    #print(next_url)
    #spider.set_url(next_url)
    # print(music_list)
    music_list_url =[]
    for tmp in music_list:
        print(tmp.xpath("./p[@class = 'dec']/a/@title"))
        print("https://music.163.com/#{}".format(tmp.xpath("./p[@class = 'dec']/a/@href")[0]))
        music_list_url.append("https://music.163.com/#{}".format(tmp.xpath("./p[@class = 'dec']/a/@href")[0]))
        print(tmp.xpath(".//a[@class ='nm nm-icn f-thide s-fc3' ]/text()"))
    #print(music_list_url)
    #print(next_url)
    time.sleep(2)
    html_str = spider.parse_url()
    xml_str = etree.HTML(html_str)
    music_list = xml_str.xpath("//ul[@id ='m-pl-container']/li")
    music_list_url = []
    for tmp in music_list:
        print(tmp.xpath("./p[@class = 'dec']/a/@title"))
        print("https://music.163.com/#{}".format(tmp.xpath("./p[@class = 'dec']/a/@href")[0]))
        music_list_url.append("https://music.163.com/#{}".format(tmp.xpath("./p[@class = 'dec']/a/@href")[0]))
        print(tmp.xpath(".//a[@class ='nm nm-icn f-thide s-fc3' ]/text()"))

if __name__ == "__main__":
    main()
