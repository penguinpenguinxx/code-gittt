from collections import deque
from collections import defaultdict
import heapq

N=int(input())
que=deque()
que.append(N)

List=[N]
heapq.heapify(List)
num=0
num0=0
if N==0:
    exit(print(1))
count = defaultdict(int)
count[N]=1
set1=set()

while List:
    List = list(map(lambda x: x*(-1), List))
#    print(List)
    heapq.heapify(List)
    x=heapq.heappop(List)*(-1)
    List = list(map(lambda x: x*(-1), List))
#    print(x)
    y=x//2
    if y==0:
        count[0]+=count[x]
    elif y in set1:
        count[y] += count[x]
    else:    
        List.append(y)
        set1.add(y)
        count[y]=count[x]
    z=x//3
    if z==0:
        count[0]+=count[x]
    elif z in set1:
        count[z] += count[x]
    else:    
        List.append(z)
        set1.add(z)
        count[z]=count[x]
print(count[0])
#print(count)