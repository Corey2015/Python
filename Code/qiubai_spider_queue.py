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
        self.url_queue = Queue()
        self.parse_queue = Queue()
        self.save_queue = Queue()

    def get_url_list(self):
        # return [self.base_url.format(i) for i in range(1, 14)]
        for i in range(1, 14):
            self.url_queue.put(self.base_url.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            print(url)
            html_str = requests.get(url, headers=self.headers)
            self.parse_queue.put(html_str.content.decode())
            self.url_queue.task_done()

    def parse_xml(self):
        while True:
            tmp_str = self.parse_queue.get()
            xml_str = etree.HTML(tmp_str)
            # print(etree.tostring(xml_str).decode())
            text_list = xml_str.xpath("//a[@class = 'text']")
            # print(text_list)
            for tmp in text_list:
                res = tmp.xpath("./text()")
                # print((",".join(res)).replace("\n",""))
                # print("\n")
                # self.save_file((",".join(res)).replace("\n", ""))
                self.save_queue.put((",".join(res)).replace("\n", ""))
            self.parse_queue.task_done()

    def save_file(self):
        while True:
            str_content = self.save_queue.get()
            with open("./qiubai.txt", "a") as fp:
                fp.write(str_content)
                fp.write("\n\r")
                fp.close()
            self.save_queue.task_done()

    def run(self):
        thread_list = []

        t_rul = threading.Thread(target=self.get_url_list)
        thread_list.append(t_rul)

        for i in range(20):
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)

        for i in range(20):
            t_xml = threading.Thread(target=self.parse_xml)
            thread_list.append(t_xml)

        t_save = threading.Thread(target=self.save_file)
        thread_list.append(t_save)
        for t in thread_list:
            t.setDaemon(True)
            t.start()

        for t in [self.save_queue,self.parse_queue,self.url_queue]:
            t.join()
            #有所有队列完成之后才能继续执行，只要有一个没有完成就会卡主线程，

def main():
    spider = Spider()
    spider.run()
    print("main over")


if __name__ == "__main__":
    main()
