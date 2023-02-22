import collections
N,K=map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

num=0
for i in range(len(A)):
    num+=abs(A[i]-B[i])

if K-num<0:
    print("No")
elif (K-num)%2==1:
    print("No")
else:
    print("Yes")