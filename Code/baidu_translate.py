# coding=utf-8
import requests


class NetSpider(object):
    def __init__(self, transfer_str):
        self.url = "http://fanyi.baidu.com/basetrans"
        self.header = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"}

        self.data = {"query": "hello", "from": "en", "to": "zh","token": "ecf5e4fa621d84ab28995132b55eb5ad","sign":"54706.276099"}

    def run(self):
        respon = requests.post(self.url, data=self.data, headers=self.header)
        print(respon.status_code)
        print(respon.content.decode())


def main():
    n1 = NetSpider("hello")
    n1.run()


if __name__ == "__main__":
    main()
