Li = list(map(int,input().split()))
N=Li[0]
Y=Li[1]/1000
for i in range(0,N+1):
  num=0
  num+=10*i
  for j in range(0,N+1-i):
    num+=5*j
    num+=1*(N-i-j)
    if num==Y:
      print(i,j,N-i-j)
      break
    num=10*i
  else:
    if i==N:
      print(-1,-1,-1)
    continue
  break