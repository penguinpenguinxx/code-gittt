Li = list(map(int,input().split()))
N=Li[0]
A=Li[1]
B=Li[2]
result=0
for i in range(1,N+1):
  num=0
  List1 =list(map(int, str(i)))
  for j in range(len(List1)):
    num+=List1[j]
  if num>=A and num<=B:
    result+=i
print(result)