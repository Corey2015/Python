# -*- coding: utf-8
import requests


class Spider(object):
    def __init__(self, url, header={}):
        self.url = url
        if header == {}:
            print("header is default")
            self.header = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
        else:
            self.header = header

    def _parse_url(self, method, data, proxies):
        if method == "POST":
            print("POST")
            response = requests.post(self.url, data=data, headers=self.header, proxise=proxies)
        else:
            print("GET")
            response = requests.get(self.url, headers=self.header,proxies = {})
            print(response.status_code)
        assert response.status_code == 200
        return response.content.decode()

    def parse_url(self, method="GET", data=None, proxies={}):
        try:
            result = self._parse_url(method, data=data, proxies=proxies)
        except:
            print("error")
            result = None
        return result

    def save_file(self,path_file,file_content,mode = "w"):
        with open(path_file,mode) as fp:
            fp.write(file_content)
            fp.close()

def main():
    spider = Spider("http://www.baidu.com")
    result = spider.parse_url()
    print(result)


if __name__ == "__main__":
    main()
