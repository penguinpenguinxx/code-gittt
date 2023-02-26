N,K=map(int,input().split())
A=list(map(int,input().split()))
set1=set()
for i in range(len(A)):
    set1.add(A[i])
for i in range(K+1):
    if i not in set1:
        break

print(i)