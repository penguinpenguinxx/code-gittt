for j in range(8):
    S=input()
    for i in range(8):
        if S[i]=='*':
            if i ==0:
                ans='a'
            if i ==1:
                ans='b'
            if i ==2:
                ans='c'
            if i ==3:
                ans='d'
            if i ==4:
                ans='e'
            if i ==5:
                ans='f'
            if i ==6:
                ans='g'
            if i ==7:
                ans='h'

            exit(print(ans,8-j,sep=''))