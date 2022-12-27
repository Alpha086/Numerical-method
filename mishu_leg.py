import numpy as np
import matplotlib.pyplot as plt
x = np.array([2,4.25,5.25,7.81,9.20,10.60])
y = np.array([7.2,7.1,6.0,5.0,3.5,5.0])



##########################

def lagrng(x,y,n,xx):
    sum=0
    for i in range(n):
        product = y[i]
        for j in range(n):
            if i!=j:
                product = product * (xx-x[j])/(x[i]-x[j])
                print(product)
        sum = sum + product
    return sum

xx = np.linspace(0,10)
#print(xx)
n=len(x)

t=lagrng(x,y,n,xx)
plt.scatter(xx,t)
plt.plot(xx,t)
plt.show()







