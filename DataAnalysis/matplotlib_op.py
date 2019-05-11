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
    # 设置中文字体
    myfont = font_manager.FontProperties(fname="/System/Library/Fonts/STHeiti Medium.ttc")
    plt.figure(figsize=(20, 8), dpi=144)
    y = [random.randint(20, 35) for i in range(120)]
    # num：0>2 2:定义为2位 >：右对齐 0 用0来填充空位
    x_list = range(120)
    x = ["10点:{num:0>2}".format(num=i) for i in range(60)]
    x += ["11点:{num:0>2}".format(num=i) for i in range(60)]
    # x_list和x的数据都传入，且2组数据必须长度一致
    # fontproperties将中文字体传入
    plt.xticks(x_list[::3], x[::3], rotation=270, fontproperties=myfont)
    plt.yticks(y)
    plt.xlabel("时间", fontproperties=myfont)
    plt.ylabel("温度", fontproperties=myfont)
    plt.title("10点到12点温度分析", fontproperties=myfont)
    plt.plot(x, y)
    plt.show()


def friends():
    myfont = font_manager.FontProperties(fname="/System/Library/Fonts/STHeiti Medium.ttc")
    y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
    y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    x = range(11, 31, 1)
    x_content = ["{}岁".format(i) for i in x]
    plt.xticks(x, x_content, rotation=45, fontproperties=myfont)
    plt.yticks(y_1)
    # 绘制第一条数据线 图例描述为自己 线条颜色红色
    plt.plot(x, y_1, label="自己", color='red')
    # 绘制第二条数据线 图例描述为同桌 线条颜色蓝色
    plt.plot(x, y_2, label="同桌", color='blue')
    # 显示图例，位置在右上方
    plt.legend(prop=myfont, loc='upper right')
    # 绘制网格
    plt.grid()
    plt.show()


def scatterpolt():
    myfont = font_manager.FontProperties(fname="/usr/share/fonts/truetype/arphic/ukai.ttc")
    plt.figure(figsize=(20, 8), dpi=144)
    y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22,
           22, 22, 23]
    y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11,
            13, 12, 13, 6]
    x_3 = range(1, 32)
    x_10 = range(41, 72)
    x = list(x_3) + list(x_10)
    xticks = ["3月{}日".format(i) for i in x_3]
    xticks += ["10月{}日".format(i - 40) for i in x_10]
    plt.xticks(x, xticks, fontproperties=myfont, rotation=45)
    plt.scatter(x_3, y_3, label="3月")
    plt.scatter(x_10, y_10, label="10月")
    plt.legend(prop=myfont, loc='upper right')
    plt.grid(alpha=0.3)
    plt.show()

#垂直条形图
def barchart():
    plt.figure(figsize=(20, 8), dpi=144)
    myfont = font_manager.FontProperties(fname="/usr/share/fonts/truetype/arphic/ukai.ttc")
    xtick = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归",
             "生化危机6：终章",
             "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊", ]

    ytick = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99,
             6.88,
             6.86, 6.58, 6.23]

    x = range(len(xtick))
    plt.xticks(x, xtick, fontproperties=myfont)
    plt.bar(x, ytick, width=0.2, color="red")
    plt.show()

#水平条形图
def barchartH():
    plt.figure(figsize=(20, 8), dpi=144)
    myfont = font_manager.FontProperties(fname="/usr/share/fonts/truetype/arphic/ukai.ttc")
    ytick = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：死无对证", "金刚：骷髅岛", "极限特工：终极回归",
             "生化危机6：终章",
             "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：殊死一战", "蜘蛛侠：英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊", ]

    xtick = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99,
             6.88,
             6.86, 6.58, 6.23]

    y = range(len(ytick))
    plt.yticks(y,ytick,fontproperties = myfont)
    plt.barh( ytick,xtick, color="red")
    plt.show()

def barcharts():
    barwidth = 0.2
    a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
    b_16 = [15746, 312, 4497, 319]
    b_15 = [12357, 156, 2045, 168]
    b_14 = [2358, 399, 2358, 362]
    myfont = font_manager.FontProperties(fname="/System/Library/Fonts/STHeiti Medium.ttc")
    #设置X坐标刻度
    #[0,1,2,3]
    x_14 = range(len(a))
    #[0.2,1.2,2.2,3.2]
    x_15 = [i+barwidth for i in x_14]
    #[0.4,1.4,2.4,3.4]
    x_16 = [i+barwidth*2 for i in x_14]
    #设定刻度用x_15，并且将a的数据映射到坐标刻度
    #3个条形图 X_15居中
    plt.xticks(x_15,a,fontproperties = myfont)
    #绘制14日的数据
    plt.bar(x_14,b_14,width=barwidth,label = "14日")
    # 绘制15日的数据
    plt.bar(x_15,b_15,width=barwidth,label = "15日")
    # 绘制16日的数据
    plt.bar(x_16, b_16, width=barwidth,label = "16日")
    #显示图标
    plt.legend(prop = myfont)
    #显示网格 透明度设置成0。3
    plt.grid(alpha = 0.3)
    plt.show()


if __name__ == "__main__":
    # main()
    # test()
    # temperature()
    # friends()
    # scatterpolt()
    #barchartH()
    barcharts()