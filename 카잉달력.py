#https://www.acmicpc.net/problem/6064

import sys

sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline().strip())

for i in range(T):
    test = list(map(int, sys.stdin.readline().split()))

