import math
n = int(input('enter order of coeffecient: '))
coe=[]
for i in range(0,n+1,1):
    print('enter coeff for x^',i)
    coe.append(int(input()))
print ('all coefficient',coe)
sum1=float(0)
x= int(input('enter for x: '))
for i in range(0,n+1,1):

    sum1 = sum1+(coe[i]*math.pow(x,i))

print("The value of the polynomial is:",sum1)