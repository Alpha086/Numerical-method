import math
with open("input.txt", "r") as file:
    x_i = float(file.readline())
    epsilon_s = float(file.readline())
    max_itr = float(file.readline())
    n = int(file.readline())
    coefficient = []
    for i in range(n+1):
        data = float(file.readline())
        coefficient.append(data)

for i in range(len(coefficient)):
    print(coefficient[i])


def func(x):
    j = 0
    f = 0
    while j <= n:
        f = f + coefficient[j]*pow(x, j)
        j = j+1
    return f


def func_derivative(x):
    j = 0
    f = 0
    while j <= n:
        f = f + j * coefficient[j]*pow(x, j-1)
        j = j + 1
    return f


f2 = open("output.txt", "w")


def newton(a):
    i = 1
    epsilon_a = 1000
    while epsilon_a >= epsilon_s and i <= max_itr:
        x = float(abs(a - (func(a)/func_derivative(a))))
        epsilon_a = float(abs((x - a)/x))

        print("Iteration number: ", i, "  x_i = ", round(a, 4), "  x_i+1 = ", round(x, 4),
              "  epsilon_a = ", round(epsilon_a, 4))
        f2.write("Iteration number: %d  " % i)
        f2.write("x_i = %.4f  " % a)
        f2.write("x_i+1 =  %.4f  " % x)
        f2.write("epsilon_a = %.4f  \n" % epsilon_a)

        a = x
        i = i+1
    return x


Final_answer = newton(x_i)
print("\nThe Final root is ", round(Final_answer, 4))
f2.write("\nThe Final root is: %.4f " % Final_answer)