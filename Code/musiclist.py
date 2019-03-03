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
        # 替换‘/’ 防止文件无法被创建
        file_name = file_name.replace("/","_")
        self.csv_name = "./tmp/"+file_name+".csv"
        with open(self.csv_name,"a",encoding='utf-8') as df:
            row =["歌名","时长","歌手"]
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
        #print(self.browser.page_source)
        tr_list = self.browser.find_elements_by_xpath("//table[@class = 'm-table ']/tbody/tr")
        print(tr_list)
        i = 0
        #name_list = self.browser.find_element_by_xpath("//h2[@class='f-ff2 f-brk']").text
        name_list = self.browser.find_element_by_xpath("//h2[contains(@class,'f-ff2')]").text
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

        self.browser.close()

    def save_file(self, file_path, file_content):
        pass


def main():
    myspider = musicspider("https://music.163.com/#/playlist?id=2671049846")
    myspider.run()



if __name__ == "__main__":
    main()
