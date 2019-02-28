# -*- coding: utf-8 -*-
from selenium import  webdriver
def main():
    browse = webdriver.Chrome()
    browse.get("http://www.baidu.com")
    browse.find_element_by_id("kw").send_keys("dolfa")
    browse.find_element_by_id("su").click()
    while True:
        pass

if __name__ == "__main__":
    main()