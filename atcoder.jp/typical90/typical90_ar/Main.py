import numpy as np

N,Q=map(int,input().split())
List=list(map(int,input().split()))
List=np.array(List)
count=0
for _ in range(Q):
    T,x,y=map(int,input().split())
    x,y=x-1,y-1
    if T==1:
        List[(x-count)%N],List[(y-count)%N]=List[(y-count)%N],List[(x-count)%N]
    if T==2:
        count+=1
    if T==3:
        print(List[(x-count)%N])