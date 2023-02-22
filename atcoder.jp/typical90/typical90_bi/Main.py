from collections import deque

Q=int(input())
List=[]
for i in range(Q):
    List.append(list(map(int,input().split())))

que=deque() #dequeオブジェクトの生成

for j in range(Q):
    if List[j][0]==1:
        que.appendleft(List[j][1])
    elif List[j][0]==2:
        que.append(List[j][1])
    else:
        print(que[List[j][1]-1])
