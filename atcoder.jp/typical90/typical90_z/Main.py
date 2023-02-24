import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

N=int(input())

G=[[] for i in range(N)] #Nは頂点の数
for i in range(N-1): #Mはつなぐ辺の数
    a, b = map(int, input().split())
    a, b = a - 1, b - 1  #頂点番号はリストで参照するので-1
    G[a].append(b)
    G[b].append(a)

cnt = [10**4]*N

# 深さ優先探索
def dfs(x,s):
    cnt[x]=s
    for nv in G[x]:
        if cnt[nv]==10**4:
            dfs(nv,-s)

dfs(0,1) # スタート位置から深さ優先探索
List=[]
if cnt.count(1)<=cnt.count(-1):
    ss=-1
if cnt.count(1)>cnt.count(-1):
    ss=1
for i in range(len(cnt)):
    if cnt[i]==ss:
        List.append(i+1)
print(*List[0:N//2])