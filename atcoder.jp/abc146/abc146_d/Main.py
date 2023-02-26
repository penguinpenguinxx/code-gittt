from collections import deque
 
n = int(input())
x = [[] for _ in range(n)]  # 隣接リスト
a, b = [[] for _ in range(n)], [[] for _ in range(n)]
for i in range(n - 1):
    a[i], b[i] = map(int, input().split())
    a[i], b[i] = a[i] - 1, b[i] - 1
    x[a[i]].append((b[i], i))
    x[b[i]].append((a[i], i))  # 辺のidex を0index でタプルで保持
# 0 からdfs
edge = [0] * (n - 1)  # 各辺の色を1 indexで持つ
parent = [-1] * (n)  # それぞれの頂点が親からの辺の色を持つ
q = deque()
q.append(0)
num_color = 0
# 頂点でBFS
while q:
    now = q.popleft()
    color = 1
    ng_color = parent[now]
    for v, e in x[now]:
        if edge[e] == 0:
            if color == ng_color:
                color += 1  # 親からの辺と同じ色になったら変える
            num_color = max(num_color, color)
            edge[e] = color
            parent[v] = color
            color += 1
            q.append(v)
print(num_color)
for i in range(n - 1):
    print(edge[i])