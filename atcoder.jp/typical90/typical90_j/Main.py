##累積和の問題、先に計算することでループから減らす

n = int(input())
c, p = [0] * n, [0] * n
for i in range(n):
    c[i], p[i] = map(int,input().split())

one=[0]*(n+1)
two=[0]*(n+1)
# 累積和を取っていく
# 1組の p[i] までの和が one[i+1] に入っているようにする
# one[6]=sigma_p[i](i=0-5)
for i in range(n):
    one[i + 1] += one[i]
    two[i + 1] += two[i]

    if c[i] == 1:
        one[i + 1] += p[i]
    else:
        two[i + 1] += p[i]

Q = int(input())
for i in range(Q):
    l, r = map(int,input().split())
    print(one[r] - one[l - 1], two[r] - two[l - 1])