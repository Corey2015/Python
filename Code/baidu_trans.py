# -*- coding: utf-8 -*-
import requests
import json

class Spider(object):
    def __init__(self, trans_str):
        self.url = "http://fanyi.baidu.com/basetrans"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Mobile Safari/537.36"        }
        self.trans_str = trans_str

    def lang_detect(self):
        data = {"query": self.trans_str}
        response = requests.post("https://fanyi.baidu.com/langdetect", headers=self.header, data=data)
        return json.loads(response.content.decode())["lan"]

    def run(self):
        lan = self.lang_detect()
        if lan == "zh":
            data = {"query": self.trans_str,
                    "from": lan,
                    "to": "en",
                   # "token": "6298971829b9a52ba695345267792138",
                   # "sign": "54706.276099"
                    }
        else:
            data = {"query": self.trans_str,
                    "from": lan,
                    "to": "cn",
                    #"token": "6298971829b9a52ba695345267792138",
                    #"sign": "54706.276099"
                    }
        response = requests.post(self.url, headers=self.header, data=data, )
        print(response.content.decode('unicode-escape'))


def main():
    s1 = Spider("hello")
    s1.run()


if __name__ == "__main__":
    main()
