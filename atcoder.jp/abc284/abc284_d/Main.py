## 素因数分解系
## N=qqpの形でかける問題
import math

T=int(input())
for i in range(T):
    N=int(input())
    for j in range(2,int(math.sqrt(N)//1)):
        if N%j==0:
            Ncon=N//j
            if Ncon%j==0:
                print(j,int(Ncon//j))
                break
            else:
                a=math.sqrt(Ncon)
                if a%1==0:
                    print(int(a),int(j))
                    break