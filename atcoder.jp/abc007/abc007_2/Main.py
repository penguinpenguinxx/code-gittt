s = input()
if len(s) > 1:
    print(s[:len(s)-1])
else:
    if s == "a":
        print(-1)
    else:
        a = ord(s)
        print(chr(a-1))