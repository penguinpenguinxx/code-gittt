from bisect import bisect_left
N=int(input())
A=list(map(int,input().split()))

M=int(input())
List=list(map(int,input().split()))
X=int(input())

dp=["False"]*(X+1)
dp[0]="True"

for i in range(X):
    x = bisect_left(List, i+1)
    if x>=M :
        for j in range(N):
            if A[j]<=i+1:
                if dp[i+1]=="True":
                    break
                if dp[i+1-A[j]]=="True":
                    dp[i+1]="True"
    elif i+1==List[x]:
        pass
    else:
        for j in range(N):
            if A[j]<=i+1:
                if dp[i+1]=="True":
                    break
                if dp[i+1-A[j]]=="True":
                    dp[i+1]="True"



if dp[X]=="True":
    print("Yes")
else:
    print("No")