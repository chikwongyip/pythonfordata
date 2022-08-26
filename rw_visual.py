import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个Random walk 实例，并将气包含的点都绘制出来
# rw = RandomWalk()
# rw.fill_walk()
# plt.scatter(rw.x_vaules, rw.y_values, s=15)
# plt.show()

# 只要程序处于活动状态，就不断得模拟随机漫步

while True:
    # 创建一个Randome Walk 实例，并将其包含的点都绘制出来
    #默认创建 5000
    # rw = RandomWalk()
    # 创建50000
    rw = RandomWalk(500000)
    rw.fill_walk()
    # 绘制窗口的尺寸
    plt.figure(figsize=(10,6))
    point_number = list(range(rw.num_point))
    # s代表圆点的精细度
    plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, 
        edgecolor="none", s=1)
    # 突出起点和终点
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", 
        edgecolors="none", s=100)
    # 隐藏坐标
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk?(y/n)")
    if keep_running == "n":
        break