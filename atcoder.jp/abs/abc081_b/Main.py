N=int(input())
Li = list(map(int,input().split()))
num=0
for j in range(0,100):
  for i in range(0,N):
    if Li[i]%2==0:
      Li[i]=int(Li[i]/2)
    else:
      break
    if i==N-1:
      num+=1
  if j==num:
    break
print(num)