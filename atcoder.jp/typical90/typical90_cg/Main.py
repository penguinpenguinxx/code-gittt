from itertools import product

def factorization(n):
    arr = [1]
    tmp = n
    set1=set()
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            arr.append(i)
            set1.add(i)
            if tmp//i not in set1:
                arr.append(tmp//i)
    if tmp != 1:
        arr.append(tmp)
    if arr == []:
        arr.append(n)
    arr.sort()
    return arr
 
K=int(input())
List=factorization(K)
num=0
for i in product(List, repeat = 2):
    if i[0]<=i[1]:
        c=K/(i[0])/(i[1])
        if i[1]<=c:
            if c%1==0:
                num+=1
print(num)