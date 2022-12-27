import math
with open("sinput.txt", "r") as file:
    x_b = float(file.readline())
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


f2 = open("soutput.txt", "w")


def newton(a, b):
    i = 1
    epsilon_a = 1000
    while epsilon_a >= epsilon_s and i <= max_itr:
        x = float(abs(a - (func(a) * (b - a) / (func(b) - func(a)))))
        epsilon_a = float(abs((x - b) / x))

        print("Iteration number: ", i, "  x_i-1 = ", round(a, 4), "  x_i = ", round(b, 4), "  x_i+1 = ", round(x, 4),
              "  epsilon_a = ", epsilon_a,)
        f2.write("Iteration number: %d  " % i)
        f2.write("x_i-1 =  %.4f " % a)
        f2.write("x_i =   %.4f " % b)
        f2.write("x_i+1 =   %.4f " % x)
        f2.write("epsilon_a =  %.16f \n" % epsilon_a)
        a = b
        b = x
        i = i + 1
    return x


Final_answer = newton(x_b, x_i)
print("\nThe Final root is ", round(Final_answer, 4))
f2.write("\nThe Final root is: %.4f " % Final_answer)