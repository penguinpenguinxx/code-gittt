N,Q=map(int,input().split())
List=[0]*(N+1) 
for i in range(Q):
    a,x=map(int,input().split())
    if a==1:
        List[x]+=1
    if a==2:
        List[x]=2
    if a==3:
        if List[x]==2:
            print("Yes")
        else:
            print("No")
