# -*- coding: utf-8
import requests


class Spider(object):
    def __init__(self, url="", header={}):
        self.url = url
        if header == {}:
            print("header is default")
            self.header = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
                "Cookie":" _iuqxldmzr_=32; _ntes_nnid=0bce1b814168d5087034f80d5ff558f7,1551324831274; _ntes_nuid=0bce1b814168d5087034f80d5ff558f7; WM_NI=eyxNnUXEeYrCbzm1l3zXy3lhO3poyp2IeGlTwz%2F3v%2B3AZtK5p3QPkaPmZrcV%2B0su1u5BJJUWPepm9sHvyf5yQgiMv%2B6lL6qUv4fafR23t2fl9gVneO1BV2d4P9UePFjOWEM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea3fb41bb8f888fd363b6e78aa2d55a868b9abaee6dbcad83b5e763829a96b2b72af0fea7c3b92aa7a7b8afed5f9c9babbaf149a2a6a3d2ef39ba88b7d4ef648dedc090fc7cf297aba8ef60b5a6e1d4f521f19f9695ca3fb4ed9fb1ea6b94b39693e25ee9f0bd96b47ff79e86abd85d94bbc08ebc798caab787b87393b9a7aef521f6b484d7f45fb6ecaa82e55af2edbcd3e568fbb99a8fe845f39e9ad3e74094e79b86d34eaa9199a6d037e2a3; WM_TID=DRdcMz2dPrdFARAVFRIthk8IXZ3QQYU5; JSESSIONID-WYYY=1bIn2A76pfs5TAGYU4FHO57kGfXmcW7cZFBRIn73%2BECrXR1BONPw3pt%2BZAvwYzlc8%5CCcX606K9QZ3%2FrfXs6%5Cg60MZZTZDoVPkRl2E98A7bg86HJXlG1ePQ721G6uxRZcBnRk%2BkuNM1zhY953%5C9iRy9Zaq4xOwzrntPz3IwQRwqdFlXnG%3A1551350718168"
            }
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

    def set_url(self,url):
        self.url = url


def main():
    spider = Spider("http://www.baidu.com")
    result = spider.parse_url()
    print(result)


if __name__ == "__main__":
    main()
