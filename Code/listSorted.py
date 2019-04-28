# -*- coding: utf-8 -*-
import re
dict = {'jprice': '17.50', 'book_pub_data': '2015-09', 'book_author': ' 杨东 ', 'subline': '军事', 'suburl': 'https://list.jd.com/1713-3258-3308.html', 'book_pub': '译林出版社', 'headline': '小说', 'book_name': '瞒天过海', 'book_ISBN': '9787544756778', 'book_url': 'https://item.jd.com/11762622.html', 'book_sku': '11762622', 'oprice': '38.00'}
l1 = list(dict)
print(sorted(l1))
add_item =[]
for each in sorted(l1):
    add_item.append(dict[each])
    print("{} : {}".format(each,dict[each]))
print(add_item)

url = 'https://item.jd.com/27818529770.html'
re = re.findall(r"https://item.jd.com/(\d+).html",url)[0]
print(re)
def main():
    pass


if __name__ == "__main__":
    main()