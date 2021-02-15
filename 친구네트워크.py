# https://www.acmicpc.net/problem/4195

import sys

sys.stdin = open('input.txt', 'r')


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
    number[b] += number[a]



for _ in range(int(sys.stdin.readline())):
    parent = {}
    number = {}

    F = int(sys.stdin.readline())
    for i in range(F):
        A, B = map(str, sys.stdin.readline().split())

        if A not in parent:
            parent[A] = A
            number[A] =1
        if B not in parent:
            parent[B] = B
            number[B] =1

        merge(A, B)

        print(number[find(A)])