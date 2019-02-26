# -*- coding: utf-8 -*-
import requests
from lxml import etree
from queue import Queue
import threading


class Spider(object):
    def __init__(self):
        self.base_url = "https://www.qiushibaike.com/text/page/{}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"}
    def get_url_list(self):
        return [self.base_url.format(i) for i in range(1, 14)]

    def parse_url(self, url):
        print(url)
        html_str = requests.get(url, headers=self.headers)
        return html_str.content.decode()

    def parse_xml(self, url):
        tmp_str = self.parse_url(url)
        xml_str = etree.HTML(tmp_str)
        # print(etree.tostring(xml_str).decode())
        text_list = xml_str.xpath("//a[@class = 'text']")
        # print(text_list)
        for tmp in text_list:
            res = tmp.xpath("./text()")
            # print((",".join(res)).replace("\n",""))
            # print("\n")
            self.save_file((",".join(res)).replace("\n", ""))

    def save_file(self, str_content):
        with open("./qiubai.txt", "a") as fp:
            fp.write(str_content)
            fp.write("\n\r")
            fp.close()

    def run(self):
        url_list = self.get_url_list()
        for tmp in url_list:
            self.parse_xml(tmp)


def main():
    spider = Spider()
    spider.run()


if __name__ == "__main__":
    main()
