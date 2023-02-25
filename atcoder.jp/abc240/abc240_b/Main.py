N=int(input())
List=list(map(int,input().split()))

set=set()
for i in List:
    if i in set:
        pass
    else:
        set.add(i)
print(len(set))