N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

count_a=[0]*46
count_b=[0]*46
count_c=[0]*46

for i in range(N):
    count_a[A[i]%46]+=1
    count_b[B[i]%46]+=1
    count_c[C[i]%46]+=1
num=0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46==0:
                num+=count_a[i]*count_b[j]*count_c[k]
print(num)