import math

A,B,C = map(int,input().split())

X=math.gcd(A,B)
Y=math.gcd(X,C)
 
print((A+B+C)//Y-3)