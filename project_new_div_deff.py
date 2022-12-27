import numpy as np
import matplotlib.pyplot as plt
x=np.array([2,4.25,5.25,7.81,9.20,10.60])
y=np.array([7.2,7.1,6.0,5.0,3.5,5.0])


def getCoeff(x,y):
    n=len(y)
    pyramid = np.zeros([n,n])
    pyramid[::,0]= y
    for j in range(1,n):
        for i in range(n-j):
            pyramid[i][j]=(pyramid[i+1][j-1]-pyramid[i][j-1])/(x[i+j]-x[i])
    return pyramid[0]

coeff_vector = getCoeff(x,y)
print(coeff_vector)

print()

x_axis=np.linspace(0,10)


#################################
def co():
    p=0
    for i in range(len(x)):
        n=1
        for j in range(i):
            n=n*(x_axis-x[j])

        p=p+n*coeff_vector[i]
    return p


t=co()




plt.plot(x_axis,t)
plt.show()


