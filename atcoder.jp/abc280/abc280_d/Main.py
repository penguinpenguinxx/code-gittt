def calc_factorial_num(x,y):
    cnt=0
    for i in range(x, x ** y + 1, x):
        n = i
        while n % x == 0:
            n //= x
            cnt += 1
        if cnt >= y:
            return i


import math
K=int(input())
List=[[0]*(2) for i in range(int(math.sqrt(K)//1)+1)]
ans=0
for j in range(2,int(math.sqrt(K)//1)+1):
    num=0
    while True:
        if K%j!=0:
            List[j][0]=j
            List[j][1]=num
            if num!=0:
                nnn=calc_factorial_num(j,num)
            else:
                nnn=0
            ans=max(ans,nnn)
            break
        K/=j
        num+=1
if K!=1:
    exit(print(int(K)))
if ans==0:
    exit(print(K))
print(ans)