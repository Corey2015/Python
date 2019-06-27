# -*- coding: utf-8 -*-
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="将文件名中的中文数字改成阿拉伯数字")
    #创建一个参数 FILE_PATH
    parser.add_argument("filepath", metavar="FILE_PATH", type=str, nargs=1, help="文件路径")
    #vars 返回对象object的属性和属性值的字典对象
    args = vars(parser.parse_args())
    print(args['filepath'][0])
    filename = os.listdir(args['filepath'][0])
    print(filename)

if __name__ == "__main__":
    main()
