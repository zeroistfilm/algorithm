# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque
# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque
import math
def solution(progresses, speeds):
    remain = deque([])
    answer = []
    for i in range(len(progresses)):
        remain.append(math.ceil((100-progresses[i])/speeds[i]))

    j=1
    while True:
        if len(remain)<=j:
            answer.append(j)
            break

        if remain[0]>=remain[j]:
            j+=1
        else:
            answer.append(j)
            for i in range(j):
                remain.popleft()
            j=1
    return answer


print(solution([5, 5, 5], [21, 25, 20]))
print(solution([99, 1, 99, 1], [1, 1, 1, 1]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([93, 30, 55], [1, 30, 5]))
