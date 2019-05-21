# -*- coding: utf-8 -*-
import numpy as np


file_path = '/Users/corey/Tmp/GB_video_data_numbers.csv'


def main():
    #读取CSV文件，delimiter设置分隔符，dtype设置读取出来的数据类型
    t1 = np.loadtxt(file_path,delimiter=',',dtype='int')
    print(t1)
    print("="*50)
    #T1转置
    #print(t1.transpose())
    #取一行 下标为0
    #print(t1[1])
    #取一列
    #print(t1[:,1])
    #取多行 从第2行开始取到第3行 一共取2行 第4行不取
    #print(t1[1:3])
    #取多列
    #print(t1[:,1:3])
    #取不连续多行
    #print(t1[[1,3,5]])
    #取不连续多列
    #print(t1[:,[0,2]])
    #取第3行第4列第值
    #print(t1[2,3])
    #取多行多列值 取第3行到第5行 第2列到第4列的值
    #print(t1[2:5,1:4])
    #取多个不相邻的点的值 (0,0),(2,1),(3,3)
    print(t1[[0,2,3],[0,1,3]])

if __name__ == "__main__":
    main()