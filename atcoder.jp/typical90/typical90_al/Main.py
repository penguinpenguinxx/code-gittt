import math

a, b = map(int,input().split())
l=math.gcd(a,b)
ans=a//l*b
if ans>10**18:
    print("Large")
else:
    print(ans)