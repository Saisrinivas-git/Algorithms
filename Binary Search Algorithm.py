#Binary Search Algorithm
arr=[int(i) for i in input().split()]
# 2 4 5 6 8
# l   m   h
target=int(input()) #5
l=0
h=len(arr)-1
while(l<=h):
    mid=(l+h)>>1
    if(arr[mid]<target):
        l=mid+1
    elif(arr[mid]>target):
        h=mid-1
    elif(arr[mid]==target):
        print(True)
        break
    else:
        print(False)
