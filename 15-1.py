import matplotlib.pyplot as plt
# x_values = list(range(5))
# y_values = [x*x*x for x in x_values]
# plt.scatter(x_values, y_values, s=100)
# plt.show()

x_values = list(range(5000))
y_values = [x*x*x for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=40)
plt.show()