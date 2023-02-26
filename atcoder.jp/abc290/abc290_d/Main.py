## 整数問題。NとDが互いに素かどうかで出力が異なる問題
## 互いに素であれば法Nの下で
##   D 2D 3D 4D ...  (N-1)D が全て異なる値になる
## 互いに素でない場合、最大公約数をgとすると
##   (N/g)*D で一致するのでその際に+1される(tmp1カウントしておく)
##  Dの位置としても L回//(N/g)*D + tmp1 しか進まないことがわかる


import math

t = int(input())
for _ in range(t):
    n, d, k = map(int, input().split())
    g = math.gcd(n, d)
    if g == 1:
        print((k - 1) * d % n)
    else:
        temp1 = (k - 1) // (n // g)
        temp2 = (k - 1) % (n // g) * d
        print((temp1 + temp2) % n)
