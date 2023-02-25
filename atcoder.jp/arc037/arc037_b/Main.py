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


N,M = map(int,input().split())

par = [0 for _ in range(N)]
# 木の深さ
rank = [0 for _ in range(N)]


init(N)

ans=[]

for i in range(M):
    s=0
    a, b = map(int, input().split())
    a=a-1
    b=b-1
    if same(a,b):
        ans.append(find(a))
    unite(a,b)
    
for i in range(N):
    find(i)
set2=set()   
for i in range(len(ans)):
    L=find(ans[i])
    set2.add(L)
set=set()
for i in par:
    set.add(i)

print(len(set)-len(set2))