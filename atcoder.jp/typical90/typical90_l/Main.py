## Union Find
## 各行列に値を持たせる際には(a,b)に対してp[i]=i(i=a*W+b)で指定可能
## 二次元のリストを持たせた場合でもpypyを用いたら通った(時間かかる)

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


H, W = map(int,input().split())

# ノードiの親がpar[i]
par = [0 for _ in range(H*W)]
# 木の深さ
rank = [0 for _ in range(H*W)]

init(H*W)

matrix = [["False"] * W for _ in range(H)]

Q=int(input())

for i in range(Q):
    List= list(map(int, input().split()))
    # pが0ならaとbを併合
    a=List[1]-1
    b=List[2]-1
    # pが0ならaとbを併合
    if List[0] == 1:
        matrix[a][b]="True"
        if a>0:
            if matrix[a-1][b]=="True":
                unite(a*W+b,(a-1)*W+b)
        if a<H-1:
            if matrix[a+1][b]=="True":
                unite(a*W+b,(a+1)*W+b)
        if b>0:
            if matrix[a][b-1]=="True":
                unite(a*W+b,a*W+b-1)
        if b<W-1:
            if matrix[a][b+1]=="True":
                unite(a*W+b,a*W+b+1)
    elif List[1]==List[3] and List[2]==List[4]:
        if matrix[a][b]=="True":
            print("Yes")
        else:
            print("No")
    else:
        if same(a*W+b,(List[3]-1)*W+List[4]-1):
            print("Yes")
        else:
            print("No")