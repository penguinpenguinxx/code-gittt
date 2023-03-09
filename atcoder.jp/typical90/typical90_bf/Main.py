N,K=map(int,input().split())
N=str(N)
num=int(N)
start=str(N)
List=['False']*(100000)
if K<1000000:
    for j in range(K):
        for i in range(len(N)):
            num+=int(N[i])
        num%=100000
        N=str(num)
    exit(print(num))


for j in range(K):
    for i in range(len(N)):
        num+=int(N[i])
    num%=100000
#    print(num)
    if List[num]=='False':
        List[num]='True'
        N=str(num)
    else:
        count=j
        fini=num
        break

N=start
num=int(N)
for j in range(K):
    for i in range(len(N)):
        num+=int(N[i])
    num%=100000
    if num==fini:
        count2=j
        break
    N=str(num)


K=count+(K-count)%(count-count2)
N=start
num=int(N)
for j in range(K):
    for i in range(len(N)):
        num+=int(N[i])
    num%=100000
    N=str(num)

print(num)