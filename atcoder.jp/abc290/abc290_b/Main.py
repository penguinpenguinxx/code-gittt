N,K=map(int,input().split())
S=input()
word=""
count=0
for i in range(len(S)):
    if S[i]=="o":
        count+=1
        if count>K:
            word+="x"
        else:
            word+="o"
    else:
        word+="x"
print(word)