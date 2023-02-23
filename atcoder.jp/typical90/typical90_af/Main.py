from itertools import permutations


N=int(input())
List = [list(map(int,input().split())) for h in range(N)]

M=int(input())
List2 = [list(map(int,input().split())) for h in range(M)]

grid=[[True]*N for _ in range(N)]

for i in range(M):
    grid[List2[i][0]-1][List2[i][1]-1]=False
    grid[List2[i][1]-1][List2[i][0]-1]=False

ans=[]

for i in permutations(range(N),N):
    Bool=True

    between=[]
    for j in range(N-1):
        if not grid[i[j]][i[j+1]]:
            Bool = False
            break
    num=0
    for j in range(N):
        num+=List[i[j]][j]
    
    if not Bool:
        num=10**5
        
    ans.append(num)

if min(ans)==10**5:
    print(-1)
else:
    print(min(ans))