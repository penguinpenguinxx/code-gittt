N=int(input())
S=input()

xcount=0
ycount=0
set1=set()
set1.add(tuple([xcount,ycount]))
for i in range(N):
    if S[i]=="R":
        xcount+=1
    if S[i]=="L":
        xcount-=1
    if S[i]=="U":
        ycount+=1
    if S[i]=="D":
        ycount-=1
    if tuple([xcount,ycount]) in set1:
        exit(print("Yes"))
        
    set1.add(tuple([xcount,ycount]))


print("No")