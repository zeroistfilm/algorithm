# https://www.acmicpc.net/problem/4358

import sys

sys.stdin = open('input.txt', 'r')
Tree={}
treelen = 0
while True:
    tmp = sys.stdin.readline().strip()
    if not tmp =='':
        if not tmp in Tree:
            Tree[tmp]=1
        else:
            value = Tree.get(tmp)
            value +=1
            Tree[tmp] = value
        treelen +=1
    else:
        break

sortedtree = sorted(Tree.items(), key=lambda x: x[0])
for i in range(sortedtree.__len__()):
    print(sortedtree[i][0],'%.4f' % (sortedtree[i][1]/treelen*100))


