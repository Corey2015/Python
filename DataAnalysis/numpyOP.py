# -*- coding: utf-8 -*-
import numpy as np


file_path = '/Users/corey/Tmp/GB_video_data_numbers.csv'


def main():
    #读取CSV文件，delimiter设置分隔符，dtype设置读取出来的数据类型
    t1 = np.loadtxt(file_path,delimiter=',',dtype='int')
    print(t1)
    #T1转置
    #print(t1.transpose())
    #取一行 下标为0
    print(t1[1])
    #取一列
    print(t1[:,1])
    #取多行 从第2行开始取到第3行 一共取2行 第4行不取
    print(t1[1:3])
    #取多列
    print(t1[:,1:3])


if __name__ == "__main__":
    main()