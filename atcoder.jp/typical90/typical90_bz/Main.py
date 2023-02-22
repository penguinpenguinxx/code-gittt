N, M = map(int, input().split())


G=[[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)
#隣接リストの参照方法：リストG[v]の要素をnvとしてそれぞれ探索していく
count=0
for v in range(N):
    num=0
    for nv in G[v]:
        if nv<v:
            num+=1
    if num==1:
        count+=1

print(count)