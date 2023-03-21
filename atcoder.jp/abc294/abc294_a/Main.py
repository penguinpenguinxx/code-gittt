N=int(input())

List=list(map(int,input().split()))

#print(List)


LL=[]

for i in List:
    if i%2==0:
        LL.append(i)

print(*LL)