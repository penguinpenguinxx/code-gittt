import math

def eratosthenes_sieve(n):  #篩_計算量O(NloglogN)とても高速、nで指定した値までTrue ,Falseで返す
    is_prime = [True]*(n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, n + 1):
#        print(p)
        if is_prime[p]:
            for q in range(2*p, n + 1, p):
                is_prime[q] = False
    return is_prime

List=eratosthenes_sieve(3*10**5)
Primenum=[]
P=[]
num=0
for i in range(3*10**5):
    if List[i]==True:
        num+=1
        P.append(i)
    Primenum.append(num)
#print(P)

l=int(input())
ans=0
num=0
for i in range(len(P)):
    for j in range(i+1,len(P)):
        num=P[i]*P[i]
        num*=P[j]
        N=int(math.sqrt(l/num))
        if N<P[j]:
            if j==i+1:
                exit(print(ans))
            break
        #print(P[i],P[j],N)
        ans+=Primenum[N]-Primenum[P[j]]
