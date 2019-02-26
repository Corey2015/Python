# -*- coding: utf-8 -*-
import requests
import json
from pprint import pprint


def main():
    # https://m.douban.com/rexxar/api/v2/subject_collection/tv_domestic/items?os=android&for_mobile=1&callback=jsonp4&start=54&count=18&loc_id=108288&_=0
    url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_domestic/items?&start=0&count=50"
    header = {"Referer": "https://m.douban.com/tv/chinese",
              "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Mobile Safari/537.36",
              }
    r = requests.get(url, headers=header)
    json_srt = json.loads(r.content.decode())
    for i in range(0,len(json_srt["subject_collection_items"])):
        print(":"*20)
        print("序号：{}".format(i))
        print("片名：")
        print(json_srt["subject_collection_items"][i]["title"])
        print("简介：")
        print(json_srt["subject_collection_items"][i]["recommend_comment"])


if __name__ == "__main__":
    main()
