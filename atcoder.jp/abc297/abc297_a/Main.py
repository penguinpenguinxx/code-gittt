N,D=map(int,input().split())

List=list(map(int,input().split()))

for i in range(len(List)-1):
    diff=List[i+1]-List[i]
    if diff<=D:
        exit(print(List[i+1]))


print(-1)