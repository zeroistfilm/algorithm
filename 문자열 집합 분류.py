import sys

#sys.stdin = open('input.txt', 'r')


def insert(src):
    tmp=T
    for char in src:
        if not char in tmp:
            tmp[char]={}
        tmp = tmp[char]
    tmp['check']=1

def check(src):
    tmp = T
    for char in src:
        if not char in tmp:
            tmp[char]={}
        tmp = tmp[char]
    if 'check' in tmp: #키 존재 체크
       if tmp['check']==1:
            return 1

N, M = map(int, sys.stdin.readline().split())
srcs = []
checks =[]
for i in range(N):
    srcs.append(sys.stdin.readline().split()[0])
for i in range(M):
    checks.append(sys.stdin.readline().split()[0])

T={}
for src in srcs:
    insert(src)

count=0
for scr2 in checks:
    flag=check(scr2)
    if flag :
        count+=1

print(count)