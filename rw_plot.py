import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 继续执行直到指令输入n 时候退出
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    plt.show()
    fill_next = input("Make another one?(y/n)")
    if fill_next == "n":
        break