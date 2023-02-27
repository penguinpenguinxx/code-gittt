N=int(input())
s=input()
s=list(s)
q=int(input())

count=0
for i in range(q):
    t,a,b=map(int,input().split())
    if t==1:
        s[((a-1)+(N)*count)%(2*N)],s[((b-1)+(N)*count)%(2*N)]=s[((b-1)+(N)*count)%(2*N)],s[((a-1)+(N)*count)%(2*N)]

    if t==2:
        count+=1
word=""
for i in range(2*N):
    word+=s[(i+(N)*count)%(2*N)]

print(word)