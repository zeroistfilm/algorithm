# https://programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    import heapq
    kinds=set(gems)
    check = set([])
    result=[]
    for i in range(len(gems)):
        check.add(gems[i])
        for j in range(i,len(gems)):
            check.add(gems[j])
            if len(check)==len(kinds):
                heapq.heappush(result, [j-i,i+1,j+1])
                break
        check = set([])


    return result[0][1:3]


test1=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(test1))