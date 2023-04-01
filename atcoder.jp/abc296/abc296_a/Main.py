N=int(input())
S=input()

if N==1:
    exit(print("Yes"))

for i in range(N-1):
    if S[i]==S[i+1]:
        exit(print("No"))
print("Yes")