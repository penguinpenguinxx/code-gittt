N=int(input())
T=input()


num=0
x=0
y=0
for i in range(N):
    if T[i]=="S":
        if num==0:
            x+=1
        if num==1:
            y+=-1
        if num==2:
            x+=-1
        if num==3:
            y+=1
    if T[i]=="R":
        num+=1
        num%=4
print(x,y)