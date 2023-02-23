import numpy as np

T = int(input())
L,X,Y = map(int,input().split())
Q = int(input())
for i in range(Q):
    E=int(input())
    y=-L/2*np.sin(E/T*2*np.pi)
    z=L/2*(1-np.cos(E/T*2*np.pi))
    l=np.sqrt(np.square(X)+np.square(Y-y))
    theta=np.arctan(z/l)*360/(2*np.pi)
    print(theta)