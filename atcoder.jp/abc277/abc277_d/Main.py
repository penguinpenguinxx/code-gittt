N,M=map(int,input().split())
List=list(map(int,input().split()))

sum=sum(List)
List.sort()
List=List+List

ans=[]
num=List[0]
for i in range(2*N-1):
    if List[i+1]==List[i] or (List[i+1])%M==(List[i]+1)%M:
        num+=List[i+1]
        if i==2*N-2:
            ans.append(num)
    else:
        ans.append(num)
        num=List[i+1]
num=max(ans)
#print(sum)
if num>=sum:
    exit(print(0))
print(sum-num)