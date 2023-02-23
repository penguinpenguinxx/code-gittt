N = int(input())
DP=[0]*(N+1)
DP[0]=1
mod=10**9+7
for i in range(1,N+1):
    List = list(map(int,input().split())) 
    DP[i]=DP[i-1]*(sum(List))
    DP[i]%=mod
print(DP[N])