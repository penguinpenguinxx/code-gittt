N,K=map(int,input().split())
S=input()
count=0
for i in range(N-1):
    if S[i+1]!=S[i]:
        count+=1
print(N-1-max(count-2*K,0))