N=int(input())
List=list(map(int,input().split()))
List.sort()
x=List[0]
all=0
number02=0
number03=0
while True:
    if x%2==0:
        x//=2
        number02+=1
        all+=1
    else:
        break
while True:
    if x%3==0:
        x//=3
        number03+=1
        all+=1
    else:
        break
ans2=number02
ans3=number03
for i in range(1,N):
    number2=0
    number3=0
    z=List[i]//x
    if List[i]%x!=0:
        exit(print(-1))
    while True:
        if z%2==0:
            z//=2
            number2+=1
            all+=1
        else:
#            print({'ans2':ans2,'ab':number2})
            ans2=min(ans2,number2)
            break
    while True:
        if z%3==0:
            z//=3
            number3+=1
            all+=1
        else:
            ans3=min(ans3,number3)
            break
    if z!=1:
        exit(print(-1))
#print(ans2,ans3)
print(all-(ans2+ans3)*N)