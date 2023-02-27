## 辞書式順序再び


def diff(s,t):
    cnt=0
    for i in range(len(s)):
        if s[i]!=t[i]:
            cnt+=1
    return cnt
 
def Main():
    n,k=map(int,input().split())
    s=input()
    origin=s
    for i in range(n):
        c=s[i]
        pos=-1
        for j in range(i+1,n):
            if s[j]<c:
                temp=s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
                if diff(temp,origin)<=k:
                    c=s[j]
                    pos=j
        if pos>i:
            s=s[:i]+s[pos]+s[i+1:pos]+s[i]+s[pos+1:]
    print(s)
    

Main()