N,M=map(int,input().split())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.append(10000000000000)
B.append(10000000000000)

ansA=[]
ansB=[]
a=0
b=0
for i in range(1,N+M+1):
    if A[a]<B[b]:
        ansA.append(i)
        a+=1
    else:
        ansB.append(i)
        b+=1
print(*ansA)
print(*ansB)