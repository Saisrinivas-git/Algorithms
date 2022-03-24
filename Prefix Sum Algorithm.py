# Prefix Sum Algorithm
arr=list(map(int,input().split()))
# 1 2 3 4 5
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
print(prefix)
l,h=map(int,input().split())
if(l==0):
    print(prefix[h])
else:
    print(prefix[h]-prefix[l-1])
