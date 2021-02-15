# https://www.acmicpc.net/problem/11660
import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
table = []
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        table.append(tmp[i])

checklist = [list(map(int, sys.stdin.readline().split())) for i in range(M)]

dp = [0 for _ in range(N ** 2 + 1)]

for i in range(1, N ** 2 + 1):
    dp[i] = dp[i - 1] + table[i - 1]


for check in checklist:
    x1, y1, x2, y2 = map(int, check)
    result = 0

    if (x2-x1==0 and y2-y1==0)or (x1==1 and y2==N):
        start = (x1 - 1) * N + y1
        end = (x2 - 1) * N + y2
        print(dp[end] - dp[start - 1])
    elif(y2 ==N):
        for i in range(y2 - y1):
            a = dp[(x2 - 1 - i) * N + y2]
            result += a
            b = dp[(x2 - x1 - i+1) * N + (y1 - 1)]
            result -= b
        print(result)
    elif (y2 != N):
        for i in range(y2 - y1):
            a = dp[(x2 - 1 - i) * N + y2]
            result += a
            b = dp[(x2 - x1 - i) * N + (y1 - 1)]
            result -= b
        print(result)