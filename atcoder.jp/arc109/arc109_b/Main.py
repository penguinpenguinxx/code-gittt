import math

N=int(input())


if N==1:
    exit(print(1))
if N==2:
    exit(print(1))
if N==3:
    exit(print(2))
if N==5:
    exit(print(3))

left=0
right=N
while right-left>1:
    mid =(left+right)//2
    sum=(mid+1)*mid//2
    if sum>N+1:
        right=mid
    else:
        left=mid
print(N+1-(left))