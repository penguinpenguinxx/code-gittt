N=int(input())
set1=set()
num=0
for i in range(N):
    s=input()
    set1.add(tuple(list(s)))
    if s[0]=='!':
        snew=s[1:]
    if s[0]!='!':
        snew='!'+s
    if tuple(list(snew)) in set1: 
        num=1
        break

if num==1:
    if s[0]=='!':
        s=s[1:]
    
    print(s)
else: 
    print("satisfiable")