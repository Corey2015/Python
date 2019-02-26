#coding = utf-8

from Code.Spider import *
from lxml import etree


class tieba(Spider):
    def __init__(self,tieba_name):
        url = "https://tieba.baidu.com/f?kw={}&pn=0&".format(tieba_name)
        headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36"}
        super().__init__(url,header=  headers)


def main():
    t1 = tieba("ibm")
    #print(t1.header)
    result = t1.parse_url()
    #print(result)
    xml_str = etree.HTML(result)
    #pprint(etree.tostring(xml_str).decode())
    title = xml_str.xpath("//a[@class = 'j_common ti_item ']")
    for tmp in title:
        contet = tmp.xpath(".//span/text()")
        href = tmp.xpath("./@href")
        print("https://tieba.baidu.com{}".format(href[0]))
        print(contet)


if __name__ == '__main__':
    main()