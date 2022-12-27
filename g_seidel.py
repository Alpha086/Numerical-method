num = int(input("enter iteration : "))
n = int(4)

x = [0, 0, 0, 0]
a = [[10., -1., 2., 0.],
     [-1., 11., -1., 3.],
     [2., -1., 10., -1.],
     [0.0, 3., -1., 8.]]
b = [6., 25., -11., 15.]
print(x)

def seidel(a, x, b):
    n = len(a)
    for j in range(0, n):
        d = b[j]
        for i in range(0, n):
            if (j != i):
                d -= a[j][i] * x[i]
        x[j] = d / a[j][j]
    return x


for i in range(1, num+1):
    x = seidel(a, x, b)
    print("iteration :", i ," ", x)
