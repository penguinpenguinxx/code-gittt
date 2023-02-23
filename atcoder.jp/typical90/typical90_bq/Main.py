N,K = map(int,input().split())
mod=10**9+7
if N==1:
    print(K)
elif N==2:
    if K==1:
        print(0)
    else:    
        print(K*(K-1))
else:
    if K==1 or K==2:
        print(0)
    else:
        print(K*(K-1)*(pow(K-2,N-2,mod))%mod)