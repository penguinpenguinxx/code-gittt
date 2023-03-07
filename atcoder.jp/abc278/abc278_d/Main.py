## 辞書型を用いた
## 初期化する情報をgのkeyに保持してもらった
## 値を急に打ち込んでも対応してくれるみたい
## 疎になりそうな時に特に有効だと思われる

from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
g = 0
base = 0
diff = defaultdict(int)

q = int(input())
for i in range(q):
    t = list(map(int, input().split()))
    if t[0] == 1:
        g += 1
        base = t[1]
    elif t[0] == 2:
        diff[(g, t[1])] += t[2]  #差分だけ加えていく
    else:
        if g > 0:
            print(base + diff[(g, t[1])])
        else:
            print(a[t[1] - 1] + diff[(g, t[1])])  #最初の情報だけ重要