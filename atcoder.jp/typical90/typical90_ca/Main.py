H,W=map(int,input().split())
matrixA = [list(map(int,input().split())) for _ in range(H)]
matrixB = [list(map(int,input().split())) for _ in range(H)]

matrixC=[[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        matrixC[i][j]=matrixB[i][j]-matrixA[i][j]


count=0
for i in range(H-1):
    for j in range(W-1):
        count+=abs(matrixC[i][j])
        matrixC[i][j+1]-=matrixC[i][j]
        matrixC[i+1][j]-=matrixC[i][j]
        matrixC[i+1][j+1]-=matrixC[i][j]
        matrixC[i][j]-=matrixC[i][j]
        if i==H-2:
            if matrixC[i+1][j]!=0:
                exit(print("No"))
            if j==W-2:
                if matrixC[i+1][j+1]!=0:
                    exit(print("No"))
print("Yes")
print(count)