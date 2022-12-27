import math
import numpy as np
x_i = float(input("X_i: "))
epsilon_s = float(input("Epsilon s: "))
max_itr = int(input("maximum iteration: "))
coefficient = []
n = int(input("Height power: "))
for i in range(n+1):
    data = float(input("Enter coefficient value: "))
    coefficient.append(data)


def func(x):
    j = 0
    f = 0
    while j <= n:
        f = f + coefficient[j]*pow(x, j)
        j = j+1
    return f


def func_derivative(x):
    p2 = np.poly1d(data)
    p3 = np.polyder(p2,1)
    return p3(x)


def newton(a):
    i = 1
    epsilon_a = 1000
    while epsilon_a >= epsilon_s and i <= max_itr:
        x = float(abs(a - (func(a)/func_derivative(a))))
        epsilon_a = float(abs((x - a)/x))

        print("Iteration number: ", i, " x(i) = ", round(x_i, 4), " x(i+1) = ", round(x, 4),
              " epsilon_a = ", round(epsilon_a, 4))
        a = x
        i = i+1
    return x


Final_answer = newton(x_i)
print("The root is", round(Final_answer, 4))