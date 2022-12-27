import numpy as np
a = np.array([[1,2,1],[3,8,1],[0,4,1]])
b = np.array([2,12,2])
print("A = \n", a)
b = b.reshape(-1, 1)

ide = np.array([[1,0,0],[0,1,0],[0,0,1]])

print("Identity: \n", ide)
f = []
i=0
while i<3:
    d = ( - (a[1, 0] * a[0, i])) + a[1, i]
    f.append(d)
    i=i+1
ide[1,0]= a[1,0]
a[1] = f




#########################################
g = []
j=0
while j<3:
    e = ( - (a[2, 0] * a[0, j])) + a[2, j]
    g.append(e)
    j=j+1
ide[2,0]= a[2,0]
a[2] = g

##########################################
w = []
k=0

while k<3:
    z =(- (a[1, 1])*(a[2, k]))+(a[1 , k] * a[2,1])
    w.append(z)
    k=k+1
ide[2,1]= a[1,1]
a[2]= w
print("U=\n", a)

###################################################

print("L=\n", ide)
