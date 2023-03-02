from collections import deque
S=input()
box=set()
List=[]
cnt=-1
que=deque()
for i in range(len(S)):
    if S[i]=='(':
        que.appendleft(set())
        cnt+=1
    elif S[i]==')':
        A=que.popleft()
        box-=A
    else:
        if S[i] in box:
            exit(print("No"))
        if cnt!=-1:
            que[0].add(S[i])
        box.add(S[i])
print("Yes")