# -*- coding: utf-8
from selenium import webdriver
from queue import Queue
from threading import Thread
from Python.Code.musiclist import musicspider


class Spider():
    def __init__(self):
        self.url = "https://music.163.com/discover/playlist"
        self.browser = webdriver.Chrome()
        self.listqueue =Queue()

    def set_url(self,url):
        self.url = url

    def thread_save(self):
        while True:
            list_url = self.listqueue.get()
            myspider = musicspider(list_url)
            myspider.run()

    def run(self):
        #self.set_url("https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=1295")
        next_url = 1
        i=1
        while next_url is not None:
            self.browser.get(self.url)
            print("pager %d"%i)
            i +=1
            self.browser.switch_to.frame("g_iframe")
            li_list = self.browser.find_elements_by_xpath("//ul[@id ='m-pl-container']/li")
            tmp_url = self.browser.find_element_by_xpath("//a[contains(@class,'zbtn znxt')]").get_attribute("href")
            print(tmp_url)
            next_url = None if tmp_url == "javascript:void(0)" else tmp_url
            self.set_url(next_url)
            #print(li_list)
            for li in li_list:
                #print(li.find_element_by_xpath(".//p[@class = 'dec']/a/").get_attribute("title"))
                print(li.find_element_by_xpath(".//div/a").get_attribute("title"))
                list_url = li.find_element_by_xpath(".//div/a").get_attribute("href")
                self.listqueue.put(list_url)
                print(li.find_element_by_xpath(".//div/a").get_attribute("href"))
                print(li.find_element_by_xpath(".//a[@class ='nm nm-icn f-thide s-fc3']").text)
        t_list = []
        for i in range(3):
            t = Thread(target=self.thread_save())
            t_list.append(t)
        for tmp in t_list:
            tmp.setDaemon(True)
            tmp.start()
        self.browser.close()
        self.listqueue.join()


def main():
    myspider = Spider()
    myspider.run()



if __name__ == "__main__":
    main()
