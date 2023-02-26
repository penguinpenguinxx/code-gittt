S=input()

word=""
for i in range(len(S)):
    word=S[i]
    if word.isupper():
        print(i+1)