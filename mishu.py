import math
xl = float(input("Lower limit: "))
xu = float(input("Upper limit: "))
xt = float(input("True value: "))
es = float(input("Error tolerance: "))
max_itr = int(input("Maximum Iteration number: "))
n = int(input("Height power: "))
coefficient = []
for i in range(n+1):
    data = float(input("Enter coefficient value: "))
    coefficient.append(data)


def func(x):
    j = 0
    f = 0
    while j <= n:
        f = f + coefficient[j]*math.pow(x,j)
        j = j+1
        return f


def bi_section(k, m):
    ea = 0.9999
    a = 0
    while a < max_itr and ea >= es:
        xr = float((k+m)/2)
        ea = float(abs(m-k)/(k+m))
        et = float(abs(xt - xr)/xt)
        print("Xl= ", round(k, 4), "Xu= ", round(m, 4), "Xr=", round(xr, 4), "Epsilon_a= ", round(ea, 4))
        print("Epsilon_true= ", round(et, 4))
        if(func(k) * func(xr)) < 0:
            m = xr
        elif(func(k) * func(xr)) > 0:
            k = xr
        elif(func(k) * func(xr)) == 0:
            return xr
        a = a+1
    return xr

ans = bi_section (xl,xu)
print(ans)