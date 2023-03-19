N,Q=map(int,input().split())

set1=set()
List=[]
for i in range(N):
    List.append(i+1)

k=0
j=0
for i in range(Q):
    q=list(map(int,input().split()))
    if q[0]==1:
        number=List[k]
        k+=1
    if q[0]==2:
        set1.add(q[1])
    if q[0]==3:
        bool='False'
        while bool:
            if List[j] not in set1:
                print(List[j])
                break
            else:
                j+=1