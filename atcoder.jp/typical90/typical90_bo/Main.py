N,K =map(int,input().split())
N=str(N)
if N=="0":
    exit(print(0))
 
for _ in range(K):
    num=0
    for i in range(len(N)):
        num+=int(N[-(i+1)])*(8**(i))

    num=int(N,8)
 
    List=[]

    while num>0:
        digit=num%9
        List.append(int(digit))
        num=num//9
        
    word=''
    for i in range(len(List)):
        word+=str(List[(len(List)-1-i)])

    N = word.replace("8", "5")

 
 
print(N)