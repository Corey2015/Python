# -*- coding: utf-8 -*-
import requests
import json
from  pprint import  pprint

class Spider(object):
    def __init__(self,url = ""):
        self.url = url
        self.header = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"}

    def run(self,proxies = {}):
        print(self.url)
        response = requests.get(self.url,proxies)
        return response.content.decode()


def main():
    proxies = {"http": "http://117.91.255.67:9999", "https": "https://117.91.255.67:9999"}
    url = "http://m.maoyan.com/ajax/movieOnInfoList"
    spider = Spider(url=url)
    json_str = spider.run()
    dict_str = json.loads(json_str)
    #pprint(dict_str["movieList"])
    for i in range(0,12):
        print("序号:{} id:{}".format(i,dict_str["movieList"][i]["id"]))
        print("片名:{}".format(dict_str["movieList"][i]["nm"]))
        print("演员:{}".format(dict_str["movieList"][i]["star"]))
        print("img:{}".format(dict_str["movieList"][i]["img"]))

if __name__ == "__main__":
    main()