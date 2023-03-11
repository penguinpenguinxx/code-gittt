from typing import *


def main():
    # 入力受け取り
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    # DPテーブル
    dp: List[List[int]] = [[-(1 << 60) for j in range(M + 1)] for i in range(N + 1)]
    # 初期条件
    for i in range(N + 1):
        dp[i][0] = 0

    # 遷移
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # i番目の要素を選ばないとき
            dp[i][j] = dp[i - 1][j]
            # i番目の要素を選ぶとき
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + j * A[i - 1])

    # 答えの出力
    print(dp[N][M])


if __name__ == "__main__":
    main()