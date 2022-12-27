import numpy as np
import matplotlib.pyplot as plt

x = np.array([2,4.25,5.25,7.81,9.20,10.60])
y = np.array([7.2,7.1,6.0,5.0,3.5,5.0])


def n(j, xc, x):
    n = 1
    for i in range(j):
        n *= (xc - x[i])

    return n


def a(j, l, x, y):
    if j == 0:
        return y[0]
    elif j - l == 1:
        return (y[j] - y[l]) / (x[j] - x[l])
    else:
        return (a(j, l + 1, x, y) - a(j - 1, l, x, y)) / (x[j] - x[l])


def N(xc, x, y):
    N = 0
    for j in range(len(x)):
        N += a(j, 0, x, y) * n(j, xc, x)



    return N


# for testing
xc = 3

yc = N(xc, x, y)

# plot
t = np.linspace(0,10)
u = N(t, x, y)

plt.plot(t, u)

plt.show()


