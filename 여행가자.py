# https://www.acmicpc.net/problem/1976
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
maps = []

for i in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))

plan = list(map(int,sys.stdin.readline().split()))
maxval=max(plan)
parent=[0for i in range(maxval+1)]
level=[0for i in range(maxval+1)]
#init
for city in plan:
    #index = node
    #value = 속해 있는
    parent[int(city)]=int(city)
    level[int(city)]=1

def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(a,b):
    a = find(a)
    b = find(b)
    if (a==b):
        return
    parent[b]=a
    # parent[a]=b

for i in range(1,N+1):
    for j in range(1,N+1):
        if maps[i-1][j-1]==1:
            merge(i,j)

travel=[]
for i in plan:
    travel.append(find(i))
a=set(travel)
if len(set(travel))==1:
    print('YES')
else:
    print('NO')