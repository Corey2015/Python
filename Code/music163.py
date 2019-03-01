# -*- coding: utf-8
import requests
from lxml import etree
from Python.Code.Spider import *
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
    cookies = {"Cookie":" _iuqxldmzr_=32; _ntes_nnid=f0c02ce15521a131449503f90f81bc8f,1551281520321; _ntes_nuid=f0c02ce15521a131449503f90f81bc8f; WM_TID=KQz3rYb5PMFFUFUUQFY9hxjvhiLERfIH; WM_NI=Q0OsmPAow5AjB2Oj7lzf6nAFJJHbK3jhovv6K%2B%2FBDstMRY7cH0eh%2BISWlo%2BGlKuRp42JXHYY6vSsRiJxMK%2BfLsxeSZc3vkmaYKh76wQFAVkO3%2BS2JO5EPGRHWowu4vryNVE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb2bc3d8eb6a782b66ea3ef8fb3c15b879f8b85b83ba5b0ff89e4628eb29cbbee2af0fea7c3b92a93f08194f05c83b1b9d6c46282ee818bb668babafa8fc44e8a968883ca39aab8a197f53e89f5e1a3c779b8939ebab6698cf0ab89aa439189a490aa4db095bbb3f340f29698a9dc53f6aa9d94d1638aa883acaa6e90adb886d252a1edba8cf06b9b95a8d8b57d939a8fb7ea45f1f59dd3c945f79ba0a8d14495b1b996b77eb2a782b7c837e2a3; JSESSIONID-WYYY=PH48dwYWD3IjEoZDCf%2Fn01nSrXC%2FqDQBNnqqtrxUd%5CctC1i56QOlbNaMaeOBefHa6ZDK6yaWsAEvoyllZrUBqJB4%5CTksijBm0iqi1ciQOQ1EZ4kFeYl7MHwJFJC5zvqlI6cYTKDCS%2FzkSP8UQ4%2BIB4t3cyR2T3i4EGMp1z4A%2Fb%5C%5CuGaF%3A1551367217295"}
    headers = {"Host": "music.163.com",
               "Referer": " https://music.163.com/",
               "User-Agent": " Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
    spider = SpiderMusic("https://music.163.com/#/discover/playlist/?order=hot&limit=35&offset=70")
    print(spider.url)
    html_str = spider.parse_url(cookies=cookies)
    spider.save_file("./text.html",html_str)
    xml_str = etree.HTML(html_str)
    print(etree.tostring(xml_str).decode())
    music_list = xml_str.xpath("//ul[@id ='m-pl-container']/li")
    # tmp_url = xml_str.xpath("//a[@class = 'zbtn znxt']/@href")[0]# if len(xml_str.xpath("//a[@class = 'zbtn znxt']/@href"))>0 else None
    # print(tmp_url)
    # next_url = "https://music.163.com/#{}".format(tmp_url) if tmp_url is not None else None
    # print(next_url)
    # spider.set_url(next_url)
    # print(music_list)
    music_list_url = []
    for tmp in music_list:
        print(tmp.xpath("./p[@class = 'dec']/a/@title"))
        # https://music.163.com/#/playlist?id=616305725
        print(tmp.xpath("./p[@class = 'dec']/a/@href"))
        print(tmp.xpath(".//a[@class ='nm nm-icn f-thide s-fc3' ]/text()"))
        print("https://music.163.com/#{}".format(tmp.xpath("./p[@class = 'dec']/a/@href")[0]))
        music_list_url.append("https://music.163.com/#{}".format(tmp.xpath("./p[@class = 'dec']/a/@href")[0]))
        print(tmp.xpath(".//a[@class ='nm nm-icn f-thide s-fc3' ]/text()"))
    # print(music_list_url)
    # print(next_url)
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
