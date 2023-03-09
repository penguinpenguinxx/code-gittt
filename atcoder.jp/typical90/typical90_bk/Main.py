def main():
    import sys
    from collections import Counter
    from itertools import product
    sys.setrecursionlimit(10 ** 9)
    input = sys.stdin.readline

    H, W = map(int, input().split())
    GRID = [list(map(int, input().split())) for _ in range(H)]

    # 行をビット全探索
    patterns = product((False, True), repeat=H)
    ans = 0
    for p in patterns:
        select_h = []  # 選択する行のリスト
        for i in range(H):
            if p[i]:
                select_h.append(i)

        # 選択する行が0または1行のみの場合の処理
        if len(select_h) == 0:  # 0は特に処理なし
            continue
        if len(select_h) == 1:  # 1行の場合は一番出現回数が多い文字を調べる
            c = Counter(GRID[select_h[0]])
            ans = max(ans, c.most_common()[0][1])
            continue

        # 選択する行が2行以上の場合の処理
        cnt_w = dict()
        for w in range(W):  # 列を1つずつ見ていって、選択した全ての行で同じ文字だった場合にcnt_wの値を増やす
            val = GRID[select_h[0]][w]
            if not all(GRID[h][w] == val for h in select_h):
                continue
            if val in cnt_w:
                cnt_w[val] += 1
            else:
                cnt_w[val] = 1

        if not cnt_w:
            max_w = 0
        else:
            max_w = max(cnt_w.values())
        ans = max(ans, len(select_h)*max_w)
    print(ans)


if __name__ == '__main__':
    main()