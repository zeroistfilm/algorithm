# https://www.acmicpc.net/problem/2096

import sys

N = int(sys.stdin.readline())

#dp=[[[0,0] for i in range(N)]for i in range(N)]
beforedp = [[0,0] for i in range(3)]
afterdp = [[0,0] for i in range(3)]
for i in range(N):

    A= list(map(int, sys.stdin.readline().split()))
    for j in range(3):

        if j==0:
            minval = min(beforedp[j][0] + A[j], beforedp[j + 1][0] + A[j])
            maxval = max(beforedp[j][1] + A[j], beforedp[j + 1][1] + A[j])

        elif j==2:
            minval = min(beforedp[j - 1][0] + A[j], beforedp[j][0] + A[j])
            maxval = max(beforedp[j - 1][1]+ A[j], beforedp[j][1] + A[j])

        elif j==1:
            minval=min(beforedp[j-1][0]+A[j], beforedp[j][0]+A[j], beforedp[j+1][0]+A[j])
            maxval=max(beforedp[j-1][1]+A[j], beforedp[j][1]+A[j], beforedp[j+1][1]+A[j])

        afterdp[j]=[minval,maxval]
    beforedp = afterdp[:]


max=0
min=sys.maxsize
for i in range(3):
    for j in range(2):
        if afterdp[i][j]<min:
            min = afterdp[i][j]
        if afterdp[i][j]>max:
            max = afterdp[i][j]

print(max,min)