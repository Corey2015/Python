# -*- coding: utf-8
from selenium import webdriver

class Spider():
    def __init__(self):
        self.url = "https://music.163.com/discover/playlist"
        self.browser = webdriver.Chrome()

    def set_url(self,url):
        self.url = url

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
                print(li.find_element_by_xpath(".//div/a").get_attribute("href"))
        self.browser.quit()



def main():
    myspider = Spider()
    myspider.run()



if __name__ == "__main__":
    main()
