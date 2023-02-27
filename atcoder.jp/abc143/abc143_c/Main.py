N=int(input())
S=input()
if S[N-1]=="a":
    S+="b"
else:
    S+="a"
word=""
for i in range(N):
    if S[i+1]==S[i]:
        pass
    else:
        word+=S[i]

print(len(word))