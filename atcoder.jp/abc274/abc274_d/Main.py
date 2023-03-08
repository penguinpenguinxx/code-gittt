from collections import deque
N,x,y=map(int,input().split())
List=list(map(int,input().split()))
LLL=[]
que=deque()
que.append(0)
LLL.append(que)
que=deque()
que.append(List[0])
LLL.append(que)

for i in range(2,N+1):
    que=deque()
    set1=set()
    while LLL[i-2]:
        k=LLL[i-2].popleft()
        if k+List[i-1] not in set1:
            set1.add(k+List[i-1])
            que.append(k+List[i-1])
        if k-List[i-1] not in set1:
            set1.add(k-List[i-1])
            que.append(k-List[i-1])
#    print(que)
    LLL.append(que)
#print(LLL)
if N%2==0:
    ans2=x
    ans1=y 
else:
    ans2=y
    ans1=x
count=0
while LLL[N-1]:
    z=LLL[N-1].popleft()
    if ans2==z:
        count+=1
        break
while LLL[N]:
    z=LLL[N].popleft()
    if ans1==z:
        count+=1
        break
if count==2:
    print('Yes')
else:
    print('No')