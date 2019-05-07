# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

def main():
    # 设置图片大小和分辨率
    plt.figure(figsize=(20, 8), dpi=144)
    # 定义X轴数据由2开始 到24 步长为2
    x = range(2, 26, 2)
    # 定义Y轴数据
    y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]
    # 传入x和y 进行绘制 x和y必须是可迭代对象
    plt.plot(x, y)
    # 设置X轴的刻度
    plt.xticks(x)
    # 保存图片 show之前调用
    # plt.savefig("./tmp.png")
    # 保存成矢量图
    plt.savefig("./tmp.svg")
    # 显示出绘制的图像
    plt.show()


def test():
    plt.figure(figsize=(30, 8), dpi=144)
    a = [random.randint(20, 35) for i in range(120)]
    x = range(1, 121, 1)
    plt.xticks(x)
    plt.yticks(a)
    plt.plot(x, a)
    plt.show()

def temperature():
    #设置中文字体
    myfont = font_manager.FontProperties(fname="/System/Library/Fonts/STHeiti Medium.ttc")
    plt.figure(figsize=(20,8),dpi=144)
    y = [random.randint(20, 35) for i in range(120)]
    #num：0>2 2:定义为2位 >：右对齐 0 用0来填充空位
    x_list = range(120)
    x = ["10点:{num:0>2}".format(num = i) for i in range(60)]
    x += ["11点:{num:0>2}".format(num = i) for i in range(60)]
    #x_list和x的数据都传入，且2组数据必须长度一致
    #fontproperties将中文字体传入
    plt.xticks(x_list[::3],x[::3],rotation=270,fontproperties = myfont)
    plt.yticks(y)
    plt.xlabel("时间",fontproperties = myfont)
    plt.ylabel("温度",fontproperties = myfont)
    plt.title("10点到12点温度分析", fontproperties=myfont)
    plt.plot(x, y)
    plt.show()

def friends():
    myfont = font_manager.FontProperties(fname="/System/Library/Fonts/STHeiti Medium.ttc")
    y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
    y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    x = range(11,31,1)
    x_content = ["{}岁".format(i) for i in x]
    plt.xticks(x,x_content,rotation = 45,fontproperties = myfont)
    plt.yticks(y_1)
    #绘制第一条数据线 图例描述为自己 线条颜色红色
    plt.plot(x,y_1,label = "自己",color = 'red')
    #绘制第二条数据线 图例描述为同桌 线条颜色蓝色
    plt.plot(x,y_2,label = "同桌",color ='blue')
    #显示图例，位置在右上方
    plt.legend(prop = myfont,loc='upper right')
    #绘制网格
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # main()
    #test()
    #temperature()
    friends()














