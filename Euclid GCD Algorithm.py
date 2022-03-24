a=3
b=8
while(True):# 4 8
    if(a>b):
        a=a%b
    if(b>a):# 4 
        b=b%a
    if(a==0):
        print(b)
        break
    if(b==0):
        print(a)
        break
