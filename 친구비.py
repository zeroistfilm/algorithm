# https://www.acmicpc.net/problem/16562

import sys

sys.stdin = open('input.txt', 'r')
N, M, k = map(int, sys.stdin.readline().split())
pays = list(map(int, sys.stdin.readline().split()))

friends = []
paylist = []
result = 0

for i in range(M):
    friends.append(list(map(int, sys.stdin.readline().split())))

parent = [0 for i in range(N + 1)]
for i in range(N + 1):
    parent[i] = i

def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(a, b):
    a = find(a)
    b = find(b)
    if (a == b):
        return
    parent[a] = b

for friend in friends:
    if pays[friend[0] - 1] > pays[friend[1] - 1]:
        merge(friend[0], friend[1])
    else:
        merge(friend[1], friend[0])

tmp = list(set([find(i) for i in parent[1:]]))

for i in range(len(tmp)):
    for j in range(1, N + 1):
        if tmp[i] == parent[j]:
            paylist.append(pays[j - 1])
    result += min(paylist)
    paylist = []

if result <= k:
    print(result)
else:
    print("Oh no")