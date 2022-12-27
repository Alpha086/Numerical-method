

x_l = float (input('enter your lower bound: '))
x_u = float (input('enter your upper bound: '))
e_s = float (input('enter value of e_s: '))
iretetion = int(input('enter value for iretetion: '))

def func(x):
    fun = pow(x,2) - 5 * x - 6
    return fun


if func(x_l) * func(x_u) > 0 :
    print("NO ROOT FOUND !! ")

else:
    def bisec(a, b):
        e_a = 9999

        while e_a >= e_s:

            x_r = float((a + b) / 2)
            e_a = float(abs((b - a) / b))
            print(" x_l = ", a, " x_u = ", b, " x_r = ", x_r, " epsilon_a = ", e_a)

            if func(a) * func(x_r) < 0:
                b = x_r

            elif func(a) * func(x_r) > 0:
                a = x_r

            elif func(a) * func(x_r) == 0:
                return x_r
        return x_r

    ans = bisec(x_l, x_u)
    print("The estimated root is = ", ans)


