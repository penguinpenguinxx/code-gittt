N,K=map(int,input().split())
num=0
ans=0
for i in range(N):
    num=(i+1)
    for j in range(K):
        ans+=num*100
        ans+=(j+1)
        
print(ans)