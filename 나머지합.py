# https://www.acmicpc.net/problem/10986

import sys

sys.stdin = open('input.txt', 'r')

def solve():
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    dp = [0] * (N + 1)
    tmp = [0] * (M)
    for i in range(1, N + 1):
        dp[i] = (dp[i - 1] + nums[i - 1]) % M
        tmp[dp[i]] += 1
    result = 0
    tmp[0] += 1
    for i in range(len(tmp)):
       result += (tmp[i] * (tmp[i] - 1)) // 2
    print(int(result))
solve()