N,L=map(int,input().split())
DP=[0]*(N+1)
DP[0]=1
mod=10**9+7
for i in range(1,N+1):
    if i<L:
        DP[i]=DP[i-1]
    else:  
        DP[i]=DP[i-1]+DP[i-L]
    DP[i]%=mod
print(DP[N])