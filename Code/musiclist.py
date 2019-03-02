# -*- coding: utf-8 -*-
from selenium import webdriver

class musicspider(object):
    def __init__(self,url ={}):
        self.browser = webdriver.Chrome()
        self.url = url
    def set_url(self,url):
        self.url = url

    def run(self):
        self.browser.get(self.url)
        self.browser.switch_to.frame("g_iframe")
        #//*[@id="auto-id-eMx3Pho1a0bCsDk1"]/table/tbody
        print(self.browser.page_source)
        tr_list = self.browser.find_elements_by_xpath("//table[@class = 'm-table ']/tbody/tr")
        print(tr_list)
        i = 0
        for tr in tr_list:
            print(tr.text)

        self.browser.close()

    def save_file(self,file_path,file_content):
        pass

def main():
    myspider = musicspider("https://music.163.com/#/playlist?id=2444897054")
    myspider.run()
    while 1:
        pass

if __name__ == "__main__":
    main()