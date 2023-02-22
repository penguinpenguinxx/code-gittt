import collections
N=int(input())
set1=set()
ans=[]
for i in range(N):
    word=input()
    if word not in set1:
        ans.append(i+1)
    set1.add(word)

print(*ans,sep="\n")