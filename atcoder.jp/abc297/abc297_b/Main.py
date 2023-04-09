s=input()
num=0
count=0
for j in range(len(s)):
    if s[j]=="B":
        num+=j
    if s[j]=="R":
        count+=1
    if s[j]=="K":
        if count!=1:
            exit(print("No"))
        


if num%2==0:
    exit(print("No"))

print("Yes")