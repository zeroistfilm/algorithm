# https://www.acmicpc.net/problem/11659
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
checklist = [list(map(int, sys.stdin.readline().split())) for i in range(M)]
prefix = [0 for i in range(N+1)]
for i in range(1,N+1):
    prefix[i] = prefix[i-1]+nums[i-1]

for check in checklist:
    print(prefix[check[1]]-prefix[check[0]-1])
