# -*- coding: utf-8 -*-
from selenium import webdriver
import csv

class musicspider(object):
    def __init__(self, url={}):
        self.browser = webdriver.Chrome()
        self.url = url

    def set_url(self, url):
        self.url = url

    def create_csv(self,file_name):
        self.csv_name = "./"+file_name+".csv"
        with open(self.csv_name,"a") as df:
            row =["name","time","artist"]
            write = csv.writer(df)
            write.writerow(row)
            df.close()

    def save_csv(self,row):
        with open(self.csv_name,"a") as df:
            #row =["name","time","artist"]
            write = csv.writer(df)
            write.writerow(row)
            df.close()

    def run(self):
        self.browser.get(self.url)
        self.browser.switch_to.frame("g_iframe")
        # //*[@id="auto-id-eMx3Pho1a0bCsDk1"]/table/tbody
        #print(self.browser.page_source)
        tr_list = self.browser.find_elements_by_xpath("//table[@class = 'm-table ']/tbody/tr")
        print(tr_list)
        i = 0
        name_list = self.browser.find_element_by_xpath("//h2[@class='f-ff2 f-brk']").text
        #print(name_list)
        self.create_csv(name_list)
        for tr in tr_list:
            music_info=[]
            title = tr.find_element_by_xpath(".//span[@class='txt']/a/b").get_attribute("title")
            music_info.append(title)
            print(title)
            time_song = tr.find_element_by_xpath(".//span[@class='u-dur ']").text
            print(time_song)
            music_info.append(time_song)
            artist= tr.find_element_by_xpath(".//div[@class='text']").get_attribute("title")
            print(artist)
            music_info.append(artist)
            self.save_csv(music_info)

        #self.browser.close()

    def save_file(self, file_path, file_content):
        pass


def main():
    myspider = musicspider("https://music.163.com/#/playlist?id=2444897054")
    myspider.run()
    while 1:
        pass


if __name__ == "__main__":
    main()
