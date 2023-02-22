##幅優先探索(Queを使う)

from collections import deque

def DFS(s):
    dist=[-1]*N
    dist[s]=0
    que = deque()
    que.append(s)
    while que:
        v = que.popleft() # キューから取り出し
        for nv in G[v]:
            if dist[nv]==-1:
                que.append(nv)
                dist[nv]=dist[v]+1
    return dist

from collections import deque

N=int(input())
G=[[] for i in range(N)]   ##隣接リスト
for i in range(N-1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

s=0
dist0 = DFS(s)
index = dist0.index(max(dist0))
# その点からさらに最も遠い点を求め、長さを直径とする
r_dist = DFS(index)
print(max(r_dist)+1)