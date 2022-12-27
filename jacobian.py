import numpy as np
num=int(4)
A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
b = np.array([6., 25., -11., 15.])
x = np.array([0,0,0,0])
new = [0,0,0,0]
k=int(input("number of iterations: "))

print("System:")
for i in range(A.shape[0]):
    row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print(" + ".join(row), "=", b[i])
print()

it=1
while it<= k:

    sum =0
    for i in range(num):
        sum = 0
        for j in range(num):
            if i !=j:
                sum = sum +( A[i][j]*x[j])

        new[i] = float(((b[i] - sum)/A[i][i]))



    print("iteration ",it,"  ",new)
    x = new


    it= it+1





# def jec():
#     print(A)
#     print(b)
#
# jec()