# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt

file_path = '/Users/corey/Tmp/GB_video_data_numbers.csv'

us_path = '/Users/corey/Tmp/US_video_data_numbers.csv'
uk_path = '/Users/corey/Tmp/GB_video_data_numbers.csv'

def datastack():
    us_data = np.loadtxt(us_path,delimiter=',',dtype='int')
    uk_data = np.loadtxt(uk_path,delimiter=',',dtype='int')
    zeros = np.zeros((us_data.shape[0],1)).astype(int)
    ones = np.ones((uk_data.shape[0],1)).astype(int)
    print(us_data.shape[0])
    print(uk_data.shape[0])
    us_data = np.hstack((us_data,zeros))
    uk_data = np.hstack((uk_data,ones))
    final_data = np.vstack((us_data,uk_data))
    print(final_data)

def test():
    t1 = np.loadtxt(file_path, delimiter=',', dtype='int')

    print(t1[:,-1])
    plt.figure(figsize=(20,8),dpi=144)
    t1 = t1[t1<=5000]
    num_bins = int((t1.max()-t1.min())//50)
    print(num_bins)
    plt.hist(t1[:-1],num_bins)
    plt.show()

def test2():
    t1 = np.loadtxt(file_path, delimiter=',', dtype='int')
    plt.figure(figsize=(20, 8), dpi=144)
    t1= t1[t1[:,1]<=500000]
    t1_like = t1[:,1]
    t1_comment = t1[:,-1]
    plt.scatter(t1_like,t1_comment)
    plt.show()


def main():
    datastack()
    #test2()
    # 布尔索引
    # t = np.arange(24).reshape(4, 6)
    # # 将t中小于10的数据设置成0
    # t[t < 10] = 0
    # print(t)
    # # 用3元运算符将小于10的设置成0 大于10的设置成10
    # np.where(t < 10, 0, 10)
    # print(t)
    # # 用clip方法，将小于3的值设置为3 大于18的值设置为18
    # t = np.clip(t, 3, 18)
    # print(t)
    # # 求和
    # print(t.sum())
    # # 求平均值
    # print(t.mean())
    # # 求中值
    # print(np.median(t))
    # # 求最大值和最小值
    # print(t.max())
    # print(t.min())
    # # 求极差
    # print(np.ptp(t))
    # # 求标准差 标准差越大 这集合中大部分数据和平均值差异很大
    # print(t.std())


if __name__ == "__main__":
    main()
