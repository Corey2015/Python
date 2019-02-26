# -*- coding: utf-8 -*-
import requests
import json


class Spider(object):
    def __init__(self):
        self.url = "http://fy.iciba.com/ajax.php?a=fy"
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
        self.data = {"f": "auto", "t": "auto", "w": "我想过过过儿过过的生活"}

    def run(self):
        response = requests.post(self.url, headers=self.header, data=self.data)
        result = json.loads(response.content.decode())
        print(result["content"]["out"])


def main():
    spider = Spider()
    spider.run()


if __name__ == "__main__":
    main()
