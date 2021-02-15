# https://www.acmicpc.net/problem/2003

import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

count = 0
start = 0
end = 0
numsum = num[end]
def visual(num,start,end):
    print(" ", end='')
    print("")
    print("  "*(start),end='')
    print("S")
    print("", end='')
    print("  "*(end),end='')
    print("E")
    for i in range(len(num)):
        print(num[i],end='')
        print(" ", end='')
    print("")
    print("numsum: ",numsum)

while end < N: #end가 먼저 끝지점에 도달했을 때에도 종료 가

    visual(num,start,end)
    if numsum >= M:
        start += 1
        if numsum == M:
            count += 1
        numsum-=num[start-1]
    else:
        end += 1
        if end==N:
            break
        numsum += num[end]

# print("")
print(count)
