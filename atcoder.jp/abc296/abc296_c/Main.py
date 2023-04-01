from bisect import bisect_left  #Listの要素の中で何番目がBを最も近いかをxが取得

N,X=map(int,input().split())
List=list(map(int,input().split()))
List.sort()

for i in range(N):
    x = bisect_left(List, List[i]+X)
    if x==N:
        pass
    elif List[x]==List[i]+X:
        exit(print("Yes"))
print('No')