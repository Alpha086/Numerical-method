import numpy as np
import matplotlib.pyplot as plt
x = np.array([2, 4.25, 5.25, 7.81, 9.20, 10.60])
y = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])


def lag_range(x, y, n, xx):
    result = 0
    for i in range(n):
        product = y[i]
        for j in range(n):
            if i != j:
                product = product * ((xx-x[j])/(x[i]-x[j]))
                # print(product)
        result = result + product
    return result


xx = np.linspace(0, 10)
print("X axis:\n", xx)
n = len(x)
t = lag_range(x, y, n, xx)
print(" Y axis:\n", t)
plt.scatter(xx, t)
plt.plot(xx, t)
plt.show()
