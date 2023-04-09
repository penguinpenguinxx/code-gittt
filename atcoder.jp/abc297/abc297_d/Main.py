A,B=map(int,input().split())
count=0
while True:
#    print(A,B)
    if A==B:
        break
    if A>B:
        mul=A//B
        A=A-mul*B
        if A==0:
            A+=B
            mul-=1
        count+=mul
    else:
        mul=B//A
        B=B-mul*A
        if B==0:
            B+=A
            mul-=1
        count+=mul
print(count)