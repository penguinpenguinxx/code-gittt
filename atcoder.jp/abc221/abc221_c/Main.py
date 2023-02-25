N=int(input())
N=str(N)
digit=len(N)

from itertools import product
ans=[]
for i in product([0, 1], repeat = digit):
    word1=""
    word2=""
    for j in range(digit):
        if i[j]==0:
            word1+=N[j]
        if i[j]==1:
            word2+=N[j]
    if word1.count('0')==len(word1):
        pass
    elif word2.count('0')==len(word2):
        pass
    else:
        word1N=sorted(word1,reverse=True)
        word1L=""
        for i in range(len(word1N)):
            word1L+=str(word1N[i])
            word1LL=int(word1L)
        word2N=sorted(word2,reverse=True)
        word2L=""
        for i in range(len(word2N)):
            word2L+=str(word2N[i])
            word2LL=int(word2L)
        ans.append(word1LL*word2LL)
print(max(ans))