# -*- coding: utf-8
from selenium import webdriver

def main():
    browser = webdriver.Chrome()
    browser.get('https://music.163.com/discover/playlist')
    while 1:
        pass


if __name__ == "__main__":
    main()
