## 尺取り法
## 基本的にlを固定してrを動かせるところまで動かす
## rが動かないようになると、今度はlが動き出す
## lごとに要素で割っていく(その都度rが進められるかwhileで検索)
## lとrが一緒になった時はS[r]がどうなってもダメなのでr=+1して進めてあげる


N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

if 0 in S:
    # Sに0が含まれている時は、全ての積は0なので0 <= Kなら積は常にK以下。よってNが答え
    print(N)
    exit()

r, ans, tmp = 0, 0, 1

for l in range(N):
    # lを固定してrを、ずらしていく。ループ条件が複数の場合、PythonだとWhileのこの書き方がベストかな
    while (r < N and tmp*S[r] <= K):
        tmp *= S[r]
        r += 1

    ans = max(ans, r-l)
    if l == r:
        r += 1
    else:
        # lが1増えるので、今のlで割っておく
        tmp //= S[l]

print(ans)