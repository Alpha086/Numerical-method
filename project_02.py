import math

def func(x):
    sum1 = float(0)
    for i in range(0, n + 1, 1):
        sum1 = sum1 + (coe[i] * math.pow(x, i))

    return sum1


####################################

n = int(input('enter highest degree of the function : '))
coe = []
for i in range(0, n + 1, 1):
    print('enter coefficient for x^', i)
    coe.append(int(input()))
#

####################################
x_l = float (input('enter your lower bound: '))
x_u = float (input('enter your upper bound: '))
e_s = float (input('enter value of e_s: '))
x_t = float(input('enter value for e_t: '))
iretetion = int(input('enter value for iretetion: '))
i = -1


########################################

if func(x_l) * func(x_u) > 0 :
    print("NO ROOT FOUND !! ")

#######################################
else:
    def bisec(a, b):
        e_a = 9999

        while e_a >= e_s:

            global i

            i = i+1

            if i== iretetion:
                break

            else:
                x_r = float(b-((func(b)*(a-b))/func(a)-func(b)))
                e_a = float(abs((b - a) / b))
                e_t = abs((x_t - x_r) / x_t)
                print(" x_l = ", a, " x_u = ", b, " x_r = ", x_r, " epsilon_a = ", e_a, "epsilon_t", e_t)

                if func(a) * func(x_r) < 0:
                    b = x_r

                elif func(a) * func(x_r) > 0:
                    a = x_r

                elif func(a) * func(x_r) == 0:
                    return x_r


        return x_r

    ans = bisec(x_l, x_u)
    print("The estimated root is = ", ans)

###################################################
