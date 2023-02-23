N,K=map(int,input().split())
List=[]
for i in range(N):
    A,B=map(int,input().split())
    C=A-B  #CはBより下
    List.append(B)
    List.append(C)

List.sort(reverse=True)

num=0
for j in range(K):
    num+=List[j]
print(num)