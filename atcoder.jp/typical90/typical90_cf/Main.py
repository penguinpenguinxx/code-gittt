N=int(input())
S=input()

indexo=S.find('o')
indexx=S.find('x')
maxin=max(indexo,indexx)
DP=[0]*(N+1)
DP[0]=0
word=""
DP[1]=0
word+=S[0]
xcount=-1
ocount=-1
for i in range(1,N):
    if i==maxin:
        DP[i+1]=maxin
        if S[i]=='o':
            xcount=i-1
            ocount=i 
        if S[i]=='x':
            xcount=i
            ocount=i-1 
    elif S[i]=='o' and i>maxin:
        DP[i+1]=DP[i]+(xcount+1)
        ocount=i
    elif S[i]=='x' and i>maxin:
        DP[i+1]=DP[i]+(ocount+1)
        xcount=i
    else:
        DP[i+1]=DP[i]
    word+=S[i]

print(DP[N])