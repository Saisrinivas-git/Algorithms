#Euclid's Algorithm for GCD
a,b=map(int,input().split())
while(True):# 4 8
    if(a>b):
        a=a%b
    if(b>a): 
        b=b%a
    if(a==0):
        print(b)
        break
    if(b==0):
        print(a)
        break
