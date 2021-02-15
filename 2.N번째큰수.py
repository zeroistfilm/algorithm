# https://www.acmicpc.net/problem/2075

import sys
import heapq
N = int(sys.stdin.readline().strip())

result=[]
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))

    for i in tmp:
        if len(result)<N:
            heapq.heappush(result,i)
        else:
            if result[0]<i:
                heapq.heappop(result)
                heapq.heappush(result, i)

print(heapq.heappop(result))