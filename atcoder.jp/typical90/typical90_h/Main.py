N=int(input())
S=input()


a=[0]*(N+1)
at=[0]*(N+1)
atc=[0]*(N+1)
atco=[0]*(N+1)
atcod=[0]*(N+1)
atcode=[0]*(N+1)
atcoder=[0]*(N+1)

a[0]=0
at[0]=0
atc[0]=0
atco[0]=0
atcod[0]=0
atcode[0]=0
atcoder[0]=0

mod=10**9+7
for i in range(N):
    a[i+1]=a[i]
    at[i+1]=at[i]
    atc[i+1]=atc[i]
    atco[i+1]=atco[i]
    atcod[i+1]=atcod[i]
    atcode[i+1]=atcode[i]
    atcoder[i+1]=atcoder[i]
    a[i+1]%=mod
    at[i+1]%=mod
    atc[i+1]%=mod
    atco[i+1]%=mod
    atcod[i+1]%=mod
    atcode[i+1]%=mod
    atcoder[i+1]%=mod
    if S[i]=='a':
        a[i+1]+=1
    if S[i]=='t':
        at[i+1]+=a[i]
    if S[i]=='c':
        atc[i+1]+=at[i]
    if S[i]=='o':
        atco[i+1]+=atc[i]
    if S[i]=='d':
        atcod[i+1]+=atco[i]
    if S[i]=='e':
        atcode[i+1]+=atcod[i]
    if S[i]=='r':
        atcoder[i+1]+=atcode[i]

print(atcoder[N]%mod)