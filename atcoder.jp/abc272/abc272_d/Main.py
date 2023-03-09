import math
from collections import deque

N,M=map(int,input().split())

List=[]
set1=set()
for i in range(0,int(math.sqrt(M)//1)+1):
    x=M-i*i
#    print(i,x,math.sqrt(x))
    if math.sqrt(x)%1==0:
        if tuple([i,int(math.sqrt(x))]) not in set1:
            List.append([i,int(math.sqrt(x))])
            set1.add(tuple([i,int(math.sqrt(x))]))
        if tuple([-i,int(math.sqrt(x))]) not in set1:
            List.append([-i,int(math.sqrt(x))])
            set1.add(tuple([-i,int(math.sqrt(x))]))
        if tuple([i,-int(math.sqrt(x))]) not in set1:
            List.append([i,-int(math.sqrt(x))])
            set1.add(tuple([i,-int(math.sqrt(x))]))
        if tuple([-i,-int(math.sqrt(x))]) not in set1:
            List.append([-i,-int(math.sqrt(x))])
            set1.add(tuple([-i,-int(math.sqrt(x))]))
        if tuple([int(math.sqrt(x)),i]) not in set1:
            List.append([int(math.sqrt(x)),i])
            set1.add(tuple([int(math.sqrt(x)),i]))
        if tuple([-int(math.sqrt(x)),i]) not in set1:
            List.append([-int(math.sqrt(x)),i])
            set1.add(tuple([-int(math.sqrt(x)),i]))
        if tuple([int(math.sqrt(x)),-i]) not in set1:
            List.append([int(math.sqrt(x)),-i])
            set1.add(tuple([int(math.sqrt(x)),-i]))
        if tuple([-int(math.sqrt(x)),-i]) not in set1:
            List.append([-int(math.sqrt(x)),-i])
            set1.add(tuple([-int(math.sqrt(x)),-i]))
#print(List)

dist = [[-1 for i in range(N)] for j in range(N)] 
dist[0][0]=0
que=deque()
que.append([0,0])

while que:
    x, y = que.popleft() # キューから取り出し

    # 現在位置から上下左右に探索
    for i, j in List:
        if x+i >= N or x+i < 0 or y+j >= N or y+j < 0: # 範囲外
            continue
        if dist[x+i][y+j] != -1: # すでに最小手数確定済み
            continue

        dist[x+i][y+j] = dist[x][y] + 1

        que.append([x+i, y+j]) # 次のマスをキューに格納
for i in range(N):
    print(*dist[i],sep=" ")