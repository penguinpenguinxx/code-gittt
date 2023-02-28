S = input()
T = input()

l = len(T)
for i in range(len(T)):
    s = S[i]
    t = T[i]
    if s == '?' or t == '?': continue
    if s != t:
        l = i
        break

r = len(T)
for i in range(len(T)):
    s = S[-i - 1]
    t = T[-i - 1]
    if s == '?' or t == '?': continue
    if s != t:
        r = i
        break

for x in range(len(T) + 1):
    if x <= l and len(T) - x <= r:
        print('Yes')
    else:
        print('No')