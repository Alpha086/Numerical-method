
y=[1,2]
def co(x):
    n = 1
    for i in range(1):
        for j in range(i):
            n = n * (j-y[j])
    return n
x=[2]
print(co(x))