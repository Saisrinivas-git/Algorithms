#Sieve Of Eratosthenes Algorithm
import math as m
n=int(input()) #10
a=[1]*n
a[0]=a[1]=0
for i in range(2,int(m.sqrt(n)+1)):
    if(a[i]):
        for j in range(i*i,n,i):
            a[j]=0
print(sum(a)) #4
 
