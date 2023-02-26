N=int(input())
List=list(map(int,input().split()))

ans=1
mod=10**18+1

A=List.count(0)
if A>0:
  exit(print(0))
for i in range(N):
    ans*=List[i]
    B=ans//mod
    if B>0:
        exit(print(-1))
print(ans)