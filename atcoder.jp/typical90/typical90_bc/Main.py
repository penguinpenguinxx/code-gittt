import sys
from itertools import combinations
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N,P,Q=map(int,input().split())
List=list(map(int,input().split()))

num2=0
for a,b,c,d,e in combinations(List,5):
    if a%P*b%P*c%P*d%P*e%P==Q:
        num2+=1


print(num2)