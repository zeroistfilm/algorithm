# https://programmers.co.kr/learn/courses/30/lessons/17676
def solution(lines):
    import heapq

    worktimelist = []
    for line in lines:
        day = int(line.split()[0].split('-')[2])
        hour = int(line.split()[1].split(":")[0])
        minute = int(line.split()[1].split(":")[1])
        sec = int(line.split()[1].split(":")[2].split('.')[0])
        msec = float(line.split()[1].split(":")[2].split('.')[1]) / 1000
        worktime = float(line.split()[2][:-1])

        endtime =  hour * (60 * 60) + minute * (60) + sec + msec
        starttime = endtime - worktime + 0.001
        worktimelist.append([endtime,starttime])
    A = []
    for line in lines:
        a = line.split()[1:]
        b = a[0].split(':')
        b = int(b[0])*3600+int(b[1])*60+float(b[2])
        c = b - float(a[1][0:-1]) + 0.001
        A.append([b,c])


    worktimelist.sort(key=lambda x: x[1])

    queue=[]
    ans=0
    for i in range(len(worktimelist)):
        heapq.heappush(queue,worktimelist[i][0]) #end
        a=worktimelist[i][1]-queue[0] #start - 제일 작은 end
        while queue and a>=1:
            heapq.heappop(queue)

        ans = max(ans,len(queue))


    return ans


# tests = ["2016-09-15 03:10:33.020 0.011s"]
tests=["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]

print(solution(tests))
