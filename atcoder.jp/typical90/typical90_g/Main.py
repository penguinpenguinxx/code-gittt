from bisect import bisect_left

n = int(input())
List = list(map(int,input().split()))	
Q = int(input())
List.sort()

for i in range(Q):
    B=int(input())
    x = bisect_left(List, B)
    if x == 0: # １番小さい場合は配列Aの最小値とb[i]との差を取る
        print(List[0] - B)
    elif x == n: # 配列外参照になってしまうので、b[i]と配列Aの最小値との差をとる
        print(B - List[-1])
    else:
        print(min(B - List[x - 1], List[x] - B))