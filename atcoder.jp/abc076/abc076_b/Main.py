N=int(input())
K=int(input())

ans=1
for i in range(N):
  ans1=2*ans
  ans2=ans+K
  if ans1>ans2:
    ans=ans2
  else:
    ans=ans1

print(ans)