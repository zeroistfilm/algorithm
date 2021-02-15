# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    map1=[]
    map2=[]
    result=[]

    for i in range(len(arr1)):
        map1.append(list((str(format(arr1[i],'b')).zfill(n))))
    for i in range(len(arr2)):
        map2.append(list((str(format(arr2[i],'b')).zfill(n))))
    for i in range(n):
        tmp = ""
        for j in range(n):
            if (int(map1[i][j])==0 and int(map2[i][j]) == 0):
                tmp+=" "
            else:
                tmp+="#"
        result.append(tmp)

    return result



print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))