## Union Find
from collections import defaultdict
# 初期化
def init(n):
    for i in range(n):
        # 初期化では自身を親とする
        par[i] = i
        # rankは0
        rank[i]= 0
 
# 木の根を求める
def find(x):
    # 自身が親なら自身の番号を返す
    if par[x] == x:
        return x
    else:
        # 根を張り替える
        par[x] = find(par[x])
        return par[x]
 
# xとyの属する集合を併合
def unite(x,y):
    root_x = find(x)
    root_y = find(y)
    # 同じグループの場合
    if root_x == root_y:
        return
    # ランクの大きいほうの根に小さいほうの根をつなぐ
    if rank[root_x] < rank[root_y]:
        par[root_x] = root_y
    else:
        par[root_y] = root_x
        # ランクが同じ場合は1だけ増加
        if rank[x] == rank[y]:
            rank[x] += 1
 
# xとyが同じ集団か
def same(x,y):
    return find(x) == find(y)
 
def members(x):
    root = find(x)
    return [i for i in range(self.n) if find(i) == root]
 
 
def all_group_members():
    group_members = defaultdict(list)
    for member in range(N):
        group_members[find(member)].append(member)
    return group_members
 
 
N,M = map(int,input().split())
#if N==1 and M==1:
#    exit(print("Yes"))
max_num = int(1e7)
# ノードiの親がpar[i]
par = [0 for _ in range(max_num)]
# 木の深さ
rank = [0 for _ in range(max_num)]
 
 
init(N)
 
DDD=[0]*(N+1)
 
for i in range(M):
    a, b = map(int, input().split())
    a=a-1
    b=b-1
    # pが0ならaとbを併合
    unite(a, b)
    DDD[a]+=1
 
#print(all_group_members().values())
#print(DDD)

for i in all_group_members().values():
    num=0
    for j in i:
        num+=DDD[j]
    if num!=len(i):
        exit(print("No"))
 
print("Yes")