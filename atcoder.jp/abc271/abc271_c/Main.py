from typing import *
import collections

def main():
    # 入力受け取り
    N: int = int(input())
    # Aは受け取った段階でソートしておく
    A: List[int] = sorted(list(map(int, input().split())))

    # 一意な数値だけを集めるリストB
    B: List[int] = []
    # 重複した余りを集めるリストC
    C: List[int] = []
    # 既に現れた数値を記録しておく集合S
    S: Set[int] = set()
    # 昇順にソートしたリストAを順に見ていく
    for a in A:
        # 既に要素aが現れていたなら、Cに格納する
        if a in S:
            C.append(a)
        else:
            # そうでないなら、Bに格納する
            B.append(a)
            S.add(a)

    # Bの後ろにCを結合する
    B.extend(C)
    # Bを元に両端キューを作る
    D = collections.deque(B)

    # 次に見る巻の数値を保持する変数current
    current: int = 1
    # 答え
    answer: int = 0
    # キューが空になるまで繰り返す
    while D:
        # キューの先頭が、次に見る巻ならばそれを1つ取り除く
        if D[0] == current:
            D.popleft()
            answer += 1
            current += 1
        else:
            # そうでない場合、後ろの2冊を売って目的の巻を入手し、それを読む
            if len(D) >= 2:
                D.pop()
                D.pop()
                answer += 1
                current += 1
            else:
                # 売る本が無ければそこで終了する
                break

    # 解答出力
    print(answer)


if __name__ == "__main__":
    main()