H,W=map(int,input().split())
for i in range(H):
    s=input()
    count=0
    PC=0
    for j in range(len(s)):
        if s[j]=="T":
            count+=1
        if count==2:
            PC+=1
            count=0
            word=""
            for k in range(len(s)):
                if k==j-1:
                    word+="P"
                elif k==j:
                    word+="C"
                else:
                    word+=s[k]
            s=word
        if s[j]==".":
            count=0
    print(s)