N=int(input())
List = list(map(int,input().split())) 

List.sort()

List3=List[N:5*N]

List4=List3[0:3*N]

num=0
for i in range(len(List4)):
    num+=List4[i]

print(num/(3*N))