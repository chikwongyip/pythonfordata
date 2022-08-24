import matplotlib.pyplot as plt

#plt.scatter(2, 4, s=200)
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
#颜色映射
plt.scatter(x_values, y_values, c=(0.1,0.,0.8), edgecolor="none", s=40)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of value", fontsize=24)

#设置刻度标记的大小
plt.tick_params(axis="both", which="major", labelsize=14)
plt.show()
