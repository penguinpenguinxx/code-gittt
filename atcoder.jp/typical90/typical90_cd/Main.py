L,R=map(int,input().split())
L=L-1
mod=10**9+7
digitL=len(str(L))
sumL=digitL*(L%mod)*((L+1)%mod)//2
for i in range(1,digitL):
    sumL-=((10**(digitL-i))%mod)*((10**(digitL-i)-1)%mod)//2

digitR=len(str(R))
sumR=digitR*(R%mod)*((R+1)%mod)//2
for i in range(1,digitR):
    sumR-=((10**(digitR-i))%mod)*((10**(digitR-i)-1)%mod)//2

print((sumR-sumL)%mod)