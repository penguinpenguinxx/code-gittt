N = int(input())
A = list(map(int, input().split()))
import bisect

#円環を2周分の配列として用意
for i in range(N):
 A.append(A[i])

B = [0]*len(A) #累積和を用意
B[0] = A[0]
for i in range(len(A)-1):
 B[i+1] = B[i] + A[i+1]
#print(B)

#10で割り切れなかったらそもそもアウト
if B[N-1] % 10 != 0:
 exit(print("No"))

#目標値
num = B[N-1] // 10

for i in range(N):
 j = bisect.bisect_left(B, num + B[i])
 if B[j] - B[i] == num:
   exit(print("Yes"))
   
print("No")