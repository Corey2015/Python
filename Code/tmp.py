from Code.Spider import *
url = "http://www.baidu.com"
s1 = Spider(url)
file_content = "this is a test "
s1.save_file("./test.txt",file_content)
