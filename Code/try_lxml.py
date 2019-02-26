# -*- coding: utf-8 -*-
from lxml import etree
from Code.Spider import Spider

xml_text = text = ''' <div> <ul> 
        <li class="item-1"><a >first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html"></a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a>  
        </ul> </div> '''


def main():
    if 0:
        html_str = etree.HTML(xml_text)
        print(etree.tostring(html_str).decode())
        result1 = html_str.xpath("//li[@class ='item-1']/a/text()")
        print(result1)
        result2 = html_str.xpath("//li[@class = 'item-1']/a/@href")
        print(result2)
        result3 = html_str.xpath("//li[@class = 'item-1']")
        print(result3)
        print(etree.tostring(result3[1]).decode())
        result_dict = {}
        for i in result3:
            result_dict["contet"] = i.xpath("a/text()")[0] if len(i.xpath("a/text()")) > 0 else None
            result_dict["href"] = i.xpath("a/@href")[0] if len(i.xpath("a/@href")) > 0 else None
            print(result_dict)

    if 1:
        url = "http://duanziwang.com/"
        s1 = Spider(url)
        result = s1.parse_url()
        # print(result)
        xml_str = etree.HTML(result)
        # print(etree.tostring(xml_str).decode('utf-8'))

        contet1 = xml_str.xpath("//div[@class='post-content']")
        print(contet1)
        for tmp in contet1:
            print("~"*100)
            print(etree.tostring(tmp).decode())
            r1 = tmp.xpath("p/text()")
            if r1 is not None:
                print(r1)


if __name__ == "__main__":
    main()
