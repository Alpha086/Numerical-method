import numpy as np

########################################################################

with open("sinput.txt", "r") as f:
    x_b = float(f.readline())
    x_i = float(f.readline())
    epsilon_s = float(f.readline())
    max_itr = int(f.readline())
    m = int(f.readline())
    n = []
    for i in range(0, m + 1, 1):
        w = float(f.readline())
        n.append(w)


#######################################################################

def function(x):
    p1 = np.poly1d(n)
    return p1(x)

########################################################################


out = open("soutput.txt", "w")


def newton(a, b):
    i = 1
    epsilon_a = 1000
    while epsilon_a >= epsilon_s and i <= max_itr:
        x = float(abs(a - (function(a) * (b - a) / (function(b) - function(a)))))
        epsilon_a = float(abs((x - b) / x))

        print("Iteration number: ", i, "  x_i-1 = ", round(a, 4), "  x_i = ", round(b, 4), "  x_i+1 = ", round(x, 4),
              "  epsilon_a = ", epsilon_a,)
        out.write("Iteration number: %d  " % i)
        out.write("x_i-1 =  %.4f " % a)
        out.write("x_i =   %.4f " % b)
        out.write("x_i+1 =   %.4f " % x)
        out.write("epsilon_a =  %.16f \n" % epsilon_a)
        a = b
        b = x
        i = i + 1
    return x


Final_answer = newton(x_b, x_i)
print("\nThe Final root is ", round(Final_answer, 4))
out.write("\nThe Final root is: %.4f " % Final_answer)