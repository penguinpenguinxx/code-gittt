A,B=map(int,input().split())

N=(A/(2*B))**(2/3)
j=int(N//1)
ans2=B*j+A*(1+j)**(-1/2)
for j in range(int(N//1),int(N//1)+2):
    ans=B*j+A*(1+j)**(-1/2)
    ans=min(ans2,ans)
    ans2=ans


print(ans)