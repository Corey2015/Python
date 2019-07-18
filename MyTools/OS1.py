# -*- coding:utf8 -*-
import os
def main():
    #获取路径
    ret = os.getcwd()
    #获取路径下的文件
    filelist = os.listdir(ret)

    tmpfilelist = filelist.copy()
    for tmp in tmpfilelist:
        # 判断是否为文件
        isfile = os.path.isfile(tmp)
        if isfile:
            print("{} is the file size is {}".format(tmp,os.stat(tmp).st_size))
        else:
            filelist.remove(tmp)
            print("{} is the directory")
    print(filelist)

if __name__ == '__main__':
    main()