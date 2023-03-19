H,W=map(int,input().split())

for i in range(H):
    word=''
    List=list(map(int,input().split()))
    for j in List:
        if j == 0:
            word+='.'
        else:
#            print(j,chr(j+64))
            word+=chr(j+64)
    print(word)