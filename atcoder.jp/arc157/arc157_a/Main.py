N ,A,B,C,D=map(int,input().split())
if A>1:
    A=1
if D>1:
    D=1
if B>0 and C>0:
    s=abs(B-C)
    if s<2:
        print("Yes")
    else:
        print("No")
elif B==0:
    if C>1:
        print("No")
    elif C==1:
        print("Yes")    
    elif C==0:
        if A==1 and D==1:
            print("No")
        else:
            print("Yes")
elif C==0:
    if B>1:
        print("No")
    elif B==1:
        print("Yes")    
    elif B==0:
        if A==1 and D==1:
            print("No")
        else:
            print("Yes")
