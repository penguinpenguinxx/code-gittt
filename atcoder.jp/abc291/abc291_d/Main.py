
import sys
input = sys.stdin.readline
  
N=int(input())
A1,B1=map(int, input().split())
if N==1:
    exit(print(2))
AA=1
BB=1
mod=998244353
for i in range(1,N):
    A2,B2=map(int, input().split())
    numA,numB=0,0
    if A1!=A2:
        numA+=AA
    if B1!=A2:
        numA+=BB
    if A1!=B2:
        numB+=AA  
    if B1!=B2:
        numB+=BB  
    A1,B1=A2,B2
    AA,BB=numA,numB
    AA%=mod
    BB%=mod
    numA%=mod
    numB%=mod
 
print((numA+numB)%mod)